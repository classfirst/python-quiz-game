
from quiz import Quiz


def create_default_quizzes():
    quizzes = [
        Quiz(
            "Python에서 문자열을 나타내는 자료형은?",
            ["int", "str", "bool", "list"],
            2
        ),
        Quiz(
            "Python에서 변수의 주요 역할은?",
            [
                "프로그램을 종료한다",
                "화면을 지운다",
                "데이터에 이름을 붙여 참조한다",
                "오류를 자동으로 수정한다"
            ],
            3
        ),
        Quiz(
            "Python에서 조건에 따라 코드를 실행할 때 사용하는 키워드는?",
            ["for", "while", "def", "if"],
            4
        ),
        Quiz(
            "Python에서 리스트의 요소를 순서대로 순회할 때 주로 사용하는 문장은?",
            ["for", "class", "return", "import"],
            1
        ),
        Quiz(
            "머신러닝의 일반적인 특징으로 가장 적절한 것은?",
            [
                "모든 규칙을 사람이 직접 입력해야 한다",
                "데이터에서 패턴을 학습한다",
                "항상 인터넷 연결이 필요하다",
                "Python에서만 구현할 수 있다"
            ],
            2
        )
    ]

    return quizzes
