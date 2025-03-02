import datetime
from unittest.mock import Mock

# test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    day_num = today.weekday()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= day_num < 5


# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()

# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()
print('No errors')
