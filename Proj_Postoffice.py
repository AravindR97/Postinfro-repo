#Program to get details of Post Offices from Indian Postal Dept API. Selections by Pincode & Post Office name

import requests
import pandas as pd

def post(url):
    r = requests.get(url)

    df = pd.DataFrame(r.json()[0]['PostOffice'],columns= ['Name','BranchType','DeliveryStatus','Division',
                                                               'District','State','Pincode'])
                                            #-In this case, r.json() gives a list of dicts with only one element. Hence r.json()[0]
                                            #is used. In that dict, the key 'PostOffice' carries a list of dicts as value. This list
                                            #of dicts is cast into a DF with selected columns-
    return df

choice = int(input("Enter 0 to search by PIN and 1 to search by Post office name: "))

if choice == 0:
    ip = input("Enter the PIN: ").strip()
    url = 'https://api.postalpincode.in/pincode/' + ip

    df_main = post(url)

    print(f"\nThere are {len(df_main.index)} Post Offices sharing the PIN code {ip}\n")

    #Modifying the row labels:
    df_main.index = list(range(1,len(df_main.index)+1))
    print(df_main)
    
elif choice == 1:
    ip = input("Enter the name of the Post Office: ")
    url = "https://api.postalpincode.in/postoffice/" + ip

    df_main = post(url)
    
    print(f"\nThere are {len(df_main.index)} Post Offices having name {ip}\n")

    #Modifying the row labels:
    df_main.index = list(range(1,len(df_main.index)+1))
    print(df_main)
    
else:
    print("Than endu thenga aado parayunne?\n")
    
excel = input("Do you want to save the DataFrame to an excel file?:(y/n)\n")
if excel == 'y':
    df_main.to_excel(f"C:/Users/Aravind R/Desktop/{ip}.xlsx")
else:
    pass
