import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_autoscale_on(False)


ax.set_title('Точек добавлено: 0')
ax.set_xlabel("Ось X")
ax.set_ylabel("Ось Y")
ax.grid(True)


points = []
def onclick(event):
    if not hasattr(onclick, 'cnt'):
        onclick.cnt = 0

    if event.button != 1:
        return

    if event.inaxes != ax:
        return

    onclick.cnt += 1

    x = event.xdata
    y = event.ydata

    points.append((round(float(x), 2), round(float(y), 2)))

    ax.set_title(f"Точек добавлено: {len(points)}")

    print(f"Точка {len(points)}: x = {x:.2f}, y = {y:.2f}")
    print("Все сохраненные точки:", points)

    ax.scatter(x, y, color='green', s=60, zorder=3)
    ax.vlines(x, 0, y, colors = 'green', linestyles="dashed")
    ax.hlines(y, 0, x, colors="green", linestyles="dashed")
    ax.annotate(
        f'({x:.2f}, {y:.2f})',
        (x, y),
        xytext=(7,7),
        textcoords="offset points"
    )
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
