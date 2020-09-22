from wwibd import metrics
import pandas as pd


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
    df.to_clipboard()
    assert 'Cycle_time' in df.columns
    assert df['Cycle_time']['a user story'] == 1    # 3-2
    assert df['Cycle_time']['a certain bug'] == 4   # 7-3
