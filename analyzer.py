from transformers import pipeline


class SentimentAnalyzer:

    def __init__(self):
        print("Loading model...")
        self.model = pipeline("sentiment-analysis")

    def analyze(self, text):
        result = self.model(text)[0]
        return result["label"], result["score"]