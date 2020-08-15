def setup_module():
    print("setup:模块级别的")


def teardown_module():
    print("teardown:模块级别的")

def setup_function():
    print("setup：函数级别的")

def teardown_function():
    print("teardown：函数级别的")

def test_case1():
    print("test_case1")

class TestA:
    def setup_class(self):
        print("setup_class:类级别")

    def teardown_class(self):
        print("teardown_class:类级别")

    def setup(self):
        print("setup:测试用例前的准备")

    def teardown(self):
        print("teardown:测试用例后的准备")

    def test_a(self):
        print("testa")

    def test_b(self):
        print("testb")
