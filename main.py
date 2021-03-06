import numpy as np


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток."""
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return (count)  # выход из цикла, если угадали


def game_core_v3(number):
    """Мой вариант. Загадываем число из середины диапазона (в нашем случае 50). Если искомое число больше,
    то нижняя граница диапазона становится серединой диапазона плюс один. Если искомое число меньше, то верхняя
    граница диапазона становится серединой диапазона минус один. Дальше снова загадываем число из середины диапазона.
    """
    min = 1
    max = 100
    count = 1
    predict = (min + max) // 2
    while number != predict:
        count += 1
        if number > predict:
            min = predict + 1
        elif number < predict:
            max = predict - 1
        predict = (min + max) // 2
    return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


if __name__ == "__main__":
    score_game(game_core_v3)
