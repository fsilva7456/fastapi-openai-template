# FastAPI OpenAI Template

A production-ready template for creating AI-powered APIs using FastAPI and OpenAI.

## Features

- FastAPI with async/await support
- OpenAI integration with GPT-4 Turbo
- Environment configuration
- Deployment-ready (Railway, Heroku, etc.)
- CORS middleware configured
- Type hints and Pydantic models
- Error handling

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration management
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   └── openai_service.py
│   └── schemas/            # Pydantic models
│       ├── __init__.py
│       ├── request.py
│       └── response.py
├── .env.example            # Environment variables template
├── requirements.txt        # Python dependencies
├── Procfile               # Deployment configuration
├── runtime.txt            # Python version specification
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-openai-template.git
cd fastapi-openai-template
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\\venv\\Scripts\\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

5. Run the server:
```bash
uvicorn app.main:app --reload
```

## Usage

1. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

2. Make a test request:
```bash
curl -X POST "http://localhost:8000/api/v1/analyze" \
     -H "Content-Type: application/json" \
     -d '{
           "query": "Analyze the current trends in electric vehicles",
           "analysis_type": "market research",
           "max_tokens": 1000,
           "temperature": 0.7
         }'
```

## Deployment

### Railway

1. Create a new project on Railway
2. Connect your GitHub repository
3. Add environment variables:
   - `OPENAI_API_KEY`
   - `ENVIRONMENT=production`
4. Deploy!

## Customization

1. Modify `app/schemas/request.py` to change input parameters
2. Modify `app/schemas/response.py` to change response structure
3. Add new endpoints in `app/main.py`
4. Add new services in `app/services/`

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

MIT