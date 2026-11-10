
from quiz import Quiz
from quiz_data import create_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None

    def list_quizzes(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 퀴즈 목록 (총 {len(self.quizzes)}개)")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
