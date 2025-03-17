# Privacy-First Ad Recommendation Engine
A next-generation ad recommendation engine that delivers hyper-relevant suggestions without tracking personal data.

## Overview

This project demonstrates how to create effective ad recommendations while respecting user privacy. Traditional ad targeting relies on collecting vast amounts of personal data, creating privacy concerns. Our solution uses contextual analysis and privacy-preserving techniques to provide relevant recommendations without tracking users.

## Key Features

- **Content-based Analysis**: Analyze webpage content to understand context and topics
- **Privacy-Preserving Techniques**:
  - Differential Privacy: Add statistical noise to prevent identification
  - Local Processing: Simulate processing on the user's device
  - Anonymization: Remove any potentially identifying information
- **Contextual Matching**: Match ads based on content relevance, not user behavior
- **Transparency**: Clear explanation of how ad recommendations are made

## Technology Stack

- **Backend**: Python with FastAPI
- **NLP**: spaCy for content analysis
- **ML**: scikit-learn for feature extraction and similarity matching
- **Frontend**: HTML/JS for demonstration

## How It Works

1. **Content Analysis**: Webpage content is analyzed to extract topics, entities, and keywords
2. **Privacy Layer**: Personal identifiers are removed, and privacy-preserving techniques are applied
3. **Ad Matching**: The system matches ads to content based on relevance
4. **Result Delivery**: Relevant ads are returned without tracking the user

## Privacy Techniques

### Differential Privacy

We add calibrated noise to numerical values, making it impossible to determine if a specific user's data was used in the computation.

### Local Processing

Data processing happens on the user's device, with only anonymized features sent to the server.

### Anonymization

We remove any potentially identifying information from the content analysis.

## Demo

The application includes a web interface demonstrating how the system works:

1. Enter webpage content
2. See the recommended ads
3. Understand how privacy was preserved

## Future Scope

- Implement federated learning for improving recommendations without collecting user data
- Add more sophisticated content analysis techniques
- Develop a browser extension for real-world testing
- Implement encrypted computation techniques

## Getting Started with the Project

### Prerequisites

- Python 3.11
- FastAPI
- Virtual environment (venv)

---

### Create virtual environment
```
python -m venv venv
```

## Activating the virtual environment on different operating systems
### On Windows
```
source venv\Scripts\activate
```
### On Windows (Git Bash)
```
source venv\\Scripts\\activate
```
### On macOS/Linux
```
source venv/bin/activate
```


## Install dependencies
```
pip install -r requirements.txt
```

## Download spaCy model
```
python -m spacy download en_core_web_sm
```

---

## Run the Quick Test
From project root directory
```
python test.py
```

---

## Run the API Server
From project root directory
```
uvicorn api.app:app --reload
```

The access the API documentation at http://localhost:8000/docs

---

## Test the API with cURL
Test the API endpoint
```
curl -X POST http://localhost:8000/recommend -d "content=The future of artificial intelligence is transforming healthcare and technology sectors, creating new opportunities for innovation while raising important questions about privacy and ethics."
```

---

# Common Troubleshooting

### Module not found errors:

Make sure you're running from the root directory and your virtual environment is activated.


### spaCy model errors:
if you get errors about missing models, then run the following command:
```
python -m spacy download en_core_web_sm
```


### Import errors within your modules:

You might need to adjust the import paths in your Python files
