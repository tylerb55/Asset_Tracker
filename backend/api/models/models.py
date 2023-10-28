from pydantic import BaseModel
from typing import Annotated, Dict, List, Literal, Tuple, Optional

class Stock(BaseModel):
    name: str
    code: str
    price: Optional[float] = None
    story_rank: Optional[int] = None
    sentiment_score_daily: Optional[float] = None
    sentiment_score_weekly: Optional[float] = None
    sentiment_score_monthly: Optional[float] = None
    sentiment_score_annually: Optional[float] = None

class Crypto(BaseModel):
    name: str
    code: str
    price: Optional[float] = None
    story_rank: Optional[int] = None
    sentiment_score_daily: Optional[float] = None
    sentiment_score_weekly: Optional[float] = None
    sentiment_score_monthly: Optional[float] = None
    sentiment_score_annually: Optional[float] = None

class Sentiment(BaseModel):
    sentence: str
    label: str
    score: float


monero = Crypto(name='Monero', code='XMR')