#-*- coding:utf-8 -*-
"""Train tickets query via command-line.

Usage:
    tickets [-gdctkz] <from> <to> <date>

Options:
    -h --help  帮助
    -g          高铁
    -d          动车
    -c          城际
    -t          特快
    -k          快车
    -z          直达

Example:
    tickets chengdu hefei 2016-10-20
"""

from docopt import docopt
from stations import stations
from TrainCollection import TrainCollection
import requests

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    #上面 """ """ 包含中的：
   #Usage:
   # test [-gdtkz] <from> <to> <date>
    #是必须要的 test 是可以随便写的，不影响解析

    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date, from_station, to_station)
    r = requests.get(url, verify = False)
    result_json  = r.json()
    if result_json['data']['flag']:
        rows = result_json['data']['datas']
        trains = TrainCollection(rows)
        trains.pretty_print()
    else:
        print(result_json['data']['message'])

if __name__ == '__main__':
      cli()
