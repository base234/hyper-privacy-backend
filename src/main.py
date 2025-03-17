# main.py
from content_analyzer import ContentAnalyzer
from ad_classifier import AdClassifier
from matching_engine import MatchingEngine
from privacy_layer import PrivacyLayer


class PrivacyAdEngine:
    def __init__(self):
        self.content_analyzer = ContentAnalyzer()
        self.ad_classifier = AdClassifier()
        self.matching_engine = MatchingEngine()
        self.privacy_layer = PrivacyLayer()

        # Load sample ads (for hackathon demo)
        self._load_sample_ads()

    def _load_sample_ads(self):
        # Sample ads for demonstration
        sample_ads = [
            "Get 50% off on the latest tech gadgets and smartphones!",
            "Healthy organic food delivery service. First week free!",
            "Online courses on data science and machine learning at discounted prices.",
            "Travel packages to exotic destinations. Book now and save!",
            "New fitness app with personalized workout plans and nutrition advice.",
        ]

        for ad in sample_ads:
            self.matching_engine.add_ad(ad)

    def process_content(self, content):
        """
        Process webpage content and find matching ads.

        Args:
            content (str): Webpage content

        Returns:
            dict: Matching ads and metrics
        """
        # Extract content features
        content_features = self.content_analyzer.analyze(content)

        # Apply privacy measures
        private_features = self.privacy_layer.apply_privacy_measures(content_features)

        # Find matching ads
        matches = self.matching_engine.match_content(private_features)

        return {
            "recommended_ads": matches,
            "content_topics": private_features.get("topic_candidates", [])[:5],
            "privacy_metrics": {
                "anonymization_applied": self.privacy_layer.anonymization_enabled,
                "differential_privacy_applied": self.privacy_layer.differential_privacy_enabled,
            },
        }
