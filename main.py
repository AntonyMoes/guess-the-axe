from random import randint
from os import system

# I HAVE ACHIEVED ART
# I HAVE ACHIEVED ART
# I HAVE ACHIEVED ART
# I HAVE ACHIEVED ART
# I HAVE ACHIEVED ART
# I HAVE ACHIEVED ART
# I HAVE ACHIEVED ART
# I HAVE ACHIEVED ART
# I HAVE ACHIEVED ART
# I HAVE ACHIEVED ART
AXES = r"""
    Т  О  П  О  Р  Ы

    |/|    |/|    |/|
    |\|    |\|    |\|
    |      |      |
    |      |      |
    
    1      2      3
"""

answers = [
    'https://youtu.be/aaD5MBueg6c?t=27',  # first
    'https://youtu.be/aaD5MBueg6c?t=65',  # second
    'https://youtu.be/aaD5MBueg6c?t=46',  # third
]

# todo(AntonyMoes): check if correct
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

        system(f'google-chrome {answers[answer]}')

        if guess == answer + 1:
            print('Ой какие мы молодцы')
            result += 1
        else:
            print('Ой как обидно как обидно')
            # print('СОСАТЬ')
        print()

    print(f'А балльчиков-то балльчиков-то у нас {result}')
