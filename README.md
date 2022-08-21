<div align="center">
 
<img src="https://raw.githubusercontent.com/Wdataorg/Wdata/main/.github/logo.svg" height=200/>
 
[![Issues](https://img.shields.io/github/issues/Wdataorg/Wdata?style=for-the-badge&color=yellogreen)](https://github.com/Wdataorg/Wdata/issues)
[![Forks](https://img.shields.io/github/forks/Wdataorg/Wdata?style=for-the-badge&color=orange)](https://github.com/Wdataorg/Wdata/network/members)
![Stars](https://img.shields.io/github/stars/Wdataorg/Wdata?style=for-the-badge&color=yellowgreen)
[![License](https://img.shields.io/github/license/Wdataorg/Wdata?style=for-the-badge&color=red)](https://shiro.apache.org/license.html) 
[![Commits](https://img.shields.io/github/commit-activity/m/Wdataorg/Wdata?label=commits&style=for-the-badge&color=blue)](https://github.com/Wdataorg/Wdata/commits "Commit History")
 [![Release version](https://img.shields.io/github/v/release/Wdataorg/Wdata?color=brightgreen&label=Download&style=for-the-badge)](#release-files "Release")
 
 [简体中文](https://github.com/Wdataorg/Wdata/tree/main/README_SimpleChinese.md)


</div>

- [Function introduction](#Features)
- [download](#Download)
- [use](#Use)
    - [Get data](#Get-data)
    - [import data](#Import-data)
    - [drawing](#Drawing)
    - [Data save](#Data-save)
- [What data do we have](#What-data-do-we-have)
- [Donation](#Donate)
- [About Pypi](#About-Pypi)
- [license](#License)
- [our internal test](#Our-closed-beta)

# Features

This project is a dataset with multiple functions, there are many datasets in it, and it has been uploaded to Pypi.

# Download
This project uses Pypi, so it is recommended to use Pypi to download

Code: `pip3 install Wdatabase`

# Use

The package name when we upload is not the same as the package name used in actual use
When importing, use the following code

````python
from Wdata import WdataMain as main
````
The main class has the following functions:

|Functions|Introduction|Syntax|Return Type|
|:-------:|:--------:|:--------:|:--------:|
|Fetch_dict|Get data|Func()|dict|
|draw|Draw|Func()|None|
|Save_file|Save file|Func(filename:str)|bool|
## Import Data
Wdata has a lot of data sets, here we use 200 years of population growth data as an example

The syntax of Wdata_class is as follows:
`Wdata_class(json_fname: str)`

`json_fname` is the name of the dataset

````python
from Wdata import WdataMain as main

test = main('Population_growth')  # import population growth over 200 years
````

## Get data
We can use the `Fetch_dict` function to fetch the data

such as these codes

````python
from Wdata import WdataMain as main

test = main('Population_growth')  # import population growth over 200 years
print(test.Fetch_dict())
````

after running
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
````
## Drawing
Drawing functions use the `draw()` function
as the following code

````python
from Wdata import WdataMain as main

test = main('Population_growth')  # import population growth over 200 years
test.draw()
````
The result is this
<img src="https://raw.githubusercontent.com/Wdataorg/Wdata/main/img/draw_pop.jpg"></img>

## Data save
You can use the `Save_file()` function to save data

The syntax of `Save_file` is `Save_file(filename:str) -> None`

Parameter Description:
The `filename` parameter is used to describe the save file

as the following code

````python
from Wdata import WdataMain as main

test = main('Population_growth')  # import population growth over 200 years
test.Save_file('Package_test')  # This function will automatically add the .json suffix
````

# What data do we have
Currently we have the following data

| name | description | unit of measure |
|:--------------------------------:|:---------------------:|:---------:|
| Population_growth | Population Growth 1800-2022 | People |
| Chinese_spacecraft | 2017-2020.06 Chinese spacecraft launches | Spacecraft |
| World_spacecraft | 2017-2020.06 World Spacecraft Launches | Spacecraft |
> The above data comes from Bing and Baidu. The author cannot guarantee the accuracy of the data and should not be used for professional purposes

# Donate
Due to special reasons, the author was unable to register a `Paypal` account and was forced to use Alipay

For details, please see [Donation Instructions](https://wdataorg.github.io/Sponsor/)

# About Pypi
The `Wdataorg` team has used `twine` to upload this library to `Pypi`

[Wdataorg Pypi account](https://pypi.org/user/Lucky_Pupil/)

[Wdatabase Pypi warehouse address](https://pypi.org/project/Wdatabase/)

# License
This open source project uses `Apache License 2.0`

In the process of using this open source project, please use it strictly in accordance with the license

The final interpretation right belongs to the development team `Wdataorg`

[Project License Link](https://github.com/Wdataorg/Wdata/blob/main/LICENSE)

# Our closed beta

`0.0.1b0` version has been released, users can put forward their valuable opinions

How to test?

Please follow the README instructions to download the project and use it, fill in the internal test form
