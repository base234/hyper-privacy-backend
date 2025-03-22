# ad_classifier.py
# A basic ad classifier that categorizes ads

from data.sample_categories import get_sample_categories

class AdClassifier:
    def __init__(self):
        # Initialize vectorizer
        from sklearn.feature_extraction.text import TfidfVectorizer

        self.vectorizer = TfidfVectorizer(max_features=1000)

        # Using simple categorization approach for the purpose of hackathon
        self.categories = get_sample_categories()

    def classify_ad(self, ad_content, ad_metadata=None):
        """
        Classify an ad based on its content and metadata.

        Args:
            ad_content (str): The ad text content
            ad_metadata (dict): Additional ad metadata

        Returns:
            dict: Ad classification including categories and keywords
        """

        # Extract keywords using TF-IDF
        if not hasattr(self, "tfidf_matrix"):
            # First time, fit the vectorizer
            self.tfidf_matrix = self.vectorizer.fit_transform([ad_content])
            self.feature_names = self.vectorizer.get_feature_names_out()
        else:
            # Transform new content
            self.tfidf_matrix = self.vectorizer.transform([ad_content])

        # Get top keywords
        feature_index = self.tfidf_matrix[0].nonzero()[1]
        tfidf_scores = zip(
            feature_index, [self.tfidf_matrix[0, x] for x in feature_index]
        )
        top_keywords = sorted(
            [(self.feature_names[i], s) for (i, s) in tfidf_scores],
            key=lambda x: x[1],
            reverse=True,
        )[:10]

        # Using a simple rule-based approach for categories for hackathon
        # In a real implementation, use trained classifier
        detected_categories = []
        for category in self.categories:
            if category in ad_content.lower() or any(
                category in kw for kw, _ in top_keywords
            ):
                detected_categories.append(category)

        # If no categories detected, use the most general one
        if not detected_categories:
            detected_categories = ["general"]

        return {
            "categories": detected_categories,
            "keywords": [kw for kw, _ in top_keywords],
            "ad_id": hash(ad_content) % 10000,  # Simple ad ID for demo
        }
