
import json
from pathlib import Path

from quiz import Quiz
from quiz_data import create_default_quizzes


STATE_FILE = Path(__file__).resolve().parent / "state.json"



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

    def save_state(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        try:
            with STATE_FILE.open("w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            print("💾 데이터 저장 완료")
            return True

        except (OSError, TypeError, ValueError) as error:
            print(f"⚠️ 데이터 저장 실패: {error}")
            return False

    def load_state(self):
        if not STATE_FILE.exists():
            print("📂 저장 파일이 없어 기본 퀴즈를 사용합니다.")
            return

        try:
            with STATE_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("데이터 구조가 올바르지 않습니다.")

            records = data["quizzes"]
            best = data["best_score"]

            if not isinstance(records, list):
                raise ValueError("퀴즈 목록 형식이 잘못되었습니다.")

            loaded_quizzes = []

            for record in records:
                if not isinstance(record, dict):
                    raise ValueError("퀴즈 항목 형식이 잘못되었습니다.")

                loaded_quizzes.append(
                    Quiz(
                        record["question"],
                        record["choices"],
                        record["answer"]
                    )
                )

            if best is not None:
                if not isinstance(best, dict):
                    raise ValueError("최고 점수 형식이 잘못되었습니다.")

                score = best["score"]
                correct = best["correct"]
                total = best["total"]

                if not all(
                    type(value) is int
                    for value in (score, correct, total)
                ):
                    raise ValueError("점수 데이터가 정수가 아닙니다.")

                if not (
                    total > 0
                    and 0 <= correct <= total
                    and score == round(correct / total * 100)
                ):
                    raise ValueError("점수 데이터가 유효하지 않습니다.")

            self.quizzes = loaded_quizzes
            self.best_score = best

            print(
                f"📂 저장된 퀴즈 {len(self.quizzes)}개를 "
                "불러왔습니다."
            )

        except (
            OSError,
            UnicodeError,
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError
        ) as error:
            print(f"⚠️ 데이터 파일 오류: {error}")
            print("기본 퀴즈 데이터로 복구합니다.")

            self.quizzes = create_default_quizzes()
            self.best_score = None

    def get_number(self, prompt, minimum, maximum):
        while True:
            text = input(prompt).strip()

            if not text:
                print("⚠️ 빈 입력입니다.")
                continue

            try:
                number = int(text)
            except ValueError:
                print("⚠️ 숫자를 입력하세요.")
                continue

            if minimum <= number <= maximum:
                return number

            print(f"⚠️ {minimum}~{maximum} 사이를 입력하세요.")

    def get_non_empty_text(self, prompt):
        while True:
            text = input(prompt).strip()

            if text:
                return text

            print("⚠️ 빈 입력은 허용되지 않습니다.")

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")

        question = self.get_non_empty_text(
            "문제를 입력하세요: "
        )

        choices = []

        for number in range(1, 5):
            choice = self.get_non_empty_text(
                f"선택지 {number}: "
            )
            choices.append(choice)

        answer = self.get_number(
            "정답 번호 (1-4): ", 1, 4
        )

        new_quiz = Quiz(question, choices, answer)

        self.quizzes.append(new_quiz)

        print("✅ 새로운 퀴즈가 등록되었습니다.")
        self.save_state()

    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        correct_count = 0
        total = len(self.quizzes)

        print(f"\n📝 퀴즈 시작! 총 {total}문제")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {index}]")
            quiz.display()

            answer = self.get_number(
                "정답 입력 (1-4): ", 1, 4
            )

            if quiz.check_answer(answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                print(f"❌ 오답! 정답은 {quiz.answer}번입니다.")

        score = round(correct_count / total * 100)

        print("\n================================")
        print(f"🏆 {total}문제 중 {correct_count}문제 정답")
        print(f"최종 점수: {score}점")
        print("================================")

        if self.update_best_score(correct_count, total):
            print("🎉 새로운 최고 점수입니다!")

        self.save_state()

    def show_menu(self):
        print("\n================================")
        print("🎯 AI & Python 퀴즈 게임")
        print("================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("================================")

    def run(self):
        self.load_state()

        try:
            while True:
                self.show_menu()

                number = self.get_number(
                    "메뉴를 선택하세요 (1-5): ", 1, 5
                )

                if number == 1:
                    self.play_quiz()

                elif number == 2:
                    self.add_quiz()

                elif number == 3:
                    self.list_quizzes()

                elif number == 4:
                    self.show_score()

                elif number == 5:
                    print("👋 게임을 종료합니다.")
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 입력이 중단되었습니다.")
            print("가능한 데이터를 저장하고 종료합니다.")

        finally:
            self.save_state()
