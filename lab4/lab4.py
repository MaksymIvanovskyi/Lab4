import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def f(x, N):
    return 1 - ((x - N/2) / (N/2))**2

# Задання значення N
N = 7

# Генерація значень x на проміжку від 0 до N
x = np.linspace(0, N, 1000)

# Обчислення значень функції f(x)
y = f(x, N)

# Побудова графіка
plt.plot(x, y)
plt.title('Графік функції f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
