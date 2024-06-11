import random
import string
from functools import wraps


def calculate_sum_and_average(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if isinstance(data, set):
            total_sum, total_count = sum_and_count(data)
            average = total_sum / total_count if total_count > 0 else 0
            print(f"总和: {total_sum}, 平均值: {average}")
        return data

    def sum_and_count(data):
        total_sum = 0
        total_count = 0
        for item in data:
            if isinstance(item, (int, float)):
                total_sum += item
                total_count += 1
            elif isinstance(item, (tuple, list)):
                for sub_item in item:
                    if isinstance(sub_item, (int, float)):
                        total_sum += sub_item
                        total_count += 1
        return total_sum, total_count

    return wrapper


class DataSampler:
    def __init__(self):
        pass

    @calculate_sum_and_average
    def data_sampling(self, datatype, datarange, num, strlen=8):
        """
        Generate a given condition random data set.

        :param datatype: the type of data to generate (int, float, str)
        :param datarange: the range of data
        :param num: the number of data points
        :param strlen: the length of the string (if generating strings)
        :return: a set of generated data
        """
        result = set()
        for _ in range(num):
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
            elif datatype is float:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
            elif datatype is str:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
            else:
                continue
        return result

    @calculate_sum_and_average
    def list_sampling(self, data_type, num_list, name, id_range, grade_range, strlen=8):
        """
        Generate a list or tuple with specified data.

        :param data_type: the type of container to generate (list, tuple)
        :param num_list: the number of data entries
        :param name: the possible characters for names
        :param id_range: the range for IDs
        :param grade_range: the range for grades
        :param strlen: the length of the names
        :return: a set of generated data entries
        """
        result = set()
        for _ in range(num_list):
            item_name = ''.join(random.SystemRandom().choice(name) for _ in range(strlen))
            it = iter(id_range)
            item_id = random.randint(next(it), next(it))
            it = iter(grade_range)
            item_grade = random.uniform(next(it), next(it))

            if data_type is list:
                result.add((item_name, item_id, item_grade))
            elif data_type is tuple:
                result.add((item_name, item_id, item_grade))
            else:
                continue
        return result


# 使用DataSampler类
sampler = DataSampler()

# 生成随机数据示例

random_data_int = sampler.data_sampling(int, (1, 100), 10)
print("生成的整型数据:", random_data_int)

random_data_float = sampler.data_sampling(float, (0.1, 0.9), 5)
print("生成的浮点型数据:", random_data_float)

# random_data_str = sampler.data_sampling(str, string.ascii_letters + string.digits, 3, 10)
# print(random_data_str)


# random_data_list = sampler.list_sampling(list, 1, string.ascii_letters, (1, 10), (0, 100), 5)
# print(random_data_list)
#
# random_data_tuple = sampler.list_sampling(tuple, 5, string.ascii_letters, (1, 20), (0, 100), 5)
# print(random_data_tuple)
