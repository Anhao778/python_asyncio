#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI() 

@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app)


