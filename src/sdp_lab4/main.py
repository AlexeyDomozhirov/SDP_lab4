import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def save_fig(name):
    plt.gcf().savefig(name, dpi=150, bbox_inches='tight')
    plt.close(plt.gcf())

#Данные из других заданий
a, b = 3, 8
def f(x):
    return np.sin(np.log(x))

def f2(x, y):
    return (x - 3) ** 2 + y

np.random.seed(42)
n = 100
low, high = 0, 100

uniform_sample = np.random.randint(low, high + 1, n)

mu = (low + high) / 2
sigma = (high - low) / 6
normal_sample = np.clip(np.round(np.random.normal(mu, sigma, n)),
                        low, high).astype(int)


#Задание 1
n = 100
x = np.linspace(a, b, n)
y = f(x)


#Задание 2
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='y = f(x)')
plt.title('График функции', fontsize=16)
plt.xlabel('x', fontsize=13)
plt.ylabel('y', fontsize=13)
plt.legend()
save_fig('plot_2.png')


#Задание 3
plt.figure(figsize=(8, 5))
plt.scatter(x, y, marker='o', color=(0.2, 0.6, 0.8), label='точки')
plt.title('Точечный график', fontsize=16)
plt.xlabel('x', fontsize=13)
plt.ylabel('y', fontsize=13)
plt.grid(True, color='gray', alpha=0.6)
plt.legend()
save_fig('plot_3.png')

#Задание 4
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.hist(uniform_sample, bins=30, color='skyblue')
ax1.set_title('Равномерное распределение', fontsize=14)
ax1.set_xlabel('Значение')
ax1.set_ylabel('Частота')

ax2.hist(normal_sample, bins=50, color='salmon')
ax2.set_title('Нормальное распределение', fontsize=14)
ax2.set_xlabel('Значение')
ax2.set_ylabel('Частота')
plt.tight_layout()
save_fig('plot_4.png')


#Задание 5
samples = np.random.randint(1, 5, 50)
values, counts = np.unique(samples, return_counts=True)

colors = ['tomato', 'seagreen', 'royalblue', 'orange']
labels_str = [str(v) for v in values]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.pie(counts, labels=labels_str, colors=colors, autopct='%1.1f%%')
ax1.set_title('Круговая диаграмма', fontsize=14)

ax2.bar(labels_str, counts, color=colors)
ax2.set_title('Столбчатая диаграмма', fontsize=14)
ax2.set_xlabel('Число')
ax2.set_ylabel('Количество')
plt.tight_layout()
save_fig('plot_5.png')


#Задание 6
xg = np.linspace(a, b, 50)
yg = np.linspace(a, b, 50)
X, Y = np.meshgrid(xg, yg)
Z = f2(X, Y)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='cyan', edgecolor='navy', linewidth=0.3)
ax.set_title('Трёхмерный график', fontsize=14)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
save_fig('plot_6.png')


#Задание 7
def draw_grid_2x2():
    fig = plt.figure(figsize=(14, 10))
    fig.suptitle('Сетка графиков 2x2', fontsize=20)

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(x, y, label='y = f(x)')
    ax1.set_title('График из п.2')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.legend()

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.scatter(x, y, marker='o', color=(0.2, 0.6, 0.8))
    ax2.set_title('График из п.3')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.grid(True, color='gray', alpha=0.6)

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.pie(counts, labels=labels_str, colors=colors, autopct='%1.1f%%')
    ax3.set_title('Диаграмма из п.5')

    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    ax4.plot_surface(X, Y, Z, color='cyan', edgecolor='navy', linewidth=0.3)
    ax4.set_title('3D из п.6')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('z')

    ax1.set_facecolor('lightyellow')
    return fig


draw_grid_2x2()
save_fig('plot_7.png')


#Задание 8
for style in ['ggplot', 'dark_background', 'bmh']:
    try:
        plt.style.use(style)
    except OSError:
        plt.style.use('default')
        print(f'Стиль "{style}" недоступен — применён default')
    draw_grid_2x2()
    save_fig('plog_8_' + style + '.png')
plt.style.use('default')
