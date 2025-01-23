# test_rag.py
def test_retrieval_relevance():
    rag = NarrativeRAG()
    rag.index_context("Test document", {"test": True})
    results = rag.retrieve_context("test query")
    assert len(results) == 1
    assert "Test document" in results