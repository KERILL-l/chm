import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Задаем функцию f(x) = (3 + x)**|x| * sin(2 * x) + 1
def f(x):
    return (3 + x)**np.abs(x) * np.sin(2 * x) + 1

# Задаем границы и количество узлов
a, b = -2, 1
N = 13  # Начальное количество узлов

# Создаем массив узлов и вычисляем значения функции в этих узлах
x_nodes = np.linspace(a, b, N)
y_nodes = f(x_nodes)

# Проводим кубическую сплайн-интерполяцию с "свободным провисанием" (натуральный сплайн)
spline_free = CubicSpline(x_nodes, y_nodes, bc_type='natural')

# Определяем точные значения функции на более частом сетке для сравнения
x_dense = np.linspace(a, b, 500)
y_true = f(x_dense)
y_spline_free = spline_free(x_dense)

# Вычисляем максимальную фактическую ошибку для сплайн-интерполяции
error_free = np.abs(y_true - y_spline_free)
max_error_free = np.max(error_free)

# Результаты
print(max_error_free, x_nodes, y_nodes, y_true, y_spline_free, x_dense, error_free)
