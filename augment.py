import sys
import jieba
from collections import defaultdict
from tqdm import tqdm
from random import choice
train_data = "./data/all_train.txt"

def double(data):
    new_data = []
    for d in data:
        new_data.append((d[1], d[0], d[2]))
    data.extend(new_data)

def readfrom(file):
    data = []
    with open(file, encoding='utf-8') as f:
        for line in f:
            data.append(line.strip().split('\t'))
    return data

def find_negative(data):
    pass

def generatre_misspelling(data):
    MISSPELLING = defaultdict(list)
    with open("rule.txt", encoding="utf-8") as f:
        for line in f:
            left, right = line.strip().split()
            MISSPELLING[left].append(right)
            MISSPELLING[right].append(left)
    to_pop = []
    for k in MISSPELLING.keys():
        if len(MISSPELLING[k]) > 1:
            to_pop.append(k)    
    for k in to_pop:
        MISSPELLING.pop(k)
    print("Misspelling", len(MISSPELLING))
    max_num = 100
    already_num = defaultdict(int)
    new_data = []
    for d in tqdm(data):
        found = False
        assert d[2] == '0' or d[2] == '1'
        seg_1 = jieba.cut(d[0])
        seg_2 = jieba.cut(d[1])
        for m in seg_1:
            if m in MISSPELLING:
                if already_num[m] > max_num:
                    continue
                else:
                    already_num[m] += 1
                miss = choice(MISSPELLING[m])
                new_data.append((d[0], d[0].replace(m, miss), "1"))
                new_data.append((d[1], d[0].replace(m, miss), d[2]))
        for m in seg_2:
            if m in MISSPELLING:
                if already_num[m] > max_num:
                    continue
                else:
                    already_num[m] += 1
                miss = choice(MISSPELLING[m])
                new_data.append((d[1], d[1].replace(m, miss), "1"))
                new_data.append((d[0], d[1].replace(m, miss), d[2]))
        print(f"\r{len(new_data)}", end='')
        sys.stdout.flush()
    data.extend(new_data)
    with open("used.txt", 'w') as f:
        for k, v in already_num.items():
            if v:
                f.write('\t'.join([k, str(v)]) + '\n')

def pass_and_back(data):
    new_data = []
    data_dict = defaultdict(list)
    for d in data:
        data_dict[d[0]].append((d[1], d[2]))
        # data_dict[d[1]].append((d[0], d[2]))
    for d in data:
        pack = data_dict[d[1]]
        label = int(d[2])
        if len(pack):
            for p in pack:
                l_p = int(p[1])
                if l_p or label:
                    new_data.append((d[0], p[0], str(l_p*label)))
    data.extend(new_data)

def write2(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        for d in data:
            f.write("\t".join(d) + '\n')


data = readfrom(train_data)
generatre_misspelling(data)
print(len(data))
pass_and_back(data)
print(len(data))
double(data)
write2(data, "./data/aug_train.txt")