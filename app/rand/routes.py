# GET Query rnd_from и rnd_to, возвращающий случайный int
# в этом диапазоне

import random
from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/random"
)


@router.get("/")
def get_random(
    rnd_from: int = 0,
    rnd_to: int = 100
):
    if rnd_from > rnd_to:
        raise HTTPException(400, "rnd_from должно быть <= rnd_to")
    return {
        "value": random.randint(rnd_from, rnd_to)
    }
