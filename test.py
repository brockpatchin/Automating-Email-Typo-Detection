import pandas as pd
import matplotlib as mat
from openpyxl import Workbook

list_of_domains = []

def split(s, a):
    result = []

    s.split('@')

    return result

def similarity_score(s, a):
    first = len(s)
    second = len(a)

    counter = 0

    for i in range(min(first, second)):
        if s[i].lower() == a[i].lower():
            counter += 1

    if counter / max(first, second) >= 0.85:
        return True
    else:
        return False

def clean(filename, column_name):
    data = pd.read_excel(filename)
    df = pd.DataFrame(data, columns = [column_name])

    #Puts all of the emails into a numpy array
    list_of_emails = df.values

    email_amounts = {}

    total_emails = len(list_of_emails)

    for i in list_of_emails:
        if str(i) not in email_amounts.keys():
            email_amounts[str(i)] = 1
        else:
            email_amounts[str(i)] += 1

    total_domains = len(email_amounts)
    
    print("There are a total of " + str(total_emails) + " emails addresses in your excel sheet.")
    print("More specifically, there are " + str(total_domains) + " unique email domains.")

    most_popular_emails = []

    #Test
    #for x in email_amounts.keys():
    #    if email_amounts[x] > 1:
    #        print(x + " has " + str(email_amounts[x]) + " occurences!")

    #Creating a list that holds the most common emails (specifically trying to avoid typo emails so this list will include only the most popular email domains)
    for x in email_amounts.keys():
        if email_amounts[x] > total_emails * (0.006):
            most_popular_emails.append(x)

    print("Here are the most common email domains in your excel sheet")
    print(most_popular_emails)

    possible_typos = []

    for x in email_amounts.keys():
        for y in most_popular_emails:
            if similarity_score(x, y) == True and x not in possible_typos and x not in most_popular_emails:
                possible_typos.append(x)
    
    print("Here are the tagged domains that could be possible typos. These will be the domains that will be preseneted in a graph that will then be presented to the user")
    print(possible_typos)

clean('C:/Users/brock/OneDrive/Desktop/brock/holdem.xlsx', 'emails')