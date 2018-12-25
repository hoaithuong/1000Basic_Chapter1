# Exercise 6: S(n) = 1+ 1/1x2 + 1/2x3 + ... + 1/nx(n+1) = ?
def exe6():
    s = 1.0
    n = int(input("Nhap n lon hon 0: "))
    if n < 0:
        return
    elif n==0:
        return s
    else:
        for i in range(1,n+1):
            s = s + 1/(i*(i+1))
        return s

print("S(n)= " + str(exe6()))
