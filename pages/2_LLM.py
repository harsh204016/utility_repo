import streamlit as st

with st.expander("What are indexing techniques in vector databases?"):
    st.markdown("""Large language models work on vector embeddings, which are numerical representations of text. These embeddings are stored in vector databases. Indexing is a process of organizing these high dimensional vectors to efficiently search for similar vectors.

There are four common indexing techniques:

- Flat indexing or linear search: This is a simple method that compares the query vector with every other vector in the database. This is slow for large datasets.
- IVF or inverted file: This technique clusters the vectors and then searches for the nearest neighbor in the cluster that is closest to the query vector.
- Scalar quantization: This technique reduces the precision of the vectors to reduce their memory footprint.
- HNSW or hierarchical navigable small world: This is a graph-based technique that is the most common indexing technique used in vector databases. It uses a hierarchical graph structure to index the vectors. It is scalable and efficient for large datasets but can be expensive in terms of memory footprint.

""")