import json
import re

def tokenise(text):
    return re.findall(r"[a-z0-9]+", text.lower())    

def build_index(pages):
    index = {}
    
    for url, text in pages.items():
        tokens = tokenise(text)
        
        for position, token in enumerate(tokens):
            
            if token not in index:
                index[token] = {}
                
            if url not in index[token]:
                index[token][url] = {"freq": 0, "positions": []}
                
            index[token][url]["freq"] += 1
            index[token][url]["positions"].append(position)
            
    return index

def save_index(index, filename="index.json"):
    with open(filename, "w") as f:
        json.dump(index, f)


def load_index(filename="index.json"):
    with open(filename, "r") as f:
        return json.load(f)