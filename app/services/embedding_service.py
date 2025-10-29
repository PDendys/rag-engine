from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ):
        self.model = SentenceTransformer(model_name)

    def create_embedding(self, text: str) -> list[float]:
        return self.model.encode(text).tolist()