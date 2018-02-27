#coding=utf-8
from qqbot import _bot as bot
import time

args = [
    # 用户名
  #  '--user', 'username',

    #  QQ 号码
    '--qq', '954950195',

    # 插件目录
  #  '--pluginPath', '/my/plugin/path',

    # 启动时自动加载的插件
    '--plugins', 'plugin1,plugin2,plugin3',

    # 启动方式：慢启动（获取全部联系人之后再启动）
    '--startAfterFetch',

    # 打印调试信息
    '--debug',
]

def list():
    """
    bot.List('buddy')        # 返回 好友列表：
    bot.List('buddy', 'jack')   # 返回名为 'jack' 的好友的列表：
    bot.List('group')              # 返回 群列表：
    bot.List('group', '机器人测试')  # 返回名为 “机器人测试” 的群的列表：
    g = bot.List('group', "456班")[0]   # g 是一个 Group 对象（群“456班”）
    bot.List(g)                         # 返回 群“456班” 的成员列表
    bot.List(g, 'card=jack')          # 返回 群“456班” 中名片为 “jack” 的成员列表
    bot.Update('buddy') # 更新 好友列表 ：
    bot.Update('group') # 更新 群列表 ：
    gl = bot.List('group', "456班")  # 更新 某个群的成员列表 ：
    if gl:
      g = gl[0]
      bot.Update(g)
    """
    l= bot.List('buddy')    # l 是一个 list 对象
    m=1
    for i in l :
        print i ,i.qq,i.uin,i.nick,i.mark,i.name
        print '成功获取第%s个好友------------------'%(m),'\n'
        m+=1
        time.sleep(0.5)


if __name__ == '__main__':
   bot.Login(args)
   list()
   bot.Run()