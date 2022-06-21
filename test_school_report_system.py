import pytest
from school_report import Report

# should be an empty array at start
def test_check_for_test_results():
    report = Report()
    assert report.test_results == []

def test_new_report_is_created():
    report = Report(['Green', 'Green', 'Red', 'Amber', 'Red'])
    assert report.test_results == ['Green', 'Green', 'Red', 'Amber', 'Red']

def test_count_results_in_array():
    report = Report(['Green', 'Green', 'Red', 'Amber', 'Red'])
    assert report.count_results() == "Green: 2\nAmber: 1\nRed: 2"


