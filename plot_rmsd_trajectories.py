import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import print_averages
import create_figures

app = Dash(__name__)
print("Running")
basedir = "Z:\\interstitial-spaces\\MD-tests\\validationSet-MDtests\\"
# basedir = ""

# Protein Restart Runs
combo1ejg = pd.read_csv(
    basedir + "superpose.1ejg.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1bpi = pd.read_csv(
    basedir + "superpose.1bpi.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1l2y = pd.read_csv(
    basedir + "superpose.1l2y.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1ubq = pd.read_csv(
    basedir + "superpose.1ubq.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1ucs = pd.read_csv(
    basedir + "superpose.1ucs.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1vii = pd.read_csv(
    basedir + "superpose.1vii.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1wm3 = pd.read_csv(
    basedir + "superpose.1wm3.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo2oed = pd.read_csv(
    basedir + "superpose.1bpi.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo2ppn = pd.read_csv(
    basedir + "superpose.1bpi.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo7skw = pd.read_csv(
    basedir + "superpose.7skw.combo.restart.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])

# Proteins 2langevin runs
combo1ejg_1 = pd.read_csv(
    basedir + "superpose.1ejg.combo.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1bpi_1 = pd.read_csv(
    basedir + "superpose.1bpi.combo.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1l2y_1 = pd.read_csv(
    basedir + "superpose.1l2y.combo.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1ubq_1 = pd.read_csv(
    basedir + "superpose.1ubq.combo.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1ucs_1 = pd.read_csv(
    basedir + "superpose.1ucs.combo.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1vii_1 = pd.read_csv(
    basedir + "superpose.1vii.combo.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo1wm3_1 = pd.read_csv(
    basedir + "superpose.1wm3.combo.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo2oed_1 = pd.read_csv(
    basedir + "superpose.1bpi.combo.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo2ppn_1 = pd.read_csv(
    basedir + "superpose.1bpi.combo.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])
combo7skw_1 = pd.read_csv(
    basedir + "superpose.7skw.combo.hidb.2langevin.csv", header=None,
    names=['snapshot', 'All_HA_RMSD_min', 'Calpha_RMSD_min', 'BBRMSD_min', 'All_HA_RMSD_non_term',
           'Calpha_RMSD_non_term', 'BBRMSD_non_term'])

fig1ejg = create_figures.create_protein_figures(combo1ejg, '1EJG Restart Superpose')
fig1bpi = create_figures.create_protein_figures(combo1bpi, '1BPI Restart Superpose')
fig1l2y = create_figures.create_protein_figures(combo1l2y, '1L2Y Restart Superpose')
fig1ubq = create_figures.create_protein_figures(combo1ubq, '1UBQ Restart Superpose')
fig1ucs = create_figures.create_protein_figures(combo1ucs, '1UCS Restart Superpose')
fig1vii = create_figures.create_protein_figures(combo1vii, '1VII Restart Superpose')
fig1wm3 = create_figures.create_protein_figures(combo1wm3, '1WM3 Restart Superpose')
fig2oed = create_figures.create_protein_figures(combo2oed, '2OED Restart Superpose')
fig2ppn = create_figures.create_protein_figures(combo2ppn, '2PPN Restart Superpose')
fig7skw = create_figures.create_protein_figures(combo7skw, '7SKW Restart Superpose')
fig1ejg_1 = create_figures.create_protein_figures(combo1ejg_1, '1EJG Superpose')

print_averages.print_averages([combo1bpi['BBRMSD_non_term'], combo1l2y['BBRMSD_non_term'],
                               combo1ubq['BBRMSD_non_term'], combo1ucs['BBRMSD_non_term'],
                               combo1vii['BBRMSD_non_term'], combo1wm3['BBRMSD_non_term'],
                               combo2oed['BBRMSD_non_term'], combo2ppn['BBRMSD_non_term'],
                               combo7skw['BBRMSD_non_term']], "Proteins, Restart ")

print_averages.print_averages([combo1bpi_1['BBRMSD_non_term'], combo1l2y_1['BBRMSD_non_term'],
                               combo1ubq_1['BBRMSD_non_term'], combo1ucs_1['BBRMSD_non_term'],
                               combo1vii_1['BBRMSD_non_term'], combo1wm3_1['BBRMSD_non_term'],
                               combo2oed_1['BBRMSD_non_term'], combo2ppn_1['BBRMSD_non_term'],
                               combo7skw_1['BBRMSD_non_term']], "Proteins, Original Runs ")

print_averages.print_averages([combo1bpi_1['BBRMSD_non_term'], combo1l2y_1['BBRMSD_non_term'],
                               combo1ubq_1['BBRMSD_non_term'], combo1ucs_1['BBRMSD_non_term'],
                               combo1vii_1['BBRMSD_non_term'], combo1wm3_1['BBRMSD_non_term'],
                               combo2oed_1['BBRMSD_non_term'], combo2ppn_1['BBRMSD_non_term'],
                               combo7skw_1['BBRMSD_non_term'], combo1ejg['BBRMSD_non_term']],
                              "Proteins, Original Runs + Crambin ")

app.layout = html.Div([
    html.H3("Protein Restart Runs"),
    dcc.Graph(figure=fig1ejg),
    dcc.Graph(figure=fig1ejg_1),
    dcc.Graph(figure=fig1bpi),
    dcc.Graph(figure=fig1l2y),
    dcc.Graph(figure=fig1ubq),
    dcc.Graph(figure=fig1ucs),
    dcc.Graph(figure=fig1vii),
    dcc.Graph(figure=fig1wm3),
    dcc.Graph(figure=fig2oed),
    dcc.Graph(figure=fig2ppn),
    dcc.Graph(figure=fig7skw),
])
if __name__ == '__main__':
    app.run_server(debug=True, port=8091)
