import numpy as np
import matplotlib.pyplot as plt

for a in range(3):
    print(a)

sr = 320000
mes_len_ms = 0.1
mes_len_sa = int(sr * mes_len_ms/1000)
freq_mhz = 250

x_list = [a for a in range(mes_len_sa)]
plt.plot(x_list, np.sin(x_list), marker="o")
plt.show()

#仮の位相差(0度〜180度でランダム)

#同調のズレ
sync_freq_diff_hz = 0.001

#


