"""Teste de unidade para as menores unidades de programa testáveis, como funções e métodos.
Este arquivo usa `unittest.TestCase` para testar as funções de pesquisa."""
from unittest import TestCase

from example01 import seq_search, bin_search


class TestExample01(TestCase):
    """Casos de teste para as funções de pesquisa."""

    # Execute antes de cada método de teste.
    def setUp(self):
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        self.data2 = [12, 35, 40, 55, 68, 73, 81, 97]

    # Execute após cada método de teste.
    def tearDown(self):
        pass

    def test_seq_search(self):
        """Teste a pesquisa sequencial."""
        self.assertEqual(0, seq_search(self.data1, 35))
        self.assertEqual(2, seq_search(self.data1, 12))
        self.assertEqual(6, seq_search(self.data1, 81))
        self.assertEqual(7, seq_search(self.data1, 40))
        self.assertEqual(-1, seq_search(self.data1, 99))
        self.assertEqual(-1, seq_search(self.data1, 7))

    def test_bin_search(self):
        """Teste a pesquisa binária."""
        self.assertEqual(1, bin_search(self.data2, 35))
        self.assertEqual(0, bin_search(self.data2, 12))
        self.assertEqual(6, bin_search(self.data2, 81))
        self.assertEqual(2, bin_search(self.data2, 40))
        self.assertEqual(7, bin_search(self.data2, 97))
        self.assertEqual(-1, bin_search(self.data2, 7))
        self.assertEqual(-1, bin_search(self.data2, 99))
