from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.schemas import MultipleLuckyBetsResponse
from src.core import multiple_lucky_numbers

origins = ["*"]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"status": "live"}


@app.get("/megasena")
def create_random_megasena_games(bets: int = 1, numbers_quantity: int = 6) -> MultipleLuckyBetsResponse:
    response = multiple_lucky_numbers(bets, numbers_quantity)
    return MultipleLuckyBetsResponse(data=response)
