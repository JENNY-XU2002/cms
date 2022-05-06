import json

class Info():

    #注册及登录信息文件的创建
    def __init__(self, json_path):
        with open(json_path) as f:
            info = json.load(f)  # 将json格式数据转换为字典
            self.__dict__.update(info)

    #保存数据到json文件中
    def save(self, json_path):
        with open(json_path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)

    #判断登陆的是不是正确的
    def T(self,name,password):
        with open('info.json') as f:
            info = json.load(f)
            if name not in info:
                return False
            else:
                if info[name]==password:
                    return True
                else:
                    return False


    #修改数据
    def update(self, json_path):
        """Loads parameters from json file"""
        with open(json_path) as f:
            info = json.load(f)
            self.__dict__.update(info)

    @property  # Python内置的@property装饰器就是负责把一个方法变成属性调用的
    def dict(self):
        """Gives dict-like access to Params instance by `params.dict['learning_rate']"""
        return self.__dict__


if __name__ == '__main__':
    information = {'ljl':'123'}
    json_str = json.dumps(information, indent=4)

    with open('info.json', 'w') as f:  # 创建一个info.json文件
        f.write(json_str)  # 将json_str写到文件中

    print(Info.T('n','ljl','123'))
    info = Info('info.json')
    info.Name = 'ttt'   # 修改json中的数据
    info.save('info.json')  # 将修改后的数据保存
