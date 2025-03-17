# api/app.py

from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import sys
import os
import json

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import PrivacyAdEngine

app = FastAPI(title="Privacy-First Ad Recommendation API")

# Configure CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For hackathon; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the ad engine
ad_engine = PrivacyAdEngine()


@app.post("/recommend")
# async def recommend_ads(content: str = Form(...)):
async def recommend_ads(request: Request):
    request_data = await request.json()
    content = request_data['data']['content']
    """
    Recommend ads based on content without using personal data.
    """
    try:
        result = ad_engine.process_content(content)

        # Serialize the result for JSON response
        # This handles NumPy types and other non-JSON serializable objects
        cleaned_result = json.loads(
            json.dumps(
                result,
                default=lambda o: float(o) if hasattr(o, "__float__") else str(o),
            )
        )

        return JSONResponse(content=cleaned_result)
    except Exception as e:
        import traceback

        print(traceback.format_exc())
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/health")
async def health_check():
    """API health check endpoint"""
    return {"status": "healthy"}


# Create a static directory for the frontend demo
os.makedirs("static", exist_ok=True)

# Write the frontend HTML file
with open("static/index.html", "w") as f:
    f.write(
        """
<!DOCTYPE html>
<html lang="en">
<!-- Front-end code here (copy from the HTML artifact) -->
</html>
    """
    )

# Mount the static directory
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
