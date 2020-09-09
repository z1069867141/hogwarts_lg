import yaml


class Utils:
    @classmethod
    def from_file(cls, path):
        with open(path, encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            params = yaml_data['params']
            keys = set()  # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
            values = []
            if isinstance(params, list):
                for row in params:
                    if isinstance(row, dict):
                        """
                        for key in row.keys():
                            keys.append(key)
                        下方代码相当于，操作是一样的
                        keys += row.keys()
                        通过使用循环取出key和value，value会以列表形式
                        例如：[[1],[2]]
                        如此进行添加数据，使用list转换格式变成列表，并且取出第一个值
                        可以有效转换成列表，从而转换成[1,2]
                        """
                        for key in row.keys():
                            keys.add(key)
                            values.append(list(row.values())[0])
            var_names = ','.join(keys)
            return {'keys': var_names, 'values': values}

# if __name__ == '__main__':
#     a = Utils()
#     a.from_file('test_search.yaml')