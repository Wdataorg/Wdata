<div align="center">
 
<img src="https://raw.githubusercontent.com/Wdataorg/Wdata/main/.github/logo.svg" height=200/>
 
[![Issues](https://img.shields.io/github/issues/Wdataorg/Wdata?style=for-the-badge&color=yellogreen)](https://github.com/Wdataorg/Wdata/issues)
[![Forks](https://img.shields.io/github/forks/Wdataorg/Wdata?style=for-the-badge&color=orange)](https://github.com/Wdataorg/Wdata/network/members)
![Stars](https://img.shields.io/github/stars/Wdataorg/Wdata?style=for-the-badge&color=yellowgreen)
[![License](https://img.shields.io/github/license/Wdataorg/Wdata?style=for-the-badge&color=red)](https://shiro.apache.org/license.html) 
[![Commits](https://img.shields.io/github/commit-activity/m/Wdataorg/Wdata?label=commits&style=for-the-badge&color=blue)](https://github.com/Wdataorg/Wdata/commits "Commit History")
 [![Release version](https://img.shields.io/github/v/release/Wdataorg/Wdata?color=brightgreen&label=Download&style=for-the-badge)](#release-files "Release")

 [English](https://github.com/Wdataorg/Wdata/#readme)

</div>

- [功能介绍](#功能介绍)
- [下载](#下载)
- [使用](#使用)
    - [获取数据](#获取数据)
    - [导入数据](#导入数据)
    - [绘图](#绘图)
    - [保存文件](#数据保存)
- [附加功能](#附加功能)
    - [余弦相似度函数](#余弦相似度函数)
    - [距离函数](#距离函数)
- [我们有哪些数据](#我们有哪些数据)
- [捐款](#捐款)
- [有关Pypi](#有关Pypi)
- [许可证](#许可证)
- [我们的内测](#我们的内测)

# 功能介绍

本项目是一个含有多功能的数据集，里面有很多数据集，目前已经上传到Pypi。

# 下载
本项目使用Pypi,所以建议使用Pypi下载

有一些依赖库，请将以下代码粘贴到终端

```
pip3 install simplejson
pip3 install openpyxl
pip3 install matplotlib
pip3 install setuptools
```

代码：`pip3 install Wdatabase`

# 使用

我们上传时包名和实际使用时用的包名不太一样
导入时，使用以下代码

```python
from Wdata import WdataMain as main
```
主类中有以下函数：

|函数|介绍|语法|返回类型|
|:--------:|:--------:|:--------:|:--------:|
|draw|绘图|Func()|None|
|Save_file|保存文档|Func(filename:str, type='json', Sheet='Data', RowOrColumn=True)|bool|
## 导入数据
Wdata有很多数据集，我们这里使用200年来人口增长数据举例

Wdata_class的语法如下:
`Wdata_class(json_fname: str)`

`json_fname`为数据集的名字

```python
from Wdata import WdataMain as main

test = main('Population_growth')  # 导入200年来人口增长
```

## 获取数据
我们可以使用`Fetch_dict`函数获取数据

比如这些代码

```python
from Wdata import WdataMain as main

test = main('Population_growth')  # 导入200年来人口增长
print(dict(test))
```

运行后
```shell
~/python test.py
{   
    '1800': 900000000,
    '1820': 1100000000, 
    '1840': 1200000000,
    '1860': 1300000000, 
    '1880': 1400000000, 
    '1900': 1650000000, 
    '1920': 1800000000, 
    '1940': 2200000000, 
    '1960': 3000000000,
    '1980': 4400000000, 
    '2000': 5900000000,
    '2022': 7400000000
    }
```
## 绘图
绘图功能使用`draw()`函数
如以下代码

```python
from Wdata import WdataMain as main

test = main('Population_growth')  # 导入200年来人口增长
test.draw()
```
结果是这样的
<img src="https://raw.githubusercontent.com/Wdataorg/Wdata/main/img/draw_pop.jpg"></img>

## 数据保存
你可以使用`Save_file()`函数来保存数据

`Save_file`的语法是`Save_file(filename:str, type='json', Sheet='Data', RowOrColumn=True) -> None`

参数说明：
`filename`参数是用于说明保存文件
`type`参数是用于说明文件类型
`Sheet`只在保存`.xlsx`文件时生效，表示保存的工作表
`RowOrColumn`只在保存`.xlsx`文件时生效，表示保存的格式

文件类型有以下几个:

|文件类型|使用方式|说明|
|:---:|:---:|:---:|
|csv|Wdata.CSV|保存文件`file.csv`|
|json|Wdata.JSON|保存文件`file.json`，为默认选项|
|xlsx|Wdata.XLSX|保存文件`file.xlsx`|

保存`JSON`文件的代码

```python
from Wdata import WdataMain as main
from Wdata import CSV
test = main('Population_growth')  # 导入200年来人口增长
test.Save_file('Package_test')  # 默认选项
```

保存`CSV`文件的代码

```python
from Wdata import WdataMain as main
test = main('Population_growth')  # 导入200年来人口增长
test.Save_file('Package_test', CSV)  # 该函数会自动添加.csv后缀
```

保存`.xlsx`文件会使用到`Sheet`和`RowOrColumn`参数

`Sheet`表示保存单元格，默认为`Data`

`RowOrColumn`表示保存形式，默认为`True`

```python
from Wdata import WdataMain as main
from Wdata import XLSX
test = main('Population_growth')  # 导入200年来人口增长
test.Save_file('Package_test', XLSX)  # 该函数会自动添加.xlsx后缀
# test.Save_file('Package_test', XLSX, RowOrColumn=False)   这条代码会以列的形式保存
```

当`RowOrColumn`为`True`时，保存形式是这样的

| 1820 |1840 | 1860 | 1880 | 1900 | 1920 | 1940 |1960|1980 | 2000 |2022|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1100000000|1200000000|1300000000|1400000000|1650000000|1800000000|2200000000|3000000000|4400000000|5900000000|7400000000|

反之，是这样的

| 1820 | 1100000000 | 
|:---:|:---:|
|1840 |1200000000|
|1860|1300000000|
|1880|1400000000|
|1900|1650000000|
|1920|1800000000|
|1940|2200000000|
|1960|3000000000|
|1980|4400000000|
|2000|5900000000|
|2022|7400000000|
# 附加功能
## 余弦相似度函数

余弦相似度函数可以根据余弦相似度公式计算出二维空间中两个坐标的余弦相似度

使用方法：

```python
from Wdata import mathfunc
xy1 = (2, 3) #  第一个坐标
xy2 = (3, 5) # 第二个坐标
result = mathfunc.similarity(xy1, xy2) # 余弦相似度
print(result)
```

## 距离公式

距离公式使用欧几里得距离公式计算出二维空间中两个坐标的距离

使用方法：

```python
from Wdata import mathfunc
xy1 = (2, 3)
xy2 = (3, 5)
result = mathfunc.distance(xy1, xy2) # 距离公式
print(result)
```

# 我们有哪些数据
目前我们有以下数据

|                名字                |          说明           |   计量单位    | 
|:--------------------------------:|:---------------------:|:---------:|
|        Population_growth         |    1800-2022年人口增长     |     人     |
|        Chinese_spacecraft        | 2017-2020.06中国航天器发射次数 |    航天器    |
|    World_spacecraft              | 2017-2020.06世界航天器发射次数 |    航天器    |
> 以上数据来源于Bing以及Baidu,作者无法确保数据的准确性，切勿用于专业用途

# 捐款
由于特殊原因，作者无法注册`Paypal`账号，被迫使用支付宝

具体详情请见[捐款说明](https://wdataorg.github.io/Sponsor/)

# 有关Pypi
`Wdataorg`团队已经使用`twine`将本库上传到`Pypi`

[Wdataorg Pypi账号](https://pypi.org/user/Lucky_Pupil/)

[Wdatabase Pypi仓库地址](https://pypi.org/project/Wdatabase/)

# 许可证
本开源项目使用`Apache License 2.0`

在使用本开源项目过程中，请严格按照许可证规定使用

最终解释权归开发团队`Wdataorg`所有

[项目许可证链接](https://github.com/Wdataorg/Wdata/blob/main/LICENSE)

# 我们的内测

`0.0.1b0`版本已经发布，各位使用者可以提出自己宝贵的意见

如何内测？

请按照README指示下载项目并且使用，填写内测单