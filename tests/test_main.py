from src.third_module import third_function
import src


def test_second_function():
    assert src.third_module.third_function()
    assert third_function()
