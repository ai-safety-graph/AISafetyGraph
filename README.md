# AI Safety Graph

<img src="/docs/assets/ai_graph_3_sec.gif" width="100%">

<div align="center">

####  📅 Recent Updates
**[August 2024]** 🥇 First Place at [Research Augmentation Hackathon](https://www.apartresearch.com/event/research-augmentation-hackathon-supercharging-ai-alignment)  
**[January 2025]** 🎉 Now part of [Apart Lab Studio](https://www.apartresearch.com/post/announcing-apart-lab-studio)!

</div>

---

#### 👉 Check out the live version here: [AI Alignment Research Graph][live-gh-pages]

## 👋🏻 Getting Started & Join Our Community

Whether you're a newcomer or a seasoned researcher, we have a place for you in our community. Here are some ways to get started:

| [![live-demo-badge]][live-gh-pages]  | Visit the website                       |
| :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| [![][discord-shield-badge]][discord-link] | Join our Discord community!  |


> \[!IMPORTANT]
>
> **Star Us**, to get updates from GitHub \~ ⭐️

## Features
- Interactive graph visualization of AI Alignment Research
- High-Quality LLM-based segementation of papers
- Search for papers by title, author, or abstract
- Click on a node to view a summary of the topic


## Local Build

To build locally, first clone with submodules:
```bash
# Clone repo with submodule
git clone --recurse-submodules https://github.com/ai-safety-graph/AISafetyGraph.git
# Or if you've already cloned without submodules:
git submodule update --init --recursive

# node lts/iron
npm i
npx quartz build --serve
```

## Development Notes:
- the [aisgraph_quartz](./aisgraph_quartz/) submodule points to  [aisgraph](https://github.com/ai-safety-graph/aisgraph)  which is a fork of quartz
- the [content](./content/) folder stores the markdown files that represents the graph strucuture
- the [generate_md](./generate_md/) folder contains the code to generate the .md files
- generating .md files requires [ai-alignement-dataset-jsonl-file](https://the-eye.eu/public/AI/Alignment/moirage_alignment-research-dataset/) to be placed under [generate_md/dataset](./generate_md/dataset) folder
- generating .md files requires a anthropic api key to be stored in ```/generate_md/.env``` file

## Troubleshooting
<details>
<summary>If you get ADDRINUSE: address already in use :::8080</summary>

```bash
npx kill-port 8080
```

</details>

## Contributors
![GitHub Contributors](https://contrib.rocks/image?repo=ai-safety-graph/AISafetyGraph)

## Acknowledgements
- Thanks to [alignment-research-dataset](https://github.com/moirage/alignment-research-dataset) for the dataset
- Built using [Quartz v4](https://quartz.jzhao.xyz/)
- **Commits prior to commit hash #5c7cb55 come from the quartz v4 web framework, this is to allow easier updates of the web-framework using ```git pull upstream```**


| <img src="docs/assets/LISA.svg" width="120" alt="LISA"> | <img src="docs/assets/Apart.png" width="120" alt="Apart Research"> | <img src="docs/assets/SAIL.png" width="120" alt="SAFE AI London"> |
|:---:|:---:|:---:|
| **LISA** | **Apart Research** | **SAFE AI London** |

------------------

TODO:
- [ ] Refactor the code in [explore_ds.py](/generate_md/explore_ds.py) to output in json and not yaml format
- [ ] run [llm_cluster.py](/generate_md/llm_cluster.py) on the entire source

Improvements:
- [ ] [explore_ds.py](/generate_md/explore_ds.py) currently filters by arxiv papers, could also support other sources

<!-- LINK GROUP -->

[live-gh-pages]: https://ai-safety-graph.github.io/AISafetyGraph/
[discord-link]: https://discord.gg/skqQ8y4quR
[discord-shield-badge]: https://img.shields.io/discord/1275110552661659658?style=for-the-badge&logo=discord&logoColor=white&label=discord&labelColor=black
[live-demo-badge]: https://img.shields.io/badge/Live%20Demo-Visit-brightgreen?style=for-the-badge&logo=web&logoColor=white&labelColor=black


