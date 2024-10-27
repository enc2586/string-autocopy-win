# string-autocopy-win
![image](https://github.com/user-attachments/assets/c40302b6-1809-42c7-8c4c-854e4af17313)

여러 줄의 문자열을 하나 하나 복사/붙여넣기하는 것을 돕는 프로그램입니다.

문자열 여러 개를 따로, 지속적으로 붙여넣기해야할 때 유용합니다.

## 사용법
1. 문자열 여러 개를 공백으로 구분하여 입력창에 붙여넣습니다.
2. 시작 버튼을 누르면 작동되며, 첫 문자열이 자동으로 복사됩니다.
3. Ctrl+B를 누르면 다음 문자열로 넘어갑니다.
4. 중지 버튼을 누르기 전까지 계속됩니다.

## 실행 파일 다운로드
[Releases](https://github.com/enc2586/string-autocopy-win/releases)에서 다운받을 수 있습니다.

`string-autocopy-win.exe`를 다운받으시면 됩니다.

## 빌드
Releases의 실행파일을 신뢰하지 못하거나 직접 빌드하고 싶으신 경우, 아래 절차를 따르세요.

### Python 설치
Python 3.13.0 버전을 설치하세요.

### Requirements 설치 및 빌드
0. (선택사항) repo 폴더에 터미널 실행 후, `python -m venv venv`로 가상환경을 만들고 활성화하세요.
1. `pip install -r requirements.txt`로 Requirements를 설치하세요.
2. `pyinstaller -w -F main.py`로 실행파일을 빌드하세요.
3. dist/ 하위에 실행파일이 생성됩니다.
