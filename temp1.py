# coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
import os, datetime
from matplotlib.ticker import LinearLocator


def get_data():
    """
    获取Result.txt中数据
    :return: pandas.core.frame.DatFrame
    """
    path = r'C:\Users\Administrator\Desktop\Result.txt'
    df = pd.read_table(path, sep=' ')
    return df


def get_describe(df):
    """
    获取DataFrame汇总数据，包含最大值，最小值，平均值，标准偏差及其它IQR值
    :param df: pandas.core.frame.DatFrame
    :return: None
    """
    describe = df.describe()
    with open("result.csv", "w") as f:
        describe.to_csv(f)


def get_columns(df):
    """
    返回DataFrame除第一列之外所有的列名
    """
    return df.columns[1:]


def get_x_data(df):
    """
    返回DataFrame第一列值，也就是时间列
    """
    return df['time']


def get_y_data(args, df):
    """
    根据列名返回相应的列值。
    """
    if set(args) < set(get_columns(df)):
        columns = df.loc[:, args]
        return columns
    else:
        return ValueError


def get_picture(xlabels, ylabels, title):
    """
    绘图并保存
    """
    fig, ax = plt.subplots()
    # 设置x轴与下边框的间距，避免x轴部分数据被遮挡
    plt.subplots_adjust(bottom=0.26)
    # 20个刻度
    ax.xaxis.set_major_locator(LinearLocator(20))
    # ax.xaxis.set_major_locator(ticker.LinearLocator(numticks=None, presets=None)) 默认刻度
    plt.plot(xlabels, ylabels)
    # 设置x轴数据旋转角度
    plt.xticks(rotation=60)
    plt.legend(title)
    plt.title("phoenix")
    plt.grid()
    plt.savefig('%s.png' % '_'.join(title))
    # plt.show()


def set_save_path():
    """
    设置图片保存路径
    :return: None
    """
    str_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if os.name == "nt":
        os.makedirs(r"C:\Users\Administrator\Desktop\result\%s" % str_time)
        result_path = r"C:\Users\Administrator\Desktop\result\%s" % str_time
        os.chdir(result_path)
    if os.name == "posix":
        os.makedirs("/result/%s" % str_time)
        result_path = "/result/%s" % str_time
        os.chdir(result_path)


if __name__ == "__main__":
    df = get_data()
    set_save_path()
    x = get_x_data(df)
    print("共读取到%s列，分别为%s" % (len(get_columns(df)), get_columns(df)))
    while True:
        column = input('请输入需要画图的列名(求平均值请按w,退出请按q)：').split()
        y = get_y_data(column, df)
        if column[0] == "q":
            break
        if column[0] == "w":
            get_describe(df)
            continue
        if (y == ValueError) is True:
            print('输入列名不正确！！！')
            continue
        get_picture(x, y, column)
