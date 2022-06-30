import matplotlib.pyplot as plt
import math

def line_chart(data: dict, title: str) -> None:
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x = list(data['datas'].keys())
    y = list(data['datas'].values())
    plt.plot(x,y)
    plt.xlabel(data['unit'])
    plt.ylabel(data["count_unit"])
    plt.title(title)
    plt.show()

