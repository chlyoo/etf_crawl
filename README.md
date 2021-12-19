# README

## 실행 방법 

### run.bat 파일 클릭하여 실행

### run.bat 실패 시 압축을 푼 폴더 위치에서 CMD 실행 

`탐색기 주소표시줄`에 `CMD` 라고 입력

### 프로그램 실행에 필요한 파일 설치

`pip install -r requirements.txt` 실행

### 프로그램 실행

`python crawl.py`

## 조회할 ETF 추가 또는 변경 방법

1. ETF.py 파일 수정

```python
class ETF(Enum) 
    KODEX_게임산업 = "300950" 
```
ETF 파일을 열어서 ETF종목명을 아래에 넣고, ETF 코드를 입력   
공백, & 기호가 들어가면 에러 발생-> _ 언더스코어로 변경해서 입력

ETF 코드는 `https://finance.naver.com/api/sise/etfItemList.nhn?etfType=0&targetColumn=market_sum&sortOrder=desc` 여기에서 조회 가능