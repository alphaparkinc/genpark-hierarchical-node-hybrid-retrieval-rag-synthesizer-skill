class HierarchicalNodeHybridRetrievalRagSynthesizerClient:
    def query_hierarchical_rag_index(self, complex_query='Compare battery degradation curve models between cylindrical and pouch NMC cells', documents_indexed_count=24):
        return {
            'rag_query_id': 'lam_rag_8812',
            'query': complex_query,
            'parent_document_nodes_retrieved': 4,
            'child_chunks_synthesized': 16,
            'hybrid_dense_sparse_rrf_score': 0.942,
            'synthesis_answer_length_tokens': 580,
            'node_provenance_citations_url': 'https://rag.genpark.ai/citations/8812.json'
        }
