import pytest


def test_case1(connDB):
    print("case1")


class TestDemo1:
    def test_a(self, connDB):
        print("testa")

    def test_b(self, connDB):
        print("testb")

class TestDemo2:
    def test_a(self, connDB):
        print("testa")

    def test_b(self, connDB):
        print("testb")