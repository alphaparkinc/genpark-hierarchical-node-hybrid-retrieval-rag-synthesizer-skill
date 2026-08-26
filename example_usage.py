from client import HierarchicalNodeHybridRetrievalRagSynthesizerClient

def main():
    client = HierarchicalNodeHybridRetrievalRagSynthesizerClient()
    res = client.query_hierarchical_rag_index('Analyze transformer architectural revisions across DeepSeek-V3 and Llama 3.3', 30)
    print('RAG Query ID: ' + res['rag_query_id'] + ' | ' + res['query'])
    print('Parent Nodes: ' + str(res['parent_document_nodes_retrieved']) + ' | Child Chunks: ' + str(res['child_chunks_synthesized']))
    print('RRF Hybrid Score: ' + str(res['hybrid_dense_sparse_rrf_score']) + ' | Tokens: ' + str(res['synthesis_answer_length_tokens']))
    print('Citations: ' + res['node_provenance_citations_url'])

if __name__ == '__main__':
    main()
