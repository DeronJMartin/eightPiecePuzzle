import pandas as pd
from matplotlib import pyplot as plt

uniformCostData = pd.read_csv('UniformCostSearchMetrics/cpuTime.csv', index_col=None, header=None)
misplacedTileData = pd.read_csv('MisplacedTileSearchMetrics/cpuTime.csv', index_col=False)
manhattanTileData = pd.read_csv('ManhattanTileSearchMetrics/cpuTime.csv', index_col=False)

x1 = uniformCostData.iloc[:, 0]
y1 = uniformCostData.iloc[:, 1]
x2 = misplacedTileData.iloc[:, 0]
y2 = misplacedTileData.iloc[:, 1]
x3 = manhattanTileData.iloc[:, 0]
y3 = manhattanTileData.iloc[:, 1]

plt.plot(x1,y1, label = "Uniform Cost")
plt.plot(x2,y2, label = "Misplaced Tile")
plt.plot(x3,y3, label = "Manhattan Tile")
plt.xlabel("Depth")
plt.ylabel("CPU Time in seconds")
plt.legend()
plt.savefig('cpuTime.png')