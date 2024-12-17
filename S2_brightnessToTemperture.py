import os
import numpy as np
from fittingLM import inverseFunc

def briToTem(iMatrix, fileName, outputFolder):
    iMatrix[iMatrix < 22] = 22   #将小于22的值改成22, 以避免I过小导致溢出误差
    tMatrix = inverseFunc(iMatrix)
    # 替换 NaN 为 0 或其他值
    tMatrix = np.nan_to_num(tMatrix, nan=20)
    avg = np.average(tMatrix)
    
    # 构造保存文件路径（带前缀 `matrix_`）
    base_name, ext = os.path.splitext(fileName)  # 分离文件名和扩展名
    prefix_name = f"tMatrix_{base_name}"
    
    # 保存为 .npy 文件
    npy_path = os.path.join(outputFolder, f"{prefix_name}.npy")
    np.save(npy_path, tMatrix)
    print(f"{fileName}'s npy has been saved\n average temperture is {avg}")

    # 保存为 .csv 文件
    csv_path = os.path.join(outputFolder, f"{prefix_name}.csv")
    np.savetxt(csv_path, tMatrix, delimiter=",", fmt='%d')
    print(f"{fileName}'s csv has been exported. ")

# 识别文件夹中的所有图片并生成同名矩阵
def main(inputFolder):
    # 获取输入文件夹的父目录和名称
    parentDir, folderName = os.path.split(os.path.abspath(inputFolder))
    
    # 新建文件夹名（加上后缀）
    outputFolder = os.path.join(parentDir, f"{folderName}_s2ed")
    
    # 确保输出文件夹存在
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    
    # 遍历输入文件夹中的所有文件
    for fileName in os.listdir(inputFolder):
        # 构造完整的文件路径
        input_path = os.path.join(inputFolder, fileName)
        
        # 检查是否为图片文件
        if os.path.isfile(input_path) and fileName.lower().endswith(('.npy')):
                iMatrix = np.load(input_path)
                briToTem(iMatrix, fileName, outputFolder)
    print ("step2 finished")
    return outputFolder

#inputFolder = "train_s1ed"
#main(inputFolder)
