# Exercise 2: S(n) = 1^2 + 2^2 + ... + n^2 = ?
def exe2():
    s=0
    n = int(input("Nhap n lon hon 0: "))
    if n < 0:
        return
    elif n==0:
        return s
    else:
        for i in range(1,n+1):
            s = s + i**2
        return s

print("S(n)= " + str(exe2()))
