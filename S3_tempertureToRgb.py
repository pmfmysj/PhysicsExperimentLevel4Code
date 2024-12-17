import os
import numpy as np
from PIL import Image

def temToRgb(tMatrix):
    # 创建RGB矩阵（3通道）
    rgbMatrix = np.zeros((tMatrix.shape[0], tMatrix.shape[1], 3), dtype=np.uint8)

    # 遍历矩阵中的每个温度值，进行颜色映射
    for i in range(tMatrix.shape[0]):
        for j in range(tMatrix.shape[1]):
            t = tMatrix[i, j]  # 获取当前温度值

            # 温度范围限制
            if t < 10:
                rgbMatrix[i, j] = (0, 0, 255)  # 深蓝
            elif t > 210:
                rgbMatrix[i, j] = (255, 0, 0)  # 红色
            else:
                # 将温度值标准化到[0, 1]区间
                tNormed = (t - 10) / (210 - 10)  # 标准化温度值 (20 -> 0, 200 -> 1)

                # 使用彩虹色谱法进行映射
                if tNormed <= 0.1 :  # 蓝色到绿色
                    r = 0
                    g = int(255 * tNormed / 0.1)
                    b = 255
                elif tNormed <= 0.5 :  # 绿色到黄色
                    r = int(255 * (tNormed - 0.1) / 0.4)
                    g = 255
                    b = 0
                elif tNormed <= 0.9:  # 黄色到橙色
                    r = 255
                    g = int(255 * (1 - (tNormed - 0.5) / 0.4))
                    b = 0
                else:  # 橙色到红色
                    r = 255
                    g = 0
                    b = 0

                # 将计算的颜色赋值给矩阵
                rgbMatrix[i, j] = (r, g, b)

    return rgbMatrix

# 从npy文件读取矩阵并保存为图像
def TemperatureToColorImage(inputMatrixPath, outputFolder):
    # 读取温度矩阵（假设保存为npy文件）
    tempMatrix = np.load(inputMatrixPath)

    # 将温度矩阵转换为RGB矩阵
    rgbMatrix = temToRgb(tempMatrix)

    # 将RGB矩阵转换为图片
    colorImage = Image.fromarray(rgbMatrix)

    # 构造保存图像的文件名
    base_name, _ = os.path.splitext(os.path.basename(inputMatrixPath))
    outputImagePath = os.path.join(outputFolder, f"{base_name}_color.png")

    # 保存图片
    colorImage.save(outputImagePath)
    print(f"Processed image saved at {outputImagePath}")

# 识别文件夹中的所有npy文件并进行处理
def main(inputFolder):
    # 获取输入文件夹的父目录和名称
    parentDir, folderName = os.path.split(os.path.abspath(inputFolder))
    
    # 新建文件夹名（加上 "grayed" 后缀）
    outputFolder = os.path.join(parentDir, f"{folderName}_s3ed")
    
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

# 示例调用
# inputFolder = "train_s1ed_s2ed"  # 输入文件夹路径
# main(inputFolder)