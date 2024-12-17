'''20241216 四级大物'''
'''将每张图图片转化成各个像素点的数组, 再求每张图的平均值并保存'''

import os
from PIL import Image
import numpy as np

# 设置起始值
start = 40
stop = 200
step = 20
matrixs = []
avgs = []

def pic2Numpy4Train():

    # 新建文件夹名（加上 "grayed" 后缀）
    outputFolder = f"train_trained"
    
    # 确保输出文件夹存在
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    # 循环
    for i in range(start, stop + 1, step):
        imageName = f"A_{i:03d}"
        imagePath = os.path.join("train", f"{imageName}.bmp")        # 带0
        image = Image.open(imagePath).convert('L')          # 转为灰度图像
        iMatrix = np.array(image)                           # 转换为矩阵
        matrixs.append(iMatrix)
        avg = np.average(iMatrix)                           # 取平均
        avgs.append(avg)
        print(avg)

        #⬇️导出成npy
        npyPath = os.path.join(outputFolder, f"{imageName}.npy")
        np.save(npyPath, iMatrix)
        print(f"A_{i:03d}'s iMatrix has saved")

        #⬇️导出成csv
        csvPath = os.path.join(outputFolder, f"{imageName}.csv")                             
        np.savetxt(csvPath, iMatrix, delimiter=",", fmt='%d')          
        print(f"A_{i:03d}'s pixelMatrix has exported")

    #⬇️导出成npy
    np.save(f"iData.npy", avgs)

    #⬇️和tData合并导出成txt 以方便在origin上操作
    tData = list(range(40,201,20))
    data = np.column_stack((avgs, tData))
    np.savetxt("datas.txt", data, delimiter="\t", header="X\tY", fmt="%.2f")

def pic2Numpy(image, imageName, outputFolder):
    # 转为灰度图像
    image = image.convert('L')

    # 转换为矩阵
    iMatrix = np.array(image)
    matrixs.append(iMatrix)

    # 构造保存文件路径（带前缀 `matrix_`）
    base_name, ext = os.path.splitext(imageName)  # 分离文件名和扩展名
    prefix_name = f"matrix_{base_name}"
    
    # 保存为 .npy 文件
    npy_path = os.path.join(outputFolder, f"{prefix_name}.npy")
    np.save(npy_path, iMatrix)
    print(f"{imageName}'s iMatrix has been saved as {npy_path}")

    # 保存为 .csv 文件
    csv_path = os.path.join(outputFolder, f"{prefix_name}.csv")
    np.savetxt(csv_path, iMatrix, delimiter=",", fmt='%d')
    print(f"{imageName}'s pixelMatrix has been exported as {csv_path}")


# 识别文件夹中的所有图片并生成同名矩阵
def main(inputFolder):
    # 获取输入文件夹的父目录和名称
    parentDir, folderName = os.path.split(os.path.abspath(inputFolder))
    
    # 新建文件夹名（加上后缀）
    outputFolder = os.path.join(parentDir, f"{folderName}_s1ed")
    
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
                pic2Numpy(image, fileName, outputFolder)
    print ("step1 finished")
    return outputFolder

# 示例调用
# inputFolder = "analyse"  # 替换为你的图片文件夹路径
# main(inputFolder)