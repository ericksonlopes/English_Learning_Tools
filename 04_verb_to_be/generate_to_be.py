import csv
import os
import platform
import chromedriver_autoinstaller
from random import choice
from selenium import webdriver


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

with open('100_verbs.csv') as file_csv:
    verbs = choice([line[0] for line in csv.reader(file_csv) if not line[1] == 'x'])

driver.get("https://pt.bab.la/verbo/ingles/" + verbs)

# Your code to scrap start here , everything above I like as default in my codes!
search_box = driver.find_elements_by_class_name('conj-tense-block')

# Dicionario que recebe todas os tempos verbais
completed_time = {}
for line in search_box:
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


for item in completed_time:
    print(item, completed_time[item])

# good practice to kill the process, for dont speeding too much resources
driver.close()
driver.quit()
