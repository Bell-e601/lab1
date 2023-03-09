from bs4 import BeautifulSoup
import requests
import sys

def parse(let):
    ALPHABET = [
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л',
        'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
        'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']
    if let.upper() not in ALPHABET:
        let = 'А'
    index = ALPHABET.index(let.upper())
    URL = 'https://www.omgtu.ru/university/about-the-university/persons/index.php?b=' + str(index)
    
    try:
        page = requests.get(URL)
    except Exception as _ex:
        print(_ex)
        sys.exit(0)
        
    soup = BeautifulSoup(page.text, "html.parser")
    items = soup.findAll('div', style="padding: 5px; font-size: 120%;")
    workers = []
    for data in items:
        workers.append(data.text.replace('\n ', ''))

    return workers

let = input('Введите вашу фамилию: ')[0]
workers = parse(let)
print ('Если бы начнёте работать в Политехе, то будете находится среди этих людей: ')
for worker in workers:
    print(worker, end='')
try:
    file = open('Workers.txt', 'w')
    file.writelines(workers)
except Exception as _ex:
    print(_ex)
finally:
    file.close()