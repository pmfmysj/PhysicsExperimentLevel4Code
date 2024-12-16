'''20241216 四级大物'''
'''将每张图图片转化成各个像素点的数组并展平, 再求每张图的平均值并保存'''

from PIL import Image
import numpy as np

# 设置起始值
start = 40
stop = 200
step = 20
matrixs = []
avgs = []

# 循环
for i in range(start, stop + 1, step):

    imageName = f"A_{i:03d}.bmp"                        # 带0
    image = Image.open(imageName).convert('L')          # 转为灰度图像

    iMatrix = np.array(image).ravel()                   # 转换为一维数组
    matrixs.append(iMatrix)
    avg = np.average(iMatrix)                           # 取平均
    avgs.append(avg)
    print(avg)                                          # 打印平均值    

    #⬇️导出成npy
    np.save(f"iMatrix_A_{i:03d}.npy", iMatrix)
    print(f"A_{i:03d}'s iMatrix has saved as iMatrix_A_{i:03d}.npy")

    #⬇️导出成csv
    csvFilePath = f"A_{i:03d}.csv"                                     
    np.savetxt(csvFilePath, iMatrix, delimiter=",", fmt='%d')          
    print(f"A_{i:03d}'s pixelMatrix has exported: {csvFilePath}")

#⬇️导出成npy
np.save(f"iData.npy", avgs)

#⬇️和tData合并导出成txt 以方便在origin上操作
tData = list(range(40,201,20))
data = np.column_stack((avgs, tData))
np.savetxt("datas.txt", data, delimiter="\t", header="X\tY", fmt="%.2f")