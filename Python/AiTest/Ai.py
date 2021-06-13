queans={}
while True:
    print("Enter your command")
    command=input()
    if command in queans:
        print(queans[command])
    else:
        print("I dont know Answer")
        print("tell me answer")
        ans=input()
        queans[command]=ans
