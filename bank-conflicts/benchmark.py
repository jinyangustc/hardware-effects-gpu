import os
import sys

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(ROOT)
from utils import benchmark


keys = ["Offset"]
# values = [0, 1, 2, 4, 8, 16, 32, 36]
values = list(range(36))

frame = benchmark(keys, values)

g = sns.lineplot(data=frame, x="Offset", y="Time")
plt.savefig("bank-conflicts.png", dpi=300)
plt.show()
