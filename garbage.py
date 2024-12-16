from PIL import Image
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

# 设置起始值
start = 40
stop = 200
step = 20
matrixs = []
avgs = []

# 循环
for i in range(start, stop + 1, step):

    imageName = f"A_{i:03d}.bmp"                                    # 带0
    image = Image.open(imageName).convert('L')                       # 转为灰度图像

    iMatrix = np.array(image).ravel()                                  # 转换为 NumPy 数组
    matrixs.append(iMatrix)
    avg = np.average(iMatrix)                                   # 取平均
    avgs.append(avg)
    print(avg)                                               

    csvFilePath = f"A_{i:03d}.csv"                                   # 构造文件路径
    np.savetxt(csvFilePath, iMatrix, delimiter=",", fmt='%d')   # 导出为 CSV 文件
    print(f"A_{i:03d}'s pixelMatrix has exported: {csvFilePath}")

matrixLength = len(matrixs[0])
k_B = 1.380649e-23
#i0Fits = []
#aFits = []
#deltaEFits = []
def model(T, I_0, A, delta_E):
    return I_0 / (1 + A * np.exp(-delta_E / (k_B * T)))

#for i in range(matrixLength):

    iData = [matrix[i] for matrix in matrixs]
    tData = list(range(40, 201, 20)) 
    p0 = [1e-3, 1e5, 1e-20]                     # 初值猜测
    popt, pcov = curve_fit(model, tData, iData, p0=p0, method='lm')
    i0Fit, aFit, deltaEFit = popt
    i0Fits.append(i0Fit)
    aFits.append(aFit)
    deltaEFits.append(deltaEFit)


iData = [avg in avgs]
tData = list(range(40, 201, 20)) 
p0 = [1e-3, 1e5, 1e-20]                     # 初值猜测
popt, pcov = curve_fit(model, tData, iData, p0=p0, method='lm')
i0Fit, aFit, deltaEFit = popt
print(i0Fit)
print(aFit)
print(deltaEFit)
#i0Fits.append(i0Fit)
#aFits.append(aFit)
#deltaEFits.append(deltaEFit)

# 定义温度范围
#tData = list(range(40, 201, 20)) 

# 创建一个温度的细分数据点，用于绘制平滑的拟合曲线
#tFine = np.linspace(40, 200, 500)

# 绘制前五个拟合函数的曲线
#plt.figure(figsize=(12, 8))

#for i in range(5):
    # 获取前五个拟合参数
#    i0Fit = i0Fits[i]
#    aFit = aFits[i]
#    deltaEFit = deltaEFits[i]
    
    # 计算拟合曲线
#    fitted_curve = model(tFine, i0Fit, aFit, deltaEFit)
    
    # 绘制拟合曲线
#    plt.plot(tFine, fitted_curve, label=f'Fit {i+1} (T = {tData[i]} K)', linestyle='-', marker='o')

# 添加标签和标题
#plt.xlabel('Temperature (K)')
#plt.ylabel('Intensity')
#plt.title('Fitted Curves for First 5 Sets of Parameters')
#plt.legend()

# 显示图像
# plt.tight_layout()
# plt.show()
