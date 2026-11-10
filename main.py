
from quiz_data import create_default_quizzes


def show_menu():
    print("\n================================")
    print("🎯 AI & Python 퀴즈 게임")
    print("================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("================================")


def get_number(prompt, minimum, maximum):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("⚠️ 빈 입력입니다. 숫자를 입력하세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            print("⚠️ 올바른 숫자를 입력하세요.")
            continue

        if minimum <= number <= maximum:
            return number

        print(f"⚠️ {minimum}부터 {maximum}까지 입력하세요.")


def play_quiz(quizzes):
    if not quizzes:
        print("⚠️ 등록된 퀴즈가 없습니다.")
        return

    correct_count = 0
    total = len(quizzes)

    print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

    for index, quiz in enumerate(quizzes, start=1):
        print(f"\n[문제 {index}]")
        quiz.display()

        answer = get_number("정답 입력 (1-4): ", 1, 4)

        if quiz.check_answer(answer):
            print("✅ 정답입니다!")
            correct_count += 1
        else:
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

    score = round(correct_count / total * 100)

    print("\n================================")
    print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답!")
    print(f"최종 점수: {score}점")
    print("================================")


def main():
    quizzes = create_default_quizzes()

    try:
        while True:
            show_menu()

            number = get_number(
                "메뉴를 선택하세요 (1-5): ", 1, 5
            )

            if number == 1:
                play_quiz(quizzes)

            elif number == 2:
                print("📌 퀴즈 추가 기능은 준비 중입니다.")

            elif number == 3:
                print("📋 퀴즈 목록 기능은 준비 중입니다.")

            elif number == 4:
                print("🏆 점수 확인 기능은 준비 중입니다.")

            elif number == 5:
                print("👋 게임을 종료합니다.")
                break

    except (KeyboardInterrupt, EOFError):
        print("\n⚠️ 입력이 중단되어 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
