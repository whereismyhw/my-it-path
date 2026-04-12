import random

word_list = ["Безостановочный", "Заплесневеть", "Клеврет", "Ларингит", "Обгорелый", "Пнуть", "Подзатыльник", "Ситец", "Стременной", "Хакасы", "Хромой", "Чесотка", "Чихать", "Шарлатан", "Шептать", "Щебетать", "Щегол", "Щелкать", "Щенок", "Щука", "Эвкалипт", "Юрта", "Ябеда", "Ярость"]

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def get_word(word_list):
    return random.choice(word_list).lower()

def is_valid(answer, word):
    return (len(answer) == 1 and answer.isalpha()) or answer == word

def play(word):
    word_completion = ['_'] * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print ("Давайте сыграем в вислелицу")
    print("".join(word_completion))
    print()
    print(display_hangman(tries))
    
    while not guessed and tries > 0:
        answer = input("Ваш ответ: ").lower()

        while not is_valid(answer, word):
            print("Ввод некорректен")
            answer = input().lower()
        
        if answer in guessed_letters:
            print(f"Вы уже вводили букву {answer}")
            continue

        guessed_letters.append(answer)

        if answer in word:
            for i in range(len(word)):
                if word[i] == answer:
                    word_completion[i] = answer
        else:
            tries -= 1
            print(display_hangman(tries))
            print(f"Неверно! Осталось попыток: {tries}")

        if "".join(word_completion) == word or answer == word:
            guessed = True
            break

        print("".join(word_completion))
        print()

    if guessed:
        print(f"Вы победили!!! Слово было: {word}")
    else:
        print("Увы, вы проиграли. Попробуйте еще раз...")

word = get_word(word_list)
play(word)