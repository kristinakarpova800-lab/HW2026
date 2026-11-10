import os
import pandas as pd
import pytest
from text_analyzer import read_text_file, analyze_text

def test_file_not_found():
    """Тест перевірки помилки, якщо файл не існує."""
    with pytest.raises(FileNotFoundError):
        read_text_file("non_existent.txt")


def test_empty_file(tmp_path):
    """Тест перевірки помилки на порожній файл."""
    empty_file = tmp_path / "test_empty.txt"
    empty_file.write_text("   ", encoding="utf-8")
    
    with pytest.raises(ValueError):
        read_text_file(str(empty_file))


def test_successful_analysis(tmp_path):
    """Тест коректності роботи програми."""
    test_file = tmp_path / "test_sample.txt"
    test_file.write_text("Привіт світ! Привіт, привіт усім.", encoding="utf-8")
    
    word_count, df = analyze_text(str(test_file))
    

    assert word_count == 5

    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]['Слово'] == 'привіт'
    assert df.iloc[0]['Частота вживання'] == 3

