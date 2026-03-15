from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_difficulty_ranges_increase():
    # Hard must have a wider range than Normal, which must be wider than Easy
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    assert easy_high < normal_high, "Easy range should be smaller than Normal"
    assert normal_high < hard_high, "Normal range should be smaller than Hard (was the bug: Hard returned 1-50)"


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_says_go_lower():
    # Bug: when guess > secret the hint said "Go HIGHER!" instead of "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected hint to say go lower, got: {message}"

def test_too_low_hint_says_go_higher():
    # Bug: when guess < secret the hint said "Go LOWER!" instead of "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say go higher, got: {message}"


def test_parse_guess_valid_integer():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None

def test_parse_guess_valid_float_truncates():
    ok, value, error = parse_guess("7.9")
    assert ok is True
    assert value == 7
    assert error is None

def test_parse_guess_empty_string():
    ok, value, error = parse_guess("")
    assert ok is False
    assert value is None
    assert error is not None

def test_parse_guess_none():
    ok, value, error = parse_guess(None)
    assert ok is False
    assert value is None
    assert error is not None

def test_parse_guess_non_numeric():
    ok, value, error = parse_guess("abc")
    assert ok is False
    assert value is None
    assert error is not None


def test_update_score_win_early_attempt():
    # Winning on attempt 1: points = 100 - 10 * (1+1) = 80
    assert update_score(0, "Win", 1) == 80

def test_update_score_win_late_attempt_floors_at_10():
    # Winning on attempt 10: points = 100 - 110 = -10, floored to 10
    assert update_score(0, "Win", 10) == 10

def test_update_score_too_high_even_attempt_adds_points():
    # "Too High" on even attempt_number adds 5
    assert update_score(50, "Too High", 2) == 55

def test_update_score_too_high_odd_attempt_subtracts_points():
    # "Too High" on odd attempt_number subtracts 5
    assert update_score(50, "Too High", 3) == 45

def test_update_score_too_low_subtracts_points():
    # "Too Low" always subtracts 5
    assert update_score(50, "Too Low", 1) == 45

def test_update_score_unknown_outcome_unchanged():
    # Unknown outcome leaves score unchanged
    assert update_score(50, "Unknown", 1) == 50
