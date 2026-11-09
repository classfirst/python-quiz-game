
class Quiz:
    def __init__(self, question, choices, answer):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 비어 있지 않은 문자열이어야 합니다.")

        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 정확히 4개여야 합니다.")

        if any(
            not isinstance(choice, str) or not choice.strip()
            for choice in choices
        ):
            raise ValueError("모든 선택지는 비어 있지 않은 문자열이어야 합니다.")

        if type(answer) is not int or not 1 <= answer <= 4:
            raise ValueError("정답은 1부터 4까지의 정수여야 합니다.")

        self.question = question
        self.choices = choices.copy()
        self.answer = answer

    def display(self):
        print("\n" + "-" * 40)
        print(self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

        print("-" * 40)

    def check_answer(self, user_answer):
        return user_answer == self.answer
