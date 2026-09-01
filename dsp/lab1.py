import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    $Asin(\omega \cdot t)$
    """,
    column=None, disabled=False, hide_code=True, name="_"
)


@app.cell
def _(mo):
    A = mo.ui.slider(1, 2, 0.2, label="A")
    omega = mo.ui.slider(1, 2, 0.01, label=r"$\omega$", debounce=True)
    A, omega
    return A, omega


@app.cell
def _(A, np, omega):
    x = np.arange(-3*np.pi, 3*np.pi, 0.001)
    y = A.value * np.sin(x * omega.value)
    return x, y


@app.cell
def _(plt, x, y):
    plt.plot(x, y, color="tab:blue")
    plt.grid()
    plt.show()
    return


@app.cell
def _():
    import numpy as np
    import marimo as mo
    import matplotlib.pyplot as plt

    return mo, np, plt


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
