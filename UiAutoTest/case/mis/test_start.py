import pytest

from utils import UtilsDriver


@pytest.mark.run(order=1000)
class TestStart:
    def test_start(self):
        UtilsDriver.is_mis_driver = False
