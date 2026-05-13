from closed_loop_neurostimulation.main import hello


def test_hello() -> None:
    assert hello("Test") == "Hello, Test!"
