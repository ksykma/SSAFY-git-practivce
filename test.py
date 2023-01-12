testcase = int(input())

a, b = map(int, input().split())

for t in range(1, testcase + 1):
    if (a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
        print("B")
    elif (a==2 and b==1) or (a==1 and b==3) or (a==3 and b==2):
        print("A")
    else:
        print("=")