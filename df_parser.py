


# from tkinter import N
# import tabula
# #from tabula import read_pdf
# from tabulate import tabulate
# import pandas as pd
# import io

filename = './pdf_files/proektyipobeditelirfrit-vnedrenie_10i80FX.pdf'
import PyPDF2

def pdf_2_txt(filename): 
    filepath = f'./pdf_files/{filename}'
    file = open(filepath,'rb')
    pdfReader = PyPDF2.PdfFileReader(file)
    
    # printing number of pages in pdf file
    n_pages = pdfReader.numPages

    text = ''
    # creating a page object
    for i in range(n_pages):
        pageObj = pdfReader.getPage(i)
        # extracting text from page
    #    print(pageObj.extractText())
        print(f"Page: {i+1}")
        text += '\n' 
        text += pageObj.extractText()
    
    # closing the pdf file object
    file.close()

    with open(f'./txt_files/{filename[:-4]}.txt', 'w') as fw:
        fw.write(text)
        print('Text saved')
    return f'./txt_files/{filename[:-4]}.txt'


# from tabula import read_pdf
# from tabulate import tabulate
# import pandas as pd
# import io

# Read the only the page n°6 of the file
# food_calories = read_pdf('./data/food_calories.pdf',pages = 6, 
#                          multiple_tables = True, stream = True)

# # Transform the result into a string table format
# table = tabulate(food_calories)

# # Transform the table into dataframe
# df = pd.read_fwf(io.StringIO(table))

# # Save the final result as excel file
# df.to_excel("./data/food_calories.xlsx")

# print('pizdec')


# import camelot

# file = './pdf_files/proektyipobeditelirfrit-vnedrenie_10i80FX.pdf'
# tables = camelot.read_pdf(file)

# print('1')