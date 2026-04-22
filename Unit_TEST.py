# Unit testing para merge sort

# TDD = Test Driven Development

import pytest
from Merge_sort import merge_sort

# 1. Definimos los casos de prueba en una constante clara y separada
MERGE_SORT_TEST_CASES = [
    # (input_list, expected_output)
    ([3, 1, 4, 1, 5, 9, 2], [1, 1, 2, 3, 4, 5, 9]),  # Desordenado con duplicados
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),              # Ya ordenado (Mejor caso)
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),              # Orden inverso (Peor caso)
    ([], []),                                         # Lista vacía (Caso límite)
    ([42], [42]),                                     # Un solo elemento (Caso límite)
    ([-5, 0, -3, 8], [-5, -3, 0, 8]),                # Números negativos
]

# 2. Pasamos la constante al decorador
@pytest.mark.parametrize("input_list, expected", MERGE_SORT_TEST_CASES)
def test_merge_sort(input_list, expected):
    # 3. La lógica de la prueba se mantiene ultra concisa
    assert merge_sort(input_list.copy()) == expected