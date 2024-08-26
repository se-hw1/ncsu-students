from myfiless import greetingpeople, num_even, find_maximum

def test_greet():
    assert greetingpeople("Alice") == "Hello, Alice!"  # This should pass

def test_find_max():
    assert find_maximum(10, 5) == 10  # This will fail due to the intentional error
