def read_txt():
    with open("../DataPool/txt.txt",'r',encoding="utf-8") as f:
        datas=f.readlines()
        arrs=[]
        for data in datas:
            # 去除前后换行符、空格
            """
            strip(): 去除字符串前后空格回车
            split("字符")：以指定的字符分割字符串，并以列表形式返回
            """
            arrs.append(data.strip().split(","))
        return arrs
print(read_txt())