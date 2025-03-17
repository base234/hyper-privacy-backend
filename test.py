# test.py
from src.main import PrivacyAdEngine

# Initialize the engine
engine = PrivacyAdEngine()

# Test with sample content
test_content = """
The future of artificial intelligence is transforming how we interact with technology.
From smart assistants to recommendation systems, AI is becoming an integral part of our daily lives.
However, concerns about privacy and data protection remain significant challenges in this field.
"""

# Process the content
result = engine.process_content(test_content)

# Print the results
print("Content Topics:", result["content_topics"])
print("\nRecommended Ads:")
for match in result["recommended_ads"]:
    print(f"- {match['ad']['content']} (Score: {match['relevance_score']})")
print("\nPrivacy Metrics:", result["privacy_metrics"])
