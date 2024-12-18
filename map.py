'''用来将热敏荧光材料发光图映射为温度可视化图'''

import s1_imageToBrightness as s1
import s2_brightnessToTemperture as s2
import s3_tempertureToRgb as s3

inputFolder = "train"                   #在此处更改输入文件夹
s3.main(s2.main(s1.main(inputFolder)))
