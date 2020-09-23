import pandas as pd
import matplotlib.pyplot as plt


def cycle_times(labels: list, timestamps: dict):
    """
    Based on timestamp measurements for each workitem,
    return a data data frame with cycle times.

    The structure of this data frame helps construction
    and plotting of other agile metrics.
    """
    columns = ['Arrival']
    for label in labels:
        columns.append(label + '_started')
        columns.append(label + '_completed')

    df = pd.DataFrame.from_dict(timestamps, orient='index', columns=columns)

    df['Started'] = df[df.columns[1]]
    df['Completed'] = df[df.columns[-2]]
    df['Cycle_time'] = df.Completed - df.Started

    return df


def cycle_time_scatter_plot(cycle_time_dataframe):
    """
    Create a cycle time scatter plot from a cycle time data frame.
    """
    return cycle_time_dataframe.plot(x='Completed', y='Cycle_time', title="Cycle Times",
                                     kind='scatter', xlabel='Completed Time').get_figure()


def save_plot(axes, filename):
    """
    Save an axes to file.
    """
    fig = axes.get_figure()
    fig.savefig(filename)
