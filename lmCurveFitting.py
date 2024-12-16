import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

# 玻尔兹曼常数 (单位 J/K)
k_B = 8.3144626

# 定义拟合函数
def model(T, I0, A, deltaE):
    return I0 / ( 1 + A * np.exp( -deltaE / (k_B * T ) ) )

# 实验数据
iData = np.load("iData.npy")
tData = list(range(40,201,20))
p0 = [1e-3, 1e5, 1e-20]  # 初值猜测

# LM 算法拟合，设置初始猜测值

popt, _ = curve_fit(model, tData, iData, method='lm')

# 提取拟合参数
I_0_fit, A_fit, delta_E_fit = popt
print(f"parameta: \nI_0 = {I_0_fit}\nA = {A_fit}\nΔE = {delta_E_fit}")

# 拟合曲线可视化
plt.figure(figsize=(8, 6))
plt.scatter(tData, iData, label="Data", color="red", zorder=5)
tFit = np.linspace(min(tData), max(tData), 500)
iFit = model(tFit, *popt)
plt.plot(tFit, iFit, label="Curve (LM)", color="blue", zorder=3)
plt.xlabel("T (cel)")
plt.ylabel("I")
plt.title("Levenberg-Marquardt Result")
plt.legend()
plt.show()