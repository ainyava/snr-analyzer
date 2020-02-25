import os
import csv
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

data_names = ['Downstream Rate', 'Upstream Rate', 'Downstream SNR', 'Upstream SNR', 'Downstream Attenuation',
              'Upstream Attenuation']

CHART_DIR = os.path.join(os.path.dirname(__file__), 'chart')
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.csv')

with open(DATA_FILE, 'r') as csv_file:
    data = list(csv.reader(csv_file))

    t = datetime.now().strftime('%Y%m%d-%H%M%S')

    for i, name in enumerate(data_names):

        plt.cla()

        plot_x = list(range(1, len(data) + 1))
        plot_y = []
        for row in data:
            try:
                val = float(row[i])
            except ValueError:
                val = float(row[i][0:-5])
            plot_y.append(val)

        plot_y = np.array(plot_y)

        plt.plot(plot_x, plot_y, label=name)

        plt.xlabel('Timeline')
        plt.ylabel(name)
        plt.title('Network Quality Analyze')

        if not os.path.isdir(os.path.join(CHART_DIR, t)):
            os.mkdir(os.path.join(CHART_DIR, t))
        plt.savefig(os.path.join(os.path.join(CHART_DIR, t), name + '.jpg'))
