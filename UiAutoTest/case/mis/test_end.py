import pytest

from utils import UtilsDriver


@pytest.mark.run(order = 1999)
class TestEnd:
    def test_end(self):
        UtilsDriver.is_mis_driver = True
        UtilsDriver.quit_mis_driver()