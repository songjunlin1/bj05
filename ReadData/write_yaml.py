import yaml

# 要写入yaml文件的数据
data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
# 声明 写入函数
def write_yaml():
    with open("../DataPool/write_yaml.yaml",'w',encoding="utf-8") as f:
        # 调用dump方法写入数据
        """
            f: 为要写入文件路径及文件名的文件流
            data: 要写的内容
        """
        yaml.dump(data,stream=f, encoding='utf-8',allow_unicode=True)

write_yaml()