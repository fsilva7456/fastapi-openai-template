from pydantic import BaseModel
from typing import Dict, Optional

class AIAnalysisResponse(BaseModel):
    query: str
    analysis_type: str
    result: str
    metadata: Optional[Dict] = None
