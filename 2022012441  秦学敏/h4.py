import random
import string
from collections.abc import Iterable  # 导入 Iterable


def generate_random_data(datatype, **kwargs):
    if datatype == int:
        return random.randint(kwargs['drange'][0], kwargs['drange'][1])
    elif datatype == float:
        return random.uniform(kwargs['drange'][0], kwargs['drange'][1])
    elif datatype == str:
        return ''.join(random.choices(kwargs.get('drange', string.ascii_lowercase), k=kwargs['len']))
    elif issubclass(datatype, Iterable):
        # 检查是否是可迭代类型
        subs = kwargs.get('subs', [])  # 默认subs为空列表
        if not subs:
            return datatype()  # 返回一个空的相应类型对象
        return datatype(generate_random_data(**sub_kwargs) for sub_kwargs in subs)  # 修改这里以迭代subs

    '''
       class Ran:
           def __init__(self, **kwargs):
               self.n = kwargs.get("num")
               self.m = kwargs.get("struct")
               self.num=1
           def __iter__(self):
                   return self
           def __next__(self):
               if self.num>self.n:
                   raise StopIteration
               result = generate_random_data(**self.m)
               self.num+=1
               return result

       '''

def Ran(num, struct):
    for _ in range(num):
        yield generate_random_data(**struct)

    # 使用示例


# 注意subs现在是列表的列表，每个内部列表描述了一个元素
para = {
    'datatype': tuple,
    'subs': [
        {'datatype': list, 'subs': [
            {'datatype': int, 'drange': (0, 150)},
            {'datatype': str, 'drange': string.ascii_lowercase, 'len': 8}
        ]},
        {'datatype': float, 'drange': (0, 100)}
    ]
}

if __name__ == '__main__':
    rg = Ran(3, para)
    for _ in range(3):
        print(next(rg))