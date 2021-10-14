from typing import Dict, List
from typing import List, Dict

from pydantic import BaseModel


class LuckyBets(BaseModel):
    game: int
    numbers: List

class MultipleLuckyBetsResponse(BaseModel):
    data: List[LuckyBets]
