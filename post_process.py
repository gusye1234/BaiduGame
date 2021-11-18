from collections import defaultdict

test_file = "./data/test_A.tsv"
MISSPELLING = defaultdict(list)
with open("rule.txt", encoding="utf-8") as f:
    for line in f:
        left, right = line.strip().split()
        MISSPELLING[left].append(right)
        MISSPELLING[right].append(left)

print("Misspelling", len(MISSPELLING))

def return_diff(left, right):
    current_in = False
    l_curr, r_curr = [], []
    re = []
    for i in range(len(left)):
        if left[i] == right[i]:
            current_in = False
            if len(l_curr):
                re.append(("".join(l_curr), "".join(r_curr)))
                l_curr = []
                r_curr = []
        else:
            current_in = True
            l_curr.append(left[i])
            r_curr.append(right[i])
    if len(l_curr):
        re.append(("".join(l_curr), "".join(r_curr)))
    return re

with open("./quest/predict_result") as pred, open("./post_result", 'w') as post, \
    open(test_file, encoding="utf-8") as test:
    total_change = 0
    total_hit = 0
    for label, line in zip(pred, test):
        left, right = line.strip().split('\t')
        if int(label) == 0 and len(left) == len(right):    
            total_hit += 1
            diffs = return_diff(left, right)
            change = True
            for d in diffs:
                if d[1] in MISSPELLING[d[0]] or d[0] in MISSPELLING[d[1]]:
                   continue
                change = False
            if change:
                label = "1\n"
                total_change += 1
                print(diffs, left, right)
        post.write(label)
    print(f"Hit {total_hit}, Changed {total_change}")