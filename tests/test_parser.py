from analyzer.parser import parse_log_file


def test_parser_skips_invalid_row():
    events = parse_log_file("sample_logs/events.csv")
    
    #one row has a bad timestamp and should be skipped
    assert len(events) == 3
    