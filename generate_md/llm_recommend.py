import yaml
from anthropic import Anthropic


# read key from .env
with open(".env", "r") as f:
    api_key = f.read()

# Initialize the Anthropic client
client = Anthropic(api_key=api_key)


    
def recommend_papers(paper, yaml_data):
    classification_prompt = f"""
    Your task is to recommend research papers similar to a new paper I provide to you.
    I will provide you with a list of topics, subtopics and papers belonging to each subtopic.
    I will also provide you with a new paper - you may need to identify the topics and subtopics it can be categorized as, 
    and recommend papers in the same subtopic.
    One paper can be in multiple categories.
    DO NOT WRITE ANYTHING OTHER THAN recommended papers.
    Here is the content of the new paper:
    - title: {paper["title"]}
    - abstract: {paper["abstract"]}

    The categorised list is: {yaml_data}
    """

    # print(classification_prompt)

    message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=4096,
            messages=[
                {
                    "role": "user", 
                    "content": classification_prompt}
            ]
        )

    out = message.content[0].text
    return out



# if __name__ == '__main__':
    
#     papers_yaml = "./arxiv_papers_for_llm.yaml"
#     # read the papers yaml
#     with open(papers_yaml, "r", encoding="utf-8") as f:
#         papers = yaml.safe_load(f)
    
#     llm_cluster_yaml = "./llm_cluster.yaml"
#     with open(llm_cluster_yaml, "r", encoding="utf-8") as f:
#         yaml_data = yaml.safe_load(f)
    
#     test_papers = papers[:3]
#     for paper in test_papers:
#         out = recommend_papers(paper, yaml_data)
#         print(out)
