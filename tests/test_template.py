from template import __version__

from template.example import example

from template.sub_module import example_2


def test_version() -> None:
    """
    Tests getting variables from the environment
    """
    assert __version__ == "0.1.0"


def test_example() -> None:
    assert example() == "example"


def test_submodule() -> None:
    assert example_2.example_2() == "example_2"
