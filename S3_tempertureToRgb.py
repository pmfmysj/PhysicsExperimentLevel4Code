'''将每张图的温度矩阵转化成颜色, 再导出成热可视化图像'''

import os
import numpy as np
from PIL import Image

# 将矩阵通过颜色映射转化成彩色图
def temToRgb(tMatrix):

    # 创建RGB矩阵（3通道）
    rgbMatrix = np.zeros((tMatrix.shape[0], tMatrix.shape[1], 3), dtype=np.uint8)

    # 遍历矩阵中的每个温度值，进行颜色映射
    for i in range(tMatrix.shape[0]):
        for j in range(tMatrix.shape[1]):
            t = tMatrix[i, j]  # 获取当前温度值
            '''
            t<10        蓝色
            10<t<50     蓝色->青色
            50<t<110    绿色->黄色
            110<t<210   黄色->红色
            210<t       红色
            '''
            # 温度范围限制
            if t < 10:
                rgbMatrix[i, j] = (0, 0, 255)       # 蓝色
            elif t > 210:
                rgbMatrix[i, j] = (255, 0, 0)       # 红色
            else:
                # 将温度值标准化到[0, 1]区间
                tNormed = (t - 10) / (210 - 10)     # 归一化

                # 使用彩虹色谱法进行映射
                if tNormed <= 0.2 :             # 蓝色到绿色
                    r = 0
                    g = int(255 * tNormed / 0.2)
                    b = 255
                elif tNormed <= 0.5 :           # 绿色到黄色
                    r = int(255 * (tNormed - 0.2) / 0.3)
                    g = 255
                    b = 0
                else:                           # 黄色到红色
                    r = 255
                    g = int(255 * (1 - (tNormed - 0.5) / 0.5))
                    b = 0

                # 赋值给矩阵
                rgbMatrix[i, j] = (r, g, b)

    return rgbMatrix

# 将矩阵转化成热可视化图像
def TemperatureToColorImage(inputMatrixPath, outputFolder):
  
    tempMatrix = np.load(inputMatrixPath)       # 读取温度矩阵
    rgbMatrix = temToRgb(tempMatrix)            # 将温度矩阵转换为RGB矩阵
    colorImage = Image.fromarray(rgbMatrix)     # 将RGB矩阵转换为图片

    # 构造保存图像的文件名
    baseName, _ = os.path.splitext(os.path.basename(inputMatrixPath))
    outputImagePath = os.path.join(outputFolder, f"v_{baseName}.png")

    # 保存图片
    colorImage.save(outputImagePath)
    print(f"v_{baseName}'s thermal image has been exported.")

# 识别文件夹中的所有npy文件并进行处理
def main(inputFolder):
    # 获取输入文件夹的父目录和名称
    parentDir, folderName = os.path.split(os.path.abspath(inputFolder))
    
    # 新建文件夹名（加上后缀 _s3 ）
    outputFolder = os.path.join(parentDir, f"{folderName}_s3")
    
    # 确保输出文件夹存在
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    # 遍历输入文件夹中的所有npy文件
    for fileName in os.listdir(inputFolder):
        # 构造完整的文件路径
        inputPath = os.path.join(inputFolder, fileName)

        # 检查是否为npy文件
        if os.path.isfile(inputPath) and fileName.lower().endswith('.npy'):
            TemperatureToColorImage(inputPath, outputFolder)
    print ("step3 finished")
    return outputFolder

# ⬇️调试
# inputFolder = "train_s1ed_s2ed"  # 输入文件夹路径
# main(inputFolder)