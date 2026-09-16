import pytest

from api.api_reg import RegApi



@pytest.fixture
def reg():
    # 返回去一个对象
    yield RegApi()
