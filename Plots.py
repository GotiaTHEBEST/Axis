import matplotlib.pyplot as plt


k = 2
b = 1
x = [4, 5, 7, 8, 9]
y = []
for i in x:
    yx = k * i + b
    y.append(yx)
plt.figure(figsize=(7, 5))
plt.plot(x, y, label='линия')
plt.scatter(
    x,
    y,
    color='green',
    s=60,
    label='точки',
    zorder=3
)
for xi, yi in zip(x, y):
    plt.vlines(xi, 0, yi, colors="green", linestyles="dashed")
    plt.hlines(yi, 0, xi, colors="green", linestyles="dashed")
# plt.axhline(0, color = 'gray', linewidth=0.8)
# plt.axvline(0, color = 'gray', linewidth=0.8)
plt.xlabel("ось x")
plt.ylabel("ось y")
plt.title("прямая и заданные точки")
plt.grid(True)
plt.legend()
plt.margins(0)
plt.show()
