#-*- coding:utf-8 -*-
from prettytable import PrettyTable

class TrainCollection(object):
    """
解析列车信息
"""

    header = 'train from_station to_station start_time arrive_time duration first second softsleep hardsleep hardsit'.split()
 # 显示车次、出发/到达站、 出发/到达时间、历时、一等坐、二等坐、软卧、硬卧、硬座
    def __init__(self, rows):

 #获取车次运行的时间


        self.rows = rows
    def _get_duration(self, row):
        duration = row.get('lishi').replace(':', 'h') + 'm'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for row in self.rows:
            train = [
                row['station_train_code'],
                row['from_station_name'],
                row['to_station_name'],
                row['start_time'],
                row['arrive_time'],
                self._get_duration(row),
                row['zy_num'],
                row['ze_num'],
                row['rw_num'],
                row['yw_num'],
                row['yz_num']
            ]
            yield train

    def pretty_print(self):
        #"""
       # 数据已经获取到了，剩下的就是提取我们要的信息并将它显示出来。
       # `prettytable`这个库可以让我们它像MySQL数据库那样格式化显示数据。
      #  """

        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print pt
