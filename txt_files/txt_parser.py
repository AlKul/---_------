import re

with open('./txt_files/1st.txt') as f:
    lines = f.readlines()

company_flags = ['общество', 'ооо', 'зао', 'оао', 'организация']

companies = []
grants = []

for line in lines:
    for check in company_flags:
        if line.lower().find(check) >= 0:
            companies.append(line)
            continue
    if re.search('\d\d\d\s\d\d\d,\d\d', line):
        grants.append(line)

print()
