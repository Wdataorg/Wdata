from Wdata import Wdata_class # 导入我的库

# 创建对象

test = Wdata_class('Population_growth') # 人口增长
test2 = Wdata_class('Chinese_spacecraft') # 中国航天器发射次数
test3 = Wdata_class('World_spacecraft') # 世界航天器发射次数

# 获取数据

for i in [test, test2, test3]:
    print('数据{}:{}'.format(i.jsonname, i.Fetch_dict))

# 保存文件

for i in [test, test2, test3]:
    print('保存数据{}'.format(i.jsonname))
    i.Save_file(i.jsonname)

# 绘图

for i in [test, test2, test3]:
    print('绘制数据{}'.format(i.jsonname))
    i.draw()
