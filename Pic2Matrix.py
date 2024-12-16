from PIL import Image
import numpy as np

# 1. 导入图片并转换为灰度图像
image_path = 'image.jpg'  # 图片路径
image = Image.open(image_path).convert('L')  # 转为灰度图像 ('L' 模式)

# 2. 将灰度图像转换为 NumPy 数组（矩阵）
pixel_matrix = np.array(image)

# 3. 打印像素矩阵及其形状
print("像素矩阵：")
print(pixel_matrix)
print("\n矩阵形状: ", pixel_matrix.shape)