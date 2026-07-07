
## Create RAG system (Retrieval, Augmentation, Generation)

## Task 1: Set up development Environment
ChromaDB (Vector DB)
Transformers (ML Models)
Flask (Web Server)
OpenAI (LLM API)

Purpose: Install all dependencies required for building RAG
Installation commands:
````
cd /root && mkdir -p rag-project && cd rag-project
python3 -m venv venv && source venv/bin/activate
pip install uv && uv pip install chromadb sentence-transformers openai flask
echo "READY" > /root/rag-setup-complete.txt

````

## Task 2: Explore Document vault

````
cd /root/techcorp-docs
ls -la
find . -name "*.md" | wc -l
find . -name "*.md" | wc -l > /root/doc-count.txt

````

## Task 3: Initialize Vector Database
**ChromaDB Architecture**
Documents -> Vectors -> Semantic Space

Purpose: Create AI brain for storing document vectors

Create init_vectordb.py (see also separate code file)

````
import chromadb
from chromadb.config import Settings

print(" Initializing AI Brain...")
client = chromadb.PersistentClient(
    path="./chroma_db",
    settings=Settings(anonymized_telemetry=False)
)

collection = client.get_or_create_collection(
    name="techcorp_docs",
    metadata={"hnsw:space": "cosine"}
)

print(f" Brain Created: {collection.name}")
print(f" Memories: {collection.count()}")
print(" AI Brain Ready!")

````

Execute:

````

cd /root/rag-project && python init_vectordb.py

````

## Task 4: Chunking

Learn smart chunking strategy with python:
Create test_chunking.py (see also separate file):

````

import os

print(" DOCUMENT CHUNKING ENGINE")
print("="*40)

def chunk_text(text, size=500, overlap=100):
    """Smart chunking with overlap for context preservation"""
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)

        if end >= len(text):
            break

        start += size - overlap

    return chunks

# Process sample document
sample_doc = """TechCorp Pet Policy: 
Employees may bring pets to the office on Fridays. 
Dogs must be well-behaved and vaccinated. 
The CEO's golden retriever is the office mascot.

Remote Work Policy:
Employees can work remotely up to 3 days per week.
Core hours are 10 AM - 3 PM in your local timezone.
All meetings should be recorded for async collaboration.

Benefits Overview:
Comprehensive health insurance including dental and vision.
401k matching up to 6% of salary.
Unlimited PTO after first year.
Annual learning budget of $2,000."""

print(f" Original document: {len(sample_doc)} characters")
print("-"*40)

chunks = chunk_text(sample_doc, size=500, overlap=100)

print(f" Created {len(chunks)} chunks")
print("-"*40)

for i, chunk in enumerate(chunks, 1):
    print(f"\nChunk {i} ({len(chunk)} chars):")
    print(f"Preview: {chunk[:60]}...")

# Save verification
with open('/root/chunk-test.txt', 'w') as f:
    f.write(f"CHUNKS:{len(chunks)}")

print("\n" + "="*40)
print(" Chunking complete!")
print(f" Stats: {len(chunks)} chunks from {len(sample_doc)} chars")
print(" Ready for vectorization!")

````

## Task 5: Test to understand how Embeddings work (skip in real world)
Purpose: Learn how AI converts text to math BEFORE processing real docs in task 6

**Semantic Embedding Transformation:**
"Dogs allowed Fridays" → AI Model → 384D Vector (each word becomes 384 numbers)
[0.23, -0.45, 0.67, ..., 0.12]
Semantic Similarity:
"Pets permitted" ↔ "Dogs allowed" = 92%
"Remote work" ↔ "Dogs allowed" = 18%

Run test_embeddings.py (see file):
````
python test_embeddings.py

````

## Task 6: Chunking and embedding docs into database (no test)

Documents -> Chunking -> Embdding -> ChromaDB

Create ingest_documents.py (see the file).

Execute ingestion:
````
python ingest_documents.py

````

## Task 7: Activate Semantic Search

Purpose: Build semantic search that understands MEANING, not just keywords

Build test search engine (see file test_search.py):

````


python test_search.py
````


## Task 8: 

Test your pipeline (see file test_rag_pipeline.py):

````

python test_rag_pipeline.py

````

## Task 9: Launch Your AI Assistant



Step 1: Start the server

cd /root/rag-assistant
python app.py






