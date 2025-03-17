# matching_engine.py
# A matching engine that connects content to relevant ads

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MatchingEngine:
    def __init__(self):
        # Initialize with empty ad inventory
        self.ad_inventory = []
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.ad_vectors = None
        self.feature_names = None

    def add_ad(self, ad_content, ad_metadata=None):
        """Add an ad to the inventory with its classification"""
        from src.ad_classifier import AdClassifier
        classifier = AdClassifier()

        ad_data = classifier.classify_ad(ad_content, ad_metadata)
        self.ad_inventory.append({
            "content": ad_content,
            "metadata": ad_metadata or {},
            "classification": ad_data,
        })

        # Update vectors when a new ad is added
        self._update_vectors()

    def _update_vectors(self):
        """Update TF-IDF vectors for all ads"""
        if not self.ad_inventory:
            return

        # Extract ad content and create vectors
        ad_texts = [ad["content"] for ad in self.ad_inventory]
        self.ad_vectors = self.vectorizer.fit_transform(ad_texts)
        self.feature_names = self.vectorizer.get_feature_names_out()

    def match_content(self, content_features):
        """
        Match content features with relevant ads.

        Args:
            content_features (dict): Features extracted from content

        Returns:
            list: Ranked list of matching ads
        """
        if not self.ad_inventory:
            return []

        # Combine features into a single text document
        content_text = " ".join(content_features.get("keywords", []) +
                               content_features.get("topic_candidates", []) +
                               [e[0] for e in content_features.get("entities", [])])
        matches = []

        # 1. Content-based matching using TF-IDF and cosine similarity
        content_vector = self.vectorizer.transform([content_text])
        similarity_scores = cosine_similarity(content_vector, self.ad_vectors)[0]

        # 2. Keyword matching (with weights)
        content_keywords = set(content_features.get("keywords", []))
        content_topics = set(content_features.get("topic_candidates", []))

        # 3. Combine the scores
        for i, ad in enumerate(self.ad_inventory):
            # Get similarity score from TF-IDF
            tfidf_score = similarity_scores[i]

            # Calculate keyword matching score
            ad_keywords = set(ad["classification"].get("keywords", []))
            keyword_overlap = len(content_keywords.intersection(ad_keywords))

            # Calculate context relevance score
            ad_categories = set(ad["classification"].get("categories", []))
            category_match = sum(
                1
                for topic in content_topics
                if any(cat in topic for cat in ad_categories)
            )

            # Calculate weighted score
            # We can adjust these weights based on performance
            final_score = (
                (0.5 * tfidf_score)
                + (0.3 * (keyword_overlap / max(1, len(content_keywords))))
                + (0.2 * category_match)
            )

            # Add to matches
            matches.append(
                {
                    "ad": ad,
                    "relevance_score": float(
                        final_score
                    ),  # Convert to float for JSON serialization
                    "match_factors": {
                        "content_similarity": float(tfidf_score),
                        "keyword_overlap": keyword_overlap,
                        "category_relevance": category_match,
                    },
                    "match_reason": self._generate_match_reason(ad, content_features),
                }
            )

        # Sort by relevance score
        matches.sort(key=lambda x: x["relevance_score"], reverse=True)
        return matches[:5]  # Return top 5 matches

    def _generate_match_reason(self, ad, content_features):
        """Generate a human-readable reason for the match"""
        ad_keywords = set(ad["classification"]["keywords"])
        content_keywords = set(content_features.get("keywords", []))
        common_keywords = ad_keywords.intersection(content_keywords)

        if common_keywords:
            return f"Matched based on keywords: {', '.join(list(common_keywords)[:3])}"

        ad_categories = set(ad["classification"]["categories"])
        content_topics = set(content_features.get("topic_candidates", []))
        matched_topics = [
            topic
            for topic in content_topics
            if any(cat in topic for cat in ad_categories)
        ]

        if matched_topics:
            return f"Matched based on topics: {', '.join(matched_topics[:3])}"

        return "Matched based on content similarity"
