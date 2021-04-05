import json


def write_json(table, dataname, datavalue):
    data = {}
    data[table] = []
    data[table].append({
        dataname: datavalue
    })
    with open('pers_datas.txt', 'w') as outfile:
        json.dump(data, outfile)


def read_json():
    with open('pers_datas.txt') as json_file:
        data = json.load(json_file)
        return data


def read_spec_json(table, dataname):
    with open('pers_datas.txt') as json_file:
        data = json.load(json_file)
        for specs in data[table]:
            return specs[dataname]