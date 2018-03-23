# coding:utf-8
# python一元回归分析实例：预测房子价格
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# 从csv文件中读取数据，分别为：X列表和对应的Y列表
def get_data(file_name):
    # 1. 用pandas读取csv
    data = pd.read_csv(file_name)

    # 2. 构造X列表和Y列表
    X_parameter = []
    Y_parameter = []
    for single_square_feet,single_price_value in zip(data['square_feet'],data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))

    return X_parameter,Y_parameter

# 线性回归分析，其中predict_square_feet为要预测的平方英尺数，函数返回对应的房价
def linear_model_main(X_parameter,Y_parameter,predict_square_feet):
    # 1. 构造回归对象
    regr = LinearRegression()
    regr.fit(X_parameter,Y_parameter)

    # 2. 获取预测值
    predict_outcome = regr.predict(predict_square_feet)

    # 3. 构造返回字典
    predictions = {}
    # 3.1 截距值
    predictions['intercept'] = regr.intercept_
    # 3.2 回归系数（斜率值）
    predictions['coefficient'] = regr.coef_
    # 3.3 预测值
    predictions['predict_value'] = predict_outcome

    return predictions

# 绘出图像
def show_linear_line(X_parameter,Y_parameter):
    # 1. 构造回归对象
    regr = LinearRegression()
    regr.fit(X_parameter,Y_parameter)

    # 2. 绘出已知数据散点图
    plt.scatter(X_parameter,Y_parameter,color = 'blue')

    # 3. 绘出预测直线
    plt.plot(X_parameter,regr.predict(X_parameter),color = 'red',linewidth = 4)

    plt.title('Predict the house price')
    plt.xlabel('square_feet')
    plt.ylabel('price')
    plt.show()

def main():
    # 1. 读取数据
    X,Y = get_data('./price_info.csv')

    # 2. 获取预测值，在这里我们预测700平方英尺大小的房子的房价
    predict_square_feet = 700
    result = linear_model_main(X,Y,predict_square_feet)
    for key,value in result.items():
        print '{0}:{1}'.format(key,value)

    # 3. 绘图
    show_linear_line(X,Y)

if __name__ == '__main__':
    main()