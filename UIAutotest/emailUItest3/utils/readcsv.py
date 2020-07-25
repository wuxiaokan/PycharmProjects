import csv
import os, yaml



def readcsv(path):
    try:
        file = open(path, "r", encoding="utf8")
        list1 = csv.reader(file, delimiter=";")
        list2 = []
        for list in list1:
            if list[0] != "caseid":
                list2.append(tuple(list))
    except IOError as e:
        print(e)
    finally:
        file.close()
    return list2


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data