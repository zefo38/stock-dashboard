import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_KEY = os.getenv("KIS_APP_KEY")
APP_SECRET = os.getenv("KIS_APP_SECRET")
ACCOUNT_NO = os.getenv("KIS_ACCOUNT_NO")
ACCOUNT_PROD_CODE = os.getenv("KIS_ACCOUNT_PROD_CODE")
IS_MOCK = os.getenv("IS_MOCK", "true").lower() == "true"

# .env에서 IS_MOCK=true 면 모의투자 URL 자동 선택
# 나중에 실전으로 바꿀 때 .env에서 false만 바꾸기
BASE_URL = (
    "https://openapivts.koreainvestment.com:29443"  # 모의투자
    if IS_MOCK
    else "https://openapi.koreainvestment.com:9443"  # 실전투자
)

# 토큰 파일 경로
TOKEN_FILE = "token.json"

# 토큰 파일에 저장
def save_token(token: str):
    data = {
        "access_token": token,
        "saved_at":time.time() # 저장 시간 기록
    }
    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f)
    print("✅ 토큰 파일 저장 완료!")

# 토큰 파일에서 불러오기
def load_token() -> str|None:
    # 파일 없으면 None 반환
    if not os.path.exists(TOKEN_FILE):
        print("토큰 파일 없음 -> 새로 발급")
        return None

    with open(TOKEN_FILE, "r") as f:
        data = json.load(f)

    # 저장된 지 23시간 이상 지났으면 만료 처리
    # 토큰 유효시간이 24시간이므로 23시간으로 설정해서 여유있게 갱신
    elapsed = time.time() - data["saved_at"]
    if elapsed > 23 * 3600:  # 23시간 (초)
        print("토큰 만료 -> 새로 발급")
        return None

    print("저장된 토큰 재사용")
    return data.get("access_token")

# 토큰 발급
def get_access_token():
    url = f"{BASE_URL}/oauth2/tokenP"
    headers = {"Content-Type": "application/json"}
    body = {
        "grant_type": "client_credentials",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET
    }
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json().get("access_token")


# 계좌 잔고 조회
def get_stock_balance(token: str) -> dict : 
    """주식 잔고 조회"""
    url = f"{BASE_URL}/uapi/domestic-stock/v1/trading/inquire-balance"
    headers = {
        "content-type":"application/json",
        "authorization":f"Bearer {token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id":"VTTC8434R" if IS_MOCK else "TTTC8434R"  # 모의투자와 실전투자 트랜잭션 ID가 다름
    }
    params = {
        "CANO": ACCOUNT_NO,
        "ACNT_PRDT_CD": ACCOUNT_PROD_CODE,
        "AFHR_FLPR_YN": "N",
        "OFL_YN": "N",
        "INQR_DVSN": "02",
        "UNPR_DVSN": "01",
        "FUND_STTL_ICLD_YN": "N",
        "FNCG_AMT_AUTO_RDPT_YN": "N",
        "PRCS_DVSN": "01",
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": ""
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()



def get_stock_price(token: str, stock_code: str) -> dict:
    """개별 주식 현재가 조회"""
    url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-price"
    headers = {
        "content-type":"application/json",
        "authorization":f"Bearer {token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id":"FHKST01010100",
    }
    params = {
        "FID_COND_MRKT_DIV_CODE": "J",  # 주식
        "FID_INPUT_ISCD": stock_code
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
