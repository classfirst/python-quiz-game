
# AI & Python Quiz Game

Codyssey Pre-course Week 2 Project

## 1. 프로젝트 개요

Python 기본 문법과 객체 지향 프로그래밍을 활용하여
개발한 콘솔 기반 퀴즈 게임입니다.

사용자는 퀴즈를 풀거나 새로운 문제를 등록할 수 있으며,
JSON 파일을 통해 퀴즈 데이터와 최고 점수를 저장합니다.

## 2. 퀴즈 주제 및 선정 이유

주제: AI 및 Python 기초

AI 엔지니어로 성장하기 위해 Python과 인공지능의
기본 개념을 반복 학습하고 이해도를 확인하고자
해당 주제를 선정했습니다.

## 3. 개발 환경

- OS: Windows 11
- Python: 3.15.0
- Editor: Visual Studio Code
- Version Control: Git / GitHub
- External Libraries: None

## 4. 실행 방법

1. 저장소 복제

git clone https://github.com/classfirst/python-quiz-game.git

2. 프로젝트 폴더 이동

cd python-quiz-game

3. 프로그램 실행

python main.py

Python 3.10 이상이 필요합니다.

## 5. 주요 기능

1. 퀴즈 풀기
   - 기본 퀴즈 및 추가 퀴즈 출제
   - 정답과 오답 판정
   - 최종 점수 계산

2. 퀴즈 추가
   - 문제와 선택지 4개 입력
   - 정답 번호 검증
   - JSON 파일 저장

3. 퀴즈 목록
   - 등록된 문제 목록 확인

4. 점수 확인
   - 최고 점수 확인
   - 새로운 최고 점수 갱신

5. 종료
   - 데이터 저장 후 안전하게 종료

## 6. 파일 구조

python-quiz-game/
├── main.py
├── quiz.py
├── quiz_data.py
├── quiz_game.py
├── state.json
├── .gitignore
├── README.md
└── docs/
    └── screenshots/

## 7. 데이터 파일 설명

파일명: state.json
위치: 프로젝트 루트
인코딩: UTF-8

주요 필드:
- quizzes: 퀴즈 목록
- question: 문제 문장
- choices: 선택지 4개
- answer: 정답 번호
- best_score: 최고 점수 기록

state.json이 없는 경우 기본 퀴즈 5개를 사용합니다.

파일이 손상된 경우 오류를 안내하고
기본 퀴즈 데이터로 초기화합니다.

## 8. Git 개발 이력

- Git 저장소 초기화
- 메뉴 기능 구현
- Quiz 클래스 구현
- 기본 퀴즈 데이터 작성
- feature/quiz-play 브랜치 생성
- 퀴즈 풀기 기능 구현
- main 브랜치 병합
- 퀴즈 추가 기능 구현
- QuizGame 클래스 구현
- 최고 점수 관리
- JSON 데이터 저장 및 불러오기

## 9. 테스트

- 정상적인 메뉴 입력
- 잘못된 숫자 및 빈 입력
- 퀴즈 정답·오답 판정
- 퀴즈 추가 및 목록 확인
- 최고 점수 갱신
- 프로그램 재실행 후 데이터 유지
- Ctrl+C 및 EOF 처리
- JSON 파일 오류 처리

## 10. 실행 결과

실행 스크린샷은 docs/screenshots/ 폴더에 저장합니다.
