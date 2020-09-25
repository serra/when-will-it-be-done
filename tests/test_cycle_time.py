from wwibd import metrics
import pandas as pd
import numpy as np


def test_returns_dataframe_from_labels_and_dictionary():
    assert isinstance(metrics.cycle_times(['Build'], {}), pd.DataFrame)


def test_returns_labels_as_column_headers():
    df = metrics.cycle_times(['Specify', 'Build', 'Verify'], {})
    assert 'Specify_started' in df.columns
    assert 'Build_completed' in df.columns


def test_starts_with_arrival_timestamp():
    df = metrics.cycle_times(['Specify', 'Build', 'Verify'], {})
    assert df.columns[0] == 'Arrival'


def test_each_value_in_dictionary_results_in_a_row():
    timestamps = {1: [1, 2, 3], 2: [2, 3, 4]}
    df = metrics.cycle_times(['Build'], timestamps)
    assert len(df) == len(timestamps)


def test_missing_timestamps_is_OK():
    timestamps = {1: [1, 2, 3], 2: [2]}
    df = metrics.cycle_times(['Build'], timestamps)
    assert len(df) == len(timestamps)


def test_started_and_completed_column_added_and_set_to_first_started_timestamp():
    timestamps = {'a user story': [1, 2, 3]}
    df = metrics.cycle_times(['Build'], timestamps)
    assert 'Started' in df.columns
    assert 'Completed' in df.columns
    assert df['Started']['a user story'] == 2
    assert df['Completed']['a user story'] == 3


def test_cycle_times_column_added():
    timestamps = {'a user story': [1, 2, 3], 'a certain bug': [2, 3, 7]}
    df = metrics.cycle_times(['Build'], timestamps)
    assert 'Cycle_time' in df.columns
    assert df['Cycle_time']['a user story'] == 1    # 3-2
    assert df['Cycle_time']['a certain bug'] == 4   # 7-3


def test_percentiles():
    timestamps = {}
    for i in range(1, 101):
        timestamps[i] = [0, 0, i]

    assert len(timestamps) == 100

    df = metrics.cycle_times(['Build'], timestamps)

    assert df['Cycle_time'][1] == 1
    assert df['Cycle_time'][100] == 100

    percentile_values = metrics.get_percentile_values(df, (70, 85, 95))

    assert abs(percentile_values[0] - 70.3) < 0.1
    assert abs(percentile_values[1] - 85.2) < 0.1
    assert abs(percentile_values[2] - 95.1) < 0.1


def test_cycle_time_flow_columns_are_at_known_location():
    timestamps = {}
    cycle_times_df = metrics.cycle_times(['Build', 'Verify'], timestamps)
    cols = metrics.get_flow_columns(cycle_times_df)

    assert len(cols) == 4

    assert cols[0] == 'Build_started'
    assert cols[3] == 'Verify_completed'


def test_retrieve_event_stream_from_cycle_time_dataframe():
    timestamps = {'a': [1, 2, 3, 5, 7], 'b': [2.5, 5.7, 6.5, 8.8, 9.1]}
    cycle_times_df = metrics.cycle_times(['Build', 'Verify'], timestamps)

    stream = metrics.get_event_stream(cycle_times_df)
    assert len(stream) == 8
    assert stream[0] == 2   # first timestamp for a.build_started


def test_cfd_dataframe_has_zeros_first_row():
    timestamps = {'a': [1, 2, 3, 5, 7], 'b': [2.5, 5.7, 6.5, 8.8, 9.1]}
    cycle_times_df = metrics.cycle_times(['Build', 'Verify'], timestamps)

    df = metrics.get_cfd_dataframe(cycle_times_df)
    first_row_with_counts = df.iloc[0, 1:]
    assert np.all(first_row_with_counts == 0)


def test_cfd_dataframe_at_t5():
    timestamps = {'a': [1, 2, 3, 5, 7], 'b': [2.5, 5.7, 6.5, 8.8, 9.1]}
    cycle_times_df = metrics.cycle_times(['Build', 'Verify'], timestamps)

    df = metrics.get_cfd_dataframe(cycle_times_df)
    # at t5, task a has started verify stage, but not yet completed
    # at t5, task b has not started, so the cunts should be
    t5_expected_counts = np.array([1, 1, 1, 0])
    t5_row_with_counts = df.iloc[3, 1:]
    print(t5_expected_counts)
    print(t5_row_with_counts)
    assert (t5_expected_counts == t5_row_with_counts).all()


def test_cfd_dataframe_everything_completed_at_t_last():
    timestamps = {'a': [1, 2, 3, 5, 7], 'b': [2.5, 5.7, 6.5, 8.8, 9.1]}
    cycle_times_df = metrics.cycle_times(['Build', 'Verify'], timestamps)

    df = metrics.get_cfd_dataframe(cycle_times_df)
    # at t_last everything is completed and all counts should be two
    tl_expected_counts = np.array([2, 2, 2, 2])
    tl_row_with_counts = df.iloc[-1, 1:]
    assert (tl_expected_counts == tl_row_with_counts).all()
