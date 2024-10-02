def f5_1(h, s):
    if (h==3 or h==5) and s>=66:
        return 1
    elif (h==5)and s<66:
        return 0
    elif (h==2 or h==4) and s>=66:
        return 0
    elif h%2==0:
        return f5_1(h+1, s+1) or f5_1(h+1, s*3)
    return f5_1(h+1, s+1) and f5_1(h+1, s*3)


def f5_2(h, s):
    if (h==3 or h==5) and s>=98:
        return 1
    elif (h==5)and s<98:
        return 0
    elif (h==2 or h==4) and s>=98:
        return 0
    elif h%2==0:
        return f5_2(h+1, s+1) or f5_2(h+1, s*2)
    return f5_2(h+1, s+1) and f5_2(h+1, s*2)

def f5_3(h, s):
    if (h==3 or h==5) and s>=40:
        return 1
    elif (h==5)and s<40:
        return 0
    elif (h==2 or h==4) and s>=40:
        return 0
    elif h%2==0:
        return f5_3(h+1, s+1) or f5_3(h+1, s*2)or f5_3(h+1, s+4)
    return f5_3(h+1, s+1) and f5_3(h+1, s*2) and f5_3(h+1, s+4)

def f5_4(h, s):
    if (h==3 or h==5) and s>=46:
        return 1
    elif (h==5)and s<46:
        return 0
    elif (h==2 or h==4) and s>=46:
        return 0
    elif h%2==0:
        return f5_4(h+1, s+1) or f5_4(h+1, s*3)
    return f5_4(h+1, s+1) and f5_4(h+1, s*3)

def f5_5(h, s):
    if (h==3 or h==5) and s>=129:
        return 1
    elif (h==5)and s<129:
        return 0
    elif (h==2 or h==4) and s>=129:
        return 0
    elif h%2==0:
        return f5_5(h+1, s+1) or f5_5(h+1, s*2)
    return f5_5(h+1, s+1) and f5_5(h+1, s*2)


def f6_6(h, s1, s2):
    if (h==3 or h==5) and s1+s2>=68:
        return 1
    elif (h==5)and s1+s2<68:
        return 0
    elif (h==2 or h==4) and s1+s2>=69:
        return 0
    elif h%2==0:
        return f6_6(h+1, s1+1, s2) or f6_6(h+1, s1, s2+1) or f6_6(h+1, s1*3, s2) or f6_6(h+1, s1, s2*3)
    return f6_6(h+1, s1+1, s2) and f6_6(h+1, s1, s2+1) and f6_6(h+1, s1*3, s2) and f6_6(h+1, s1, s2*3)

def f6_7(h, s1, s2):
    if (h==3 or h==5) and s1+s2>=67:
        return 1
    elif (h==5)and s1+s2<67:
        return 0
    elif (h==2 or h==4) and s1+s2>=67:
        return 0
    elif h%2==0:
        return f6_7(h+1, s1+1, s2) or f6_7(h+1, s1, s2+s1) or f6_7(h+1, s1+s2, s2) or f6_7(h+1, s1, s2+1)
    return f6_7(h+1, s1+1, s2) and f6_7(h+1, s1, s2+s1) and f6_7(h+1, s1+s2, s2) and f6_7(h+1, s1, s2+1)

def f6_8(h,s1,s2):
    if (h==3 or h==5) and s1+s2<=20:
        return 1
    elif (h==5)and s1+s2>20:
        return 0
    elif (h==2 or h==4) and s1+s2<=20:
        return 0
    elif h%2==0:
        return f6_8(h+1, s1-1, s2) or f6_8(h+1, s1, s2-1) or f6_8(h+1, s1//2, s2) or f6_8(h+1, s1, s2//2)
    return f6_8(h+1, s1-1, s2) and f6_8(h+1, s1, s2-1) and f6_8(h+1, s1//2, s2) and f6_8(h+1, s1, s2//2)

def f6_9(h, s1, s2):
    if (h==3 or h==5) and s1+s2>=231:
        return 1
    elif (h==5)and s1+s2<231:
        return 0
    elif (h==2 or h==4) and s1+s2>=231:
        return 0
    elif h%2==0:
        return f6_9(h+1, s1+1, s2) or f6_9(h+1, s1, s2+1) or f6_9(h+1, s1*2, s2) or f6_9(h+1, s1, s2*2)
    return f6_9(h+1, s1+1, s2) and f6_9(h+1, s1, s2+1) and f6_9(h+1, s1*2, s2) and f6_9(h+1, s1, s2*2)


for i in range(1, 65):
    if f5_1(1, i) == 1:
        print("5.1: ", i)
        break
    
for i in range(1, 65):
    if f5_2(1, i) == 1:
        print("5.2: ", i)
        break

for i in range(1, 40):
    if f5_3(1, i) == 1:
        print("5.3: ", i)
        break

for i in range(1, 46):
    if f5_4(1, i) == 1:
        print("5.4: ", i)
        break
    
for i in range(1, 128):
    if f5_5(1, i) == 1:
        print("5.5: ", i)
        break

for i in range(1, 61):
    if f6_6(1, 6, i) == 1:
        print("6.6: ", i)
        break

for i in range(1, 61):
    if f6_7(1, 9, i) == 1:
        print("6.7: ", i)
        break

maxF=0
for i in range(11, 10000):
    if f6_8(1, 10, i) == 1 and maxF<=i:
        maxF=i
print("6.8: ", maxF)

for i in range(1, 213):
    if f6_9(1, 17, i) == 1:
        print("6.9: ", i)
        break
