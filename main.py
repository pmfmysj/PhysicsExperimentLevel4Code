import fittingLM as lm
import S1_imageToNumpy as s1
import S2_brightnessToTemperture as s2
import S3_tempertureToRgb as s3

# ⬇️训练函数
#s1.pic2Numpy4Train()
#lm.lmFitting()

# ⬇️图片亮度信息转为温度颜色
inputFolder = "train"
s3.main(s2.main(s1.main(inputFolder)))
