# Exercise 10: T(x,n) = x^n = ?
def exe10(x,n):
    s = 1
    n = int(input("Nhap n lon hon 0: "))
    if n < 0:
        return
    elif n==0:
        return s
    else:
        for i in range(1,n+1):
            s = s*i
        return s

print("S(n)= " + str(exe10()))
