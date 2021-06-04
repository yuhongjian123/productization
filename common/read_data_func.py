"""
数据源解析,读取数据方法
"""
import json


def read_account_data():
    """帐号数据读取方法"""
    with open('../data_pool/account_data.json', encoding='utf-8') as a:
        account_data = json.load(a)
        list_a = list()
        for i in account_data:
            list_a.append((i.get('zhzhwh'),
                           i.get('zhzhsh'),
                           i.get('zhzhszs'),
                           i.get('dwjb'),
                           i.get('dwsh'),
                           i.get('bmsh'),
                           i.get('password')))
        print(list_a)
        return list_a


def read_zhzhwh_data():
    """专户账户录入数据读取方法"""
    with open('../data_pool/zhzhwh_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = list()  # 声明空列表
        for i in data:
            data_list.append((i.get('name'),
                              i.get('czqhdm'),
                              i.get('zhlbdm'),
                              i.get('xz'),
                              i.get('hsnr'),
                              i.get('splxdm'),
                              i.get('kuyhxzfs'),
                              i.get('dwdm'),
                              i.get('khyj'),
                              i.get('kuyh')))
        print(data_list)
        return data_list


def read_zhzhwh_smoke_data():
    """专户账户维护冒烟数据读取方法"""
    with open('../data_pool/zhzh/smoke/zhzhwh_smoke_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = list()  # 声明空列表
        for i in data:
            data_list.append((i.get('name'),
                              i.get('czqhdm'),
                              i.get('zhlbdm'),
                              i.get('xz'),
                              i.get('hsnr'),
                              i.get('splxdm'),
                              i.get('khyhxzfs'),
                              i.get('dwdm'),
                              i.get('khyj'),
                              i.get('khxkzhzh'),
                              i.get('account'),
                              i.get('khyh'),
                              i.get('czzhzhdm')
                              ))
        print(data_list)
        return data_list


def read_zhzhzx_smoke_data():
    """专户账户维护冒烟数据读取方法"""
    with open('../data_pool/zhzh/smoke/zhzhzx_smoke_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = list()  # 声明空列表
        for i in data:
            data_list.append((i.get('')))
        print(data_list)
        return data_list


if __name__ == '__main__':
    read_zhzhwh_smoke_data()