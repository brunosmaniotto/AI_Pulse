# Training Data

The training data consists of ~2,000 condensed matter physics abstracts from arXiv (category `cond-mat.str-el`).

## Regenerating the data

```bash
pip install arxiv tqdm
python download_arxiv.py --category "cond-mat.str-el" --max-results 2000
python prepare_training_data.py
```

This produces:
- `abstracts/` -- individual abstract text files
- `abstracts.jsonl` -- all abstracts as a single JSONL file
- `train.jsonl` + `val.jsonl` -- formatted training/validation splits (1,800/200)
