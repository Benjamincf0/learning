from datetime import timedelta
from main import myrange
from hypothesis import settings, given, strategies as st

MAX = 999999

@given(a=st.integers(-MAX,MAX), b=st.integers(-MAX,MAX), c=st.integers(-MAX,MAX).filter(lambda x: x != 0))
@settings(
    max_examples=1000,
    deadline=timedelta(seconds=2)
)
def testMyrange(a, b, c):
    assert tuple(myrange(a, b, c)) == tuple(range(a, b, c))
