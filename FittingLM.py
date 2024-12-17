import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# P = 8.314462618 = k_B * N_A 
def model(T, C, I0, A, B): #B=- delta E / k_B
    return C + I0 / ( 1+ A * np.exp( B / ( T + 273.15 )  ) ) 

def func(T):
    return model(T, 2.19710237e+01, 1.49651951e+02, 1.28138805e+09, -7.46231589e+03)

def lmFitting():
    iDatas = np.load("iData.npy")
    print(iDatas)
    y_data = iDatas
    x_data = np.arange(40, 201, 20)
    p0 = [ 2.19710237e+01, 1.49651951e+02 , 1.28138805e+09 , -7.46231589e+03 ]
    popt, pcov = curve_fit(model, x_data, y_data, p0=p0)

    # popt 包含拟合的最佳参数值
    print("拟合的参数值:", popt)
    # 使用拟合的参数计算预测值
    x_fit = np.arange(35, 205, 0.1)
    y_fit = model(x_fit, *popt)

    perr = np.sqrt(np.diag(pcov))
    print(f"参数不确定性：\n C = {perr[0]} \nI_0 = {perr[1]} \nA = {perr[2]} \nΔE/k_B = {perr[3]}")

    # 绘图
    plt.scatter(x_data, y_data, label="Data", color="red")
    plt.plot(x_fit, y_fit, label="Fitted Curve", color="blue")
    plt.legend()
    plt.show()