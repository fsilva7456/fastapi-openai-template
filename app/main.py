from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.services.openai_service import OpenAIService
from app.config import Settings, get_settings
from app.schemas.request import AIAnalysisRequest
from app.schemas.response import AIAnalysisResponse

app = FastAPI(
    title="FastAPI OpenAI Template",
    description="A template for creating AI-powered APIs using FastAPI and OpenAI",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

@app.post("/api/v1/analyze",
    response_model=AIAnalysisResponse,
    description="Generic endpoint for AI analysis")
async def analyze(
    request: AIAnalysisRequest,
    settings: Settings = Depends(get_settings)
):
    try:
        openai_service = OpenAIService(settings.openai_api_key)
        
        # Generate system prompt based on the analysis type
        system_prompt = f"You are an expert in {request.analysis_type}. "
        system_prompt += "Provide detailed, actionable insights based on the given input."
        
        # Process the query
        response = await openai_service.get_analysis(
            user_prompt=request.query,
            system_prompt=system_prompt,
            max_tokens=request.max_tokens or 1000,
            temperature=request.temperature or 0.7
        )
        
        # Return structured response
        return AIAnalysisResponse(
            query=request.query,
            analysis_type=request.analysis_type,
            result=response,
            metadata={
                "model": "gpt-4-turbo-preview",
                "max_tokens": request.max_tokens or 1000,
                "temperature": request.temperature or 0.7
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
