'''通过指定温度下的热敏荧光材料发光来标定采样 以拟合函数参数'''

import func_curveFittingLM as lm
import s1_imageToBrightness as s1

s1.picToBrightnessForTrain()
lm.lmFitting()
