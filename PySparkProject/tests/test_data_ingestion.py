import pytest
from src.main.python.data_ingestion import load_data

def test_load_data():
    # Test loading data from a file
    file_path = "path/to/transactions.csv"
    data_df = load_data(file_path)
    assert data_df is not None
    assert data_df.count() > 0

def test_load_data_missing_file():
    # Test loading data from a missing file
    file_path = "path/to/missing_file.csv"
    with pytest.raises(FileNotFoundError):
        load_data(file_path)
