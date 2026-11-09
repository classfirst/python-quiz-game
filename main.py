
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


def main():
    while True:
        show_menu()

        try:
            choice = input("메뉴를 선택하세요 (1-5): ").strip()

            if choice == "":
                print("⚠️ 빈 입력입니다. 번호를 입력하세요.")
                continue

            number = int(choice)

            if number == 1:
                print("📝 퀴즈 풀기 기능은 준비 중입니다.")

            elif number == 2:
                print("📌 퀴즈 추가 기능은 준비 중입니다.")

            elif number == 3:
                print("📋 퀴즈 목록 기능은 준비 중입니다.")

            elif number == 4:
                print("🏆 점수 확인 기능은 준비 중입니다.")

            elif number == 5:
                print("👋 게임을 종료합니다.")
                break

            else:
                print("⚠️ 1부터 5까지 입력하세요.")

        except ValueError:
            print("⚠️ 숫자를 입력해야 합니다.")

        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 입력이 중단되어 안전하게 종료합니다.")
            break


if __name__ == "__main__":
    main()
