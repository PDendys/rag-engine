
from typing import List, Dict, Any
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class RerankerService:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-12-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def rerank(self, query: str, chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        ranked_items = []

        for chunk in chunks:
            chunk_text = chunk.get('payload', {}).get('text', '')
            
            inputs = self.tokenizer(query, chunk_text, return_tensors="pt", truncation=True)
            with torch.no_grad():
                score = self.model(**inputs).logits.item()
            
            ranked_item = {
                **chunk,
                "score": float(score)
            }
            ranked_items.append(ranked_item)

        ranked_items.sort(key=lambda x: x["score"], reverse=True)
        return ranked_items