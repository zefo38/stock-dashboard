from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import JSONResponse, HTMLResponse
from kis_api import get_access_token, get_stock_balance, get_stock_price


app = FastAPI()

# 토큰 캐싱
_token = None

def get_token():
    global _token
    if not _token:
        _token = get_access_token()
    return _token

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """메인 페이지"""
    with open("templates/index.html","r",encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(content=html)

@app.get("/api/balance")
async def balance():
    """잔고 조회 API"""
    try:
        token = get_token()
        data = get_stock_balance(token)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/api/price/{stock_code}")
async def price(stock_code: str):
    """현재가 조회 API"""
    try:
        token = get_token()
        price_data = get_stock_price(token, stock_code)
        return JSONResponse(content=price_data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)