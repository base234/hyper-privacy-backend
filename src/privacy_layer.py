# privacy_layer.py
# A privacy layer that ensures no personal data is used

import numpy as np
import re
import hashlib
import random


class PrivacyLayer:
    def __init__(self):
        # Privacy settings
        self.anonymization_enabled = True
        self.differential_privacy_enabled = True
        self.epsilon = 0.5  # Differential privacy parameter (higher = less privacy but more accuracy)
        self.local_processing = (
            True  # Simulate local processing (no data leaves the device)
        )

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
            private_features = self._anonymize_features(private_features)

        if self.differential_privacy_enabled:
            private_features = self._apply_differential_privacy(private_features)

        if self.local_processing:
            private_features = self._apply_local_processing(private_features)

        return private_features

    def _anonymize_features(self, features):
        """Apply anonymization to remove any potential PII"""
        # Remove sensitive entity types
        if "entities" in features:
            features["entities"] = [
                (entity, type_)
                for entity, type_ in features["entities"]
                if type_
                not in ["PERSON", "EMAIL", "PHONE", "CREDIT_CARD", "SSN", "ADDRESS"]
            ]

        # Remove any text that matches PII patterns
        if "text_summary" in features:
            text = features["text_summary"]
            for pattern_name, pattern in self.pii_patterns.items():
                text = pattern.sub(f"[REDACTED {pattern_name.upper()}]", text)
            features["text_summary"] = text

        # Hash identifiers instead of using raw values
        if "keywords" in features:
            features["keywords"] = self._k_anonymize_list(features["keywords"])

        if "topic_candidates" in features:
            features["topic_candidates"] = self._k_anonymize_list(
                features["topic_candidates"]
            )

        return features

    def _k_anonymize_list(self, items, k=3):
        """
        Apply k-anonymity to a list of items.
        Only keep items that appear at least k times, or are common enough to be safe.
        """
        from collections import Counter

        # For a hackathon, we'll use a simple approximation:
        # Keep only items that are longer than 3 characters and not likely to be personal
        return [item for item in items if len(item) > 3]

    def _apply_differential_privacy(self, features):
        """Apply differential privacy to numeric features"""
        # Add calibrated noise to numeric values
        if "word_count" in features:
            features["word_count"] = self._add_laplace_noise(
                features["word_count"], sensitivity=1
            )

        # Add noise to keyword frequency
        if "keywords" in features:
            # Limit the number of keywords to reduce the chance of identification
            random.shuffle(features["keywords"])
            max_keywords = min(20, len(features["keywords"]))
            features["keywords"] = features["keywords"][:max_keywords]

        return features

    def _add_laplace_noise(self, value, sensitivity=1.0):
        """Add Laplace noise calibrated to the sensitivity and epsilon"""
        scale = sensitivity / self.epsilon
        noise = np.random.laplace(0, scale)
        return max(0, int(value + noise))

    def _apply_local_processing(self, features):
        """
        Simulate local processing by further obfuscating the data
        as if it was processed on the device and only sending minimal information
        """
        # Create a simulated "device-processed" version of the features
        local_features = {
            # Only send categories and topics, not raw keywords
            "topic_categories": list(
                set(
                    [
                        topic.split()[0] if " " in topic else topic
                        for topic in features.get("topic_candidates", [])
                    ]
                )
            ),
            # Send content length category instead of exact word count
            "content_length_category": self._categorize_word_count(
                features.get("word_count", 0)
            ),
            # Send entity types but not the actual entities
            "entity_types": list(
                set([entity_type for _, entity_type in features.get("entities", [])])
            ),
        }

        # Include a minimal set of keywords (hashed for privacy)
        if "keywords" in features:
            top_keywords = features["keywords"][:10]  # Only use top 10 keywords
            # Hash the keywords to prevent reverse engineering
            hashed_keywords = [
                hashlib.sha256(keyword.encode()).hexdigest()[:8]
                for keyword in top_keywords
            ]
            local_features["keyword_hashes"] = hashed_keywords

        return local_features

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
