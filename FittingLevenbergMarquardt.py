import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# P = 8.314462618 = k_B * N_A 
def func(T, I0, A, B): #B=- delta E / k_B
    return I0 / ( 1+ A * np.exp( B / ( T + 273.15 )  ) ) 

def lmFitting():
    iDatas = np.load("iData.npy")
    print(iDatas)
    y_data = iDatas
    x_data = np.arange(40, 201, 20)
    p0 = [ 223.18696083 , 46018.09379944 , -3713.37794921 ]
    popt, pcov = curve_fit(func, x_data, y_data, p0=p0)

    # popt 包含拟合的最佳参数值
    print("拟合的参数值:", popt)
    # 使用拟合的参数计算预测值
    y_fit = func(x_data, *popt)

    perr = np.sqrt(np.diag(pcov))
    print(f"参数不确定性：\nI_0 = {perr[0]}\nA = {perr[1]}\nΔE = {perr[2]}")

    # 绘图
    plt.scatter(x_data, y_data, label="Data", color="red")
    plt.plot(x_data, y_fit, label="Fitted Curve", color="blue")
    plt.legend()
    plt.show()