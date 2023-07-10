# Nerve auto label tool
## 基于Opencv的CCM神经分割半自动化标注工具

> Author: github.com/SummerColdWind

> 本项目仅为测试用框架，不具备实际使用价值。

## 1.准备数据集

在./sample文件夹中存放了一些CCM的图像，大小为384x484，其中感兴趣的区域为384x384。


## 2.边缘检测
```python
from qqlabel import EdgeDetect

detection = EdgeDetect(f'./sample/image_0.jpg')
detection.detect()
detection.show()
```
 - 导入EdgeDetect类并在实例化时传入图片路径。
 - 使用detect方法执行边缘检测
 - 使用show方法展示识别结果

## 3.转换标注格式
```python
from qqlabel import EdgeDetect, Convert

detection = EdgeDetect(f'./sample/image_0.jpg')
detection.detect()
detection.save(f'./results/image/result_0.png')
data = detection.output()

convert = Convert(data)
convert.create()
convert.save(f'./results/json/result_0.json')
```
 - 使用detect对象的save方法储存轮廓检测后的图片
 - 使用output方法输出用于转换标注的数据
 - 导入Convert类并在实例化时传入output输出的数据
 - 使用create方法创建并完成用于标注的数据格式
 - 使用convert对象的save方法储存Labelme可打开的json文件。

## 4.手动修正

使用Labelme打开输出的json文件并且手动修正。
