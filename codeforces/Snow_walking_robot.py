# contest: Codeforces Round #605 (Div. 3), problem: (B) Snow Walking Robot, Happy New Year!, #
 
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
# ░░░░░░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░░░░░
# ░░░░░░█░░▄▀▀▀▀▀▀▀▀▀▀▀▀▄░░█░░░░░
# ░░░░░░█░█░░▀░░░░░░░░▀░░█░█░░░░░
# ░░░░░░█░█░░░▀░░░░░░▀░░░█░█░░░░░
# ░░░░░░█░█░░░░▀░░░░▀░░░░█░█░░░░░
# ░░░░░░█░█▄░░░░▀░░▀░░░░▄█░█░░░░░
# ░░░░░░█░█░░░░░░██░░░░░░█░█░░░░░
# ░░░░░░█░▀░░░░░░░░░░░░░░▀░█░░░░░
# ░░░░░░█░░░░░░░░░░░░░░░░░░█░░░░░
# ░░░░░░█░░░░░░░░░░░░░░░░░░█░░░░░
# ░░░░░░▀░░░░░░░░░░░░░░░░░░▀░░░░░
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 
t = int(input())
for i in range(t):
    s =input()
    l=s.count("L")
    r=s.count("R")
    d=s.count("D")
    u=s.count("U")
    lr,ud = min(l,r),min(u,d)
    if lr==0 and ud==0:
        print(0)
    elif lr==0:
        print(2)
        print("UD")
    elif ud==0:
        print(2)
        print("LR")
    else:
        print(2*(lr+ud))
        print("L"*lr + "U"*ud + "R"*lr + "D"*ud)