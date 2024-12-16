from PIL import Image
import numpy as np
import os

# 导入图片 转换为灰度图像
imagePath = 'image.jpg'                                         # 图片路径
image = Image.open(imagePath).convert('L')                      # 转为灰度图像

# 转换为 NumPy 数组
pixelMatrix = np.array(image)

# 取平均
avg = np.average(pixelMatrix)

# 处理矩阵
processed_matrix = pixelMatrix

# 导出文件名
fileDir, file_name = os.path.split(imagePath)                   # 分离路径和文件名
fileBase, _ = os.path.splitext(file_name)                       # 分离文件名和扩展名
csvFilePath = os.path.join(fileDir, f"{fileBase}.csv")          # 构造文件路径
print(avg)

# 导出为 CSV 文件
np.savetxt(csvFilePath, pixelMatrix, delimiter=",", fmt='%d') 

print(f"像素矩阵已导出为: {csvFilePath}")