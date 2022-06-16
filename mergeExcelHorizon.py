# Read and store content
# of an excel file
# 递归获取目录（文件夹）下的所有文件路径
# 递归获取目录（文件夹）下的所有文件路径
import os

import csvToxlsx
import deleteFIle
from ExcelUtil import ExcelUtil

file_dir = []


def get_filepath(dir_path, list_name):
    """递归获取目录下（文件夹下）所有文件的路径"""
    for file in os.listdir(dir_path):  # 获取文件（夹）名
        file_path = os.path.join(dir_path, file)  # 将文件（夹）名补全为路径
        if os.path.isdir(file_path):  # 如果是文件夹，则递归
            if file_path.endswith("WT") or file_path.endswith("16p"):
                file_dir.append(file_path)
            get_filepath(file_path, list_name)
        else:
            list_name.append(file_path)  # 保存路径
    return list_name


path = r'./new'
get_filepath(path, [])
for xls_dir in file_dir:
    ExcelUtil.merge_horizon(xls_dir)
deleteFIle.delete()
