import os
import pandas as pd


class ExcelUtil:
    @staticmethod
    def change_format(xlsx):
        if xlsx.endswith('xlsx'):
            os.rename(xlsx, xlsx.split(".xlsx")[0] + ".csv")

    @staticmethod
    def write_csv(target, source):
        with open(target, mode='a') as tar:
            with open(source) as f:
                f.readline()
                line = f.readline()
                while line:
                    tar.write(line)
                    line = f.readline()

    @staticmethod
    def excel_to_csv(xlsx):
        # 文件内容转换
        read_file = pd.read_excel(xlsx)
        # Write the dataframe object
        # into csv file
        read_file.to_csv(xlsx.split('.xlsx')[0] + ".csv",
                         index=None,
                         header=True)
        # read csv file and convert
        # into a dataframe object
        df = pd.DataFrame(pd.read_csv(xlsx.split('.xlsx')[0] + ".csv"))
        # show the dataframe
        df

    @staticmethod
    def merge_horizon(path):
        print(path)
        df1 = []
        for i in os.listdir(path):
            # 重构文件路径
            name = os.path.join(path, i)
            # print(name)
            # 将excel转换成DataFrame
            a = pd.read_excel(name)

            # 保存到新列表中
            df1.append(a)

        # 多个DataFrame合并为一个
        df = pd.concat(df1, axis=1)
        # print(df)
        df.to_excel(path+'/result.xlsx', index=False)
