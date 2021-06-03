import pandas as pd
import matplotlib as mat
from openpyxl import Workbook

def clean(filename, column_name):
    data = pd.read_excel(filename)
    df = pd.DataFrame(data, columns = [column_name])
    print(df)
