# AI Alignment Research Graph Visualization

TODO:
- [ ] Refactor the code in [explore_ds.py](/generate_md/explore_ds.py) to output in json and not yaml format
- [ ] Impove the code in [llm_cluster.py](/generate_md/llm_cluster.py) to take a batch of papers (eg. 20) in each call to the LLM instead
- [ ] run [llm_cluster.py](/generate_md/llm_cluster.py) on the entire source

Improvements:
- [ ] [explore_ds.py](/generate_md/explore_ds.py) currently filters by arxiv papers, could also support other sources
- [ ] Chatbot to the right side of the page for some questioning...

Other Notes:
- the [content](./content/) folder stores the markdown files that represents the graph strucuture
- the [generate_md](./generate_md/) folder contains the code to generate the .md files
- generating .md files requires [ai-alignement-dataset-jsonl-file](https://the-eye.eu/public/AI/Alignment/moirage_alignment-research-dataset/) to be placed under [generate_md/dataset](./generate_md/dataset) folder
- generating .md files requires a anthropic api key to be stored in ```/generate_md/.env``` file


# Local Build
To build locally
```bash
# node lts/iron
npm i
npx quartz build --serve
```

# FAQ
if you get ADDRINUSE: address already in use :::8080 run 
```bash
npx kill-port 8080
```

- Thanks to [alignment-research-dataset](https://github.com/moirage/alignment-research-dataset) for the dataset
- Built using [Quartz v4](https://quartz.jzhao.xyz/)