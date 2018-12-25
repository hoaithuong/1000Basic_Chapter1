# Exercise 4: S(n) = 1+ 1/2 + 1/4 + ... + 1/2n = ?
def exe4():
    s = 1.0
    n = int(input("Nhap n lon hon 0: "))
    if n < 0:
        return
    elif n==0:
        return s
    else:
        for i in range(2,n+1,2):
            s = s + 1/i
        return s

print("S(n)= " + str(exe4()))
