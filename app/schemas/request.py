from pydantic import BaseModel, Field
from typing import Optional, Dict

class AIAnalysisRequest(BaseModel):
    query: str = Field(..., description="The input text to analyze")
    analysis_type: str = Field(..., description="Type of analysis to perform (e.g., 'market research', 'sentiment analysis', etc.)")
    max_tokens: Optional[int] = Field(None, description="Maximum tokens in the response")
    temperature: Optional[float] = Field(None, description="Temperature for response creativity (0.0-1.0)")
    additional_context: Optional[Dict] = Field(None, description="Any additional context for the analysis")
