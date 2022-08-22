import pandas as pd

#df = pd.read_csv('student.csv')
na_values = {
    'Name': ["hari","abcd"],
    'price':[100,10],
    'stroke':["1","7"],
    'horsepower':["999","2"],
    'peak-rpm':["10","5"],
    'average_milege':["115","15"],
}
'''
#print(df)
#df.to_csv("student.csv")
#print(na_values)
print("_________________________________")
df = pd.DataFrame(na_values)
#print(df)
df.to_csv("student.csv",index=False,header=-1)
print(pd.read_csv("student.csv"))
print("_________________________________")
print(df.describe())
print("_________________________________")
'''

df = pd.DataFrame(
    [
        [1,"Hari",20,"cse"],
        [2,"Krishnan",21,"it"],
        [3,"Hari",20,"cse"],
        [4,"Krishnan",21,"it"],
        [5,"Hari",20,"cse"],
        [6,"Krishnan",21,"it"]
    ],
    columns=["Roll","Name","Age","Dep"]
    )
print(df)

df.to_csv("student1.csv",index=False)