from typing import Dict

from fastapi import FastAPI

from src.schemas import MultipleLuckyBetsResponse
from src.core import multiple_luckynumbers

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "live"}

@app.get("/megasena")
def create_random_megasena_games(bets: int = 1, numbers_quantity: int = 6) -> MultipleLuckyBetsResponse:
    response = multiple_luckynumbers(bets, numbers_quantity)
    return MultipleLuckyBetsResponse(data=response)
