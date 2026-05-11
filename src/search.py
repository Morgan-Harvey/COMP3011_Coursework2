from src.indexer import tokenise

def find(query, index):
    tokens = tokenise(query)
    if not tokens:
        return []
    
    url_sets = []
    
    for token in tokens:
        if token not in index:
            return[]
        url_sets.append(set(index[token].keys()))
        
    matching_urls = url_sets[0]
    for s in url_sets[1:]:
        matching_urls = matching_urls & s
        
    ranked = []
    
    for url in matching_urls:
        score = 0
        for token in tokens:
            score += index[token][url]["freq"]
        ranked.append((url, score))
        
    ranked.sort(key=lambda item: item[1], reverse=True)
    return [url for url, score in ranked]
        
def print_word(word, index):
    """Print the inverted index entry for a single word."""
    
    word = word.lower()
    
    if word not in index:
        print(f"'{word}' not found in index.")
        return
    
    print(f"Word: {word}")
    print(f"Found in {len(index[word])} page(s):")
    
    for url, data in index[word].items():
        freq = data["freq"]
        positions = data["positions"]
        print(f"  {url}  (freq: {freq}, positions: {positions})")