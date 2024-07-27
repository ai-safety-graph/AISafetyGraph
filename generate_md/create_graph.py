import yaml
import os

content_file_path = "../content"

def create_file(filename, content):
    filename = os.path.join(content_file_path, filename)
    with open(filename, 'w') as f:
        f.write(content)

def create_obsidian_graph(yaml_data):
    # Create index.md
    index_content = "# Research Topics\n\n"
    for topic in yaml_data:
        main_topic = topic['Main_Topic']
        index_content += f"- [[{main_topic}]]\n"
        
        # Create main topic file
        main_topic_content = f"# {main_topic}\n\n## Sub-topics\n\n"
        for sub_topic in topic['Sub_Topics']:
            sub_topic_name = sub_topic['Sub_Topic']
            main_topic_content += f"- [[{sub_topic_name}]]\n"
            
            # Create sub-topic file
            sub_topic_content = f"# {sub_topic_name}\n\n## Research Papers\n\n"
            for paper in sub_topic['Research_Papers']:
                sub_topic_content += f"- {paper['Title']}\n"
            
            create_file(f"{sub_topic_name}.md", sub_topic_content)
        
        create_file(f"{main_topic}.md", main_topic_content)
    
    create_file("index.md", index_content)

llm_cluster_yaml = "llm_cluster.yaml"
with open(llm_cluster_yaml, "r") as f:
    yaml_data = yaml.safe_load(f)

create_obsidian_graph(yaml_data)