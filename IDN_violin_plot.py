import seaborn as sns
import matplotlib.pyplot as plt
import csv
import numpy as np

f_path = "/Users/leejmacbook/Desktop/"
f_name = f_path + "IDN_exp_crop_def.txt"

region = []
crop = []
defo = []
cexp = []
texp = []

prd_idx, cns_idx, hprd_idx = [], [], []
marg_area = 0
mid_area = 0
n_gr = 2

crop_sort = "sugc"
crop_items = [crop_sort + "_mean"]
defo_items = ["defo_mean"]
fexp_item = "2"

# exp_items = ["13"]    # potato
# exp_items = ["122"]   # cooking oil
# exp_items = ["122", "124"]  # cooking and other oils
# exp_items = ["53", "54", "55", "56", "57", "58", "59"]    # meats
# exp_items = ["130"]    # coffee
# exp_items = ["131"]    # instant coffee
# exp_items = ["2","3"]     # rice
# exp_items = ["159","160","161"]   # cooked rice
# exp_item = ["78"]   # bean
# exp_item = ["114","115"]   # banana
# exp_items = ["99","100","101"]    # nuts
# exp_items = ["182"]               # liquor
# exp_items = ["184","185","186","187","188"]   # cigarettes and tobacco
exp_items = ["126","127"]         # sugar
# exp_items = ["128", "129","130", "131","132"]     # teas
# exp_items = ["121", "123"]      # coconut

def split(lst, n):
    k, m = divmod(len(lst), n)
    return list(lst[i*k+min(i,m):(i+1)*k+min(i+1,m)] for i in range(n))

with open(f_name) as dfile:
    reader = csv.reader(dfile, delimiter='\t')
    title = next(reader)
    cexp_idx = [title.index(eit) for eit in exp_items]
    crop_idx = [title.index(cit) for cit in crop_items]
    defo_idx = [title.index(dit) for dit in defo_items]
    fexp_idx = title.index(fexp_item)

    for row in reader:
        region.append(row[0])
        crop.append(sum([float(row[cidx]) for cidx in crop_idx]))
        defo.append(sum([float(row[didx]) for didx in defo_idx]))
        cexp.append(sum([float(row[eidx]) for eidx in cexp_idx]))
        texp.append(sum([float(e) for e in row[fexp_idx:]]))

n = len(region)

for i in range(n):
    if mid_area > 0 and crop[i] > mid_area: hprd_idx.append(i)
    elif crop[i] > marg_area: prd_idx.append(i)
    elif crop[i] <= marg_area: cns_idx.append(i)

prd_idx, cns_idx = np.array(prd_idx), np.array(cns_idx)
n_prd, n_cns = len(prd_idx), len(cns_idx)
prd_defo = np.array(defo)[prd_idx]
cns_texp = np.array(texp)[cns_idx]

prd_def_idx = split(prd_idx[sorted(range(n_prd), key = lambda i:prd_defo[i])], n_gr)
cns_exp_idx = split(cns_idx[sorted(range(n_cns), key = lambda i:cns_texp[i])], n_gr)

if mid_area > 0:
    hprd_idx = np.array(hprd_idx)
    n_hprd = len(hprd_idx)
    hprd_defo = np.array(defo)[hprd_idx]
    hprd_def_idx = split(hprd_idx[sorted(range(n_hprd), key = lambda i:hprd_defo[i])], n_gr)

gr_idx = np.zeros(n)
for i in range(n_gr):
    for j in cns_exp_idx[i]: gr_idx[j] = i
    for j in prd_def_idx[i]: gr_idx[j] = i + n_gr
    if mid_area > 0:
        for j in hprd_def_idx[i]: gr_idx[j] = i + n_gr * 2

if n_gr == 2: label_tag = ["Low", "High"]
elif n_gr == 3: label_tag = ["Low", "Middle", "High"]

gr_label = [str(label_tag[i])+" exp.\n(consumer)" for i in range(n_gr)]
gr_label.extend([str(label_tag[i])+" defor.\n(producer)" for i in range(n_gr)])
if mid_area > 0:
    gr_label.extend([str(label_tag[i])+" defor.\n(hproducer)" for i in range(n_gr)])

fig, ax = plt.subplots()

# sns.set(style = 'whitegrid')
sns.violinplot(x = gr_idx, y = cexp)
# sns.violinplot(x = gr_idx, y = cexp, inner = None)
# sns.violinplot(x = gr_idx, y = cexp, inner = "points")
sns.stripplot(x = gr_idx, y = cexp, s = 2.5, color = 'black', edgecolor='gray')
ax.set_xticklabels(gr_label)
ax.set(ylabel = 'Consumption (IDR/capita)')
ax.set_ylim(0, 20)
ax.set_title(crop_sort.upper())

plt.show()
