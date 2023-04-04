# import pandas as pd
# import os
# from PyPDF2 import PdfFileReader
# df = pd.DataFrame(columns=['fileName', 'fileLocation', 'pageNumber'])
# for root, dirs, files in os.walk(r'C:/Users/chitl/OneDrive\Desktop/pdf pages/Class 7/Section A/'):
# # folder_link = 'https://learnbasicsfun-my.sharepoint.com/:f:/g/personal/saran_learnbasics_fun/EtSZCqJUALRGi7DSZXnrcNkBJZNqjbcKwLuLOgR4gowcqQ?e=BY3ahs'
# # for root, dirs, files in os.walk(folder_link):
#     for f in files:
#         if f.endswith(".pdf"):
#             pdf=PdfFileReader(open(os.path.join(root, f),'rb'))
#             df2 = pd.DataFrame([[f, os.path.join(root,f), pdf.getNumPages()]], columns=['fileName', 'fileLocation', 'pageNumber'])
#             df = df.append(df2, ignore_index=True)
# print(df)
# df.to_csv('page_number.csv')

import pandas as pd
import os
from PyPDF2 import PdfFileReader

df = pd.DataFrame(columns=['fileName', 'fileLocation', 'pageNumber'])
for root, dirs, files in os.walk(r'D:\BHANU\Internship\Python\no.of_pages_in_pdfs\Class 7'):
    for f in files:
        if f.endswith(".pdf"):
            pdf = PdfFileReader(open(os.path.join(root, f), 'rb'))
            df2 = pd.DataFrame([[f, os.path.join(root, f), pdf.getNumPages()]],
                               columns=['fileName', 'fileLocation', 'pageNumber'])
            df = df.append(df2, ignore_index=True)
print(df.head)

