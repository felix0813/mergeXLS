import os


def get_filepath(dir_path):
    """递归获取目录下（文件夹下）所有文件的路径"""
    for file in os.listdir(dir_path):  # 获取文件（夹）名
        file_path = os.path.join(dir_path, file)  # 将文件（夹）名补全为路径
        if os.path.isdir(file_path):  # 如果是文件夹，则递归
            get_filepath(file_path)
        elif (not file_path.endswith("result.xlsx")) and (not file_path.endswith("result.csv")):
            os.remove(file_path)  # 保存路径


def delete():
    get_filepath("./new") ## 修改  


delete()
