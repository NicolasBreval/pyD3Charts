from pyd3charts.base import scatter_chart
from random import randint

## Scatter plot chart with random values without 0 and 100

scatter_chart(
    data = [[randint(0, 100), randint(0, 100)] for _ in range(0, 100)],
    title='TEST CHART',
    header='TEST CHART',
    offset=1,
    top=10,
    right=30,
    bottom=30,
    left=10,
    width=300,
    height=300,
    radius=5,
    fill="red",
    axis=True,
    tooltip=True,
    exportpath='./example.html'
)