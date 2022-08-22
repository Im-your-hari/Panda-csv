#import csv

#Read CSV File__________________________
'''
f = open('cities.csv', 'rt')

myReader = csv.reader(f)

for i in myReader:
    print(i[8])
'''

#Write CSV File_________________________
'''
list = [
    ['Name','Age','DoB'],
    ['Hari','20','29-03-2002'],
    ['Krishnan','21','03-29-2002']
]
with open('student.csv', 'w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    for i in list:
        writer.writerow(i)
'''
#Write in existing CSV file_______________
'''
list = [
    ['Hari','20','29-03-2002'],
    ['Krishnan','21','03-29-2002']
]
with open('student.csv', 'a',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    for i in list:
        writer.writerow(i)
'''
#Using Panda_______________________________
import pandas as pd

a = pd.read_csv('student.csv')

print(a.head())#Starting thott ulla data kaanikkan
print("______________________________________")
print(a.tail(2))#End thott ulla data kaanikkan - Last 2 ennam
print("______________________________________")
print(a["Name"])#Column Nameil ullath display chyyn