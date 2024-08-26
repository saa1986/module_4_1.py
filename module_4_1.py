from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Вызов функций с произвольными числами
result1 = fake_divide(69, 3)  # 69 / 3
result2 = fake_divide(3, 0)    # 3 / 0
result3 = true_divide(49, 7)   # 49 / 7
result4 = true_divide(15, 0)   # 15 / 0

# Вывод результатов на экран
print(result1)  # Ожидается: 23.0
print(result2)  # Ожидается: 'Ошибка'
print(result3)  # Ожидается: 7.0
print(result4)  # Ожидается: inf