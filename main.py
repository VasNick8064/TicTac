import random
import time

'''
get_word - функция, которая случайно выбирает одно слово из словаря "dict", возвращает список отдельных букв
'''


def get_word():
    with open("dict.txt", "r", encoding="utf-8") as file:
        return list(random.choice(file.readlines())[:-1])


'''
hide_letters - функция, которая шифрует наше слово, которае возвращает функция get_word, возвращает список зашифрованных
букв с двумя известными буквами
'''


def hide_letters(word):
    hidden_word = ["*" for _ in word]  # Создаем список звездочек
    reveal_indices = random.sample(range(len(word)), 2)  # Выбираем 2 случайных индекса
    for i in reveal_indices:
        hidden_word[i] = word[i]  # Открываем буквы на выбранных индексах
    return hidden_word


'''
Наши переменны word - случайное слово из словаря, hidden_word - то же слово, но зашифрованное
'''
word = get_word()
hidden_word = hide_letters(word)
'''
reval_letter - функция которая открывает одну букву в списке, если она присутсствует в результате возврата get_word
'''


def reveal_letter(guess, word=word, hidden_word=hidden_word):
    for i, letter in enumerate(word):
        if letter == guess:
            hidden_word[i] = guess
    return hidden_word


'''
call_ans() - функция алгоритма игры. Выводим два приветсвенных сообщения, далее в цикле, пока количество неправильных ответов
death не будет равно 6, мы вызываем функицю reveal_latter с параметром guess, если guess содержится в reveal_latter, то
мы возвращаем обновленныйы список hiden_word с угаданной буквой.
'''


def call_ans():  # Главный алгоритм игры
    print(
        f"\033[32mЯ загадал слово (сущ.), у тебя есть 6 попыток, чтобы отгадать это слово. Поехали....\033[0m")  # Зеленый цвет
    time.sleep(2)
    print(f"\033[32mЗагаданное слово: \033[0m\033[33m{' '.join(hidden_word)}\033[0m")
    death = 0
    while death < 6:
        guess = input("\033[32mВведите букву: \033[0m")
        reveal_letter(guess)
        print("\033[32m" + " ".join(hidden_word) + "\033[0m")
        if guess not in word:  # Проверяем, есть ли буква в слове
            death += 1  # Буквы нет, счетчик +1
            print(f"\033[32mНеверный ответ! Количество ошибок {death}\033[0m")
            if death == 6:
                print("\033[31mВы проиграли...\033[0m")
                time.sleep(2)
                print(f"\033[31m| Загаданное слово: '{(''.join(word)).title()}' |\033[0m")
        if hidden_word == word:
            print("\033[33mВы победили!!!\033[0m\n")
            break


'''
show_intro_message - функция приветствие
'''


def show_intro_message():
    print(
        "\033[32m"
        "Привет, мой друг.\n"
        "Я предлагаю тебе сыграть со мной в игру 'Виселица'.\n\n"
        "### 1. Я согласен ###\n"
        "### 2. Отказаться ###\n"
        "\033[0m"
    )


'''
main - точка входа
'''


def main():
    show_intro_message()
    choice = input()
    call_ans() if choice == "1" else print("\033[31mЕще увидимся }:-)\033[0m")


if __name__ == "__main__":
    main()
