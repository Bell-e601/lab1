from bs4 import BeautifulSoup
import requests

def parse(let):
    alphabet = [
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л',
        'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
        'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']
    index = alphabet.index(let.upper())
    url = 'https://www.omgtu.ru/university/about-the-university/persons/index.php?b=' + str(index) # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    items = soup.findAll('div', style="padding: 5px; font-size: 120%;")
    workers = []
    for data in items:
        #if data.find('a'):
        workers.append(data.text.replace('\n ', ''))

    return workers

let = input('Введите вашу фамилию: ')[0]
workers = parse(let)
print ('Если бы начнёте работать в Политехе, то будете находится среди этих людей: ')
for worker in workers:
    print(worker, end='')
file = open('Workers.txt', 'w')
file.writelines(workers)
file.close()