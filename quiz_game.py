
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

    def update_best_score(self, correct, total):
        if total <= 0:
            return False

        score = round(correct / total * 100)

        if (
            self.best_score is None
            or score > self.best_score["score"]
        ):
            self.best_score = {
                "score": score,
                "correct": correct,
                "total": total
            }
            return True

        return False

    def show_score(self):
        if self.best_score is None:
            print("🏆 아직 퀴즈를 완료한 기록이 없습니다.")
            return

        record = self.best_score

        print("\n🏆 최고 점수")
        print(f"점수: {record['score']}점")
        print(
            f"정답: {record['total']}문제 중 "
            f"{record['correct']}문제"
        )
