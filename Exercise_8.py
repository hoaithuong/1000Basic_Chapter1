# Exercise 8: S(n) = 1/2+ 3/4 + 5/6 + ... + (2n+1)/(2n+2) = ?
def exe8():
    s = 0.0
    n = int(input("Nhap n lon hon 0: "))
    if n < 0:
        return
    elif n==0:
        return s
    else:
        for i in range(1,n+1):
            s = (2*i+1)/(2*i+2)
        return s

print("S(n)= " + str(exe8()))
