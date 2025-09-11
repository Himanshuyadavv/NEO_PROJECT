import numpy as np
from models.llm import generate_response

class SimpleRAG:
    def __init__(self, documents):
        self.documents = documents
        self.knowledge_base = "\n".join(documents)
    
    def retrieve(self, query, k=3):
        """Simple retrieval - return relevant parts"""
        # For simplicity, return first k documents
        # In real implementation, use proper similarity search
        return self.documents[:k]
    
    def generate_answer(self, query, mode="concise"):
        """Generate answer based on knowledge base"""
        if not self.documents:
            return "No knowledge base loaded. Please upload a TXT file first."
        
        # Create prompt with context
        prompt = f"""Based on this knowledge:

{self.knowledge_base}

Question: {query}

Please provide a {"concise" if mode == "concise" else "detailed"} answer:"""
        
        return generate_response(prompt, mode)