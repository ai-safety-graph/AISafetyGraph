import yaml
import os
import anthropic

content_file_path = "../content"

def to_id(text):
    return ''.join(char for char in text.lower() if char.islower())

def create_file(filename, content):
    filename = os.path.join(content_file_path, filename)
    with open(filename, 'w') as f:
        f.write(content)

def create_obsidian_graph(yaml_data, arxiv_data):
    # Create index.md
    index_content = """
---\n\n
title: AI Alignment Research Graph\n
---\n\n
        """
    index_content += "# Main Topics\n\n"
    for topic in yaml_data:
        print(topic)
        main_topic = topic['Main_Topic']
        index_content += f"- [[{main_topic}]]\n"
        # Create main topic file
        main_topic_content = f"# {main_topic}\n\n## Summary\n{topic['Summary']}\n## Sub-topics\n\n"
        for sub_topic in topic['Sub_Topics']:
            sub_topic_name = sub_topic['Sub_Topic']
            main_topic_content += f"- [[{sub_topic_name}]]\n"
            summary = sub_topic['Summary']
            
            # Create sub-topic file
            sub_topic_content = f"## Summary\n {summary}\n## Research Papers\n\n"
            papers = ""
            for paper in sub_topic['Research_Papers']:
                paper_id = to_id(paper['Title'])
                try:
                    arxiv_url = arxiv_data[paper_id]['url']
                    sub_topic_content += f"- [[{paper['Title']}]]\n"

                    page_content = f"# {paper['Title']}\n{arxiv_url}\n## Abstract\n{arxiv_data[paper_id]['abstract']}"
                    create_file(f"{paper['Title']}.md", page_content)
                except:
                    print(paper['Title'])

            sub_topic_content = f"# {sub_topic_name}\n\n" + sub_topic_content


            
            create_file(f"{sub_topic_name}.md", sub_topic_content)
        
        create_file(f"{main_topic}.md", main_topic_content)
    
    create_file("index.md", index_content)

llm_cluster_yaml = "llm_cluster_with_summaries.yaml"
with open(llm_cluster_yaml, "r") as f:
    yaml_data = yaml.safe_load(f)

arxiv_data_path = "arxiv_papers_for_llm.yaml"
with open(arxiv_data_path) as f:
    arxiv_data = yaml.safe_load(f)

arxiv_data = {to_id(item['title']) : item for item in arxiv_data}

create_obsidian_graph(yaml_data, arxiv_data)