import os
from src.crawler import crawl
from src.indexer import build_index, save_index, load_index
from src.search import find, print_word

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_FILE = os.path.join(PROJECT_ROOT, "data", "index.json")
REL_PATH = os.path.relpath(INDEX_FILE, PROJECT_ROOT)


BASE_URL = "https://quotes.toscrape.com/"

def index_builder():
    print(f"Crawling {BASE_URL}")
    pages = crawl(BASE_URL)
    print(f"Crawled {len(pages)} pages.")
    
    print("Building index")
    index = build_index(pages)
    
    os.makedirs("data", exist_ok=True)
    save_index(index, REL_PATH)

    print(f"Index saved to {REL_PATH}")

    return index


def index_loader():
    try:
        index = load_index(REL_PATH)
    except FileNotFoundError:
        print("No index file found. Run 'build' first.")
        return None

    print(f"Index loaded from {REL_PATH}")
    return index

def main():
    index = None
        
    while True:
        
        try:
            user_input = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
     
        parts = user_input.split()
        if not parts:
            continue
        command = parts[0].lower()
        args = parts[1:]
        
        if command == "build":
            index = index_builder()
        
        elif command == "load":
            index = index_loader()
        
        elif command == "print":
            if index is None:
                print("No index loaded. Use 'build' or 'load'.")
                continue
            
            if len(args) != 1:
                print("Search for One word")
                continue

            print_word(args[0], index)

        
        elif command == "find":
            if index is None:
                print("No index loaded. Use 'build' or 'load'.")
                continue

            if len(args) == 0:
                print("Usage: find WORDS")
                continue

            results = find(" ".join(args), index)

            if not results:
                print("No results found.")
            else:
                for url in results:
                    print(url)
        
        else:
            print(f"Unknown command: {command}")
            
if __name__ == "__main__":
    main()