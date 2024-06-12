import sys
tamSeq = int(input())
Seq = sys.stdin.readline().split()
for i in range(0, tamSeq):
    Seq[i] = int(Seq[i])
escadinha = 1
if (tamSeq == 1):
    print(escadinha)
elif (tamSeq == 2):
    print(escadinha)
else:
    difatual = Seq[0] - Seq[1]
    for i in range(1, tamSeq-1):
        difnova = Seq[i] - Seq[i+1]
        if (difatual != difnova):
            difatual = difnova
            escadinha = escadinha+1
    print(escadinha)
# 8
#1 1 1 3 5 4 8 12
