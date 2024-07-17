import seaborn as sns
import matplotlib.pyplot as plt
import csv
import numpy as np

f_path = "/Users/leejmacbook/Desktop/"
# f_name = f_path + "IDN_def_data.txt"
# f_name = f_path + "IDN_def_data_trimed.txt"
f_name = f_path + "IDN_def_data_all.txt"

region = []
def_ov = []
exp_ov = []
def_pa = []
exp_pc = []
te_pc = []

# exp_items = ["Exp_pc_all"]
# exp_items = ["13"]    # potato
# exp_items = ["122"]   # cooking oil
# exp_items = ["122", "124"]  # cooking and other oils
# exp_items = ["53", "54", "55", "56", "57", "58", "59"]    # meats
# exp_items = ["130", "131"]    # coffee
# exp_items = ["2","3"]     # rice
# exp_items = ["159","160","161"]   # cooked rice
# exp_items = ["99","100","101"]    # nuts
# exp_items = ["182"]               # liquor
# exp_items = ["184","185","186","187","188"]   # cigarettes and tobacco
# exp_items = ["126","127"]         # sugar
# exp_items = ["128", "129","130", "131","132"]     # teas

with open(f_name) as dfile:
    reader = csv.reader(dfile, delimiter='\t')
    title = next(reader)
    exp_idx = [title.index(eit) for eit in exp_items]

    for row in reader:
        region.append(row[0])
        def_ov.append(float(row[1]))
        exp_ov.append(float(row[3]))
        def_pa.append(float(row[4]))

        exp_pc.append(sum([float(row[eidx]) for eidx in exp_idx]))
        # exp_pc.append(float(row[6]))

        # te_pc.append(float(row[7]))

n = len(region)

dov_i = sorted(range(n), key=lambda k: def_ov[k])
dpa_i = sorted(range(n), key=lambda k: def_pa[k])

epc_i = sorted(range(n), key=lambda k: exp_pc[k])

gr = [0.2, 0.4, 0.6, 0.8, 1.0]
ng = len(gr)

gr_def_ov = [0 for i in range(n)]
gr_def_pa = [0 for i in range(n)]

gr_exp_pc = [0 for i in range(n)]

for i in range(ng):
    if i == 0: si = 0
    else: si = int(n * gr[i-1])
    ei = int(n * gr[i])

    for j in dov_i[si:ei]:
        gr_def_ov[j] = i

    for j in dpa_i[si:ei]:
        gr_def_pa[j] = i

    for j in epc_i[si:ei]:
        gr_exp_pc[j] = i

fig, ax = plt.subplots()

# sns.violinplot(x = gr_def_ov, y = exp_ov)
# sns.violinplot(x = gr_def_pa, y = exp_ov)
# sns.violinplot(x = gr_def_ov, y = exp_pc)
sns.violinplot(x = gr_def_pa, y = exp_pc)
# sns.violinplot(x = gr_def_pa, y = te_pc)

ax.set_ylim(0, 20)

plt.show()
