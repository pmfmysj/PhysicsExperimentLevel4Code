from PIL import Image
import numpy as np
import os

# 导入图片 转换为灰度图像
image_path = 'image.jpg'                                        # 图片路径
image = Image.open(image_path).convert('L')                     # 转为灰度图像

# 转换为 NumPy 数组
pixel_matrix = np.array(image)

# 处理矩阵
processed_matrix = pixel_matrix

# 导出文件名
file_dir, file_name = os.path.split(image_path)                 # 分离路径和文件名
file_base, _ = os.path.splitext(file_name)                      # 分离文件名和扩展名
csv_file_path = os.path.join(file_dir, f"{file_base}.csv")      # 构造文件路径

# 导出为 CSV 文件
np.savetxt(csv_file_path, pixel_matrix, delimiter=",", fmt='%d') 

print(f"像素矩阵已导出为: {csv_file_path}")