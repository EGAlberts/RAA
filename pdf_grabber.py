import urllib.request
import csv
# Installation of selenium and the crome web driver is required, assuming
# chrome browser is installed on the machine.
# https://chromedriver.chromium.org/downloads
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import os
import time
import shutil

papers = [
    #('journals/pacmpl/GhoshHMM20', 'https://doi.org/10.1145/3428300'),
    #('journals/pacmpl/MajumdarYZ20', 'https://doi.org/10.1145/3428202'), FORMAT
]
with open(input("csv input file name > "), 'r', encoding='utf-8', newline="") as csvfile:
    venue_reader = csv.DictReader(csvfile)
    #next(venue_reader) #skip header
    
    for row in venue_reader:
        papers.append((row["key"], row["ee"]))

PAPER_DIRECTORY = 'downloaded_papers'

opener = urllib.request.build_opener()
opener.addheaders = [
    ('Accept', 'application/vnd.crossref.unixsd+xml'),
    ('User-Agent', 'PostmanRuntime/7.6.0')
]

#input("Now?")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument(r"user-data-dir=C:\Users\Elvin\AppData\Local\Google\Chrome\User Data")
chrome_options.add_experimental_option('prefs', {
        "plugins.plugins_disabled": ["Chrome PDF Viewer"],
        "download.default_directory": r"C:\Users\Elvin\Repositories\RAA\downloaded_papers\new_downloads\\",
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
    }
)
#input("Now??")

print('Starting browser...')
browser = webdriver.Chrome('/C:/Users/Elvin/Downloads/chromedriver_win32',options=chrome_options)

print('Starting loop...')
while len(papers) > 0:
    #input("Now???")
    try:
        os.mkdir(f'{os.getcwd()}/{PAPER_DIRECTORY}/new_downloads')
    except FileExistsError: 
        pass
    current_paper = papers.pop(0)
    file_title = current_paper[0].replace('/', '@')

    if not os.path.exists(f'{PAPER_DIRECTORY}/{file_title}.pdf'):
        print('='*80)
        print(f'Looking up {current_paper[0]}')
        try:
            if 'doi.org/' in current_paper[1]:
                print(f'Retrieving full text from doi: {current_paper[1]}')
                r = opener.open(current_paper[1])
                link = r.headers['Link'].split(', ')[1].split('; ')[0][1:-1]
                if 'ieeexplore' in link and '-aam.pdf' in link:
                    print('Linkie:', link)
                    ieee_id = link.split('-aam.pdf')[0][-7:]
                    print(ieee_id)
                    link = f'https://ieeexplore-ieee-org.tudelft.idm.oclc.org/stampPDF/getPDF.jsp?tp=&arnumber={ieee_id}'
                elif 'xplorestaging' in link:
                    ieee_id = link.split('=')[-1]
                    link = f'https://ieeexplore-ieee-org.tudelft.idm.oclc.org/stampPDF/getPDF.jsp?tp=&arnumber={ieee_id}'
                elif 'elsevier' in link:
                    pii = link.split('PII:')[-1][:17]
                    link = f'https://www.sciencedirect.com/science/article/pii/{pii}/pdf'
            else:
                link = current_paper[1]
            print(f'Going to download from link: {link}')
            #link = "https://iliasger.github.io/pubs/2022-ISOLA-Inertia.pdf"
            # browser.implicitly_wait(5)
            response = browser.get(link)

            print(f'Awaiting download')

            while True:
                # Wait a bit
                time.sleep(0.5)
                print("I'm here")
                if not os.path.isdir(f'{PAPER_DIRECTORY}/new_downloads'):
                    
                    print("I hit this")
                    raise FileNotFoundError(f'No PDF could be downloaded for {current_paper[0]}')

                downloaded_files = os.listdir(f'{PAPER_DIRECTORY}/new_downloads')

                # Check if a downloaded file exists
                if len(downloaded_files) == 1:
                    print("Over here?")
                    extension = downloaded_files[0].split('.')[-1].lower()

                    # If there is still a download in progress, keep waiting.
                    if extension == 'crdownload':
                        continue
                    # If the PDF is downloaded, move it to folder using db name.
                    elif extension == 'pdf':
                        os.rename(f'{PAPER_DIRECTORY}/new_downloads/{downloaded_files[0]}', f'{PAPER_DIRECTORY}/{file_title}.pdf')
                        print(f'Download success!')
                        break
                    else:
                        raise Exception(f'Invalid file type for {current_paper[0]}')
                elif len(downloaded_files) == 0:
                    print("Or here?")
                    raise FileNotFoundError(f'No PDF could be downloaded for {current_paper[0]}')
                else:
                    raise Exception(f'Too many files for {current_paper[0]}')


        except Exception as e:
            print(f'Something went wrong for {current_paper[0]}: {e}')
            papers.append(current_paper)

        if os.path.isdir(f'{os.getcwd()}/{PAPER_DIRECTORY}/new_downloads'):
            print("something failed")
            shutil.rmtree(f'{os.getcwd()}/{PAPER_DIRECTORY}/new_downloads/')