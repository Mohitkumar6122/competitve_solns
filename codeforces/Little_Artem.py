# contest: Codeforces Round #632 (Div. 2), problem: (A) Little Artem, Accepted, 
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
 
for t in range(int(input())):
    n,m = map(int,input().split())
    l = [['B' for i in range(m)] for j in range(n)]
    l[0][0]='W'
    for n in l:
        print(*n,sep='')
