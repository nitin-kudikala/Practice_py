from tabula import read_pdf
from tabulate import tabulate


try:
    df = read_pdf('E:\\GoogleDrive\\Financials documents\\Holdings_Report\\RaniStatement_Nov2022.pdf',pages=1,password='kudikala86')
    #print(tabulate(df))
    print(df[['text']].to_string(index=False))

except Exception as e:
    print(e)
