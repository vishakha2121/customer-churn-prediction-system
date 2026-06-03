from fastapi import Header, HTTPException
from typing import Optional

async def get_token_header(x_token: Optional[str] = Header(None)):
    if x_token is None:
        raise HTTPException(status_code=400, detail="X-Token header missing")
    return x_token

async def get_query_params(
    skip: int = 0,
    limit: int = 100,
    segment_id: Optional[int] = None,
    min_probability: Optional[float] = None
):
    return {
        "skip": skip,
        "limit": limit,
        "segment_id": segment_id,
        "min_probability": min_probability
    }