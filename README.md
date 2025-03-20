# Hyper Privacy Backend
A next-generation ad recommendation engine that delivers hyper-relevant suggestions leaving your personal data in your device.

Frontend: [https://github.com/base234/hyper-privacy-frontend](https://github.com/base234/hyper-privacy-frontend)

## Overview

Traditional Ad targeting relies on collecting vast amounts of data which also includes your personal data, thus creating privacy concerns.

The project creates effective Ad recommendations while respecting user privacy. It uses contextual analysis and privacy-preserving techniques (Privacy Layer) to provide relevant recommendations without tracking users.

## Key Features

- **Content-based Analysis**: Analyze webpage content to understand context and topics
- **Privacy-Preserving Techniques**:
  - Differential Privacy: Add statistical noise to prevent identification
  - Local Processing: Simulate processing on the user's device
  - Anonymization: Remove any potentially identifying information
- **Contextual Matching**: Match ads based on content relevance, not user behavior
- **Transparency**: Clear explanation of how ad recommendations are made

To ensure no personal data is used.

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

Remove any potentially identifying information from the content analysis.

## Demo

The application includes a web interface to interact with the application in a useful way, demonstrating how the system works:

1. Enter webpage content
2. See the recommended ads
3. The **relevance score** and how it **targeted the Ads**, thus shows how privacy is preserved.

## Future Scope

- Implement federated learning for improving recommendations without collecting user data
- Add more sophisticated content analysis techniques
- Develop a browser extension for real-world testing
- Implement encrypted computation techniques

## Technology Stack

- **Backend**: Python, FastAPI
- **NLP (Natural Language Processing)**: spaCy (en_core_web_sm) for content analysis
- **ML (Machine Learning)**: scikit-learn for feature extraction and similarity matching
- **Frontend**: React for the interactive interface

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

## Activating the virtual environment on different OS
### On Windows
```
source venv\Scripts\activate
```
```
venv\Scripts\activate
```
### On Windows (Git Bash)
```
source venv\\Scripts\\activate
```
```
venv\\Scripts\\activate
```
### On macOS/Linux
```
source venv/bin/activate
```
```
venv/bin/activate
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

## Run a Quick Test? (Test)
Wanna run a quick test to see if everything is working?
```
python test.py
```

## Test the API with cURL (Run from API testing software)
Test the API endpoint (from API testing software) like **Postman**.
```
curl -X POST http://localhost:8000/recommend -d "content=The future of artificial intelligence is transforming healthcare and technology sectors, creating new opportunities for innovation while raising important questions about privacy and ethics."
```

## Run the API Server (Actual Server)
From project root directory
```
uvicorn api.app:app --reload
```

The access the API documentation at http://localhost:8000/docs


# Common Troubleshoot, if you run into any issues

**Module not found errors:**

- Make sure you're running from the root directory
- virtual environment (venv) is activated.


**spaCy model errors:**
if you get errors about missing models, then run the following command:
```
python -m spacy download en_core_web_sm
```


**Import errors within your modules:**

You might need to adjust the import paths in your Python files
