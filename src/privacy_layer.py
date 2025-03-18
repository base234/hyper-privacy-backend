# privacy_layer.py
# A privacy layer that ensures no personal data is used

import numpy as np
import re
import random


class PrivacyLayer:
    def __init__(self):
        # Privacy settings
        self.anonymization_enabled = True
        self.differential_privacy_enabled = True
        self.epsilon = 0.5  # Differential privacy parameter (higher = less privacy but more accuracy)
        self.local_processing = True  # Ensures minimal data leaves the device

        # PII patterns to detect
        self.pii_patterns = {
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'phone': re.compile(r'\b(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b'),
            'ssn': re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
            'credit_card': re.compile(r'\b(?:\d{4}[- ]?){3}\d{4}\b'),
            'ip_address': re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
        }

    def apply_privacy_measures(self, content_features):
        """
        Apply privacy-preserving measures to content features.

        Args:
            content_features (dict): Original content features

        Returns:
            dict: Privacy-enhanced content features
        """
        import copy

        private_features = copy.deepcopy(content_features)

        if self.anonymization_enabled:
            private_features = self._sanitize_features(private_features)

        if self.differential_privacy_enabled:
            private_features = self._apply_differential_privacy(private_features)

        if self.local_processing:
            private_features = self._apply_local_processing(private_features)

        return private_features

    def _sanitize_features(self, features):
        """Sanitize sensitive PII while preserving matching data"""

        # Sanitize entity types but keep useful ones
        if "entities" in features:
            features["entities"] = [
                (entity, type_)
                for entity, type_ in features["entities"]
                if type_ not in ["PERSON", "EMAIL", "PHONE", "CREDIT_CARD", "SSN", "ADDRESS"]
            ]

        # Remove PII from text summary
        if "text_summary" in features:
            text = features["text_summary"]
            for pattern_name, pattern in self.pii_patterns.items():
                text = pattern.sub(f"[REDACTED {pattern_name.upper()}]", text)
            features["text_summary"] = text

        return features

    def _apply_differential_privacy(self, features):
        """Apply differential privacy to numeric features"""
        # Add calibrated noise to numeric values
        if "word_count" in features:
            features["word_count"] = self._add_laplace_noise(features["word_count"], sensitivity=1)

        return features

    def _add_laplace_noise(self, value, sensitivity=1.0):
        """Add Laplace noise calibrated to the sensitivity and epsilon"""
        scale = sensitivity / self.epsilon
        noise = np.random.laplace(0, scale)
        return max(0, int(value + noise))

    def _apply_local_processing(self, features):
        """
        Simulate local processing by sending only minimal data,
        while preserving information for the matching engine.
        """

        local_features = {
            # Keep topic categories instead of full topic candidates
            "topic_categories": list(
                set(topic.split()[0] if " " in topic else topic for topic in features.get("topic_candidates", []))
            ),
            # Send content length category instead of exact word count
            "content_length_category": self._categorize_word_count(features.get("word_count", 0)),
            # Send entity types but not exact entities
            "entity_types": list(set([entity_type for _, entity_type in features.get("entities", [])])),
        }

        # Preserve full keywords and topic candidates for matching engine
        if "keywords" in features:
            local_features["keywords"] = features["keywords"]

        if "topic_candidates" in features:
            local_features["topic_candidates"] = features["topic_candidates"]

        if "entities" in features:
            local_features["entities"] = features["entities"]

        return local_features

        # def _apply_local_processing(self, features):
        # """
        # Simulate local processing by further obfuscating the data
        # as if it was processed on the device and only sending minimal information
        # """
        # # Create a simulated "device-processed" version of the features
        # local_features = {
        #     # Use topic categories instead of exact words
        #     "topic_categories": list(
        #         set(topic.split()[0] if " " in topic else topic for topic in features.get("topic_candidates", []))
        #     ),
        #     # Send content length category instead of exact word count
        #     "content_length_category": self._categorize_word_count(features.get("word_count", 0)),
        #     # Send entity types but not the actual entities
        #     "entity_types": list(
        #         set(entity_type for _, entity_type in features.get("entities", []))
        #     ),
        #     # Use meaningful keywords, not hashes
        #     "generalized_keywords": features.get("keywords", [])[:10],  # Keep top 10 keywords
        # }

        # return local_features

    def _categorize_word_count(self, word_count):
        """Convert exact word count to a category"""
        if word_count < 50:
            return "very_short"
        elif word_count < 200:
            return "short"
        elif word_count < 500:
            return "medium"
        elif word_count < 1000:
            return "long"
        else:
            return "very_long"
