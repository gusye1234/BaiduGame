import sys
from collections import defaultdict

test_file = "./data/test_A.tsv"


# sys.stdout = open("see.txt", 'w', encoding='utf-8')


# with open(test_file, encoding="utf-8") as f:
#     for l in f:
#         l = l.strip().split('\t')
#         if len(l[0]) == len(l[1]):
#             left = []
#             right = []
#             for i in range(len(l[0])):
#                 if l[0][i] != l[1][i]:
#                     left.append(l[0][i])
#                     right.append(l[1][i])
#             if len(left) == 1:
#                 print(f"{''.join(left)} {''.join(right)}\t{l[0]}\t{l[1]}")
# sys.stdout.close()

with open("same.txt", encoding='utf-8') as f, open("rule.txt", 'w', encoding='utf-8') as fw, \
     open("stopwords.txt") as stop:
    stop_set = set([l.strip() for l in stop])
    for line in f:
        l = line.strip().split()
        if len(l[0]) == len(l[1]):
            if l[0] not in stop_set and l[1] not in stop_set:
                fw.write(line)


