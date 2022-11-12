import pytest


@pytest.fixture(autouse=True)
def mock_third_function(monkeypatch):
    
    def _mocker():
        print('MOCKER\n' * 10)
        return True

    monkeypatch.setattr(
        'src.third_module.third_function',
        _mocker
    )
