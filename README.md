# COMP3011_Coursework2 - Search Engine tool

A python program that crawls a website, builds an inverted index for word based searches.


## Overview
1. Web crawling - crawls pages from a target website
2. Text processing - Tokenises words
3. Indexing - builds an inverted index with word frequencies and positions
4. Search - search words via a Command line interface

## Project structure
```
COMP3011_Coursework2/
│── src/
│   ├── crawler.py
│   ├── indexer.py
│   ├── search.py
│   └── main.py
│
│── data/
│   └── index.json
│
├── tests/
│   ├── test_crawler.py
│   ├── test_indexer.py
│   └── test_search.py
│
│── requirements.txt
│── README.md
```


## Target Website
The crawler targets: https://quotes.toscrape.com/ 
- Crawling all internal pages
- implements a 6 second politeness window between requests


## Installation
Requires Python 3.10 or higher.

```bash
# Clone the repository
git clone https://github.com/Morgan-Harvey/COMP3011_Coursework2.git
cd COMP3011_Coursework2

# (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt
```


## Usage

Run from the project root:

```bash
python -m src.main
```

this launches an interactive command line shell with four commands:

### `build`
crawls quotes.toscrape.com and builds the inverted index before saving it to
`data/index.json`.

```bash
> build
Crawling https://quotes.toscrape.com/

[1] Fetched https://quotes.toscrape.com/
[2] Fetched https://quotes.toscrape.com/tag/choices/page/1/
...
Crawled 50 pages.
Building index
Index saved to data/index.json
```
the saved index is automatically loaded

### `load`

loads the saved index into the shell.
```bash
> load
Index loaded from data/index.json

```

### `print WORD`   

```bash
> print hello
Word: hello
Found in 1 page(s):
  https://quotes.toscrape.com/author/Stephenie-Meyer  (freq: 1, positions: [346])
```

### `find WORD [WORD ...]`

```bash
> find no nonsense
https://quotes.toscrape.com/tag/life/page/1/
https://quotes.toscrape.com/tag/life/
https://quotes.toscrape.com/page/7/
https://quotes.toscrape.com/page/2/
https://quotes.toscrape.com/tag/regrets/page/1/
```

## Testing

The project uses pytest, with tests covering Link extraction, tokenisation, index construction, save/load function and search logic

tests are run from the project root with:
```bash
pytest tests/
```
or individually with:

```bash
pytest tests/test_crawler.py
pytest tests/test_indexer.py
pytest tests/test_search.py
```

## Dependencies

- `requests` — HTTP requests
- `beautifulsoup4` — HTML parsing
- `pytest` — testing framework