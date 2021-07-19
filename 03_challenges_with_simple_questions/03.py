import csv
from random import choice


def challenge_builder_simples_tenses_verb():
    # Preenche as variaveis com um dado da lista
    simple_tenses = choice(['Preset', 'Past', 'Future'])
    typ = choice(['Phrase', 'Question'])
    pronouns = choice(['I', 'You', 'He', 'She', 'It', 'We', 'They'])

    # Captura os verbos do arquivo csv
    with open('100_verbs.csv') as file_csv:
        # Seleciona um dos itens da lista com todos os verbos (exceto os com x no [1])
        verbs = choice([line for line in csv.reader(file_csv) if not line[1] == 'x'])

    print(
        f"With the pronoun \033[33m{pronouns}\033[38m, "
        f"create a \033[33m{typ} \033[38m"
        f"in the \033[33m{simple_tenses} \033[38m"
        f"tense with the verb to \033[33m{verbs[0]} | {verbs[1]}\033[38m (Affirmative and Negative)"
    )


[(challenge_builder_simples_tenses_verb(), input()) for item in range(10)]
