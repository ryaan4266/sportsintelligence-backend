# Athena Sports Intelligence Backend

Athena Sports Intelligence Backend is the Phase 1 API foundation for the Athena Sports Intelligence project. This backend currently provides a clean FastAPI application structure, PostgreSQL database setup, environment configuration, CORS configuration, and a health check endpoint.

The frontend runs separately from this backend.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- python-dotenv
- Uvicorn
- CORS middleware

## Project Structure

```text
app/
  main.py              FastAPI app setup, CORS, and route registration
  config.py            Environment variable loading and app settings
  database.py          SQLAlchemy engine, session, Base, and get_db dependency
  models/              Future SQLAlchemy database models
    __init__.py
  schemas/             Future Pydantic request and response schemas
    __init__.py
  routes/              API route modules
    __init__.py
    health.py          GET /health endpoint
  services/            Future business logic helpers
    __init__.py
requirements.txt      Python dependencies for this backend
.env.example          Example environment variables
README.md             Local setup instructions
```

## Local Setup

### 1. Create a Virtual Environment

From the project root, run:

```bash
python -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

On Windows, use:

```bash
venv\Scripts\activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Create Your Environment File

Copy the example environment file:

```bash
cp .env.example .env
```

Open `.env` and update the values if needed:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/athena_sports
FRONTEND_URL=http://localhost:5173
```

Do not commit private database credentials.

### 4. Prepare PostgreSQL

Make sure PostgreSQL is running locally and create a database named:

```text
athena_sports
```

The default local connection string expects:

```text
postgresql://postgres:password@localhost:5432/athena_sports
```

Update `DATABASE_URL` in `.env` if your PostgreSQL username, password, host, port, or database name is different.

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

The backend should start at:

```text
http://127.0.0.1:8000
```

### 6. Test the Health Endpoint

Visit this URL in your browser:

```text
http://127.0.0.1:8000/health
```

Or test it with curl:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "Athena Sports Intelligence API"
}
```

## Notes

- This repo is backend-only.
- The frontend runs separately and should use the backend API URL.
- `FRONTEND_URL` controls which frontend origin is allowed by CORS.
- This is Phase 1 setup only. Authentication, sports models, analytics, Redis, WebSockets, AI, testing, Docker, and deployment are intentionally not included yet.
