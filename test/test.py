import Wdata
Wdata.upload("thg", {
        "count_unit":"spacecraft",
        "Type": "Line Chart",
        "unit": "years",
        "Unit length":1,
        "datas":{
            "2017": 467,
            "2018": 438,
            "2019": 492,
            "2020.6": 1277
        }
    })

print(Wdata.data_py.data)
test = Wdata.Wdata_class('thg')