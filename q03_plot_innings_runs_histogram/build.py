import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)


def plot_innings_runs_histogram():
    group_sum = ipl_df.groupby(["match_code", "inning"]).sum().reset_index()
    inning1_df = group_sum[group_sum['inning'] == 1]
    inning2_df = group_sum[group_sum['inning'] == 2]

    fig, axes = plt.subplots(1, 2)

    axes[0].hist(inning1_df['runs'])
    axes[1].hist(inning2_df['runs'])
    plt.savefig("plot_innings_runs_histogram.png")
    plt.show()

plot_innings_runs_histogram()