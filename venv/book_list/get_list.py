import pandas as pd
import os

if __name__ == '__main__':
    path = 'D:/20210228/new.xlsx'
    df = pd.read_excel(path,sheet_name='Sheet1',names=['小说名'],usecols=[0])
    print(df.shape)
    book_list = list(df['小说名'].values)
    print(book_list, len(book_list))   