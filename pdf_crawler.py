import requests
import os

from pdf_2_txt import pdf_saver
from df_parser import pdf_2_txt
from txt_parser2 import txt_parser2
from df_union import df_union

urls = [
    "https://digital.gov.ru/uploaded/files/proektyipobeditelirfrit-razrabotka_L44JfEn.pdf", 
    "https://digital.gov.ru/uploaded/files/proektyipobeditelirfrit-vnedrenie_10i80FX.pdf",
    "https://digital.gov.ru/uploaded/files/proektyi-pobediteli-fsi.pdf",
    "https://digital.gov.ru/uploaded/files/proektyi-pobediteli-skolkovo.pdf"
    ]
#url = 'https://digital.gov.ru/uploaded/files/proektyipobeditelirfrit-vnedrenie_10i80FX.pdf'

# Downloading pdf's
files = []
for url in urls:
    files.append(pdf_saver(url))


# Converting Pdf's to txt
txt_files = []
for file in files:
    txt_files.append(pdf_2_txt(f'{file}'))
print("Pdf's converting to txt complete")

# Parsing txt
for file in txt_files:
    txt_parser2(file.split('/')[-1])
print("Txt's parsing complete")

# Collecting all dfs to one
df_union()

