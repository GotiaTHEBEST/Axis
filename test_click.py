import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_autoscale_on(False)
def onclick(event):
    if not hasattr(onclick, 'cnt'):
        onclick.cnt = 0

    onclick.cnt += 1

    if event.button != 1:
        return

    if event.inaxes != ax:
        return

    print(onclick.cnt)

    x = event.xdata
    y = event.ydata
    print(x, y)

    ax.scatter(x, y, color='green', s=60, zorder=3)
    ax.annotate(
        f'({x:.2f}, {y:.2f})',
        (x, y),
        xytext=(7,7),
        textcoords="offset points"
    )
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
