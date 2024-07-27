#%%
# read the file dataset/alignment_texts.jsonl
import jsonlines
from pprint import pprint

dataset_file = "dataset/alignment_texts.jsonl"

dictionary = {}
with jsonlines.open("dataset/alignment_texts.jsonl", "r") as reader:
  for entry in reader:
    # print(type(entry)) # dict
    # print(entry.keys())
    # dict_keys(['title', 'title_detail', 
    # 'links', 'link', 
    # 'authors', 'author', 'author_detail', 
    # 'published', 'published_parsed', 
    # 'tags', 'id', 'guidislink', 
    # 'summary', 'summary_detail', 
    # 'content', 
    # 'post-id', 'text', 
    # 'source', 'source_type'])

    try:
      if not entry["source"] == "arxiv":
        continue
    except KeyError:
      continue
    
    print(f"{entry['source']=}")
    # print(entry.keys())
    # dict_keys([
    # 'source', 'source_type', 
    # 'converted_with', 'paper_version', 
    # 'title', 'authors', 
    # 'date_published', 'data_last_modified', 'url', 
    # 'abstract', 
    # 'author_comment', 'journal_ref', 'doi', 
    # 'primary_category', 'categories', 
    # 'citation_level', 
    # 'alignment_text', 'confidence_score', 
    # 'main_tex_filename', 'text', 
    # 'bibliography_bbl', 'bibliography_bib', 
    # 'arxiv_citations'])

    try:
      print(f"{entry["title"]=}")
      # print(f"{entry["primary_category"]=}")
      # print(f"{entry["categories"]=}")
      # print(f"{entry["alignment_text"]=}")
      # print(f"{entry["confidence_score"]=}")
      # print(f"{entry["text"]=}")
      print(f"{entry["abstract"]=}")
    except KeyError:
      print("title key not found")
      continue

    break

    # write all to a yaml file
    # break
# %%
def extract_arxiv_papers(output_file):
    input_file = dataset_file
    with open(output_file, "w", encoding="utf-8") as out_file:
        paper_count = 0
        
        with jsonlines.open(input_file, "r") as reader:
            for entry in reader:
                try:
                    if entry["source"] != "arxiv":
                        continue
                    
                    title = entry["title"]
                    abstract = entry["abstract"]



                    
                    # Write the paper information in Markdown format
                    out_file.write(f"# {title}\n\n")
                    out_file.write(f"{abstract}\n\n")
                    out_file.write("---\n\n")  # Separator between papers
                    
                    paper_count += 1

                    if paper_count >= 20:
                       break
                    
                except KeyError:
                    continue
    
    print(f"Extracted {paper_count} arXiv papers to {output_file}")

# Usage
# output_file = "arxiv_papers_for_llm.md"
# extract_arxiv_papers(output_file)

def extract_arxiv_papers_to_yaml(output_file):
    # extract title, abstract and url
    input_file = dataset_file
    with open(output_file, "w", encoding="utf-8") as out_file:
        paper_count = 0
        
        with jsonlines.open(input_file, "r") as reader:
            for entry in reader:
                try:
                    if entry["source"] != "arxiv":
                        continue
                    
                    title = entry["title"]
                    abstract = entry["abstract"]
                    url = entry["url"]

                    # remove colon from title and abstract
                    title = title.replace(":", "")
                    abstract = abstract.replace(":", "")
                    
                    # Write the paper information in YAML format
                    out_file.write(f"- title: {title}\n")
                    out_file.write(f"  abstract: {abstract}\n")
                    out_file.write(f"  url: {url}\n\n")
                    
                    paper_count += 1

                    if paper_count >= 20:
                       break
                    
                except KeyError:
                    continue
                
# Usage
output_file = "arxiv_papers_for_llm.yaml"
extract_arxiv_papers_to_yaml(output_file)

