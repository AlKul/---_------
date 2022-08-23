import requests
import os

from parser2 import pdf_to_text


def pdf_saver(url):
    filename = url.split('/')[-1]
    response = requests.get(url)
    dir_path = os.path.join('pdf_files')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(f'./pdf_files/{filename}', 'wb') as f:
        f.write(response.content)
    return filename


url = 'https://digital.gov.ru/uploaded/files/proektyipobeditelirfrit-vnedrenie_10i80FX.pdf'
filename = url.split('/')[-1]

response = requests.get(url)

print('1')

dir_path = os.path.join('pdf_files')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
with open(f'./pdf_files/{filename}', 'wb') as f:
    f.write(response.content)

dir_path = os.path.join('txt_files')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
print('2')
pdf_to_text(f'./pdf_files/{filename}', './txt_files/1st.txt')