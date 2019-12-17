import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM


cls = "[CLS]"
sep = "[SEP]"


class BertEmbeddingsService:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')
        self.model.eval()

    def create_embeddings(self, text):
        marked_text = self.mark(text)
        tokenized_text = self.tokenizer.tokenize(marked_text)
        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)
        segments_ids = [1] * len(tokenized_text)

        tokens_tensor = torch.tensor([indexed_tokens])
        segments_tensors = torch.tensor([segments_ids])

        with torch.no_grad():
            encoded_layers, _ = self.model(tokens_tensor, segments_tensors)

        tokens_vecs = encoded_layers[11][0]
        sentence_embedding = torch.mean(tokens_vecs, dim=0)
        return sentence_embedding, tokenized_text

    @staticmethod
    def mark(text):
        marked_text = cls
        for sent in text:
            marked_text = marked_text + " " + sent + " " + sep
        return marked_text