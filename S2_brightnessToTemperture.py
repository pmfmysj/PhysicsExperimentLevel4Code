'''将每个亮度矩阵通过拟合函数的反函数转化成温度矩阵 并保存'''

import os
import numpy as np
from func_curveFittingLM import inverseFunc

# 将任意矩阵通过拟合函数反函数转化成另一个矩阵
def briToTem(iMatrix, fileName, outputFolder):
    '''
    由于拟合函数反函数中存在对数 当 x=I0/(I-C)-1<0 => I<21.97 或 I>171.62, 
    当考虑到拟合函数反函数彼时早已远离实验的测量范围
    (f^{-1}(22)=327.6℃ f^{-1}(171)=9.0℃), 
    故粗暴地将所有亮度低于22的点变为22, 高于171的点变成171.
    '''
    iMatrix[iMatrix < 22] = 22
    iMatrix[iMatrix > 171] = 171
    tMatrix = inverseFunc(iMatrix)

    #tMatrix = np.nan_to_num(tMatrix, nan=20)        # 为了鲁棒性
    avg = np.average(tMatrix)
    
    # 构造保存文件路径（带前缀 t_ ）
    base_name, _ = os.path.splitext(fileName)  # 分离文件名和扩展名
    prefix_name = f"t_{base_name}"
    
    # 保存为 .npy 文件
    npy_path = os.path.join(outputFolder, f"{prefix_name}.npy")
    np.save(npy_path, tMatrix)

    # 保存为 .csv 文件
    csv_path = os.path.join(outputFolder, f"{prefix_name}.csv")
    np.savetxt(csv_path, tMatrix, delimiter=",", fmt='%d')

    print(f"{fileName}'s tMatrix has been exported. ")

# 识别文件夹中的所有矩阵并生成同名矩阵
def main(inputFolder):
    # 获取输入文件夹的父目录和名称
    parentDir, folderName = os.path.split(os.path.abspath(inputFolder))
    
    # 新建文件夹名（加上后缀 _s2 ）
    outputFolder = os.path.join(parentDir, f"{folderName}_s2")
    
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

# ⬇️调试
#inputFolder = "train_s1ed"
#main(inputFolder)
