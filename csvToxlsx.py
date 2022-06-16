import os

from pandas import read_csv


def get_filepath(dir_path, list_name):
    """递归获取目录下（文件夹下）所有文件的路径"""
    for file in os.listdir(dir_path):  # 获取文件（夹）名
        file_path = os.path.join(dir_path, file)  # 将文件（夹）名补全为路径
        if os.path.isdir(file_path):  # 如果是文件夹，则递归
            get_filepath(file_path, list_name)
        elif file_path.endswith("result.csv"):
            list_name.append(file_path)  # 保存路径
    return list_name


def csv_to_xlsx():
    path = './cleaned result'
    res = get_filepath(path, [])
    for file in res:
        data = read_csv(file)
        data.to_excel(file.split(".csv")[0] + ".xlsx")
