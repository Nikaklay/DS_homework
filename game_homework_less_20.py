"""Игра угадай число
Компьютер сам загадывает и сам угадывает число меньше, чем за 20 попыток
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    lower_bound = 1  # нижний предел ряда предполагемых чисел 
    upper_bound = 101  # верхний предел ряда предполагемых чисел

    while True:
        count += 1
        predict_number = np.random.randint(lower_bound, upper_bound)  # предполагаемое число
        
        if predict_number == number:
            break  # выход из цикла если угадали
        
        # меняем верхний предел ряда, если предполагаемое число больше загаданного
        elif predict_number > number:
            upper_bound = predict_number 
            
        # меняем нижний пределя ряда, если предполагаемое число меньше загаданного
        else:
            lower_bound = predict_number + 1   
            
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
