# FastAPI Authentication Example

A simple API with JWT authentication using FastAPI.

## Setup

```bash
# 1. Clone the repo
git clone <repo-url>
cd fastapi-auth-api

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn main:app --reload
