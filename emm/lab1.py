import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np):
    def generate_matrix(
        size: int = 10,
        seed: int = 10,
    ):
        np.random.seed(seed)
        dummy = np.zeros((size,) * 2)
        for i in range(size):
            for j in range(size):
                if i == j:
                    dummy[i][j] = 0
                else:
                    dummy[i][j] = round(np.random.uniform(0.01, 0.99), 2)
        return np.triu(dummy) + np.triu(dummy).T

    return (generate_matrix,)


@app.cell
def _(generate_matrix):
    matrix_1 = generate_matrix(10)
    matrix_1
    return


app._unparsable_cell(
    r"""
    |
    """,
    name="_",
)


if __name__ == "__main__":
    app.run()
