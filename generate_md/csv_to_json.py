
#  Run get_arxiv_to_csv.py or arxiv_papers_from_dataset.py 
# Steps
# Load and process the CSV to extract titles and abstracts 
# Extract those of unclassified papers
# Get only categories from the JSON structure
# Use batches of papers to query the LLM
# Update an in-memory JSON structure with categories
# Save updates periodically to avoid loss of progress
# TODO
# Generate Markdown files from the final JSON structure

import os
import json
import yaml
import pandas as pd
from anthropic import Anthropic

with open(".env", "r") as f:
    api_key = f.read().strip()

# Initialize Anthropic client
client = Anthropic(api_key=api_key)

# %%
def load_papers_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    papers = df.to_dict(orient="records")
    return [{"title": paper["title"], "abstract": paper["abstract"]} for paper in papers]

# %%
# Load or initialize categories.json
def load_or_initialize_categories(json_file):
    if os.path.exists(json_file):
        with open(json_file, "r", encoding="utf-8") as f:
            full_categories = json.load(f)
        # Extract topics and subtopics only
        simplified_categories = {
            main_topic: list(subtopics.keys()) for main_topic, subtopics in full_categories.items()
        }
        return full_categories, simplified_categories
    else:
        # Initialize with an empty structure
        return {}, {}


# Save updated categories to the JSON file
def save_categories(json_file, existing_categories, new_categories):
    # Merge new categories into the existing ones
    for main_topic, subtopics in new_categories.items():
        if main_topic not in existing_categories:
            existing_categories[main_topic] = {}
        for subtopic, papers in subtopics.items():
            if subtopic not in existing_categories[main_topic]:
                existing_categories[main_topic][subtopic] = []
            # Add new papers, avoiding duplicates
            existing_titles = set(existing_categories[main_topic][subtopic])
            new_papers = [paper for paper in papers if paper not in existing_titles]
            existing_categories[main_topic][subtopic].extend(new_papers)
    # Save merged categories to the JSON file
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(existing_categories, f, indent=2)


# %%
def re_write_cat_yamls(papers, relevant_categories):
    classification_prompt = f"""
    Your task is to categorize AI Alignment research papers into a hierarchical JSON structure of topics and subtopics. 

    ### Instructions:
    1. **Input**: I will provide you with:
    - Titles and abstracts of unclassified research papers.
    - A list of current topics and subtopics.
    2. Check if the paper falls under AI safety. If it is unrelated to AI safety, do not use it for categorization.
    2. **Categorization**:
    - Assign each paper to one or more **existing subtopics** under the appropriate **Main_Topic**.
    - If no suitable subtopic exists, you may create a **new subtopic** under an appropriate **Main_Topic**, or create a **new Main_Topic** if necessary.
    - Be concise and ensure subtopics are descriptive yet general enough to accommodate related papers.
    
    3. **Output Requirements**:
    - Return only **valid JSON** following this structure:
        {{
            "Main_Topic_1": {{
                "Subtopic_1": ["Paper Title 1", "Paper Title 2"],
                "Subtopic_2": ["Paper Title 3"]
            }},
            "Main_Topic_2": {{
                "Subtopic_3": ["Paper Title 4"]
            }}
        }}
    - Do not include any additional comments, explanations, or invalid content.

    ### Examples of Main Topics and Subtopics:
    - **Main_Topic: Value Alignment**
    - Subtopics: Defining Human Values, Inverse Reinforcement Learning, Societal Value Alignment, Agent Reward Management, Low Impact AI
    - **Main_Topic: Safety and Robustness**
    - Subtopics: Robustness to Distributional Shift, Adversarial Machine Learning, Safe Reinforcement Learning, Uncertainty Quantification, Multi-Agent Safety
    - **Main_Topic: Interpretability, Explainability, and Transparency**
    - **Main_Topic: Meta-learning, Transfer Learning, and Generalization**
    - **Main_Topic: Ethical and Societal Implications of AI**
    - **Main_Topic: AI Governance and Policy**
    - **Main_Topic: Human-AI Interaction and Collaboration**
    - **Main_Topic: AI Benchmarks and Evaluation**
    - **Main_Topic: Biological Inspiration in AI**
    - **Main_Topic: AI Security and Privacy**

    ### Papers:
    {json.dumps(papers, indent=2)}

    ### Current Categories:
    {json.dumps(relevant_categories, indent=2)}
    """
    
    # TODO: cache prompt - reduce API calls 
    # no need to pass topics and subtopics every call - only new topics 

    # LLM call
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4096,
        messages=[{"role": "user", "content": classification_prompt}]
    )
    # try:
    #     response = message.content[0].text
    #     updated_categories = json.loads(response)
    #     return updated_categories
    # except Exception as e:
    #     print(f"Error in LLM response: {e, message}")
    #     return message
    try:
        # Ensure the response starts with a JSON object or array
        response_content = message.content[0].text.strip()
        if not (response_content.startswith("{") or response_content.startswith("[")):
            raise ValueError("Response does not start with valid JSON.")
        updated_categories = json.loads(response_content)
        return updated_categories
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        print("LLM response:", message.content[0].text)
        return message
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("LLM response:", message.content[0].text)
        return message


# %%

def main():
    # papers_csv_path = "ai_safety_papers.csv"
    papers_csv_path = "arxiv_papers_for_llm.csv"
    json_file = "categories.json"
    
    papers = load_papers_from_csv(papers_csv_path)  #list of dictionaries - title and abstract
    existing_categories, simplified_categories = load_or_initialize_categories(json_file)
    # simplified_categories


    # Create a set of already classified paper titles
    classified_papers = set()
    for main_topic, subtopics in existing_categories.items():
        for subtopic, titles in subtopics.items():
            classified_papers.update(titles)
    print(len(classified_papers), "papers already classified.")

    # Filter out already classified papers
    unclassified_papers_all = [paper for paper in papers if paper["title"] not in classified_papers]
    # unclassified_papers
    
    max_papers = 500  # Limit 
    unclassified_papers = unclassified_papers_all[:max_papers]
    print(len(unclassified_papers_all), "papers to classify,", len(unclassified_papers), "papers processed this call.")

    batch_size = 20
    # Process unclassified papers in batches
    for i in range(0, len(unclassified_papers), batch_size):
        papers_batch = unclassified_papers[i:i + batch_size]

        # Get updated categories from LLM
        new_categories = re_write_cat_yamls(papers_batch, simplified_categories)

        # Merge with existing categories
        save_categories(json_file, existing_categories, new_categories)
        
        processed_papers = i + len(papers_batch)
        print(f"Processed {processed_papers} of {len(unclassified_papers)} papers...")

    # Convert to Markdown
    # convert_categories_to_markdown(categories, output_dir)

if __name__ == "__main__":
    main()

