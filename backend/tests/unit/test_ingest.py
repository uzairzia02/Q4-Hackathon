from src.scripts.ingest import chunk_text

def test_chunk_text():
    text = "This is the first sentence. This is the second sentence. This is the third sentence."
    chunks = chunk_text(text, chunk_size=40, overlap=10)
    assert len(chunks) > 1
    assert "This is the first sentence." in chunks[0]
