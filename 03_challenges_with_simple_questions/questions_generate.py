import csv
from random import choice


def challenge_generator():
    simple_tense = choice(['Preset', 'Past', 'Future'])
    pronoun = choice(['I', 'you', 'he', 'she', 'it', 'we', 'they'])
    aff_neg = choice([True, False])
    correct_aff, correct_neg = '', ''

    with open('100_verbs.csv') as file_csv:
        verbs = choice([line for line in csv.reader(file_csv) if not line[1] == 'x'])

    if simple_tense == 'Preset':
        if aff_neg:
            if pronoun in ['she', 'he', 'it']:
                print(f'Does {pronoun} {verbs[0]}?')
            else:
                print(f'Do {pronoun} {verbs[0]}?')
        else:
            if pronoun in ['she', 'he', 'it']:
                print(f'Doesn\'t {pronoun} {verbs[0]}?')
            else:
                print(f'Don\'t {pronoun} {verbs[0]}?')

        if pronoun in ['she', 'he', 'it']:
            correct_aff = f'{pronoun} {verbs[0]}s'
            correct_neg = f'{pronoun} doesn\'t {verbs[0]}'
        else:
            correct_aff = f'{pronoun} {verbs[0]}'
            correct_neg = f'{pronoun} don\'t {verbs[0]}'

    elif simple_tense == 'Past':
        if aff_neg:
            print(f'did {pronoun} {verbs[0]}?')
        else:
            print(f'didn\'t {pronoun} {verbs[0]}?')

        correct_aff = f'{pronoun} {verbs[1]}'
        correct_neg = f'{pronoun} didn\'t {verbs[0]}'

    elif simple_tense == 'Future':
        if aff_neg:
            print(f'Will {pronoun} {verbs[0]}?')
        else:
            print(f'won\'t {pronoun} {verbs[0]}?')

        correct_aff = f'{pronoun} will {verbs[0]}'.lower()
        correct_neg = f'{pronoun} won\'t {verbs[0]}'.lower()

    if correct_aff.lower() == input('Answer in an affirmative form: ').lower():
        print('\033[32m Win(Affirmative)\033[38m')
    else:
        print(f'\033[31m Lose (Affirmative) \033[33m correct answer: {correct_aff}\033[38m')

    if correct_neg.lower() == input('Answer in an negative form: ').lower():
        print('\033[32m Win(Negative)\033[38m')
    else:
        print(f'\033[31m Lose (Negative) \033[33m correct answer: {correct_neg}\033[38m')


how_many_times = int(input('How often do you want to practice? '))

for item in range(0, how_many_times):
    print('\n')
    challenge_generator()
