import arxiv
import pandas as pd
from datetime import datetime
import time

# Define a list of AI safety related keywords and phrases
AI_SAFETY_KEYWORDS = [
    "AI safety", "artificial intelligence safety", "AI alignment", "AI ethics",
    "AI governance", "AI risk", "AI robustness", "AI transparency",
    "AI accountability", "AI value alignment", "machine ethics", "ethical AI",
    "responsible AI", "AI existential risk", "AI control problem", "AI containment",
    "AI corrigibility", "AI value learning", "AI reward modeling", "AI interpretability",
    "AI fairness", "AI bias mitigation", "safe AI", "AI safety engineering",
    "AI accident prevention", "AI oracle", "AI boxing", "AI takeoff",
    "AI goal structure", "AI decision theory", "AI scalable oversight",
    "AI inverse reinforcement learning", "AI side effects", "AI interruptibility",
    "AI off switch", "AI tripwires", "AI honeypots", "AI sandboxing",
    "AI adversarial examples", "AI robustness to distributional shift",
    "AI safe exploration", "AI impact assessment", "AI policy",
    "long-term AI safety", "transformative AI safety", "AGI safety",
    "artificial general intelligence safety"
]

def construct_search_query(keywords=None):
    # Base query for AI-related categories
    base_query = 'cat:cs.AI OR cat:cs.LG OR cat:stat.ML'
    
    if keywords:
        # Construct the keyword part of the query
        keyword_query = ' OR '.join(f'(ti:"{kw}" OR abs:"{kw}")' for kw in keywords)
        # Combine the base query and keyword query
        full_query = f'({base_query}) AND ({keyword_query})'
    else:
        # If no keywords provided, search all AI papers
        full_query = base_query
    
    return full_query

def fetch_papers(keywords=None):
    # Construct the search query
    search_query = construct_search_query(keywords)

    # Set up the API client
    client = arxiv.Client()

    # Create a search object
    search = arxiv.Search(
        query=search_query,
        max_results=None,  # Fetch all results
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    # Fetch the results
    results = list(client.results(search))

    return results

def save_to_csv(papers, keywords=None, filename='ai_papers.csv'):
    # Convert papers to a list of dictionaries
    paper_dicts = []
    for paper in papers:
        # Lowercase the title and summary for case-insensitive matching
        lower_title = paper.title.lower()
        lower_summary = paper.summary.lower()
        
        # Find matching keywords if keywords are provided
        if keywords:
            matching_keywords = [
                kw for kw in keywords 
                if kw.lower() in lower_title or kw.lower() in lower_summary
            ]
        else:
            matching_keywords = []
        
        paper_dict = {
            'title': paper.title,
            'authors': ', '.join(author.name for author in paper.authors),
            'published': paper.published.strftime('%Y-%m-%d'),
            'updated': paper.updated.strftime('%Y-%m-%d'),
            'doi': paper.doi,
            'arxiv_id': paper.entry_id.split('/')[-1],
            'pdf_url': paper.pdf_url,
            'abstract': paper.summary.replace('\n', ' '),
            'keywords': ', '.join(matching_keywords) if matching_keywords else 'None'
        }
        paper_dicts.append(paper_dict)

    # Create a DataFrame
    df = pd.DataFrame(paper_dicts)

    # Check if the file exists
    try:
        existing_df = pd.read_csv(filename)
        # Combine existing and new data, drop duplicates
        combined_df = pd.concat([existing_df, df]).drop_duplicates(subset='arxiv_id', keep='first')
        combined_df.to_csv(filename, index=False)
        print(f"Updated {filename} with {len(df)} new papers.")
    except FileNotFoundError:
        # If the file doesn't exist, create a new one
        df.to_csv(filename, index=False)
        print(f"Created {filename} with {len(df)} papers.")

    # Print some statistics about keyword matches if keywords were provided
    if keywords:
        keyword_counts = df['keywords'].value_counts()
        print("\nKeyword match statistics:")
        print(keyword_counts)
        print(f"\nPapers with no keyword matches: {keyword_counts.get('None', 0)}")

def main():    
    keywords = None # None to fetch all AI papers

    if keywords:
        print("Fetching AI Safety papers from arXiv...")
    else:
        print("Fetching AI papers from arXiv...")
    
    papers = fetch_papers(keywords)
    print(f"Found {len(papers)} papers.")
    
    filename = 'ai_safety_papers.csv' if keywords else 'all_ai_papers.csv'
    save_to_csv(papers, keywords, filename)

if __name__ == "__main__":
    main()