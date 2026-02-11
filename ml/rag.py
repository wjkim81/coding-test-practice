# RAG (Retrieval-Augmented Generation) 핵심 코드 조각
# **1. Embedding + 검색 (가장 기본)**
# 이 정도는 눈 감고 짤 수 있어야 해
from openai import OpenAI

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# **2. 간단한 RAG 흐름**
def simple_rag(query, documents):
    # 1. query embedding
    q_emb = get_embedding(query)
    
    # 2. 유사도 계산 + 상위 k개
    scores = [(doc, cosine_similarity(q_emb, doc['embedding'])) 
              for doc in documents]
    top_k = sorted(scores, key=lambda x: x[1], reverse=True)[:3]
    
    # 3. context 구성 + LLM 호출
    context = "\n".join([doc['text'] for doc, _ in top_k])
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Context:\n{context}"},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content

# **3. Chunking 로직**

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks
