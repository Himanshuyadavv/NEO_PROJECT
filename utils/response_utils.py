from models.llm import generate_llm_response

def build_final_response(query, rag_chunks, web_results, mode):
    """Combine retrieved context + web search + query into a final LLM response."""
    
    # Build context from RAG chunks
    context = ""
    if rag_chunks and len(rag_chunks) > 0:
        context += "## Relevant Information from Knowledge Base:\n"
        for i, chunk in enumerate(rag_chunks, 1):
            context += f"{i}. {chunk}\n"
        context += "\n"
    
    # Build context from web results
    if web_results and len(web_results) > 0 and "No web results" not in web_results[0] and "Web search error" not in web_results[0]:
        context += "## Live Web Search Results:\n"
        for i, result in enumerate(web_results, 1):
            context += f"{i}. {result}\n"
        context += "\n"
    
    # Build the final prompt
    if context:
        prompt = f"""Based on the following information:

{context}
Please answer this question: {query}

Provide a {"concise" if mode == "concise" else "detailed"} answer:"""
    else:
        prompt = f"""Answer the following question: {query}

Provide a {"concise" if mode == "concise" else "detailed"} answer:"""
    
    print(f"Final prompt length: {len(prompt)} characters")
    return generate_llm_response(prompt, mode)