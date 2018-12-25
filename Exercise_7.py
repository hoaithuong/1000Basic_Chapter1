# Exercise 7: S(n) = 1/2+ 2/3 + 3/4 + ... + n/(n+1) = ?
def exe7():
    s = 0.0
    n = int(input("Nhap n lon hon 0: "))
    if n < 0:
        return
    elif n==0:
        return s
    else:
        for i in range(1,n+1):
            s = s + i/(i+1)
        return s

print("S(n)= " + str(exe7()))
