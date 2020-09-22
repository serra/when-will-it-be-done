import pandas as pd
import numpy as np


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
