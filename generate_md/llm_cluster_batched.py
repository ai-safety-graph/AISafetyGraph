import os
import json
import yaml
from anthropic import Anthropic
from tqdm import tqdm

# Read key from .env
with open(".env", "r") as f:
    api_key = f.read()

# Initialize the Anthropic client
client = Anthropic(api_key=api_key)

def re_write_cat_yamls(batch, categories_yaml):
    classification_prompt = f"""
    Your task is to categorize AI Alignment research papers.
    I will provide you with titles, abstracts, and URLs of alignment research papers.
    I will also provide you with the current categories (categories_yaml).
    Your task is to re-write the categories_yaml with the new papers added to the appropriate categories.
    You can create/merge new main categories or sub-categories as needed.
    Papers can be in multiple categories.
    Aim for conciseness of main and sub-categories.
    DO NOT WRITE ANYTHING OTHER THAN THE CONTENTS of categories_yaml.
    Here are the papers to categorize:

    {yaml.dump(batch)}

    The current categories are:
    {categories_yaml}
    """

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4096,
        messages=[
            {
                "role": "user", 
                "content": classification_prompt
            }
        ]
    )

    return message.content[0].text

def process_batch(batch, categories_yaml, max_retries=3):
    for attempt in range(max_retries):
        try:
            out = re_write_cat_yamls(batch, categories_yaml)
            # Ensure it's correct YAML
            yaml.safe_load(out)
            return out
        except yaml.YAMLError:
            print(f"Attempt {attempt + 1} failed. Retrying...")
    
    print(f"Failed to process batch after {max_retries} attempts. Skipping...")
    return categories_yaml

if __name__ == '__main__':
    papers_yaml = "./arxiv_papers_for_llm.yaml"
    categories_yaml = "./llm_cluster.yaml"
    batch_size = 5  # Adjust this based on your needs and context window size

    # Read the papers YAML
    with open(papers_yaml, "r", encoding="utf-8") as f:
        papers = yaml.safe_load(f)

    # Read the current categories YAML
    with open(categories_yaml, "r", encoding="utf-8") as f:
        categories = yaml.safe_load(f)

    # Create a set of already classified paper titles
    classified_papers = set()
    for main_topic in categories:
        for sub_topic in main_topic.get('Sub_Topics', []):
            classified_papers.update(paper['Title'] for paper in sub_topic.get('Research_Papers', []))

    # Filter out already classified papers
    unclassified_papers = [paper for paper in papers if paper['title'] not in classified_papers]

    # Process papers in batches
    for i in tqdm(range(0, len(unclassified_papers), batch_size)):
        batch = unclassified_papers[i:i+batch_size]
        
        # Read the current categories YAML
        with open(categories_yaml, "r", encoding="utf-8") as f:
            current_categories = f.read()

        # Process the batch
        out = process_batch(batch, current_categories)

        # Overwrite the categories YAML
        with open(categories_yaml, "w") as f:
            f.write(out)

    print("Classification complete.")