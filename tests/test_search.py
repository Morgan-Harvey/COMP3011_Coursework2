from src.indexer import build_index
from src.search import find, print_word


SAMPLE_INDEX = {
    "good": {
        "url1": {"freq": 2, "positions": [0, 5]},
        "url2": {"freq": 1, "positions": [3]},
    },
    "friends": {
        "url1": {"freq": 1, "positions": [1]},
        "url3": {"freq": 1, "positions": [7]},
    },
}

def test_find_basic():
    results = find("good", SAMPLE_INDEX)
    
    assert "url1" in results
    assert "url2" in results
    
def test_find_word_not_in_index():
    assert find("Hello World", SAMPLE_INDEX) == []
    
    
def test_interaction():
    results = find("good friends", SAMPLE_INDEX) 
    assert "url1" in results
    
def test_no_interaction():
    assert find("Good day", SAMPLE_INDEX) == []
    
def test_case_sensitivity():
    results = find("GOoD", SAMPLE_INDEX)
    
    assert "url1" in results
    assert "url2" in results
    
def find_empty():
    assert find("", SAMPLE_INDEX) == []