import yaml


class Utils:
    @classmethod
    def from_file(cls, path):
        with open(path, encoding="utf8") as f:
            yaml_data = yaml.safe_load(f)
            params = yaml_data['params1']
            keys = set()
            values = []
            if isinstance(params, list):
                for row in params:
                    if isinstance(row, dict):
                        for key in row.keys():
                            keys.add(key)
                            values.append(list(row.values())[0])
            var_names = ','.join(keys)
            return {'keys': var_names, 'values': values}


# if __name__ == "__main__":
#     Utils.from_file("test_search.yaml")
# {'keys': {'keyword'}, 'values': [dict_values(['alibaba']), dict_values(['baidu']), dict_values(['jd'])]}
# {'keys': 'keyword', 'values': [dict_values(['alibaba']), dict_values(['baidu']), dict_values(['jd'])]}