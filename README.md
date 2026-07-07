# BMI Calculator

회원 기반 BMI 계산, 결과 저장, 개인 기록 조회, 전체 통계 확인 기능을 제공하는 Flask 웹 애플리케이션입니다.

## 한줄 소개

Flask와 MariaDB를 활용해 BMI 계산부터 회원별 기록 관리와 전체 통계 조회까지 제공하는 웹 기반 BMI 관리 서비스

## 프로젝트 개요

BMI Calculator는 사용자가 키와 몸무게를 입력해 BMI를 계산하고, 계산 결과를 회원별 기록으로 저장할 수 있는 웹 서비스입니다. 회원가입과 로그인을 통해 개인 기록을 관리할 수 있으며, 최근 BMI 기록 조회, 기록 삭제, 전체 사용자 BMI 통계 확인 기능을 제공합니다.

애플리케이션은 Flask 기반 MVC 구조로 구성되어 있으며, 라우트, 서비스, 모델 계층을 분리해 회원 관리, BMI 계산, 기록 관리, 통계 조회 기능을 담당합니다. 데이터 저장소는 MariaDB/MySQL 계열 데이터베이스를 사용하며, PyMySQL을 통해 DB와 연동합니다.

## 주요 기능

- BMI 계산
  - 몸무게와 키 입력을 통한 BMI 산출
  - BMI 소수점 둘째 자리 반올림
  - 저체중, 정상, 과체중, 비만, 고도비만 등 BMI 구간 판정

- 회원 기능
  - 회원가입
  - 로그인 및 로그아웃
  - 세션 기반 로그인 상태 관리
  - 비밀번호 해시 저장
  - 비활성화 회원 로그인 제한

- BMI 기록 관리
  - 로그인 사용자별 BMI 계산 결과 저장
  - 최근 BMI 기록 최대 10개 조회
  - 사용자 본인의 BMI 기록 삭제

- 통계 기능
  - 전체 BMI 기록 수 조회
  - 평균 BMI, 최저 BMI, 최고 BMI 조회
  - 평균 몸무게와 평균 키 조회
  - BMI 카테고리별 인원 수와 비율 계산
  - 최신 BMI 기록 확인

- 요청 로그 저장
  - 정적 파일을 제외한 요청 로그 저장
  - HTTP 메서드, 요청 URI, 상태 코드, 회원 ID 기록
  - 요청 방식에 따라 SELECT, INSERT, UPDATE, DELETE 유형 분류

## 기술 스택

### Backend

- Python
- Flask
- PyMySQL
- Gunicorn
- python-dotenv
- Werkzeug Security

### Database

- MariaDB 또는 MySQL
- `members` 테이블
- `bmi_records` 테이블
- `activity_logs` 테이블

### Frontend

- Jinja2 Templates
- HTML
- CSS

## 프로젝트 구조

```text
BMI_Calculator/
├── app.py                    # Flask 앱 생성 및 요청 로그 처리
├── config.py                 # 환경 변수 기반 설정
├── requirements.txt          # Python 의존성 목록
├── tableSetting.sql          # DB 및 테이블 생성 SQL
├── models/                   # DB 접근 모델
├── routes/                   # Flask Blueprint 라우터
├── services/                 # 비즈니스 로직 계층
├── templates/                # Jinja2 HTML 템플릿
└── static/
    └── css/                  # 스타일시트
```

## 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/Polalise/BMI_Calculator.git
cd BMI_Calculator
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 생성

MariaDB 또는 MySQL에서 `tableSetting.sql`을 실행해 데이터베이스와 테이블을 생성합니다.

```bash
mysql -u your_user -p < tableSetting.sql
```

기본 SQL은 `test` 데이터베이스와 다음 테이블을 생성합니다.

- `members` : 회원 정보
- `bmi_records` : BMI 계산 기록
- `activity_logs` : 요청 활동 로그

### 5. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 DB 접속 정보를 설정합니다.

```env
SECRET_KEY=your_secret_key
DB_HOST=localhost
DB_DATABASE=test
DB_USER=your_db_user
DB_PASSWORD=your_db_password
FLASK_ENV=development
```

### 6. 애플리케이션 실행

```bash
python app.py
```

실행 후 브라우저에서 아래 주소로 접속합니다.

```text
http://localhost:5000
```

## 주요 화면 및 라우트

| Method | Route | Description |
| --- | --- | --- |
| GET | `/` | 메인 화면 |
| GET | `/bmi` | BMI 입력 화면 |
| POST | `/calculate` | BMI 계산 및 기록 저장 |
| GET | `/member/signup` | 회원가입 화면 |
| POST | `/member/signup` | 회원가입 처리 |
| GET | `/member/login` | 로그인 화면 |
| POST | `/member/login` | 로그인 처리 |
| GET | `/member/logout` | 로그아웃 |
| GET | `/history` | 최근 BMI 기록 조회 |
| POST | `/history/delete/<record_id>` | BMI 기록 삭제 |
| GET | `/statistics/` | 전체 BMI 통계 화면 |

## BMI 판정 기준

| BMI 범위 | 분류 |
| --- | --- |
| 18.5 미만 | 저체중 |
| 18.5 이상 23 미만 | 정상 |
| 23 이상 25 미만 | 과체중 |
| 25 이상 30 미만 | 비만 |
| 30 이상 | 고도비만 |

## 기대 효과

- 단순 BMI 계산을 넘어 회원별 기록을 저장해 개인 건강 변화를 확인할 수 있습니다.
- 전체 사용자 통계를 통해 BMI 분포와 평균 지표를 한눈에 파악할 수 있습니다.
- 라우트, 서비스, 모델 계층을 분리해 Flask 프로젝트 구조를 학습하고 확장하기 좋습니다.
