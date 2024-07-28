import yaml
import os
from anthropic import Anthropic

# read key from .env
with open(".env", "r") as f:
    api_key = f.read()

# Initialize the Anthropic client
client = Anthropic(api_key=api_key)

def create_summaries(subtopic_name, paper_info):
    prompt = f"You are an AI alignment research assistant. Your task is to create a summary of the subtopic {subtopic_name}. Make use of the following paper abstracts:\n {paper_info}\nSummary:"

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4096,
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ]
    )

    return message.content[0].text

def to_id(text):
    return ''.join(char for char in text.lower() if char.islower())

def add_subtopic_summaries(yaml_data, arxiv_data):
    for topic in yaml_data:
        main_topic = topic['Main_Topic']
        
        # Create main topic file
        for sub_topic in topic['Sub_Topics']:
            sub_topic_name = sub_topic['Sub_Topic']
            
            # Create sub-topic file
            papers_info = ""
            for paper in sub_topic['Research_Papers']:
                paper_id = to_id(paper['Title'])
                try:
                    papers_info += f"# {paper['Title']}\n## Abstract\n_{arxiv_data[paper_id]['abstract']}_\n\n---\n\n"
                except:
                    print(paper['Title'])

            summary = create_summaries(sub_topic_name, papers_info)
            sub_topic['Summary'] = summary
            print(summary)

            
    
llm_cluster_yaml = "generate_md/llm_cluster.yaml"
with open(llm_cluster_yaml, "r") as f:
    yaml_data = yaml.safe_load(f)

arxiv_data_path = "generate_md/arxiv_papers_for_llm.yaml"
with open(arxiv_data_path) as f:
    arxiv_data = yaml.safe_load(f)

arxiv_data = {to_id(item['title']) : item for item in arxiv_data}

add_subtopic_summaries(yaml_data, arxiv_data)

with open('generate_md/llm_cluster_with_summaries', "w") as f:
    yaml.dump(yaml_data)