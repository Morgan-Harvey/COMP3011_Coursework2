from src.indexer import tokenise, build_index, save_index, load_index

def test_tokenise_basic():

    assert tokenise("Hello, World!") == ["hello", "world"]


def test_tokenise_empty_string():
    assert tokenise("") == []
    

def test_tokenise_lowercases_mixed_case():
    assert tokenise("GOOD Good gOoD") == ["good", "good", "good"]
    
def test_tokenise_punctuation_only():
    assert tokenise("!!! ??? ...") == []

def test_tokenise_preserves_numbers():
    assert tokenise("the year 1984") == ["the", "year", "1984"]


def test_build_index_counts_frequency():
    pages = {"url1": "good goOd GOod"}
    index = build_index(pages)
    assert index["good"]["url1"]["freq"] == 3


def test_build_index_records_positions():
    pages = {"url1": "alpha beta alpha"}
    index = build_index(pages)
    
    assert index["alpha"]["url1"]["positions"] == [0, 2]


def test_build_index_multiple_pages():
    pages = {
        "url1": "good day",
        "url2": "good night"
    }
    
    index = build_index(pages)
    
    assert "url1" in index["good"]
    assert "url2" in index["good"]


def test_build_index_empty_pages():
    assert build_index({}) == {}


def test_save_and_load_round_trip(tmp_path):
    index = {"hello": {"url1": {"freq": 1, "positions": [0]}}}
    filepath = tmp_path / "test_index.json"
    save_index(index, str(filepath))
    loaded = load_index(str(filepath))
    assert loaded == index