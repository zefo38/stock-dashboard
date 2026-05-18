# 📈 내 주식 대시보드

한국투자증권 API를 활용한 실시간 주식 포트폴리오 대시보드

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 주요 기능

- 📊 보유 종목 실시간 조회
- 💰 총 평가금액 / 매입금액 / 평가손익 확인
- 📈 종목별 수익률 확인
- 🔄 30초마다 자동 새로고침
- 🌙 다크모드 UI

---

## 🛠 기술 스택

| 분류 | 기술 |
|------|------|
| Backend | Python, FastAPI |
| Frontend | HTML, CSS, JavaScript |
| API | 한국투자증권 KIS API |
| 버전관리 | Git, GitHub |

---

## ⚙️ 설치 방법

### 1. 레포지토리 클론
\```bash
git clone https://github.com/zefo38/stock-dashboard.git
cd stock-dashboard
\```

### 2. 가상환경 생성 및 활성화
\```bash
python -m venv venv
venv\Scripts\activate
\```

### 3. 패키지 설치
\```bash
pip install fastapi uvicorn python-dotenv requests jinja2
\```

### 4. 환경변수 설정
루트 폴더에 `.env` 파일 생성:
\```
KIS_APP_KEY=발급받은_앱키
KIS_APP_SECRET=발급받은_시크릿
KIS_ACCOUNT_NO=계좌번호앞8자리
KIS_ACCOUNT_PROD_CODE=01
IS_MOCK=true
\```

### 5. 서버 실행
\```bash
uvicorn main:app --reload
\```

### 6. 브라우저에서 확인
\```
http://127.0.0.1:8000
\```

---

## 📁 프로젝트 구조

\```
stock-dashboard/
├── .env                # API 키 (GitHub 비공개)
├── .gitignore          
├── kis_api.py          # 한투 API 연동
├── main.py             # FastAPI 서버
├── README.md           
└── templates/
    └── index.html      # 대시보드 UI
\```

---

## 🔑 API 발급 방법

1. [KIS Developers](https://apiportal.koreainvestment.com/) 접속
2. 로그인 → 앱 등록
3. App Key / App Secret 발급
4. `.env` 파일에 입력

---

## ⚠️ 주의사항

- `.env` 파일은 절대 GitHub에 올리지 마세요!
- 모의투자 / 실전투자 API Key는 다르게 발급됩니다

---

## 📝 License

MIT License