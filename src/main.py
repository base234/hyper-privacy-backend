# src/main.py
from src.content_analyzer import ContentAnalyzer
from src.ad_classifier import AdClassifier
from src.matching_engine import MatchingEngine
from src.privacy_layer import PrivacyLayer


class PrivacyAdEngine:
    def __init__(self):
        self.content_analyzer = ContentAnalyzer()
        self.ad_classifier = AdClassifier()
        self.matching_engine = MatchingEngine()
        self.privacy_layer = PrivacyLayer()

        # Load sample ads (for hackathon demo)
        self._load_sample_ads()

    def _load_sample_ads(self):
        # More diverse sample ads for a better demo
        sample_ads = [
            {
                "content": "Get 50% off on the latest tech gadgets and smartphones! New models with AI features.",
                "metadata": {"category": "technology", "target_audience": "tech-savvy"},
            },
            {
                "content": "Healthy organic food delivery service. First week free! Fresh ingredients delivered to your door.",
                "metadata": {
                    "category": "health",
                    "target_audience": "health-conscious",
                },
            },
            {
                "content": "Online courses on data science and machine learning at discounted prices. Learn from industry experts.",
                "metadata": {"category": "education", "target_audience": "learners"},
            },
            {
                "content": "Travel packages to exotic destinations. Book now and save! Experience the adventure of a lifetime.",
                "metadata": {"category": "travel", "target_audience": "travelers"},
            },
            {
                "content": "New fitness app with personalized workout plans and nutrition advice. Stay fit and healthy!",
                "metadata": {
                    "category": "health",
                    "target_audience": "fitness-enthusiasts",
                },
            },
            {
                "content": "Sustainable fashion brands with eco-friendly materials. Stylish and good for the planet!",
                "metadata": {"category": "fashion", "target_audience": "eco-conscious"},
            },
            {
                "content": "Investment opportunities in renewable energy. Grow your portfolio while supporting green initiatives.",
                "metadata": {"category": "finance", "target_audience": "investors"},
            },
            {
                "content": "Smart home devices to automate your daily routines. Control everything from your phone!",
                "metadata": {"category": "technology", "target_audience": "homeowners"},
            },
            {
                "content": "Family-friendly vacation packages with activities for all ages. Create lasting memories together!",
                "metadata": {"category": "travel", "target_audience": "families"},
            },
            {
                "content": "Professional financial advisory services. Plan your future with expert guidance.",
                "metadata": {"category": "finance", "target_audience": "professionals"},
            },
        ]

        for ad in sample_ads:
            self.matching_engine.add_ad(ad["content"], ad["metadata"])

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

        # Prepare the response
        response = {
            "recommended_ads": matches,
            "privacy_metrics": {
                "anonymization_applied": self.privacy_layer.anonymization_enabled,
                "differential_privacy_applied": self.privacy_layer.differential_privacy_enabled,
                "local_processing_simulated": self.privacy_layer.local_processing,
            },
        }

        # Only include content topics if they exist in the private features
        if "topic_categories" in private_features:
            response["content_topics"] = private_features["topic_categories"]
        elif "topic_candidates" in private_features:
            response["content_topics"] = private_features["topic_candidates"][:5]

        return response
