# Privacy-First Innovation

Build a next-gen ad recommendation engine that delivers hyper-relevant suggestions — without ever tracking personal data.

## Create virtual environment
```
python -m venv venv
```

## Activate virtual environment
### On Windows
```
source venv\Scripts\activate
```
### On macOS/Linux
```
source venv/bin/activate
```
### On Windows (Git Bash)
```
source venv\\Scripts\\activate
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
