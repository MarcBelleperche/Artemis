import json
import os


def write_json(table, dataname, datavalue):
    filesize = os.path.getsize("pers_datas.txt")
    if filesize != 0:
        data = read_json()
        if table in data:
            data[table].append({
                dataname: datavalue
            })
        else:
            data[table] = []
            data[table].append({
                dataname: datavalue
            })

    else:
        data = {}
        data[table] = []
        data[table].append({
                dataname: datavalue
            })

    with open('pers_datas.txt', 'w') as outfile:
        json.dump(data, outfile)


def write_json_details(table, dependency, dataname, datavalue):
    file = read_json()
    if table in file:
        for obj in file[table]:
            if obj['name'] == dependency:
                obj[dataname] = datavalue

    with open('pers_datas.txt', 'w') as outfile:
        json.dump(file, outfile)


def read_json():
    with open('pers_datas.txt') as json_file:
        data = json.load(json_file)
        return data


def read_spec_json(table, dataname):
    with open('pers_datas.txt') as json_file:
        data = json.load(json_file)
        for specs in data[table]:
            return specs[dataname]


def ip_address(table, devicename):
    with open('pers_datas.txt') as json_file:
        data = json.load(json_file)
        for specs in data[table]:
            if specs['name'] == devicename:
                return specs['ip']