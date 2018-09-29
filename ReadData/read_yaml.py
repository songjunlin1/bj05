import yaml
def read_yaml():
    with open("../DataPool/yaml.yaml",'r',encoding="utf-8") as f:
        # 使用load加载文件
        return yaml.load(f)
print(read_yaml())