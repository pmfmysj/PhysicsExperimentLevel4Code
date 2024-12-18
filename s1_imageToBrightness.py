'''将每张图图片转化成各个像素点的数组, 再求每张图的平均值(可选)并保存'''

import os
from PIL import Image
import numpy as np

# 将 train 文件夹的所有命名为 A_xxx.bmp 的图片转化成像素点亮度的矩阵 并取平均 并导出成.npy和.csv
def picToBrightnessForTrain():

    # 定义常数
    start = 40      # 起始温度 40 摄氏度
    stop = 200      # 最高温度 200 摄氏度
    step = 20       # 步长 20 摄氏度
    matrixs = []    # 每个图片亮度矩阵组成的数组
    avgs = []       # 每个图片亮度平均值组成的数组

    # 设置导出文件夹
    outputFolder = f"train_trained"             # 新建导出文件夹
    if not os.path.exists(outputFolder):        # 确保输出文件夹存在
        os.makedirs(outputFolder)

    # 循环 将每个符合条件的图像转换为亮度矩阵
    for i in range(start, stop + 1, step):
        imageName = f"A_{i:03d}"                                # 保证图片名后面的数字是3位
        imagePath = os.path.join("train", f"{imageName}.bmp")   # 定义图片路径
        image = Image.open(imagePath).convert('L')              # 转为灰度图像
        iMatrix = np.array(image)                               # 转换为矩阵
        matrixs.append(iMatrix)                                 # 将矩阵加到数组中
        avg = np.average(iMatrix)                               # 矩阵元素取平均
        avgs.append(avg)                                        # 将平均值加到数组中
        print(f"{imageName}'s average brightness is {avg}.")    # 输出平均值

        #⬇️导出成npy
        npyPath = os.path.join(outputFolder, f"{imageName}.npy")
        np.save(npyPath, iMatrix)
        #print(f"A_{i:03d}'s iMatrix has saved")

        #⬇️导出成csv
        csvPath = os.path.join(outputFolder, f"{imageName}.csv")                             
        np.savetxt(csvPath, iMatrix, delimiter=",", fmt='%d')          
        #print(f"A_{i:03d}'s pixelMatrix has exported")

    #⬇️导出平均值(即拟合函数的取样点的实际值)成npy
    np.save(f"iData.npy", avgs)

    #⬇️将平均值和tData合并导出成txt 方便查看或在origin上操作
    tData = list(range(40,201,20))
    data = np.column_stack((avgs, tData))
    np.savetxt("datas.txt", data, delimiter="\t", header="X\tY", fmt="%.2f")

# 将任意图片转化成像素点亮度的矩阵
def pictureToBrightness(image, imageName, outputFolder):

    matrixs = []                    # 定义每个图片亮度矩阵组成的数组

    image = image.convert('L')      # 转为灰度图像
    iMatrix = np.array(image)       # 转换为矩阵
    matrixs.append(iMatrix)         # 将矩阵加到数组中

    # 构造保存文件路径（带前缀 i_ ）
    baseName, _ = os.path.splitext(imageName)  # 分离文件名和扩展名
    prefixName = f"i_{baseName}"
    
    # 保存为 .npy 文件
    npy_path = os.path.join(outputFolder, f"{prefixName}.npy")
    np.save(npy_path, iMatrix)

    # 保存为 .csv 文件
    csv_path = os.path.join(outputFolder, f"{prefixName}.csv")
    np.savetxt(csv_path, iMatrix, delimiter=",", fmt='%d')

    print(f"{imageName}'s iMatrix has been exported")

# 识别文件夹中的所有图片并生成同名矩阵
def main(inputFolder):
    # 获取输入文件夹的父目录和名称
    parentDir, folderName = os.path.split(os.path.abspath(inputFolder))
    
    # 新建文件夹名（加上后缀 _s1 ）
    outputFolder = os.path.join(parentDir, f"{folderName}_s1")
    
    # 确保输出文件夹存在
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    
    # 遍历输入文件夹中的所有文件
    for fileName in os.listdir(inputFolder):

        # 构造完整的文件路径
        input_path = os.path.join(inputFolder, fileName)
        
        # 检查是否为图片文件
        if os.path.isfile(input_path) and fileName.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                image = Image.open(input_path)
                pictureToBrightness(image, fileName, outputFolder)
    print ("step1 finished")

    # 返回输出文件夹
    return outputFolder

# ⬇️调试
# inputFolder = "analyse"
# main(inputFolder)