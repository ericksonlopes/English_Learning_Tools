import csv
from random import choice


def challenge_builder_simples_tenses_verb():
    simple_tenses = choice(['Preset', 'Past', 'Future'])
    typ = choice(['Phrase', 'Question'])
    pronouns = choice(['I', 'You', 'He', 'She', 'It', 'We', 'They'])

    with open('100_verbs.csv') as file_csv:
        verbs = choice([line for line in csv.reader(file_csv) if not line[1] == 'x'])

    print(
        f"With the pronoun \033[33m{pronouns}\033[38m, "
        f"create a \033[33m{typ} \033[38m"
        f"in the \033[33m{simple_tenses} \033[38m"
        f"tense with the verb to \033[33m{verbs[0]} | {verbs[1]}\033[38m (Affirmative and Negative)"
    )


[challenge_builder_simples_tenses_verb() for item in range(10)]
