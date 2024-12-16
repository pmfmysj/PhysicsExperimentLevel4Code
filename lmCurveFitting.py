import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

# 玻尔兹曼常数 (单位 J/K)
k_B = 1.380649e-23

# 定义拟合函数
def model(T, I_0, A, delta_E):
    return I_0 / (1 + A * np.exp(-delta_E / (k_B * T)))

# 实验数据
data = pd.read_csv('image.csv', header=None)
array_2d = data.to_numpy()
iData = array_2d.ravel()
tData = np.full(10, 300)
p0 = [1e-3, 1e5, 1e-20]  # 初值猜测

# LM 算法拟合，设置初始猜测值

popt, pcov = curve_fit(model, tData, iData, p0=p0, method='lm')

# 提取拟合参数
I_0_fit, A_fit, delta_E_fit = popt
print(f"parameta: \nI_0 = {I_0_fit}\nA = {A_fit}\nΔE = {delta_E_fit}")

# 参数标准差
# perr = np.sqrt(np.diag(pcov))
# print(f"delta: \nI_0 = {perr[0]}\nA = {perr[1]}\nΔE = {perr[2]}")

# 拟合曲线可视化
plt.figure(figsize=(8, 6))
plt.scatter(tData, iData, label="Data", color="red", zorder=5)
tFit = np.linspace(min(tData), max(tData), 500)
iFit = model(tFit, *popt)
plt.plot(tFit, iFit, label="Curve (LM)", color="blue", zorder=3)
plt.xlabel("T (K)")
plt.ylabel("I")
plt.title("Levenberg-Marquardt Result")
plt.legend()
plt.show()