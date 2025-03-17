# matching_engine.py
class MatchingEngine:
    def __init__(self):
        # Initialize with empty ad inventory
        self.ad_inventory = []

    def add_ad(self, ad_content, ad_metadata=None):
        """Add an ad to the inventory with its classification"""
        from ad_classifier import AdClassifier

        classifier = AdClassifier()
        ad_data = classifier.classify_ad(ad_content, ad_metadata)
        self.ad_inventory.append(
            {
                "content": ad_content,
                "metadata": ad_metadata or {},
                "classification": ad_data,
            }
        )

    def match_content(self, content_features):
        """
        Match content features with relevant ads.

        Args:
            content_features (dict): Features extracted from content

        Returns:
            list: Ranked list of matching ads
        """
        matches = []

        # Extract content keywords and topics
        content_keywords = set(content_features["keywords"])
        content_topics = set(content_features["topic_candidates"])

        # Match with ads
        for ad in self.ad_inventory:
            ad_keywords = set(ad["classification"]["keywords"])
            ad_categories = set(ad["classification"]["categories"])

            # Calculate simple relevance score
            keyword_overlap = len(content_keywords.intersection(ad_keywords))
            category_match = sum(
                1
                for topic in content_topics
                if any(cat in topic for cat in ad_categories)
            )

            relevance_score = keyword_overlap + category_match

            if relevance_score > 0:
                matches.append(
                    {
                        "ad": ad,
                        "relevance_score": relevance_score,
                        "match_reason": "Content keywords and topics match",
                    }
                )

        # Sort by relevance score
        matches.sort(key=lambda x: x["relevance_score"], reverse=True)
        return matches[:5]  # Return top 5 matches
