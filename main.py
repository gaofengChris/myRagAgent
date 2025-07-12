def main():
    print('RAG system starting...')
from src.retrieval.retriever import retrieve
from src.generation.generator import generate
if __name__ == '__main__':
    query = 'RAG systems'
    context = retrieve(query)
    response = generate(context[0], query)
    print(response)
