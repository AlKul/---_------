import re
import pandas as pd
import os



company_flags = ['общество', 'ооо', 'зао', 'оао', 'организация']

companies = []
grants = []

def get_info(x):
    flag = 0
    data_list = []
    
    while True:
        data = {}
        m = re.search('\".+?\S\"[А-Я]', x)
        if m is None:
            return data_list
        company_name = x[(m.start()+1):(m.end()-1)]
        #print(company_name)
        g = re.findall('[\d\d\d\s?]+,\d\d', x)
        #print(re.search('[\d\d\d\s?]+,\d\d', x))
        g_end_pos = re.search('[\d\d\d\s?]+,\d\d', x).end()
        x = x[g_end_pos:]
        g_end_pos = re.search('[\d\d\d\s?]+,\d\d', x).end()
        grant = g[0]
        data['company_name'] = company_name
        data['grant'] = int(re.sub('\s', '', grant[:-3]))
        if data != []:
            #print(data)
            data_list.append(data)
        x = x[g_end_pos:]

def txt_parser2(filename):
    with open(f'./txt_files/{filename}') as f:
        lines = f.readlines()
        
    data_list = []
    df = pd.DataFrame()
    for line in lines:
        info = get_info(line)
        #print(info)
        if (info is None) or (info == []):
            continue
        else:
            data_list.append(info)
            df = pd.concat([df, pd.DataFrame.from_records(info)])
    dir_path = os.path.join('pickle_files')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    df.to_pickle(f'./pickle_files/{filename[:-4]}.pkl')
    return 0

# txt_parser2('2nd.txt')

