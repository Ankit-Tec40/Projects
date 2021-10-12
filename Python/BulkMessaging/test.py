import pandas as pd
lst=list(pd.read_csv("e:\Projects\Python\BulkMessaging\data.csv").MobileNo)
for x in range(len(lst)):
    print(lst[x])
    if (x%10==0):
        print("-------------------------",x//10+1,"-----------------------------")
