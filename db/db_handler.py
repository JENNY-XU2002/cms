import json

class Info():

    #注册及登录信息文件的读取
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

    #注册，将数据存入info.json
    def create(self,name,password1,password2):
        with open('info.json') as f:
            info = json.load(f)
        if name in info:
            return '该用户已存在！'
        else:
            if password1!=password2:
                return '密码不一致！'
            else:
                info[name]=password1
                json_str = json.dumps(info)
                with open('info.json', 'w') as f1:
                    f1.write(json_str)
                return '创建成功！'

    #修改密码
    def update(self, name, password):
        with open('info.json') as f:
            info = json.load(f)
        if name in info:
            info[name]=password
            json_str = json.dumps(info)
            with open('info.json', 'w') as f1:
                f1.write(json_str)
            return '修改成功'
        else:
            return '姓名错误！'

    @property  # Python内置的@property装饰器就是负责把一个方法变成属性调用的
    def dict(self):
        return self.__dict__

'''
if __name__ == '__main__':
    information = {'ljl':'123'}#输入的姓名和密码
    json_str = json.dumps(information, indent=4)

    with open('info.json', 'w') as f:  # 创建一个info.json文件
        f.write(json_str)  # 将json_str写到文件中
    info = Info('info.json')
    info.T('ljl','123')
    info.create('hjshdjs','sadj','sadj')
'''
