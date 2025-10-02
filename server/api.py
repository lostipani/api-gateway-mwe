from typing import Any

from fastapi import FastAPI

app = FastAPI(title="A FIFO in-memory list")

data = []


@app.get("/list")
async def show():
    """
    Show list.
    """
    return ", ".join(data)


@app.post("/list/{value}")
async def insert(value: Any):
    """
    Insert value.
    """
    data.append(value)
    return "Item inserted"


@app.delete("/list")
async def pop():
    """
    Take out first value.
    """
    return data.pop(0)
