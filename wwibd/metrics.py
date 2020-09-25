import pandas as pd
import numpy as np
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


def get_percentile_values(cycle_time_dataframe, percentiles):
    """
    Get percentile values for cycle times from cycle time data frame.
    """
    return tuple([cycle_time_dataframe.Cycle_time.quantile(p/100.0) for p in percentiles])


def cycle_time_scatter_plot(cycle_time_dataframe, percentiles=(50, 85, 95), ax=None):
    """
    Create a cycle time scatter plot from a cycle time data frame.
    """
    axes = cycle_time_dataframe.plot(x='Completed', y='Cycle_time', title="Cycle Times",
                                     kind='scatter', xlabel='Completed Time', alpha=0.5, ax=ax)

    percentile_values = get_percentile_values(
        cycle_time_dataframe, percentiles)

    # draw horizontal line on axes
    for i, p in enumerate(percentile_values):
        axes.axhline(y=p, color='r', ls=':')
        axes.text(0, p, f'{percentiles[i]}th percentile', color='r')

    return axes


def cycle_time_histogram_plot(cycle_time_dataframe, ax=None):
    return cycle_time_dataframe['Cycle_time'].plot(kind='hist', ax=ax)


def save_plot(axes, filename):
    """
    Save an axes to file.
    """
    fig = axes.get_figure()
    fig.savefig(filename)


def get_flow_columns(cycle_time_dataframe):
    return cycle_time_dataframe.columns[1:-3]


def get_event_stream(cycle_time_dataframe):
    flow_columns = get_flow_columns(cycle_time_dataframe)
    flow_data = cycle_time_dataframe[flow_columns]

    return flow_data.stack().sort_values()


def get_cfd_dataframe(cycle_time_dataframe):
    flow_columns = get_flow_columns(cycle_time_dataframe)
    event_stream = get_event_stream(cycle_time_dataframe)

    n = len(event_stream) + 1

    t = np.zeros(n)

    counts = {'Time': t}
    for c in flow_columns:
        counts[c] = np.zeros(n)

    for i, evt in enumerate(event_stream.items()):
        prev = i
        now = i + 1

        time_stamp = evt[1]
        flow_event_id = evt[0][1]

        t[now] = time_stamp
        for c in flow_columns:
            # copy previous values
            counts[c][now] = counts[c][prev]

        # increment flow count for this event
        counts[flow_event_id][i+1] = counts[flow_event_id][i] + 1

    return pd.DataFrame(counts)


def cfd_plot_from_cfd_dataframe(cfd_dataframe):
    return cfd_dataframe.plot.area(x='Time', stacked=False)


def cfd_plot(cycle_time_dataframe):
    return cfd_plot_from_cfd_dataframe(get_cfd_dataframe(cycle_time_dataframe))
