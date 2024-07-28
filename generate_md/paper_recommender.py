import os
import json
import yaml
from anthropic import Anthropic

def select_topics(topics, project_idea):
    prompt = f"""Select the most relevant subtopics from the provided list based on the given project idea. Return only a JSON object with the following format:

{
  "relevant_subtopics": ["topic1", "topic2", "topic3"]
}

Respond only with JSON. No explanations or additional text.

topics: {topics}"""
    
    print(prompt)


if __name__ == "__main__":
    # read key from .env
    with open(".env", "r") as f:
        api_key = f.read()

    # Initialize the Anthropic client
    client = Anthropic(api_key=api_key)

    llm_cluster_yaml = "generate_md/llm_cluster.yaml"
    with open(llm_cluster_yaml, "r") as f:
        yaml_data = yaml.safe_load(f)

    topics = {
        topic['Main_Topic']: topic['Sub_Topics'] for topic in yaml_data
    }

    project_idea = "I am working on a project that involves mechanistic interpretability"

    select_topics(topics, project_idea)


