import google.generativeai as genai
import time
import numpy as np
from config.config import GEMINI_API_KEY

# Configure Gemini with error handling
try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    # Continue but embeddings will fail gracefully

def get_embeddings(texts, max_retries=3):
    """Get embeddings using Gemini embeddings API with robust error handling."""
    if not GEMINI_API_KEY:
        print("Warning: No Gemini API key configured. Using random embeddings as fallback.")
        return [list(np.random.rand(768).astype(np.float32)) for _ in texts]
    
    model = "models/embedding-001"
    embeddings = []
    
    for text in texts:
        if not text or len(text.strip()) == 0:
            # Handle empty text
            embeddings.append([0] * 768)
            continue
            
        # Truncate text if it's too long
        if len(text) > 10000:
            text = text[:10000]
            
        for attempt in range(max_retries):
            try:
                resp = genai.embed_content(model=model, content=text)
                if "embedding" in resp:
                    embeddings.append(resp["embedding"])
                    break
                else:
                    raise ValueError("No embedding found in response")
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"Failed to get embedding after {max_retries} attempts: {e}")
                    # Return a random vector as fallback
                    embeddings.append(list(np.random.rand(768).astype(np.float32)))
                else:
                    # Wait before retrying (exponential backoff)
                    time.sleep(2 ** attempt)
    
    return embeddings