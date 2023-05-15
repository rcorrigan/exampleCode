# This script reads in csv files containing dipole moment magnitudes
# for protein simulation trajectories and prints out averages for the
# average in vacuum conditions (vacavg), in generalized Kirkwood
# implicit solvent (gkavg), and in generalized Kirkwood implicit solvent
# without additional corrections (gkuncorravg)
import pandas as pd

basedir = "file\\dipoleMoments\\"

proteins = ['1bpi', '1l2y', '1ubq', '1ucs', '1vii', '1wm3', '2oed', '2ppn', '7skw']
averages = pd.DataFrame(columns=['vacavg', 'gkavg', 'gkuncorravg'])
for prot in proteins:
    file = pd.read_csv(basedir+"dipoleMomentMagn."+prot+".csv", header=None, names=['vac', 'gkcorr', 'gkuncorr'])
    data = {'vacavg': [file['vac'].mean()], 'gkavg': [file['gkcorr'].mean()], 'gkuncorravg': [file['gkuncorr'].mean()]}
    current = pd.DataFrame(data)
    averages = pd.concat([averages, current])

averages.to_csv('averages.csv', index=False)

