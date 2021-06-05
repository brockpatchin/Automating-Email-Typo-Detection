import pandas as pd
import matplotlib as mat
from openpyxl import Workbook

def clean(filename, column_name):
    data = pd.read_excel(filename)
    df = pd.DataFrame(data, columns = [column_name])

    #Puts all of the emails into a numpy array
    list_of_emails = df.values

    email_amounts = {}

    for i in list_of_emails:
        if str(i) not in email_amounts.keys():
            email_amounts[str(i)] = 1
        else:
            email_amounts[str(i)] += 1
    
    for x in email_amounts.keys():
        if email_amounts[x] > 1:
            print(x + " has " + str(email_amounts[x]) + " occurences!")
            

clean('C:/Users/brock/OneDrive/Desktop/brock/holdem.xlsx', 'emails')