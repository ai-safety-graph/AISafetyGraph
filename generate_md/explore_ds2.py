#%%
# read the file dataset/alignment_texts.jsonl

import json
import re
import yaml
import jsonlines

dataset_file = "dataset/alignment_texts.jsonl"

def clean_text(text):
    # Remove patterns like {#sec:sec:search-space}
    text = re.sub(r'\{#.*?\}', '', text)
    # Remove colons, quotes, and backticks
    text = text.replace(":", "").replace("\"", "").replace("`", "")
    return text

def extract_arxiv_papers_to_yaml(output_file):
    # extract title, abstract, and url
    input_file = dataset_file
    papers = []
    paper_count = 0
    with jsonlines.open(input_file, "r") as reader:
        for entry in reader:
            try:
                if entry["source"] != "arxiv":
                    continue

                title = entry["title"]
                abstract = entry["abstract"]
                url = entry["url"]
                text = clean_text(entry["text"])

                # remove colon from title and abstract
                title = title.replace(":", "").replace("\"", "").replace("`", "")
                abstract = abstract.replace(":", "").replace("\"", "").replace("`", "")

                paper_info = {
                    'title': title,
                    'abstract': abstract,
                    'url': url,
                    'text': text
                }

                papers.append(paper_info)
                paper_count += 1
                print('paper_count: ',paper_count)

                # if paper_count >= 2:
                #     break

            except KeyError:
                continue

    with open(output_file, "w", encoding="utf-8") as out_file:
        yaml.safe_dump(papers, out_file, allow_unicode=True, default_flow_style=False, sort_keys=False)

# Usage
output_file = "arxiv_papers_for_llm.yaml"
extract_arxiv_papers_to_yaml(output_file)

