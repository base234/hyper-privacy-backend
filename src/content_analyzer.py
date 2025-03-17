# content_analyzer.py
class ContentAnalyzer:
    def __init__(self):
        # Initialize NLP tools
        import nltk

        nltk.download("punkt")
        nltk.download("stopwords")
        self.stopwords = set(nltk.corpus.stopwords.words("english"))

        # Optional: Load spaCy for better entity recognition
        import spacy

        self.nlp = spacy.load("en_core_web_sm")

    def analyze(self, content):
        """
        Analyze webpage content and extract key information.

        Returns:
            dict: Content features including keywords, entities, topics
        """
        # Process text
        doc = self.nlp(content)

        # Extract keywords (excluding stopwords)
        keywords = [
            token.lemma_.lower()
            for token in doc
            if not token.is_stop and not token.is_punct and token.is_alpha
        ]

        # Extract named entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Extract noun phrases (potential topics)
        noun_phrases = [chunk.text for chunk in doc.noun_chunks]

        # Basic topic extraction (can be improved with more sophisticated methods)
        topic_candidates = [
            token.lemma_.lower()
            for token in doc
            if token.pos_ in ("NOUN", "PROPN") and not token.is_stop
        ]

        return {
            "keywords": keywords,
            "entities": entities,
            "noun_phrases": noun_phrases,
            "topic_candidates": topic_candidates,
            "word_count": len(doc),
            "text_summary": content[:200] + "..." if len(content) > 200 else content,
        }
