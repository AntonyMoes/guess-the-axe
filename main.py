from random import randint, choice
import os
import subprocess

AXES = r"""
    Т  О  П  О  Р  Ы

    |/|    |/|    |/|
    |\|    |\|    |\|
    |      |      |
    |      |      |
    
    1      2      3
"""

answers = [
    ['https://youtu.be/aaD5MBueg6c?t=27','https://youtu.be/aaD5MBueg6c?t=121', 
        'https://youtu.be/aaD5MBueg6c?t=199'],                                       # first

    ['https://youtu.be/aaD5MBueg6c?t=65', 'https://youtu.be/aaD5MBueg6c?t=141'],     # second

    ['https://youtu.be/aaD5MBueg6c?t=46', 'https://youtu.be/aaD5MBueg6c?t=85', 
        'https://youtu.be/aaD5MBueg6c?t=161', 'https://youtu.be/aaD5MBueg6c?t=179']   # third
]

ROUNDS_NUM = 4


def get_axe_guess(text: str) -> int:
    """Function returns the axe guess"""
    """:param text: str - displayed text"""
    """:returns guess: int"""
    return int(input(text))


if __name__ == '__main__':
    result = 0
    for i in range(ROUNDS_NUM):
        print(f'ПОПЫТОЧКА №{i + 1}')
        print(AXES)
        guess = get_axe_guess('УХАДАЙ> ')
        answer = randint(0, 2)
        print('Каааакоооооой же тапор ето быыыл?')

        proc = subprocess.Popen(f'chromium-browser {choice(answers[answer])}', shell=True, 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.wait()

        if guess == answer + 1:
            print('Ой какие мы молодцы')
            result += 1
        else:
            print('Ой как обидно как обидно')
        print()
    print(f'А балльчиков-то балльчиков-то у нас {result}')
