
from retrieval.retriever import retrieve
from generation.generator import generate_answer


def answer_question(question, history=None):

    # Step 1: Retrieve relevant documents
    documents = retrieve(question)

    # Step 2: Build context
    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    # Step 3: Generate answer using context and history
    answer = generate_answer(
        question,
        context,
        history
    )

    return {
        "answer": answer
    }
