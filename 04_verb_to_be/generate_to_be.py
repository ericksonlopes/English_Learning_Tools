import csv
import os
import platform
import chromedriver_autoinstaller
from random import choice
from selenium import webdriver
import tqdm

# Check your operational system!
OP_SYSTEM = platform.system()
# print(OP_SYSTEM)

if OP_SYSTEM.lower() == 'windows':
    chromedriver_autoinstaller.install()

# Create a folder to recieve your donwloads
try:
    os.mkdir(os.path.dirname(os.path.realpath(__file__)) + '//data')
except:
    pass

folder = os.path.dirname(os.path.realpath(__file__)) + '/data'  # Set Google Options
options = webdriver.ChromeOptions()

# Define donwload settings
prefs = {''
         # Set a specific folder to download files from selenium ( Default is download folder )
         "download.default_directory": r"%s" % folder,
         "download.prompt_for_download": False,
         "download.directory_upgrade": True
         }

options.add_experimental_option('prefs', prefs)
options.add_argument("--headless")  # This option hide the browser... to see the browser comment this line
options.add_argument("--no-sandbox")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# Remove selenium logs on console ( More clean! )
options.add_argument('--log-level=3')

# Chose the webdriver according with your system

if OP_SYSTEM.lower() == 'windows':
    driver = webdriver.Chrome(options=options)
else:
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)


how_many_times = int(input('How often do you want to practice? '))

for item in range(0, how_many_times):
    with open('100_verbs.csv') as file_csv:
        verbs = choice([line[0] for line in csv.reader(file_csv) if not line[1] == 'x'])

    driver.get("https://pt.bab.la/verbo/ingles/" + verbs)

    # Your code to scrap start here , everything above I like as default in my codes!
    search_box = driver.find_elements_by_class_name('conj-tense-block')

    # Dicionario que recebe todas os tempos verbais
    completed_time = {}
    print()
    for line in tqdm.tqdm(search_box):
        try:
            # Recebe todos os pronomes
            pronouns = [item.text for item in line.find_elements_by_class_name('conj-person')]
            # Recebe o tempo verbal
            time = line.find_element_by_class_name('conj-tense-block-header').text
            # Recebe a sentença do verbo
            sentense_verb = [item.text for item in line.find_elements_by_class_name('conj-result')]
            # Remove o elemento "he/she/it"
            sentense_end = sentense_verb.pop(2)
            # atribui as sentenças he/she/it na variavel
            sentense = [f"{pronoun} {sentense_end}" for pronoun in pronouns.pop(2).split('/')]

            for num in range(len(sentense_verb)):
                sentense.append(f"{pronouns[num]} {sentense_verb[num]}")

            completed_time.update({time: sentense})
        except:
            pass

    simple_tense = choice(['Present continuous', 'Past continuous', 'Future continuous'])
    pronoun = choice(['I', 'you', 'he', 'she', 'it', 'we', 'they'])
    aff_neg = choice([True, False])
    correct_aff, correct_neg = '', ''

    print()
    for sent in completed_time[simple_tense]:
        sl = sent.split(' ')
        if pronoun == sl[0]:
            if sl[1] != 'will':
                if aff_neg:
                    print(f"{sl[1].title()} {sl[0]} {sl[2]}?")

                else:
                    print(f"{sl[1].title()} {sl[0]} not {sl[2]}?")

                correct_aff = sent
                correct_neg = f"{sl[0].title()} {sl[1]} not {sl[2]}"
            else:
                if aff_neg:
                    print(f"{sl[1].title()} {sl[0]} {sl[2]} {sl[3]}?")
                else:
                    print(f"Won't {sl[0]} {sl[2]} {sl[3]}?")

                correct_aff = sent
                correct_neg = f"{sl[0]} won't be {sl[3]}"

    if correct_aff.lower() == input('Answer in an affirmative form: ').lower():
        print('\033[32m Win(Affirmative)\033[38m')
    else:
        print(f'\033[31m Lose (Affirmative) \033[33m correct answer: {correct_aff}\033[38m')

    if correct_neg.lower() == input('Answer in an negative form: ').lower():
        print('\033[32m Win(Negative)\033[38m')
    else:
        print(f'\033[31m Lose (Negative) \033[33m correct answer: {correct_neg}\033[38m')


driver.close()
driver.quit()
