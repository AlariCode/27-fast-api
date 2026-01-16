# GET Query rnd_from и rnd_to, возвращающий случайный int
# в этом диапазоне

import random
from fastapi import APIRouter, Depends, HTTPException

from .schema import RandQuery


router = APIRouter(
    prefix="/random"
)


@router.get("/")
def get_random(query: RandQuery = Depends()):
    return {
        "value": random.randint(query.rnd_from, query.rnd_to)
    }
