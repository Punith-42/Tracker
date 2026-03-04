"""
Pydantic schemas for structured JSON responses in LLM Agent System.
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any

class SQLQueryResponse(BaseModel):
    """Structured response for SQL query generation."""
    sql_query: str = Field(description="The generated SQL query")
    reasoning: str = Field(description="Brief explanation of the query logic")
    confidence: float = Field(description="Confidence score between 0 and 1", ge=0, le=1)

class DataAnalysisResponse(BaseModel):
    """Structured response for data analysis and formatting."""
    response: str = Field(description="Natural language response to the user's question")
    results: List[Dict[str, Any]] = Field(description="Structured data results from the query")
    summary: Dict[str, Any] = Field(description="Summary statistics and insights")
    metadata: Dict[str, Any] = Field(description="Additional metadata about the analysis")
