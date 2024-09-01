# AI Alignment Research Graph Visualization

<img src="/docs/assets/ai_graph_3_sec.gif" width="100%">



---
### 🗓️ 1st August 2024
# 🏆 **First Place Winner at the [Research Augmentation Hackathon](https://www.apartresearch.com/event/research-augmentation-hackathon-supercharging-ai-alignment)** 🏆
## 🥇 **We are proud to announce that we secured** **_First Place_** **at the prestigious** **_[Research Augmentation Hackathon: Supercharging AI Alignment](https://www.apartresearch.com/event/research-augmentation-hackathon-supercharging-ai-alignment)_** **event!**

---

## 👉 Check out the live version here: [AI Alignment Research Graph](https://mnm-matin.github.io/ai_alignment_graph/)

## Features
- Interactive graph visualization of AI Alignment Research
- High-Quality LLM-based segementation of papers
- Search for papers by title, author, or abstract
- Filter by year, source, and category
- Click on a node to view a summary of the topic


## Local Build
To build locally
```bash
# node lts/iron
npm i
npx quartz build --serve
```

## Troubleshooting
if you get ADDRINUSE: address already in use :::8080 run 
```bash
npx kill-port 8080
```

## Development Notes:
- the [content](./content/) folder stores the markdown files that represents the graph strucuture
- the [generate_md](./generate_md/) folder contains the code to generate the .md files
- generating .md files requires [ai-alignement-dataset-jsonl-file](https://the-eye.eu/public/AI/Alignment/moirage_alignment-research-dataset/) to be placed under [generate_md/dataset](./generate_md/dataset) folder
- generating .md files requires a anthropic api key to be stored in ```/generate_md/.env``` file

## Contributors
- Matin
- Samuel
- Sruthi and 
- Pandelis

## Acknowledgements
- Thanks to [alignment-research-dataset](https://github.com/moirage/alignment-research-dataset) for the dataset
- Built using [Quartz v4](https://quartz.jzhao.xyz/)
- **Commits prior to commit hash #5c7cb55 come from the quartz v4 web framework, this is to allow easier updates of the web-framework using ```git pull upstream```**


<p align="center">
  <img src="docs/assets/LISA.svg" width="100" alt="LISA">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/assets/Apart.png" width="100" alt="Apart Research">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/assets/SAIL.png" alt="SAFE AI London">
</p>

------------------

TODO:
- [ ] Refactor the code in [explore_ds.py](/generate_md/explore_ds.py) to output in json and not yaml format
- [ ] Impove the code in [llm_cluster.py](/generate_md/llm_cluster.py) to take a batch of papers (eg. 20) in each call to the LLM instead
- [ ] run [llm_cluster.py](/generate_md/llm_cluster.py) on the entire source

Improvements:
- [ ] [explore_ds.py](/generate_md/explore_ds.py) currently filters by arxiv papers, could also support other sources
- [ ] Chatbot to the right side of the page for some questioning...
