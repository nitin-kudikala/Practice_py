import numpy as np
import pandas as pd

pd.read_csv()


#pip install xlrd
pd.read_excel('excel_sample.xlsx',sheet_name='Sheet1')

pd.read_html('https://google.com/')

# # from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:')
# df = pd.DataFrame()

# df.to_sql('mytable',engine)
# sqldf = pd.read_sql('mytable',con=engine)
