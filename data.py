import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook

list_of_domains = []

possible_typos = {}

def split(s):
    temp = s.split('@')[1]
    new = temp[0:len(temp)-2]
    return new

def similarity_score(s, a):
    first = len(s)
    second = len(a)

    counter = 0

    for i in range(min(first, second)):
        if s[i].lower() == a[i].lower():
            counter += 1

    if counter / max(first, second) >= 0.75:
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
        temp = split(str(i))
        if temp not in email_amounts.keys():
            email_amounts[temp] = 1
        else:
            email_amounts[temp] += 1

    total_domains = len(email_amounts)
    
    print("There are a total of " + str(total_emails) + " emails addresses in your excel sheet.")
    print("More specifically, there are " + str(total_domains) + " unique email domains.")

    most_popular_emails = []

    #Creating a list that holds the most common emails (specifically trying to avoid typo emails so this list will include only the most popular email domains)
    for x in email_amounts.keys():
        if email_amounts[x] > total_emails * (0.006):
            most_popular_emails.append(x)

    print("Here are the most common email domains in your excel sheet")
    print(most_popular_emails)

    for x in email_amounts.keys():
        for y in most_popular_emails:
            if similarity_score(x, y) == True and x not in possible_typos and x not in most_popular_emails:
                possible_typos[x] = email_amounts[x]
    
    print("Here are the tagged domains that could be possible typos.")
    # These are the email domains that will be presented to the user in a graphical format. 
    print(possible_typos)
    return True



def show_graph():
    plt.bar(possible_typos.keys(), possible_typos.values())
    plt.xticks(rotation = 90)
    plt.show()