import pandas as pd
import plotly.graph_objects as go
import numpy as np

def create_figures(rmsd_df, title):
    x = pd.Series(np.arange(0.1, 500, 0.1))
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Non_Terminal_RMSD_orig'],
            name="Non-Term HA RMSD: orig, \n" + str("{:.3f}".format(rmsd_df['Non_Terminal_RMSD_orig'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Non_Terminal_BBRMSD_orig'],
            name="Non-Term BBRMSD: orig, \n" + str("{:.3f}".format(rmsd_df['Non_Terminal_BBRMSD_orig'].mean()))
        )
    )
    fig.update_yaxes(range=[0, 7], title_text="RMSD")
    fig.update_xaxes(range=[0, 500], title_text="Simulation Time (ns)")
    fig.update_layout(title=title)

    return fig


def create_ion_figures(rmsd_df, title):
    x = pd.Series(np.arange(0.1, 500, 0.1))
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Non_Terminal_RMSD_min'],
            name="Non-Term HA RMSD: min, " + str("{:.3f}".format(rmsd_df['Non_Terminal_RMSD_min'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Non_Terminal_BBRMSD_min'],
            name="Non-Term BBRMSD: min, " + str("{:.3f}".format(rmsd_df['Non_Terminal_BBRMSD_min'].mean()))
        )
    )
    fig.update_yaxes(range=[0, 7], title_text="RMSD")
    fig.update_xaxes(range=[0, 500], title_text="Simulation Time (ns)")
    fig.update_layout(title=title)

    return fig


def create_dna_figures(rmsd_df, title):
    x = pd.Series(np.arange(0.1, 500, 0.1))
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Non_Terminal_RMSD_aform'],
            name="Non-Term HA RMSD: aform, " + str(
                "{:.3f}".format(rmsd_df['Non_Terminal_RMSD_aform'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Non_Terminal_BBRMSD_aform'],
            name="Non-Term BBRMSD: aform, " + str("{:.3f}".format(rmsd_df['Non_Terminal_BBRMSD_aform'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Non_Terminal_RMSD_bform'],
            name="Non-Term HA RMSD: bform, " + str(
                "{:.3f}".format(rmsd_df['Non_Terminal_RMSD_bform'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Non_Terminal_BBRMSD_bform'],
            name="Non-Term BBRMSD: bform, " + str("{:.3f}".format(rmsd_df['Non_Terminal_BBRMSD_bform'].mean()))
        )
    )
    fig.update_yaxes(range=[0, 12], title_text="RMSD")
    fig.update_xaxes(range=[0, 400], title_text="Simulation Time (ns)")
    fig.update_layout(title=title)

    return fig


def create_protein_figures(rmsd_df, title):
    x = pd.Series(np.arange(0.1, 500, 0.1))
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['All_HA_RMSD_min'],
            name="All HA RMSD: min, " + str("{:.3f}".format(rmsd_df['All_HA_RMSD_min'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Calpha_RMSD_min'],
            name="Calpha RMSD: min " + str("{:.3f}".format(rmsd_df['Calpha_RMSD_min'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['BBRMSD_min'],
            name="BBRMSD: min, " + str("{:.3f}".format(rmsd_df['BBRMSD_min'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['All_HA_RMSD_non_term'],
            name="All HA RMSD: non-term, " + str("{:.3f}".format(rmsd_df['All_HA_RMSD_non_term'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['Calpha_RMSD_non_term'],
            name="Calpha RMSD: non-term, " + str("{:.3f}".format(rmsd_df['Calpha_RMSD_non_term'].mean()))
        )
    )
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=x[0:len(rmsd_df)],
            y=rmsd_df['BBRMSD_non_term'],
            name="BBRMSD: non-term, " + str("{:.3f}".format(rmsd_df['BBRMSD_non_term'].mean()))
        )
    )
    fig.update_yaxes(range=[0, 7], title_text='RMSD')
    fig.update_xaxes(range=[0, 500], title_text='Simulation Time (ns)')
    fig.update_layout(title=title)

    return fig
