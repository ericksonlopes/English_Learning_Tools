import csv
from random import choice


def query_generator():
    simple_tense = choice(['Preset', 'Past', 'Future'])
    pronoun = choice(['I', 'you', 'he', 'she', 'it', 'we', 'they'])
    aff_neg = choice([True, False])

    with open('100_verbs.csv') as file_csv:
        verbs = choice([line for line in csv.reader(file_csv) if not line[1] == 'x'])

    if simple_tense == 'Preset':
        if aff_neg:
            if pronoun in ['she', 'se', 'it']:
                print(f'Does {pronoun} {verbs[0]}?')
            else:
                print(f'Do {pronoun} {verbs[0]}?')
        else:
            if pronoun in ['she', 'he', 'it']:
                print(f'Doesn\'t {pronoun} {verbs[0]}?')
            else:
                print(f'Don\'t {pronoun} {verbs[0]}?')

    elif simple_tense == 'Past':
        if aff_neg:
            print(f'did {pronoun} {verbs[0]}?')
        else:
            print(f'didn\'t {pronoun} {verbs[0]}?')

    elif simple_tense == 'Future':
        if aff_neg:
            print(f'Will {pronoun} {verbs[0]}?')
        else:
            print(f'won\'t {pronoun} {verbs[0]}?')


[query_generator() for item in range(10)]
