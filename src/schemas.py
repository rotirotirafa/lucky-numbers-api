from typing import List

from pydantic import BaseModel


class LuckyBets(BaseModel):
    game: int
    numbers: List

class MultipleLuckyBetsResponse(BaseModel):
    data: List[LuckyBets]
