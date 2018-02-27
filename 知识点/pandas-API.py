#coding=utf-8
from selenium import webdriver
from scrapy.selector import Selector


"""
http://www.usyiyi.cn/translate/Pandas_0j2/index.html

API参考
输入/输出
Pickling

read_pickle（path）	从指定的加载pickled pandas对象（或任何其他pickled对象）
文本文件

read_table（filepath_or_buffer [，sep，...]）	将一般分隔文件读入DataFrame
read_csv（filepath_or_buffer [，sep，...]）	将CSV（逗号分隔）文件读入DataFrame
read_fwf（filepath_or_buffer [，colspecs，width]）	将固定宽度格式的行的表读入DataFrame
read_msgpack（path_or_buf [，encoding，iterator]）	从指定的加载msgpack pandas对象
剪贴板

read_clipboard（\ * \ * kwargs）	从剪贴板读取文本并传递给read_table。
Excel

read_excel（io [，sheetname，headers，...]）	将Excel表读入pandas DataFrame
ExcelFile.parse（[sheetname，header，...]）	将指定的工作表解析到DataFrame中
JSON

read_json（[path_or_buf，orient，typ，dtype，...]）	将JSON字符串转换为pandas对象
json_normalize（data [，record_path，meta，...]）	将规范化的半结构化JSON数据转换为平面表格
HTML

read_html（io [，match，flavor，header，...]）	将HTML表格读入DataFrame对象的list。
HDFStore: PyTables (HDF5)

read_hdf（path_or_buf [，key]）	从商店读取，如果我们打开它关闭它
HDFStore.put（key，value [，format，append]）	将对象存储在HDFStore中
HDFStore.append（key，value [，format，...]）	附加到文件中的表。
HDFStore.get（key）	检索存储在文件中的pandas对象
HDFStore.select（键[，其中，start，stop，...]）	检索存储在文件中的pandas对象，可选地基于where
SAS

read_sas（filepath_or_buffer [，format，...]）	读取以XPORT或SAS7BDAT格式文件存储的SAS文件。
SQL

read_sql_table（table_name，con [，schema，...]）	将SQL数据库表读入DataFrame。
read_sql_query（sql，con [，index_col，...]）	将SQL查询读入DataFrame。
read_sql（sql，con [，index_col，...]）	将SQL查询或数据库表读入DataFrame。
Google BigQuery

read_gbq（query [，project_id，index_col，...]）	从Google BigQuery载入数据。
to_gbq（dataframe，destination_table，project_id）	将DataFrame写入Google BigQuery表格。
STATA

read_stata（filepath_or_buffer [，...]）	将Stata文件读入DataFrame
StataReader.data（\ * \ * kwargs）	DEPRECATED：从Stata文件读取观察结果，将它们转换为数据帧
StataReader.data_label()	返回Stata文件的数据标签
StataReader.value_labels()	返回一个dict，关联每个变量名称一个dict，关联
StataReader.variable_labels()	返回变量标签作为dict，关联每个变量名
StataWriter.write_file()
一般函数
数据操作

melt（frame [，id_vars，value_vars，var_name，...]）	将DataFrame从宽格式“不透明”为长格式，可选择离开
pivot（索引，列，值）	基于此DataFrame的3列生成'pivot'表。
pivot_table（data [，values，index，columns，...]）	创建一个电子表格样式的数据透视表作为DataFrame。
crosstab（索引，列[，values，rownames，...]）	计算两个（或更多）因子的简单交叉列表。
cut（x，bins [，right，labels，retbins，...]）	x的每个值所属的半开箱的返回索引。
qcut（x，q [，labels，retbins，precision]）	基于分位数的离散化函数。
merge（left，right [，how，on，left_on，...]	通过按列或索引执行数据库样式的连接操作来合并DataFrame对象。
merge_ordered（left，right [，on，left_on，...]）	执行与为时序数据等有序数据设计的可选填充/插值合并。
merge_asof（left，right [，on，left_on，...]）	执行asof合并。
concat（objs [，axis，join，join_axes，...]）	沿着特定轴连接pandas对象，沿着其他轴连接可选的设置逻辑。
get_dummies（data [，prefix，prefix_sep，...]）	将分类变量转换为虚拟/指示符变量
factorize（values [，sort，order，...]）	将输入值编码为枚举类型或类别变量
顶级缺失数据

isnull（obj）	检测缺失值（数值数组中的NaN，对象数组中的无/ NaN）
notnull（obj）	替换适用于对象数组的numpy.isfinite / -numpy.isnan。
顶级转换

to_numeric（arg [，errors，downcast]）	将参数转换为数字类型。
顶级处理datetimelike

to_datetime（\ * args，\ * \ * kwargs）	将参数转换为datetime。
to_timedelta（\ * args，\ * \ * kwargs）	将参数转换为timedelta
date_range（[start，end，periods，freq，tz，...]）	返回固定频率日期时间索引，将日（日历）作为默认值
bdate_range（[start，end，periods，freq，tz，...]）	返回固定频率datetime索引，以工作日为默认值
period_range（[start，end，periods，freq，name]）	返回固定频率日期时间索引，将日（日历）作为默认值
timedelta_range（[start，end，periods，freq，...]）	返回固定频率timedelta索引，以天为默认值
infer_freq（index [，warn]）	给定输入索引，推断最可能的频率。
顶级评估

eval（expr [，parser，engine，truediv，...]）	使用各种后端将Python表达式评估为字符串。
测试

test	使用鼻子运行模块的测试。
系列
构造

Series（[data，index，dtype，name，copy，...]）	带轴标签的一维参考线（包括时间序列）。
属性

轴
索引：轴标签
Series.values	返回系列为ndarray或ndarray样
Series.dtype	返回底层数据的dtype对象
Series.ftype	返回如果数据稀疏|密集
Series.shape	返回基础数据的形状的元组
Series.nbytes	返回底层数据中的字节数
Series.ndim	返回底层数据的维数，
Series.size	返回底层数据中的元素数量
Series.strides	返回基础数据的步幅
Series.itemsize	返回底层数据项的dtype的大小
Series.base	如果基础数据的内存是，则返回基础对象
Series.T	返回转置，这是通过定义self
Series.memory_usage（[index，deep]）	系列的内存使用情况
转换

Series.astype（dtype [，copy，raise_on_error]）	投射对象以输入numpy.dtype
Series.copy（[deep]）	复制此对象数据。
Series.isnull()	返回一个布尔大小相同的对象，指示值是否为null。
Series.notnull()	返回一个布尔大小相同的对象，指示这些值是否为空。
索引，迭代

Series.get（key [，default]）	从给定键的对象获取项目（DataFrame列，面板切片等）。
Series.at	基于快速标签的标量访问器
Series.iat	快速整数位置标量存取器。
Series.ix	主要是基于标签位置的索引器，具有整数位置后备。
Series.loc	纯标签位置索引器，用于按标签选择。
Series.iloc	纯粹基于整数位置的索引，用于按位置选择。
Series.__iter__()	提供对系列的值的迭代
Series.iteritems()	Lazily迭代（索引，值）元组
有关.at，.iat，.ix，.loc和.iloc，请参阅indexing documentation。

二进制运算符函数

Series.add（其他[，level，fill_value，axis]）	添加系列和其他，元素方式（二元运算符add）。
Series.sub（其他[，level，fill_value，axis]）	减法系数和其他，元素方式（二元运算符子）。
Series.mul（其他[，level，fill_value，axis]）	系列和其他元素乘法（二元算符mul）的乘法。
Series.div（其他[，level，fill_value，axis]）	浮点除法的系列和其他，元素（二进制运算符truediv）。
Series.truediv（other [，level，fill_value，axis]）	浮点除法的系列和其他，元素（二进制运算符truediv）。
Series.floordiv（其他[，level，fill_value，axis]）	系列的整数除法和其他，元素方式（二元运算符floordiv）。
Series.mod（其他[，level，fill_value，axis]）	系列模和其他，元素方式（二元运算符mod）。
Series.pow（其他[，level，fill_value，axis]）	系数和其他元指数（二元运算符pow）的指数幂。
Series.radd（其他[，level，fill_value，axis]）	添加系列和其他，元素方式（二元算符radd）。
Series.rsub（其他[，level，fill_value，axis]）	减法系列和其他，元素方式（二元运算符rsub）。
Series.rmul（其他[，level，fill_value，axis]）	系列和其他元素乘法（二元算符rmul）的乘法。
Series.rdiv（其他[，level，fill_value，axis]）	浮点除法的系列和其他，元素（二进制运算符rtruediv）。
Series.rtruediv（other [，level，fill_value，axis]）	浮点除法的系列和其他，元素（二进制运算符rtruediv）。
Series.rfloordiv（other [，level，fill_value，...]）	系列的整数除法和其他，元素方式（二元运算符rfloordiv）。
Series.rmod（其他[，level，fill_value，axis]）	系列模和其他，元素方式（二元算符rmod）。
Series.rpow（其他[，level，fill_value，axis]）	系列和其他元指数（二元运算符rpow）的指数幂。
Series.combine（other，func [，fill_value]）	对两个系列使用给定的函数执行元素二进制操作
Series.combine_first（other）	组合系列值，首先选择调用系列的值。
Series.round（[小数]）	将系列中的每个值四舍五入为给定的小数位数。
Series.lt（其他[，level，fill_value，axis]）	小于系列和其他，元素方式（二元运算符lt）。
Series.gt（其他[，level，fill_value，axis]）	大于系列和其他，元素方式（二元运算符gt）。
Series.le（其他[，level，fill_value，axis]）	小于或等于系列和其他，元素方式（二元运算符le）。
Series.ge（其他[，level，fill_value，axis]）	大于或等于系列和其他，元素方式（二元运算符ge）。
Series.ne（其他[，level，fill_value，axis]）	不等于系列和其他，元素方式（二元运算符ne）。
Series.eq（other [，level，fill_value，axis]）	等于系列和其他，元素方式（二元运算符eq）。
功能应用，GroupBy & Window

Series.apply（func [，convert_dtype，args]）	对Series的值调用函数。
Series.map（arg [，na_action]）	使用输入对应关系（可以是
Series.groupby（[by，axis，level，as_index，...]）	使用mapper的组系列（dict或key函数，将给定函数应用于组，将结果返回为系列）或通过一系列列。
Series.rolling（window [，min_periods，freq，...]）	提供滚动窗口计算。
Series.expanding（[min_periods，freq，...]）	提供扩展转换。
Series.ewm（[com，span，halflife，alpha，...]）	提供指数加权函数
计算/描述性统计

Series.abs()	返回具有绝对值的对象，仅适用于全部为数字的对象。
Series.all（[axis，bool_only，skipna，level]）	返回所有元素是否超过请求的轴的True
Series.any（[axis，bool_only，skipna，level]）	返回任何元素是否超过请求的轴为True
Series.autocorr（[lag]）	Lag-N自相关
Series.between（左，右[，含]）	返回boolean系列相当于left
Series.clip（[下，上，轴]）	修整输入阈值处的值。
Series.clip_lower（threshold [，axis]）	返回具有低于给定值的值的输入的副本。
Series.clip_upper（threshold [，axis]）	返回具有高于给定值的值的输入的副本。
Series.corr（other [，method，min_periods]）	与其他系列计算相关性，不包括缺少的值
Series.count（[level]）	返回系列中非NA /零值观察值的数量
Series.cov（其他[，min_periods]）	计算与系列的协方差，不包括缺少的值
Series.cummax（[axis，skipna]）	返回请求轴上的累积最大值。
Series.cummin（[axis，skipna]）	返回所请求轴上的累积最小值。
Series.cumprod（[axis，skipna]）	通过请求轴返回累积乘积。
Series.cumsum（[axis，skipna]）	通过请求轴返回累积和。
Series.describe（[percentiles，include，exclude]）	生成各种汇总统计，不包括NaN值。
Series.diff（[periods]）	对象的第一离散差异
Series.factorize（[sort，na_sentinel]）	将对象编码为枚举类型或类别变量
Series.kurt（[axis，skipna，level，numeric_only]）	使用Fisher的峰度定义（kurtosis of normal == 0.0）返回无偏的峰度超过请求的轴。
Series.mad（[axis，skipna，level]）	返回请求轴的值的平均绝对偏差
Series.max（[axis，skipna，level，numeric_only]）	此方法返回对象中值的最大值。
Series.mean（[axis，skipna，level，numeric_only]）	返回请求轴的值的平均值
Series.median（[axis，skipna，level，...]）	返回请求轴的值的中值
Series.min（[axis，skipna，level，numeric_only]）	此方法返回对象中值的最小值。
Series.mode()	返回数据集的模式。
Series.nlargest（\ * args，\ * \ * kwargs）	返回最大的n元素。
Series.nsmallest（\ * args，\ * \ * kwargs）	返回最小的n元素。
Series.pct_change（[periods，fill_method，...]）	给定周期数的百分比变化。
Series.prod（[axis，skipna，level，numeric_only]）	返回请求轴的值的乘积
Series.quantile（[q，interpolation]）	返回给定分位数的值，即一个数字。
Series.rank（[axis，method，numeric_only，...]）	沿轴计算数值数据（1到n）。
Series.sem（[axis，skipna，level，ddof，...]）	返回所要求轴的平均值的无偏差标准误差。
Series.skew([axis, skipna, level, numeric_only])	返回所请求轴的无偏斜
Series.std（[axis，skipna，level，ddof，...]）	返回样品标准偏差超过请求的轴。
Series.sum（[axis，skipna，level，numeric_only]）	返回请求轴的值的总和
Series.var（[axis，skipna，level，ddof，...]）	返回与请求轴无关的方差。
Series.unique()	返回对象中的唯一值的np.ndarray。
Series.nunique（[dropna]）	返回对象中唯一元素的数量。
Series.is_unique	如果对象中的值是唯一的，则返回布尔值
Series.is_monotonic	如果对象中的值为，则返回布尔值
Series.is_monotonic_increasing	如果对象中的值为，则返回布尔值
Series.is_monotonic_decreasing	如果对象中的值为，则返回布尔值
Series.value_counts（[normalize，sort，...]）	返回包含唯一值计数的对象。
重新索引/选择/标签操作

Series.align（其他[，join，axis，level，...]）	将它们的轴上的两个对象与
Series.drop（标签[，axis，level，inplace，...]）	返回请求轴中标签已删除的新对象。
Series.drop_duplicates（\ * args，\ * \ * kwargs）	删除重复值的返回系列
Series.duplicated（\ * args，\ * \ * kwargs）	返回boolean表示重复值的系列
Series.equals（other）	确定两个NDFrame对象是否包含相同的元素。
Series.first（offset）	用于基于日期偏移对时间序列数据的初始时间进行子集化的便利方法。
Series.head（[n]）	返回前n行
Series.idxmax（[axis，skipna]）	首次出现最大值的索引。
Series.idxmin（[axis，skipna]）	首次出现最小值的索引。
Series.isin（values）	返回布尔Series，显示Series中的每个元素是否完全包含在传递的values序列中。
Series.last（offset）	基于日期偏移对时间序列数据的最终周期子集化的便利方法。
Series.reindex（[index]）	使用可选填充逻辑将系列更新为新索引，将NA / NaN放在前一个索引中没有值的位置。
Series.reindex_like（other [，method，copy，...]）	将具有匹配索引的对象返回给我自己。
Series.rename（[index]）	改变轴输入功能。
Series.rename_axis（mapper [，axis，copy，inplace]）	使用输入函数或函数修改索引和/或列。
Series.reset_index（[level，drop，name，inplace]）	类似于pandas.DataFrame.reset_index()函数，请参见docstring。
Series.sample（[n，frac，replace，weights，...]）	从对象的轴返回项目的随机样本。
Series.select（crit [，axis]）	返回与轴标签匹配条件相对应的数据
Series.take（indices [，axis，convert，is_copy]）	return对应于请求的索引
Series.tail（[n]）	返回最后n行
Series.truncate（[before，after，axis，copy]）	在某个特定索引值之前和/或之后截断排序的NDFrame。
Series.where（cond [，other，inplace，axis，...]）	返回一个与self相同形状的对象，其对应的条目来自self，其中cond为True，否则为其他对象。
Series.mask（cond [，other，inplace，axis，...]）	返回一个与self相同形状的对象，并且其对应的条目来自self，其中cond是False，否则是来自其他。
缺少数据处理

Series.dropna（[axis，inplace]）	返回无null值的系列
Series.fillna（[value，method，axis，...]）	使用指定的方法填充NA / NaN值
Series.interpolate（[method，axis，limit，...]）	根据不同的方法内插值。
重新整形，排序

Series.argsort（[axis，kind，order]）	覆盖ndarray.argsort。
Series.reorder_levels（order）	使用输入顺序重新排列索引级别。
Series.sort_values（[axis，ascending，...]）	按任一轴的值排序
Series.sort_index（[axis，level，ascending，...]）	按标签（沿轴）对对象排序
Series.sortlevel（[level，ascending，...]）	按所选级别对MultiIndex进行排序。
Series.swaplevel（[i，j，copy]）	在MultiIndex中交换级别i和j
Series.unstack（[level，fill_value]）	Unstack，a.k.a.
Series.searchsorted（v [，side，sorter]）	查找要插入元素以维持顺序的索引。
组合/加入/合并

Series.append（to_append [，ignore_index，...]）	串联两个或更多系列。
Series.replace（[to_replace，value，inplace，...]）	将'to_replace'中给出的值替换为'value'。
Series.update（other）	使用通过的系列中的非NA值修改系列。
时间序列相关的

Series.asfreq（freq [，method，how，normalize]）	将TimeSeries转换为指定的频率。
Series.asof（其中[，subset]）	最后一行没有任何NaN被采取（或最后一行没有
Series.shift（[periods，freq，axis]）	使用可选的时间频率按期望的周期数切换索引
Series.first_valid_index()	返回第一个非NA /空值的标签
Series.last_valid_index()	返回最后一个非NA /空值的标签
Series.resample（rule [，how，axis，...]）	时间序列的频率转换和重采样的方便方法。
Series.tz_convert（tz [，axis，level，copy]）	将tz感知轴转换为目标时区。
Series.tz_localize（\ * args，\ * \ * kwargs）	将tz-naive TimeSeries本地化为目标时区。
Datetimelike属性

Series.dt可用于以datetimelike访问系列的值，并返回多个属性。这些可以像Series.dt.<property>一样访问。

日期时间属性

Series.dt.date	返回numpy数组的python datetime.date对象（即，没有时区信息的时间戳的日期部分）。
Series.dt.time	返回datetime.time的numpy数组。
Series.dt.year	datetime的年份
Series.dt.month	月份为1月= 1月，12月= 12月
Series.dt.day	datetime的日期
Series.dt.hour	datetime的小时数
Series.dt.minute	datetime的分钟
Series.dt.second	datetime的秒数
Series.dt.microsecond	datetime的微秒
Series.dt.nanosecond	datetime的纳秒
Series.dt.week	一年的周数
Series.dt.weekofyear	一年的周数
Series.dt.dayofweek	一周中的星期几，星期一= 0，星期六= 6
Series.dt.weekday	一周中的星期几，星期一= 0，星期六= 6
Series.dt.weekday_name	一周中的日期名称（例如：星期五）
Series.dt.dayofyear	一年的序数日
Series.dt.quarter	日期的四分之一
Series.dt.is_month_start	逻辑指示是否每月的第一天（由频率定义）
Series.dt.is_month_end	逻辑指示是否每月的最后一天（由频率定义）
Series.dt.is_quarter_start	逻辑指示季度的第一天（由频率定义）
Series.dt.is_quarter_end	逻辑指示季度的最后一天（由频率定义）
Series.dt.is_year_start	逻辑指示一年中的第一天（由频率定义）
Series.dt.is_year_end	逻辑指示一年中的最后一天（由频率定义）
Series.dt.is_leap_year	逻辑指示日期是否属于闰年
Series.dt.daysinmonth	每月的天数
Series.dt.days_in_month	每月的天数
Series.dt.tz
Series.dt.freq	获取/设置索引的频率
日期时间方法

Series.dt.to_period（\ * args，\ * \ * kwargs）	以特定频率投射到PeriodIndex
Series.dt.to_pydatetime()
Series.dt.tz_localize（\ * args，\ * \ * kwargs）	将tz-naive DatetimeIndex本地化到给定时区（使用
Series.dt.tz_convert（\ * args，\ * \ * kwargs）	将tz感知DatetimeIndex从一个时区转换到另一个（使用
Series.dt.normalize（\ * args，\ * \ * kwargs）	将DatetimeIndex与时间返回到午夜。
Series.dt.strftime（\ * args，\ * \ * kwargs）	返回由date_format指定的格式化字符串数组，该数组支持与python标准库相同的字符串格式。
Series.dt.round（\ * args，\ * \ * kwargs）	将索引循环到指定的频率
Series.dt.floor（\ * args，\ * \ * kwargs）	将索引落到指定的频率
Series.dt.ceil（\ * args，\ * \ * kwargs）	ceil索引到指定的频率
Timedelta属性

Series.dt.days	每个元素的天数。
Series.dt.seconds	每个元素的秒数（> = 0和小于1天）。
Series.dt.microseconds	每个元素的微秒数（> = 0和小于1秒）。
Series.dt.nanoseconds	每个元素的纳秒数（> = 0和小于1微秒）。
Series.dt.components	返回Timedeltas的组件（天，小时，分钟，秒，毫秒，微秒，纳秒）的数据帧。
Timedelta方法

Series.dt.to_pytimedelta()
Series.dt.total_seconds（\ * args，\ * \ * kwargs）	每个元素的总持续时间，单位为秒。
字符串处理

Series.str可用于以字符串的形式访问系列的值，并对其应用多种方法。这些可以像Series.str.<function/property>一样访问。

Series.str.capitalize()	转换要大写的系列/索引中的字符串。
Series.str.cat（[others，sep，na_rep]）	None
Series.str.center（width [，fillchar]）	使用附加字符填充系列/索引中字符串的左侧和右侧。
Series.str.contains（pat [，case，flags，na，...]）	返回boolean Series / array是否在Series / Index中的每个字符串中包含给定pattern / regex。
Series.str.count（pat [，flags]）	计算系列/索引的每个字符串中模式的出现次数。
Series.str.decode（encoding [，errors]）	使用指定的编码对Series / Index中的字符串进行解码。
Series.str.encode（encoding [，errors]）	使用指定的编码对Series / Index中的字符串进行编码。
Series.str.endswith（pat [，na]）	返回boolean表示系列/索引中的每个字符串是否以传递模式结束的系列。
Series.str.extract（pat [，flags，expand]）	对于系列中的每个主题字符串，从正则表达式pat的第一个匹配中提取组。
Series.str.extractall（pat [，flags]）	对于系列中的每个主题字符串，从正则表达式pat的所有匹配中提取组。
Series.str.find（sub [，start，end]）	返回系列/索引中每个字符串中的最低索引，其中子字符串完全包含在[start：end]之间。
Series.str.findall（pat [，flags]）	在Series / Index中查找所有出现的模式或正则表达式。
Series.str.get（i）	从系列/索引中的每个元素中的列表，元组或字符串中提取元素。
Series.str.index（sub [，start，end]）	返回每个字符串中的最低索引，其中子字符串完全包含在[start：end]之间。
Series.str.join（sep）	加入列表作为元素在Series / Index中包含传递的分隔符。
Series.str.len()	计算系列/索引中每个字符串的长度。
Series.str.ljust（width [，fillchar]）	使用附加字符填充系列/索引中字符串的右侧。
Series.str.lower()	将Series / Index中的字符串转换为小写。
Series.str.lstrip（[to_strip]）	从左侧的系列/索引中的每个字符串剥除空格（包括换行符）。
Series.str.match（pat [，case，flags，na，...]）	不推荐：使用传递的正则表达式在Series / Index中的每个字符串中查找组。
Series.str.normalize（form）	返回系列/索引中的字符串的Unicode正常形式。
Series.str.pad（width [，side，fillchar]）	在系列/索引中的填充字符串，在指定的一侧有一个附加字符。
Series.str.partition（[pat，expand]）	拆分第一次出现sep时的字符串，并返回包含分隔符之前的零件，分隔符本身和分隔符后面的零件的3个元素。
Series.str.repeat（重复）	按照指定的次数复制系列/索引中的每个字符串。
Series.str.replace（pat，repl [，n，case，flags]）	用一些其他字符串替换Series / Index中的pattern / regex的出现。
Series.str.rfind（sub [，start，end]）	返回系列/索引中每个字符串中的最高索引，其中子字符串完全包含在[start：end]之间。
Series.str.rindex（sub [，start，end]）	返回每个字符串中的最高索引，其中子字符串完全包含在[start：end]之间。
Series.str.rjust（width [，fillchar]）	使用附加字符填充系列/索引中字符串的左侧。
Series.str.rpartition（[pat，expand]）	拆分最后一次出现sep时的字符串，并返回包含分隔符之前的零件，分隔符本身和分隔符后面的零件的3个元素。
Series.str.rstrip（[to_strip]）	从右侧系列/索引中的每个字符串剥除空格（包括换行符）。
Series.str.slice（[start，stop，step]）	从Series / Index中的每个元素切割子串
Series.str.slice_replace（[start，stop，repl]）	将Series / Index中的每个字符串的切片替换为另一个字符串。
Series.str.split（[pat，n，expand]）	按照给定模式拆分系列/索引中的每个字符串（a la re.split），传播NA值。
Series.str.rsplit（[pat，n，expand]）	使用给定的分隔符字符串将系列/索引中的每个字符串拆分，从字符串的结尾开始，并向前面进行。
Series.str.startswith（pat [，na]）	返回布尔系列/ array指示Series / Index中的每个字符串是否以传递模式开头。
Series.str.strip（[to_strip]）	从左/右边的系列/索引中的每个字符串剥离空格（包括换行符）。
Series.str.swapcase()	转换要交换的系列/索引中的字符串。
Series.str.title()	将系列/索引中的字符串转换为titlecase。
Series.str.translate（table [，deletechars]）	通过给定的映射表映射字符串中的所有字符。
Series.str.upper()	将Series / Index中的字符串转换为大写。
Series.str.wrap（width，\ * \ * kwargs）	在要在长度小于给定宽度的段落中格式化的系列/索引中包装长字符串。
Series.str.zfill（width）	填充系列/索引中的字符串左侧为0。
Series.str.isalnum()	检查系列/索引中每个字符串中的所有字符是否为字母数字。
Series.str.isalpha()	检查系列/索引中每个字符串中的所有字符是否为字母。
Series.str.isdigit()	检查系列/索引中每个字符串中的所有字符是否为数字。
Series.str.isspace()	检查Series / Index中每个字符串中的所有字符是否为空格。
Series.str.islower()	检查系列/索引中每个字符串中的所有字符是否为小写。
Series.str.isupper()	检查系列/索引中每个字符串中的所有字符是否为大写。
Series.str.istitle()	检查系列/索引中每个字符串中的所有字符是否都是titlecase。
Series.str.isnumeric()	检查系列/索引中每个字符串中的所有字符是否都是数字。
Series.str.isdecimal()	检查系列/索引中每个字符串中的所有字符是否为十进制。
Series.str.get_dummies（[sep]）	将系列中的每个字符串拆分为sep，并返回一个虚拟/指示符变量框架。
分类

如果系列属于category，则Series.cat可用于更改分类数据。此存取器类似于Series.dt或Series.str，并具有以下可用的方法和属性：

Series.cat.categories	这个分类的类别。
Series.cat.ordered	获取有序属性
Series.cat.codes
Series.cat.rename_categories（\ * args，\ * \ * kwargs）	重命名类别。
Series.cat.reorder_categories（\ * args，\ * \ * kwargs）	重新排序在new_categories中指定的类别。
Series.cat.add_categories（\ * args，\ * \ * kwargs）	添加新类别。
Series.cat.remove_categories（\ * args，\ * \ * kwargs）	删除指定的类别。
Series.cat.remove_unused_categories（\ * args，...）	删除未使用的类别。
Series.cat.set_categories（\ * args，\ * \ * kwargs）	将类别设置为指定的new_categories。
Series.cat.as_ordered（\ * args，\ * \ * kwargs）	设置要排序的分类
Series.cat.as_unordered（\ * args，\ * \ * kwargs）	将分类设置为无序
要创建一系列dtype category，请使用cat = s.astype（“category”） 。

以下两个Categorical构造函数被视为API，但只应在添加排序信息时使用，或在创建分类数据时需要特殊类别：

Categorical（值[，类别，有序，...]）	表示经典R / S加方式的分类变量
Categorical.from_codes（codes，categories [，...]）	从代码和类别数组创建分类类型。
np.asarray(categorical)通过实现数组接口工作。请注意，这会将分类转换回numpy数组，因此级别和顺序信息不会保留！

Categorical.__array__（[dtype]）	numpy数组接口。
绘制

Series.plot是Series.plot.<kind>形式的特定绘图方法的可调用方法和命名空间属性。

Series.plot（[kind，ax，figsize，....]）	系列绘图存取器和方法
Series.plot.area（\ * \ * kwds）	面积图
Series.plot.bar（\ * \ * kwds）	垂直条图
Series.plot.barh（\ * \ * kwds）	水平条图
Series.plot.box（\ * \ * kwds）	箱形图
Series.plot.density（\ * \ * kwds）	核密度估计图
Series.plot.hist（[bins]）	直方图
Series.plot.kde（\ * \ * kwds）	核密度估计图
Series.plot.line（\ * \ * kwds）	线图
Series.plot.pie（\ * \ * kwds）	饼形图
Series.hist（[by，ax，grid，xlabelsize，...]）	使用matplotlib绘制输入序列的直方图
序列化/ IO /转换

Series.from_csv（path [，sep，parse_dates，...]）	读取CSV文件（DISCOURAGED，请改用pandas.read_csv()）。
Series.to_pickle（path）	Pickle（序列化）对象到输入文件路径。
Series.to_csv（[path，index，sep，na_rep，...]）	将系列写入逗号分隔值（csv）文件
Series.to_dict()	将系列转换为{label - > value}
Series.to_frame（[name]）	将系列转换为DataFrame
Series.to_xarray()	从pandas对象返回一个xarray对象。
Series.to_hdf（path_or_buf，key，\ * \ * kwargs）	使用HDFStore将包含的数据写入HDF5文件。
Series.to_sql（name，con [，flavor，schema，...]）	将存储在DataFrame中的记录写入SQL数据库。
Series.to_msgpack（[path_or_buf，encoding]）	msgpack（serialize）对象到输入文件路径
Series.to_json（[path_or_buf，orient，...]）	将对象转换为JSON字符串。
Series.to_sparse（[kind，fill_value]）	将系列转换为稀疏系列
Series.to_dense()	返回NDFrame的密集表示（而不是稀疏）
Series.to_string（[buf，na_rep，...]）	呈现系列的字符串表示形式
Series.to_clipboard（[excel，sep]）	尝试将对象的文本表示写入系统剪贴板例如，可以将其粘贴到Excel中。
稀疏方法

SparseSeries.to_coo（[row_levels，...]）	从带有MultiIndex的SparseSeries创建scipy.sparse.coo_matrix。
SparseSeries.from_coo（A [，dense_index]）	从scipy.sparse.coo_matrix创建SparseSeries。
数据帧
构造

DataFrame（[data，index，columns，dtype，copy]）	二维大小可变的，潜在异质的表格数据结构，带有标记的轴（行和列）。
属性和底层数据

轴

index：行标签
列：列标签
DataFrame.as_matrix（[columns]）	将帧转换为其Numpy数组表示。
DataFrame.dtypes	返回此对象中的dtype。
DataFrame.ftypes	返回此对象中的ftypes（稀疏/密集和dtype的指示）。
DataFrame.get_dtype_counts()	返回此对象中的dtypes的计数。
DataFrame.get_ftype_counts()	返回此对象中的ftypes的计数。
DataFrame.select_dtypes（[include，exclude]）	返回基于其dtype包含/排除列的DataFrame子集。
DataFrame.values	NDFrame的块状表示
DataFrame.axes	返回具有行轴标签和列轴标签作为唯一成员的列表。
DataFrame.ndim	轴数/阵列尺寸
DataFrame.size	NDFrame中的元素数
DataFrame.shape	返回一个表示DataFrame的维度的元组。
DataFrame.memory_usage（[index，deep]）	DataFrame列的内存使用情况。
转换

DataFrame.astype（dtype [，copy，raise_on_error]）	投射对象以输入numpy.dtype
DataFrame.convert_objects（[convert_dates，...]）	已弃用。
DataFrame.copy（[deep]）	复制此对象数据。
DataFrame.isnull()	返回一个布尔大小相同的对象，指示值是否为null。
DataFrame.notnull()	返回一个布尔大小相同的对象，指示这些值是否为空。
索引，迭代

DataFrame.head（[n]）	返回前n行
DataFrame.at	基于快速标签的标量访问器
DataFrame.iat	快速整数位置标量存取器。
DataFrame.ix	主要是基于标签位置的索引器，具有整数位置后备。
DataFrame.loc	纯标签位置索引器，用于按标签选择。
DataFrame.iloc	纯粹基于整数位置的索引，用于按位置选择。
DataFrame.insert（loc，column，value [，...]	在指定位置将列插入DataFrame。
DataFrame.__iter__()	在信息轴上迭代
DataFrame.iteritems()	迭代器结束（列名，系列）对。
DataFrame.iterrows()	将DataFrame行重复为（索引，系列）对。
DataFrame.itertuples（[index，name]）	将DataFrame行迭代为namedtuples，索引值作为元组的第一个元素。
DataFrame.lookup（row_labels，col_labels）	DataFrame基于标签的“花式索引”功能。
DataFrame.pop（item）	返回项目并从框架中删除。
DataFrame.tail（[n]）	返回最后n行
DataFrame.xs（键[，axis，level，drop_level]）	从Series / DataFrame返回横截面（行或列）。
DataFrame.isin（values）	返回布尔值DataFrame，显示DataFrame中的每个元素是否包含在值中。
DataFrame.where（cond [，other，inplace，...]）	返回一个与self相同形状的对象，其对应的条目来自self，其中cond为True，否则为其他对象。
DataFrame.mask（cond [，other，inplace，axis，...]）	返回一个与self相同形状的对象，并且其对应的条目来自self，其中cond是False，否则是来自其他。
DataFrame.query（expr [，inplace]）	使用布尔表达式查询框架的列。
有关.at，.iat，.ix，.loc和.iloc，请参阅indexing documentation。

二进制运算符函数

DataFrame.add（其他[，axis，level，fill_value]）	添加数据帧和其他，元素方式（二进制运算符add）。
DataFrame.sub（其他[，axis，level，fill_value]）	减数据帧和其他，元素方式（二元运算符子）。
DataFrame.mul（其他[，axis，level，fill_value]）	数据帧和其他元素乘法（二元运算符mul）的乘法。
DataFrame.div（其他[，axis，level，fill_value]）	数据帧和其他元素浮点划分（二元运算符truediv）。
DataFrame.truediv（其他[，axis，level，...]）	数据帧和其他元素浮点划分（二元运算符truediv）。
DataFrame.floordiv（其他[，axis，level，...]）	数据帧和其他元素整数（二进制运算符floordiv）的整数除法。
DataFrame.mod（其他[，axis，level，fill_value]）	数据帧和其他元素模式（二元运算符mod）。
DataFrame.pow（其他[，axis，level，fill_value]）	数据帧和其他元指数的幂指数（二元运算符pow）。
DataFrame.radd（其他[，axis，level，fill_value]）	添加数据帧和其他，元素方式（二元运算符radd）。
DataFrame.rsub（其他[，axis，level，fill_value]）	减数据帧和其他，元素方式（二元运算符rsub）。
DataFrame.rmul（其他[，axis，level，fill_value]）	数据帧和其他元素乘法（二元运算符rmul）的乘法。
DataFrame.rdiv（其他[，axis，level，fill_value]）	数据帧的浮动划分和其他，元素方式（二元运算符rtruediv）。
DataFrame.rtruediv（其他[，axis，level，...]）	数据帧的浮动划分和其他，元素方式（二元运算符rtruediv）。
DataFrame.rfloordiv（其他[，axis，level，...]）	数据帧和其他元素整数（二进制运算符rfloordiv）的整数除法。
DataFrame.rmod（其他[，axis，level，fill_value]）	数据帧模式和其他，元素方式（二元算符rmod）。
DataFrame.rpow（其他[，axis，level，fill_value]）	数据帧和其他元指数的幂指数（二元运算符rpow）。
DataFrame.lt（其他[，axis，level]）	用于灵活比较方法的包装器
DataFrame.gt（其他[，axis，level]）	用于灵活比较方法的包装器gt
DataFrame.le（其他[，轴，级别]）	用于灵活比较方法的包装器
DataFrame.ge（其他[，axis，level]）	用于灵活比较方法的包装器
DataFrame.ne（其他[，axis，level]）	用于灵活比较方法的包装器
DataFrame.eq（其他[，axis，level]）	用于灵活比较方法的包装器
DataFrame.combine（other，func [，fill_value，...]）	添加两个DataFrame对象，不传播NaN值，因此如果为a
DataFrame.combine_first（other）	在调用方法的帧中组合两个DataFrame对象和默认非空值。
功能应用，Group By& Window

DataFrame.apply（func [，axis，broadcast，...]）	沿DataFrame的输入轴应用函数。
DataFrame.applymap（func）	将一个函数应用到要单元操作的DataFrame，即
DataFrame.groupby（[by，axis，level，...]）	使用mapper的组系列（dict或key函数，将给定函数应用于组，将结果返回为系列）或通过一系列列。
DataFrame.rolling（window [，min_periods，...]）	提供滚动窗口计算。
DataFrame.expanding（[min_periods，freq，...]）	提供扩展转换。
DataFrame.ewm（[com，span，halflife，alpha，...]）	提供指数加权函数
计算/描述性统计

DataFrame.abs()	返回具有绝对值的对象，仅适用于全部为数字的对象。
DataFrame.all（[axis，bool_only，skipna，level]）	返回所有元素是否超过请求的轴的True
DataFrame.any（[axis，bool_only，skipna，level]）	返回任何元素是否超过请求的轴为True
DataFrame.clip（[lower，upper，axis]）	修整输入阈值处的值。
DataFrame.clip_lower（threshold [，axis]）	返回具有低于给定值的值的输入的副本。
DataFrame.clip_upper（threshold [，axis]）	返回具有高于给定值的值的输入的副本。
DataFrame.corr（[method，min_periods]）	计算列的成对相关性，不包括NA /空值
DataFrame.corrwith（other [，axis，drop]）	计算两个DataFrame对象的行或列之间的成对相关性。
DataFrame.count（[axis，level，numeric_only]）	返回具有在所请求轴上的非NA /零值观测数的返回系列。
DataFrame.cov（[min_periods]）	计算列的成对协方差，不包括NA /空值
DataFrame.cummax（[axis，skipna]）	返回请求轴上的累积最大值。
DataFrame.cummin（[axis，skipna]）	返回所请求轴上的累积最小值。
DataFrame.cumprod（[axis，skipna]）	通过请求轴返回累积乘积。
DataFrame.cumsum（[axis，skipna]）	通过请求轴返回累积和。
DataFrame.describe（[percentiles，include，...]）	生成各种汇总统计，不包括NaN值。
DataFrame.diff（[periods，axis]）	对象的第一离散差异
DataFrame.eval（expr [，inplace]）	在调用DataFrame实例的上下文中评估表达式。
DataFrame.kurt（[axis，skipna，level，...]）	使用Fisher的峰度定义（kurtosis of normal == 0.0）返回无偏的峰度超过请求的轴。
DataFrame.mad（[axis，skipna，level]）	返回请求轴的值的平均绝对偏差
DataFrame.max（[axis，skipna，level，...]）	此方法返回对象中值的最大值。
DataFrame.mean（[axis，skipna，level，...]）	返回请求轴的值的平均值
DataFrame.median（[axis，skipna，level，...]）	返回请求轴的值的中值
DataFrame.min（[axis，skipna，level，...]）	此方法返回对象中值的最小值。
DataFrame.mode（[axis，numeric_only]）	获取所选轴上每个元素的模式。
DataFrame.pct_change（[periods，fill_method，...]）	给定周期数的百分比变化。
DataFrame.prod（[axis，skipna，level，...]）	返回请求轴的值的乘积
DataFrame.quantile（[q，axis，numeric_only，...]）	在给定分位数的返回值超过请求的轴，一个数字。
DataFrame.rank（[axis，method，numeric_only，...]）	沿轴计算数值数据（1到n）。
DataFrame.round（[小数]）	将DataFrame舍入到可变小数位数。
DataFrame.sem（[axis，skipna，level，ddof，...]）	返回所要求轴的平均值的无偏差标准误差。
DataFrame.skew（[axis，skipna，level，...]）	返回所请求轴的无偏斜
DataFrame.sum（[axis，skipna，level，...]）	返回请求轴的值的总和
DataFrame.std（[axis，skipna，level，ddof，...]）	返回样品标准偏差超过请求的轴。
DataFrame.var（[axis，skipna，level，ddof，...]）	返回与请求轴无关的方差。
重新索引/选择/标签操作

DataFrame.add_prefix（prefix）	将前缀字符串与面板项名称连接。
DataFrame.add_suffix（suffix）	将后缀字符串与面板项名称连接。
DataFrame.align（其他[，join，axis，level，...]）	将它们的轴上的两个对象与
DataFrame.drop（标签[，axis，level，...]）	返回请求轴中标签已删除的新对象。
DataFrame.drop_duplicates（\ * args，\ * \ * kwargs）	返回已删除重复行的DataFrame（仅可选）
DataFrame.duplicated（\ * args，\ * \ * kwargs）	返回boolean表示重复行的系列，仅可选
DataFrame.equals（other）	确定两个NDFrame对象是否包含相同的元素。
DataFrame.filter（[items，like，regex，axis]）	子集根据指定索引中的标签的数据帧的行或列。
DataFrame.first（offset）	用于基于日期偏移对时间序列数据的初始时间进行子集化的便利方法。
DataFrame.head（[n]）	返回前n行
DataFrame.idxmax（[axis，skipna]）	在请求的轴上的第一次出现的最大值的返回索引。
DataFrame.idxmin（[axis，skipna]）	请求轴上的第一次出现的最小值的返回索引。
DataFrame.last（offset）	基于日期偏移对时间序列数据的最终周期子集化的便利方法。
DataFrame.reindex（[index，columns]）	使用可选填充逻辑将DataFrame与新索引一致，将NA / NaN放在前一个索引中没有值的位置。
DataFrame.reindex_axis（标签[，axis，...]）	使用可选填充逻辑将输入对象与新索引一致，将NA / NaN放在前一个索引中没有值的位置。
DataFrame.reindex_like（other [，method，...]）	将具有匹配索引的对象返回给我自己。
DataFrame.rename（[index，columns]）	改变轴输入功能。
DataFrame.rename_axis（mapper [，axis，copy，...]）	使用输入函数或函数修改索引和/或列。
DataFrame.reset_index（[level，drop，...]）	对于具有多级索引的DataFrame，在索引名称下的列中返回带有标签信息的新DataFrame，默认为“level_0”，“level_1”等。
DataFrame.sample（[n，frac，replace，...]）	从对象的轴返回项目的随机样本。
DataFrame.select（crit [，axis]）	返回与轴标签匹配条件相对应的数据
DataFrame.set_index（keys [，drop，append，...]）	使用一个或多个现有列设置DataFrame索引（行标签）。
DataFrame.tail（[n]）	返回最后n行
DataFrame.take（indices [，axis，convert，is_copy]）	类似于ndarray.take
DataFrame.truncate（[before，after，axis，copy]）	在某个特定索引值之前和/或之后截断排序的NDFrame。
缺失数据处理

DataFrame.dropna（[axis，how，thresh，...]）	返回具有给定轴上的标签的对象在哪里交替地被省略
DataFrame.fillna（[value，method，axis，...]）	使用指定的方法填充NA / NaN值
DataFrame.replace（[to_replace，value，...]）	将'to_replace'中给出的值替换为'value'。
形状变换，排序，转置

DataFrame.pivot（[index，columns，values]）	基于列值对数据进行形状变换（生成“透视”表）。
DataFrame.reorder_levels（order [，axis]）	使用输入顺序重新排列索引级别。
DataFrame.sort_values（由[，axis，ascending，...]）	按任一轴的值排序
DataFrame.sort_index（[axis，level，...]）	按标签（沿轴）对对象排序
DataFrame.sortlevel（[level，axis，...]）	按所选轴和主要级别对多级索引进行排序。
DataFrame.nlargest（n，columns [，keep]）	获取按列的n最大值排序的DataFrame的行。
DataFrame.nsmallest（n，columns [，keep]）	获取按列的n最小值排序的DataFrame的行。
DataFrame.swaplevel（[i，j，axis]）	在特定轴上的多索引中交换级别i和j
DataFrame.stack（[level，dropna]）	透视（可能是层次化的）列标签的级别，返回具有层次索引和新的最内层行标签的DataFrame（或者在具有单个列标签的对象的情况下为Series）。
DataFrame.unstack（[level，fill_value]）	透视（必要为分层）索引标签的级别，返回具有新级别列标签的DataFrame，其中最内层级由枢轴索引标签组成。
DataFrame.T	转置索引和列
DataFrame.to_panel()	将长（堆叠）格式（DataFrame）转换为宽（3D，面板）格式。
DataFrame.to_xarray()	从pandas对象返回一个xarray对象。
DataFrame.transpose（\ * args，\ * \ * kwargs）	转置索引和列
组合/加入/合并

DataFrame.append（other [，ignore_index，...]）	将其他的行追加到此框架的结尾，返回一个新对象。
DataFrame.assign（\ * \ * kwargs）	将新列分配给DataFrame，返回除了新对象之外的所有原始列的新对象（副本）。
DataFrame.join（other [，on，how，lsuffix，...]）	与索引或键列上的其他DataFrame连接列。
DataFrame.merge（右[，how，on，left_on，...]）	通过按列或索引执行数据库样式的连接操作来合并DataFrame对象。
DataFrame.update（其他[，join，overwrite，...]）	使用来自传递的DataFrame的非NA值修改DataFrame。
时间序列相关的

DataFrame.asfreq（freq [，method，how，normalize]）	将TimeSeries转换为指定的频率。
DataFrame.asof（其中[，subset]）	最后一行没有任何NaN被采取（或最后一行没有
DataFrame.shift（[periods，freq，axis]）	使用可选的时间频率按期望的周期数切换索引
DataFrame.first_valid_index()	返回第一个非NA /空值的标签
DataFrame.last_valid_index()	返回最后一个非NA /空值的标签
DataFrame.resample（rule [，how，axis，...]）	时间序列的频率转换和重采样的方便方法。
DataFrame.to_period（[freq，axis，copy]）	将DataFrame从DatetimeIndex转换为期间索引
DataFrame.to_timestamp（[freq，how，axis，copy]）	在期间的开始，投放到时间戳的DatetimeIndex
DataFrame.tz_convert（tz [，axis，level，copy]）	将tz感知轴转换为目标时区。
DataFrame.tz_localize（\ * args，\ * \ * kwargs）	将tz-naive TimeSeries本地化为目标时区。
绘图

DataFrame.plot是用于DataFrame.plot.<kind>形式的特定绘图方法的可调用方法和命名空间属性。

DataFrame.plot（[x，y，kind，ax，....]）	DataFrame绘制访问器和方法
DataFrame.plot.area（[x，y]）	面积图
DataFrame.plot.bar（[x，y]）	垂直条图
DataFrame.plot.barh（[x，y]）	水平条图
DataFrame.plot.box（[by]）	箱形图
DataFrame.plot.density（\ * \ * kwds）	核密度估计图
DataFrame.plot.hexbin（x，y [，C，...]）	Hexbin图
DataFrame.plot.hist（[by，bins]）	直方图
DataFrame.plot.kde（\ * \ * kwds）	核密度估计图
DataFrame.plot.line（[x，y]）	线图
DataFrame.plot.pie（[y]）	饼形图
DataFrame.plot.scatter（x，y [，s，c]）	散点图
DataFrame.boxplot（[column，by，ax，...]）	从DataFrame列创建箱绘图，可选择按一些列或分组
DataFrame.hist（data [，column，by，grid，...]）	使用matplotlib / pylab绘制DataFrame系列的直方图。
序列化/ IO /转换

DataFrame.from_csv（path [，header，sep，...]）	读取CSV文件（DISCOURAGED，请改用pandas.read_csv()）。
DataFrame.from_dict（data [，orient，dtype]）	从类array或dicts的dict构造DataFrame
DataFrame.from_items（items [，columns，orient]）	将（键，值）对转换为DataFrame。
DataFrame.from_records（data [，index，...]）	将结构化或记录ndarray转换为DataFrame
DataFrame.info（[verbose，buf，max_cols，...]）	DataFrame的简明摘要。
DataFrame.to_pickle（path）	Pickle（序列化）对象到输入文件路径。
DataFrame.to_csv（[path_or_buf，sep，na_rep，...]）	将DataFrame写入逗号分隔值（csv）文件
DataFrame.to_hdf（path_or_buf，key，\ * \ * kwargs）	使用HDFStore将包含的数据写入HDF5文件。
DataFrame.to_sql（name，con [，flavor，...]）	将存储在DataFrame中的记录写入SQL数据库。
DataFrame.to_dict（[orient]）	将DataFrame转换成字典。
DataFrame.to_excel（excel_writer [，...]）	将DataFrame写入excel表
DataFrame.to_json（[path_or_buf，orient，...]）	将对象转换为JSON字符串。
DataFrame.to_html（[buf，columns，col_space，...]）	将DataFrame呈现为HTML表格。
DataFrame.to_latex（[buf，columns，...]）	将DataFrame呈现为表格环境表。
DataFrame.to_stata（fname [，convert_dates，...]）	从数组类对象中写入Stata二进制dta文件的类
DataFrame.to_msgpack（[path_or_buf，encoding]）	msgpack（serialize）对象到输入文件路径
DataFrame.to_gbq（destination_table，project_id）	将DataFrame写入Google BigQuery表格。
DataFrame.to_records（[index，convert_datetime64]）	将DataFrame转换为记录数组。
DataFrame.to_sparse（[fill_value，kind]）	转换为SparseDataFrame
DataFrame.to_dense()	返回NDFrame的密集表示（而不是稀疏）
DataFrame.to_string（[buf，columns，...]）	将DataFrame呈现为控制台友好的表格输出。
DataFrame.to_clipboard（[excel，sep]）	尝试将对象的文本表示写入系统剪贴板例如，可以将其粘贴到Excel中。
面板
构造

Panel（[data，items，major_axis，minor_axis，...]）	表示宽格式面板数据，存储为3维数组
属性和底层数据

轴

项：axis 0；每个项目对应于其中包含的DataFrame
major_axis：轴1；每个DataFrames的索引（行）
minor_axis：axis 2；每个DataFrames的列
Panel.values	NDFrame的块状表示
Panel.axes	返回内部NDFrame的索引标签
Panel.ndim	轴数/阵列尺寸
Panel.size	NDFrame中的元素数
Panel.shape	返回轴维度的元组
Panel.dtypes	返回此对象中的dtype。
Panel.ftypes	返回此对象中的ftypes（稀疏/密集和dtype的指示）。
Panel.get_dtype_counts()	返回此对象中的dtypes的计数。
Panel.get_ftype_counts()	返回此对象中的ftypes的计数。
转换

Panel.astype（dtype [，copy，raise_on_error]）	投射对象以输入numpy.dtype
Panel.copy（[deep]）	复制此对象数据。
Panel.isnull()	返回一个布尔大小相同的对象，指示值是否为null。
Panel.notnull()	返回一个布尔大小相同的对象，指示这些值是否为空。
获取与设置

Panel.get_value（\ * args，\ * \ * kwargs）	在（项目，主要，次要）位置快速检索单个值
Panel.set_value（\ * args，\ * \ * kwargs）	在（项目，主要，次要）位置快速设置单一值
索引，迭代，切片

Panel.at	基于快速标签的标量访问器
Panel.iat	快速整数位置标量存取器。
Panel.ix	主要是基于标签位置的索引器，具有整数位置后备。
Panel.loc	纯标签位置索引器，用于按标签选择。
Panel.iloc	纯粹基于整数位置的索引，用于按位置选择。
Panel.__iter__()	在信息轴上迭代
Panel.iteritems()	在信息轴上迭代（标签，值）
Panel.pop（item）	返回项目并从框架中删除。
Panel.xs（键[，axis]）	沿所选轴返回面板
Panel.major_xs（key）	面板沿主轴返回切片
Panel.minor_xs（key）	沿着短轴返回面板
有关.at，.iat，.ix，.loc和.iloc，请参阅indexing documentation。

二进制运算符函数

Panel.add（其他[，axis]）	添加系列和其他，元素方式（二元运算符add）。
Panel.sub（其他[，轴]）	减法系数和其他，元素方式（二元运算符子）。
Panel.mul（其他[，axis]）	系列和其他元素乘法（二元算符mul）的乘法。
Panel.div（其他[，axis]）	浮点除法的系列和其他，元素（二进制运算符truediv）。
Panel.truediv（other [，axis]）	浮点除法的系列和其他，元素（二进制运算符truediv）。
Panel.floordiv（其他[，axis]）	系列的整数除法和其他，元素方式（二元运算符floordiv）。
Panel.mod（其他[，axis]）	系列模和其他，元素方式（二元运算符mod）。
Panel.pow（其他[，axis]）	系数和其他元指数（二元运算符pow）的指数幂。
Panel.radd（其他[，axis]）	添加系列和其他，元素方式（二元算符radd）。
Panel.rsub（其他[，axis]）	减法系列和其他，元素方式（二元运算符rsub）。
Panel.rmul（其他[，axis]）	系列和其他元素乘法（二元算符rmul）的乘法。
Panel.rdiv（其他[，axis]）	浮点除法的系列和其他，元素（二进制运算符rtruediv）。
Panel.rtruediv（其他[，axis]）	浮点除法的系列和其他，元素（二进制运算符rtruediv）。
Panel.rfloordiv（其他[，轴]）	系列的整数除法和其他，元素方式（二元运算符rfloordiv）。
Panel.rmod（其他[，轴]）	系列模和其他，元素方式（二元算符rmod）。
Panel.rpow（其他[，axis]）	系列和其他元指数（二元运算符rpow）的指数幂。
Panel.lt（其他[，axis]）	比较方法的包装
Panel.gt（其他[，axis]）	比较方法的包装器gt
Panel.le（其他[，axis]）	比较方法le的包装
Panel.ge（其他[，axis]）	比较方法包装
Panel.ne（其他[，axis]）	比较方法ne
Panel.eq（其他[，axis]）	比较方法的包装器
功能应用程序，GroupBy

Panel.apply（func [，axis]）	沿面板的轴（或轴）应用功能
Panel.groupby（function [，axis]）	给定轴上的数据组，返回GroupBy对象
计算/描述性统计

Panel.abs()	返回具有绝对值的对象，仅适用于全部为数字的对象。
Panel.clip（[下，上，轴]）	修整输入阈值处的值。
Panel.clip_lower（threshold [，axis]）	返回具有低于给定值的值的输入的副本。
Panel.clip_upper（threshold [，axis]）	返回具有高于给定值的值的输入的副本。
Panel.count（[axis]）	通过请求的轴返回观测值数。
Panel.cummax（[axis，skipna]）	返回请求轴上的累积最大值。
Panel.cummin（[axis，skipna]）	返回所请求轴上的累积最小值。
Panel.cumprod（[axis，skipna]）	通过请求轴返回累积乘积。
Panel.cumsum（[axis，skipna]）	通过请求轴返回累积和。
Panel.max（[axis，skipna，level，numeric_only]）	此方法返回对象中值的最大值。
Panel.mean（[axis，skipna，level，numeric_only]）	返回请求轴的值的平均值
Panel.median（[axis，skipna，level，numeric_only]）	返回请求轴的值的中值
Panel.min（[axis，skipna，level，numeric_only]）	此方法返回对象中值的最小值。
Panel.pct_change（[periods，fill_method，...]）	给定周期数的百分比变化。
Panel.prod（[axis，skipna，level，numeric_only]）	返回请求轴的值的乘积
Panel.sem（[axis，skipna，level，ddof，...]）	返回所要求轴的平均值的无偏差标准误差。
Panel.skew（[axis，skipna，level，numerical_only]）	返回所请求轴的无偏斜
Panel.sum（[axis，skipna，level，numeric_only]）	返回请求轴的值的总和
Panel.std（[axis，skipna，level，ddof，...]）	返回样品标准偏差超过请求的轴。
Panel.var（[axis，skipna，level，ddof，...]）	返回与请求轴无关的方差。
重新索引/选择/标签操作

Panel.add_prefix（prefix）	将前缀字符串与面板项名称连接。
Panel.add_suffix（suffix）	将后缀字符串与面板项名称连接。
Panel.drop（标签[，axis，level，inplace，...]）	返回请求轴中标签已删除的新对象。
Panel.equals（other）	确定两个NDFrame对象是否包含相同的元素。
Panel.filter（[items，like，regex，axis]）	子集根据指定索引中的标签的数据帧的行或列。
Panel.first（偏移）	用于基于日期偏移对时间序列数据的初始时间进行子集化的便利方法。
Panel.last（offset）	基于日期偏移对时间序列数据的最终周期进行子集化的便利方法。
Panel.reindex（[items，major_axis，minor_axis]）	使用可选填充逻辑将面板与新索引对齐，将NA / NaN放在前一个索引中没有值的位置。
Panel.reindex_axis（标签[，axis，method，...]）	使用可选填充逻辑将输入对象与新索引一致，将NA / NaN放在前一个索引中没有值的位置。
Panel.reindex_like（其他[，方法，副本，...]）	将具有匹配索引的对象返回给我自己。
Panel.rename（[items，major_axis，minor_axis]）	改变轴输入功能。
Panel.sample（[n，frac，replace，weights，...]）	从对象的轴返回项目的随机样本。
Panel.select（crit [，axis]）	返回与轴标签匹配条件相对应的数据
Panel.take（索引[，axis，convert，is_copy]）	类似于ndarray.take
Panel.truncate（[before，after，axis，copy]）	在某个特定索引值之前和/或之后截断排序的NDFrame。
缺失数据处理

Panel.dropna（[axis，how，inplace]）	从面板下降2D，保持通过轴不变
Panel.fillna（[value，method，axis，inplace，...]）	使用指定的方法填充NA / NaN值
形状变换，排序，转置

Panel.sort_index（[axis，level，ascending，...]）	按标签（沿轴）对对象排序
Panel.swaplevel（[i，j，axis]）	在特定轴上的多索引中交换级别i和j
Panel.transpose（\ * args，\ * \ * kwargs）	请选择面板的尺寸
Panel.swapaxes（axis1，axis2 [，copy]）	适当地互换轴和交换值轴
Panel.conform（框架[，轴]）	符合输入DataFrame以与所选轴对对齐。
组合/加入/合并

Panel.join（other [，how，lsuffix，rsuffix]）	加入项目与其他面板在主轴和次轴列
Panel.update（其他[，join，覆盖，...]）	使用来自传递的面板的非NA值或面板强制的对象修改面板。
时间序列相关的

Panel.asfreq（freq [，method，how，normalize]）	将TimeSeries转换为指定的频率。
Panel.shift（[periods，freq，axis]）	使用可选的时间频率按期望的周期数切换索引。
Panel.resample（rule [，how，axis，...]）	时间序列的频率转换和重采样的方便方法。
Panel.tz_convert（tz [，axis，level，copy]）	将tz感知轴转换为目标时区。
Panel.tz_localize（\ * args，\ * \ * kwargs）	将tz-naive TimeSeries本地化为目标时区。
序列化/ IO /转换

Panel.from_dict（data [，intersect，orient，dtype]）	根据DataFrame对象的dict构造面板
Panel.to_pickle（路径）	Pickle（序列化）对象到输入文件路径。
Panel.to_excel（path [，na_rep，engine]）	将Panel中的每个DataFrame写入单独的Excel表单
Panel.to_hdf（path_or_buf，key，\ * \ * kwargs）	使用HDFStore将包含的数据写入HDF5文件。
Panel.to_sparse（\ * args，\ * \ * kwargs）	NOT IMPLEMENTED：不调用此方法，因为面板对象不支持稀疏化，并且会引发错误。
Panel.to_frame（[filter_observations]）	将宽格式转换为长（堆叠）格式为DataFrame，其列是Panel的项目，其索引是由Panel的长轴和短轴组成的MultiIndex。
Panel.to_xarray()	从pandas对象返回一个xarray对象。
Panel.to_clipboard（[excel，sep]）	尝试将对象的文本表示写入系统剪贴板例如，可以将其粘贴到Excel中。
Panel4D
构造

Panel4D（[data，labels，items，major_axis，...]）	Panel4D是一个4维命名容器，非常像一个Panel，但有4个命名维度。
序列化/ IO /转换

Panel4D.to_xarray()	从pandas对象返回一个xarray对象。
属性和底层数据

轴

标签：轴1；每个标签对应一个包含在里面的Panel
项：轴2；每个项目对应于其中包含的DataFrame
major_axis：轴3；每个DataFrames的索引（行）
minor_axis：轴4；每个DataFrames的列
Panel4D.values	NDFrame的块状表示
Panel4D.axes	返回内部NDFrame的索引标签
Panel4D.ndim	轴数/阵列尺寸
Panel4D.size	NDFrame中的元素数
Panel4D.shape	返回轴维度的元组
Panel4D.dtypes	返回此对象中的dtype。
Panel4D.ftypes	返回此对象中的ftypes（稀疏/密集和dtype的指示）。
Panel4D.get_dtype_counts()	返回此对象中的dtypes的计数。
Panel4D.get_ftype_counts()	返回此对象中的ftypes的计数。
转换

Panel4D.astype（dtype [，copy，raise_on_error]）	投射对象以输入numpy.dtype
Panel4D.copy（[deep]）	复制此对象数据。
Panel4D.isnull()	返回一个布尔大小相同的对象，指示值是否为null。
Panel4D.notnull()	返回一个布尔大小相同的对象，指示这些值是否为空。
指数
这些方法或其变体中的许多可用于包含索引（Series / Dataframe）的对象，并且在直接调用这些方法之前应该最有可能使用这些方法或变体。

Index	不可变的ndarray实现有序的，可分割的集合。
属性

Index.values	将底层数据作为ndarray返回
Index.is_monotonic	is_monotonic_increasing的别名（已弃用）
Index.is_monotonic_increasing	返回如果索引是单调递增（只等于或
Index.is_monotonic_decreasing	返回如果索引是单调递减（只等于或
Index.is_unique
Index.has_duplicates
Index.dtype
Index.inferred_type
Index.is_all_dates
Index.shape	返回基础数据的形状的元组
Index.nbytes	返回底层数据中的字节数
Index.ndim	返回底层数据的维数，
Index.size	返回底层数据中的元素数量
Index.strides	返回基础数据的步幅
Index.itemsize	返回底层数据项的dtype的大小
Index.base	如果基础数据的内存是，则返回基础对象
Index.T	返回转置，这是通过定义self
Index.memory_usage（[deep]）	我的值的内存使用
修改和计算

Index.all（\ * args，\ * \ * kwargs）	返回所有元素是否为True
Index.any（\ * args，\ * \ * kwargs）	返回任何元素是否为True
Index.argmin（[axis]）	返回最小参数索引器的数组
Index.argmax（[axis]）	返回最大参数索引器的一个ndarray
Index.copy（[name，deep，dtype]）	制作此对象的副本。
Index.delete（loc）	删除已传递位置（-s）的新建索引
Index.drop（labels [，errors]）	创建新索引，并删除已通过的标签列表
Index.drop_duplicates（\ * args，\ * \ * kwargs）	返回索引，重复值已删除
Index.duplicated（\ * args，\ * \ * kwargs）	返回boolean np.ndarray表示重复值
Index.equals（other）	确定两个Index对象是否包含相同的元素。
Index.factorize（[sort，na_sentinel]）	将对象编码为枚举类型或类别变量
Index.identical（other）	类似于equals，但检查其他类似的属性
Index.insert（loc，item）	使新索引在位置插入新项目。
Index.min()	对象的最小值
Index.max()	对象的最大值
Index.reindex（target [，method，level，...]）	使用目标值创建索引（根据需要移动/添加/删除值）
Index.repeat（n，\ * args，\ * \ * kwargs）	重复索引的元素。
Index.where（cond [，other]）
版本0.19.0中的新功能。

Index.take（indices [，axis，allow_fill，...]）	返回由索引选择的值的新的％（klass）
Index.putmask（mask，value）	返回使用掩码设置的值的新索引
Index.set_names（names [，level，inplace]）	在索引上设置新名称。
Index.unique()	返回对象中唯一值的索引。
Index.nunique（[dropna]）	返回对象中唯一元素的数量。
Index.value_counts（[normalize，sort，...]）	返回包含唯一值计数的对象。
Index.fillna（[value，downcast]）	用指定值填充NA / NaN值
Index.dropna（[how]）	无NA / NaN值的返回索引
转换

Index.astype（dtype [，copy]）	创建一个值转换为dtypes的索引。
Index.tolist()	返回索引值的列表
Index.to_datetime（[dayfirst]）	DEPRECATED：改用pandas.to_datetime()。
Index.to_series（\ * \ * kwargs）	创建索引和值都等于索引键的系列
排序

Index.argsort（\ * args，\ * \ * kwargs）	返回将索引及其基础数据排序的索引。
Index.sort_values（[return_indexer，ascending]）	返回Index的排序副本
时间特定的操作

Index.shift（[periods，freq]）	Shift包含datetime对象的索引按输入的句点数和
组合/加入/集合操作

Index.append（other）	将索引选项集合附加在一起
Index.join（other [，how，level，return_indexers]）	这是一个内部非公开方法
Index.intersection（other）	形成两个Index对象。
Index.union（其他）	如果可能，形成两个Index对象的并集，并排序。
Index.difference（other）	返回索引中不在其他中的元素的新索引。
Index.symmetric_difference（other [，result_name]）	计算两个Index对象的对称差异。
选择

Index.get_indexer（target [，method，limit，...]）	给定当前索引的新索引的计算索引器和掩码。
Index.get_indexer_non_unique（target）	返回适合从非唯一索引获取的索引器
Index.get_level_values（level）	所请求级别的标签值的返回向量，等于长度
Index.get_loc（key [，method，tolerance]）	获取所请求标签的整数位置
Index.get_value（series，key）	从1维数组中快速查找值。
Index.isin（values [，level]）	计算每个索引值是否在传递的值集中找到的布尔数组。
Index.slice_indexer（[start，end，step，kind]）	对于有序索引，计算输入标签和的切片索引器
Index.slice_locs（[start，end，step，kind]）	计算输入标签的切片位置。
CategoricalIndex
CategoricalIndex	不可变索引实现有序，可分割集。
分类组件

CategoricalIndex.codes
CategoricalIndex.categories
CategoricalIndex.ordered
CategoricalIndex.rename_categories（\ * args，...）	重命名类别。
CategoricalIndex.reorder_categories（\ * args，...）	重新排序在new_categories中指定的类别。
CategoricalIndex.add_categories（\ * args，\ * \ * kwargs）	添加新类别。
CategoricalIndex.remove_categories（\ * args，...）	删除指定的类别。
CategoricalIndex.remove_unused_categories（...）	删除未使用的类别。
CategoricalIndex.set_categories（\ * args，\ * \ * kwargs）	将类别设置为指定的new_categories。
CategoricalIndex.as_ordered（\ * args，\ * \ * kwargs）	设置要排序的分类
CategoricalIndex.as_unordered（\ * args，\ * \ * kwargs）	将分类设置为无序
多指标
MultiIndex	用于大熊猫对象的多级或分层索引对象
MultiIndex组件

MultiIndex.from_arrays（arrays [，sortorder，...]）	将数组转换为MultiIndex
MultiIndex.from_tuples（tuples [，sortorder，...]）	将元组列表转换为MultiIndex
MultiIndex.from_product（iterables [，...]）	从多个迭代的笛卡尔乘积生成多索引
MultiIndex.set_levels（levels [，level，...]）	在MultiIndex上设置新级别。
MultiIndex.set_labels（labels [，level，...]）	在MultiIndex上设置新标签。
MultiIndex.to_hierarchical（n_repeat [，n_shuffle]）	返回一个重定形的MultiIndex，以符合n_repeat和n_shuffle给出的形状。
MultiIndex.is_lexsorted()	如果标签按字典顺序排序，则返回True
MultiIndex.droplevel（[level]）	返回已删除请求级别的索引。
MultiIndex.swaplevel（[i，j]）	将级别i与级别j交换。
MultiIndex.reorder_levels（order）	使用输入顺序重新排列级别。
DatetimeIndex
DatetimeIndex	datetime64数据的不可变的ndarray，在内部表示为int64，并且可以装箱到作为datetime的子类的Timestamp对象并携带诸如频率信息的元数据。
时间/日期组件

DatetimeIndex.year	datetime的年份
DatetimeIndex.month	月份为1月= 1月，12月= 12月
DatetimeIndex.day	datetime的日期
DatetimeIndex.hour	datetime的小时数
DatetimeIndex.minute	datetime的分钟
DatetimeIndex.second	datetime的秒数
DatetimeIndex.microsecond	datetime的微秒
DatetimeIndex.nanosecond	datetime的纳秒
DatetimeIndex.date	返回numpy数组的python datetime.date对象（即，没有时区信息的时间戳的日期部分）。
DatetimeIndex.time	返回datetime.time的numpy数组。
DatetimeIndex.dayofyear	一年的序数日
DatetimeIndex.weekofyear	一年的周数
DatetimeIndex.week	一年的周数
DatetimeIndex.dayofweek	一周中的星期几，星期一= 0，星期六= 6
DatetimeIndex.weekday	一周中的星期几，星期一= 0，星期六= 6
DatetimeIndex.weekday_name	一周中的日期名称（例如：星期五）
DatetimeIndex.quarter	日期的四分之一
DatetimeIndex.tz
DatetimeIndex.freq	获取/设置索引的频率
DatetimeIndex.freqstr	如果它的设置返回频率对象作为字符串，否则返回None
DatetimeIndex.is_month_start	逻辑指示是否每月的第一天（由频率定义）
DatetimeIndex.is_month_end	逻辑指示是否每月的最后一天（由频率定义）
DatetimeIndex.is_quarter_start	逻辑指示季度的第一天（由频率定义）
DatetimeIndex.is_quarter_end	逻辑指示季度的最后一天（由频率定义）
DatetimeIndex.is_year_start	逻辑指示一年中的第一天（由频率定义）
DatetimeIndex.is_year_end	逻辑指示一年中的最后一天（由频率定义）
DatetimeIndex.is_leap_year	逻辑指示日期是否属于闰年
DatetimeIndex.inferred_freq
选择

DatetimeIndex.indexer_at_time（time [，asof]）	在特定时段选择值（例如
DatetimeIndex.indexer_between_time（... [，...]）	在一天中的特定时间之间选择值（例如，9：00-9：30AM）。
时间特定的操作

DatetimeIndex.normalize()	将DatetimeIndex与时间返回到午夜。
DatetimeIndex.strftime（date_format）	返回由date_format指定的格式化字符串数组，该数组支持与python标准库相同的字符串格式。
DatetimeIndex.snap（[freq]）	捕捉时间戳到最近发生的频率
DatetimeIndex.tz_convert（tz）	将tz感知DatetimeIndex从一个时区转换到另一个（使用
DatetimeIndex.tz_localize（\ * args，\ * \ * kwargs）	将tz-naive DatetimeIndex本地化到给定时区（使用
DatetimeIndex.round（freq，\ * args，\ * \ * kwargs）	将索引循环到指定的频率
DatetimeIndex.floor（freq）	将索引落到指定的频率
DatetimeIndex.ceil（freq）	ceil索引到指定的频率
转换

DatetimeIndex.to_datetime（[dayfirst]）
DatetimeIndex.to_period（[freq]）	以特定频率投射到PeriodIndex
DatetimeIndex.to_perioddelta（freq）	计算指数值与在指定频率下转换为PeriodIndex的指数之间的差的TimedeltaIndex。
DatetimeIndex.to_pydatetime()	返回DatetimeIndex作为datetime.datetime对象的对象ndarray
DatetimeIndex.to_series（[keep_tz]）	创建索引和值都等于索引键的系列
TimedeltaIndex
TimedeltaIndex	timedelta64数据的不可变的ndarray，在内部表示为int64，和
部件

TimedeltaIndex.days	每个元素的天数。
TimedeltaIndex.seconds	每个元素的秒数（> = 0和小于1天）。
TimedeltaIndex.microseconds	每个元素的微秒数（> = 0和小于1秒）。
TimedeltaIndex.nanoseconds	每个元素的纳秒数（> = 0和小于1微秒）。
TimedeltaIndex.components	返回Timedeltas的组件（天，小时，分钟，秒，毫秒，微秒，纳秒）的数据帧。
TimedeltaIndex.inferred_freq
转换

TimedeltaIndex.to_pytimedelta()	返回TimedeltaIndex作为datetime.timedelta对象的对象ndarray
TimedeltaIndex.to_series（\ * \ * kwargs）	创建索引和值都等于索引键的系列
TimedeltaIndex.round（freq，\ * args，\ * \ * kwargs）	将索引循环到指定的频率
TimedeltaIndex.floor（freq）	将索引落到指定的频率
TimedeltaIndex.ceil（freq）	ceil索引到指定的频率
窗口
滚动对象由.rolling调用：pandas.DataFrame.rolling()，pandas.Series.rolling()等返回。展开对象通过.expanding调用：pandas.DataFrame.expanding()，pandas.Series.expanding()等返回。EWM对象由.ewm调用：pandas.DataFrame.ewm()，pandas.Series.ewm()等返回。

标准移动窗口功能

Rolling.count()	轧制数非NaN数
Rolling.sum（\ * args，\ * \ * kwargs）	滚动总和
Rolling.mean（\ * args，\ * \ * kwargs）	滚动平均值
Rolling.median（\ * \ * kwargs）	滚动中值
Rolling.var（[ddof]）	滚动方差
Rolling.std（[ddof]）	轧制标准偏差
Rolling.min（\ * args，\ * \ * kwargs）	滚动最小
Rolling.max（\ * args，\ * \ * kwargs）	轧制最大
Rolling.corr（[other，pairwise]）	滚动采样相关
Rolling.cov（[other，pairwise，ddof]）	滚动样本协方差
Rolling.skew（\ * \ * kwargs）	无偏斜歪斜
Rolling.kurt（\ * \ * kwargs）	无偏的滚动峭度
Rolling.apply（func [，args，kwargs]）	滚动功能适用
Rolling.quantile（quantile，\ * \ * kwargs）	滚动分位数
Window.mean（\ * args，\ * \ * kwargs）	窗口平均值
Window.sum（\ * args，\ * \ * kwargs）	窗口总和
标准扩展窗口函数

Expanding.count（\ * \ * kwargs）	扩展非NaN的数量
Expanding.sum（\ * args，\ * \ * kwargs）	扩大和
Expanding.mean（\ * args，\ * \ * kwargs）	扩展均值
Expanding.median（\ * \ * kwargs）	扩张中值
Expanding.var（[ddof]）	扩展方差
Expanding.std（[ddof]）	扩大标准差
Expanding.min（\ * args，\ * \ * kwargs）	扩大最小
Expanding.max（\ * args，\ * \ * kwargs）	膨胀最大
Expanding.corr（[other，pairwise]）	扩大样本相关性
Expanding.cov（[other，pairwise，ddof]）	扩大样本协方差
Expanding.skew（\ * \ * kwargs）	无偏的扩展偏度
Expanding.kurt（\ * \ * kwargs）	无偏膨胀峭度
Expanding.apply（func [，args，kwargs]）	扩展功能
Expanding.quantile（quantile，\ * \ * kwargs）	扩展分位数
指数加权移动窗口函数

EWM.mean（\ * args，\ * \ * kwargs）	指数加权移动平均
EWM.std（[bias]）	指数加权移动stddev
EWM.var（[bias]）	指数加权移动方差
EWM.corr（[other，pairwise]）	指数加权样本相关
EWM.cov（[other，pairwise，bias]）	指数加权样本协方差
GroupBy
GroupBy对象由groupby调用返回：pandas.DataFrame.groupby()，pandas.Series.groupby()等。

索引，迭代

GroupBy.__iter__()	Groupby迭代器
GroupBy.groups	dict {group name - > group labels}
GroupBy.indices	dict {group name - > group indices}
GroupBy.get_group（name [，obj]）	从提供的名称的组构造NDFrame
Grouper（[key，level，freq，axis，sort]）	Grouper允许用户为目标指定groupby指令
功能应用

GroupBy.apply（func，\ * args，\ * \ * kwargs）	应用功能并以智能方式将结果组合在一起。
GroupBy.aggregate（func，\ * args，\ * \ * kwargs）
GroupBy.transform（func，\ * args，\ * \ * kwargs）
计算/描述性统计

GroupBy.count()	计算组的计数，不包括缺少的值
GroupBy.cumcount（[ascending]）	将每个组中的每个项从0到该组的长度编号 - 1。
GroupBy.first()	计算组值的第一个值
GroupBy.head（[n]）	返回每个组的前n行。
GroupBy.last()	计算组值的最后一个
GroupBy.max()	计算组值的最大值
GroupBy.mean（\ * args，\ * \ * kwargs）	计算组的平均值，不包括缺少的值
GroupBy.median()	计算组的中间值，不包括缺失值
GroupBy.min()	计算组值的最小值
GroupBy.nth（n [，dropna]）	如果n是一个int，从每个组的第n行，或如果n是一个int列表的行的子集。
GroupBy.ohlc()	计算值的总和，不包括缺少的值
GroupBy.prod()	计算组值的prod
GroupBy.size()	计算组大小
GroupBy.sem（[ddof]）	计算组平均值的标准误差，不包括缺失值
GroupBy.std（[ddof]）	计算组的标准偏差，不包括缺失值
GroupBy.sum()	计算组值的总和
GroupBy.var（[ddof]）	计算组的方差，不包括缺少的值
GroupBy.tail（[n]）	返回每组的后n行
以下方法在SeriesGroupBy和DataFrameGroupBy对象中都可用，但可能稍有不同，通常是因为DataFrameGroupBy版本通常允许指定轴参数，并且通常指示是否将应用程序限制为特定数据类型的列的参数。

DataFrameGroupBy.agg（arg，\ * args，\ * \ * kwargs）	使用{column - >的输入函数或dict的聚合
DataFrameGroupBy.all（[axis，bool_only，...]）	返回所有元素是否超过请求的轴的True
DataFrameGroupBy.any（[axis，bool_only，...]）	返回任何元素是否超过请求的轴为True
DataFrameGroupBy.bfill（[limit]）	向后填充值
DataFrameGroupBy.corr（[method，min_periods]）	计算列的成对相关性，不包括NA /空值
DataFrameGroupBy.count()	计算组的计数，不包括缺少的值
DataFrameGroupBy.cov（[min_periods]）	计算列的成对协方差，不包括NA /空值
DataFrameGroupBy.cummax（[axis，skipna]）	返回请求轴上的累积最大值。
DataFrameGroupBy.cummin（[axis，skipna]）	返回所请求轴上的累积最小值。
DataFrameGroupBy.cumprod（[axis]）	每组的累积积
DataFrameGroupBy.cumsum（[axis]）	每组的累计和
DataFrameGroupBy.describe（[percentiles，...]）	生成各种汇总统计，不包括NaN值。
DataFrameGroupBy.diff（[periods，axis]）	对象的第一离散差异
DataFrameGroupBy.ffill（[limit]）	向前填充值
DataFrameGroupBy.fillna（[value，method，...]）	使用指定的方法填充NA / NaN值
DataFrameGroupBy.hist（data [，column，by，...]）	使用matplotlib / pylab绘制DataFrame系列的直方图。
DataFrameGroupBy.idxmax（[axis，skipna]）	在请求的轴上的第一次出现的最大值的返回索引。
DataFrameGroupBy.idxmin（[axis，skipna]）	请求轴上的第一次出现的最小值的返回索引。
DataFrameGroupBy.mad（[axis，skipna，level]）	返回请求轴的值的平均绝对偏差
DataFrameGroupBy.pct_change（[periods，...]）	给定周期数的百分比变化。
DataFrameGroupBy.plot	实现groupby对象的.plot属性的类
DataFrameGroupBy.quantile（[q，axis，...]）	在给定分位数的返回值超过请求的轴，一个数字。
DataFrameGroupBy.rank（[axis，method，...]）	沿轴计算数值数据（1到n）。
DataFrameGroupBy.resample（rule，\ * args，\ * \ * kwargs）	在使用TimeGrouper时提供重新采样
DataFrameGroupBy.shift（[periods，freq，axis]）	通过周期观察来移动每个组
DataFrameGroupBy.size()	计算组大小
DataFrameGroupBy.skew（[axis，skipna，level，...]）	返回所请求轴的无偏斜
DataFrameGroupBy.take（indices [，axis，...]）	类似于ndarray.take
DataFrameGroupBy.tshift（[periods，freq，axis]）	移动时间索引，使用索引的频率（如果可用）。
以下方法仅适用于SeriesGroupBy对象。

SeriesGroupBy.nlargest（\ * args，\ * \ * kwargs）	返回最大的n元素。
SeriesGroupBy.nsmallest（\ * args，\ * \ * kwargs）	返回最小的n元素。
SeriesGroupBy.nunique（[dropna]）	返回组中唯一元素的数量
SeriesGroupBy.unique()	返回对象中的唯一值的np.ndarray。
SeriesGroupBy.value_counts（[normalize，...]）
以下方法仅适用于DataFrameGroupBy对象。

DataFrameGroupBy.corrwith（other [，axis，drop]）	计算两个DataFrame对象的行或列之间的成对相关性。
DataFrameGroupBy.boxplot（已分组[，...]）	从DataFrameGroupBy数据创建框图。
重采样
重新取样器对象通过重新取样调用返回：pandas.DataFrame.resample()，pandas.Series.resample()。

索引，迭代

Resampler.__iter__()	Groupby迭代器
Resampler.groups	dict {group name - > group labels}
Resampler.indices	dict {group name - > group indices}
Resampler.get_group（name [，obj]）	从提供的名称的组构造NDFrame
功能应用

Resampler.apply	对重采样组应用聚合函数或函数，产生
Resampler.aggregate（arg，\ * args，\ * \ * kwargs）	对重采样组应用聚合函数或函数，产生
Resampler.transform（arg，\ * args，\ * \ * kwargs）	调用函数在每个组上产生一个类似索引的系列并返回
上采样

Resampler.ffill（[limit]）	向前填充值
Resampler.backfill（[limit]）	向后填充值
Resampler.bfill（[limit]）	向后填充值
Resampler.pad（[limit]）	向前填充值
Resampler.fillna（method [，limit]）	填充缺少的值
Resampler.asfreq()	返回新freq的值，
Resampler.interpolate（[method，axis，limit，...]）	根据不同的方法内插值。
计算/描述性统计

Resampler.count（[_ method]）	计算组的计数，不包括缺少的值
Resampler.nunique（[_ method]）	返回组中唯一元素的数量
Resampler.first（[_ method]）	计算组值的第一个值
Resampler.last（[_ method]）	计算组值的最后一个
Resampler.max（[_ method]）	计算组值的最大值
Resampler.mean（[_ method]）	计算组的平均值，不包括缺少的值
Resampler.median（[_ method]）	计算组的中间值，不包括缺失值
Resampler.min（[_ method]）	计算组值的最小值
Resampler.ohlc（[_ method]）	计算值的总和，不包括缺少的值
Resampler.prod（[_ method]）	计算组值的prod
Resampler.size（[_ method]）	计算组大小
Resampler.sem（[_ method]）	计算组平均值的标准误差，不包括缺失值
Resampler.std（[ddof]）	计算组的标准偏差，不包括缺失值
Resampler.sum（[_ method]）	计算组值的总和
Resampler.var（[ddof]）	计算组的方差，不包括缺少的值
样式
Styler对象由pandas.DataFrame.style返回。

构造

Styler（data [，precision，table_styles，...]）	帮助根据HTML和CSS的数据样式化DataFrame或Series。
样式应用

Styler.apply（func [，axis，subset]）	应用函数逐列，逐行或表格式，用结果更新HTML表示。
Styler.applymap（func [，subset]）	以元素方式应用函数，使用结果更新HTML表示。
Styler.format（formatter [，subset]）	格式化单元格的文本显示值。
Styler.set_precision（precision）	设置用于呈现的精度。
Styler.set_table_styles（table_styles）	在Styler上设置表样式。
Styler.set_caption（caption）	查看Styler上的标题
Styler.set_properties（[subset]）	Convience方法用于设置一个或多个非数据相关属性或每个单元格。
Styler.set_uuid（uuid）	设置样式器的uuid。
Styler.clear()	“重置”样式器，删除任何以前应用的样式。
内置样式

Styler.highlight_max（[subset，color，axis]）	通过阴影背景突出显示最大值
Styler.highlight_min（[子集，颜色，轴]）	通过阴影背景突出显示最小值
Styler.highlight_null（[null_color]）	对背景null_color进行阴影处理，以查找缺失值。
Styler.background_gradient（[cmap，low，...]）	根据每列（可选行）中的数据以渐变颜色背景。
Styler.bar（[subset，axis，color，width]）	为每列中的值颜色背景color。
样式导出导入

Styler.render()	将构建的样式呈现为HTML
Styler.export()	导出样式以应用于当前Styler。
Styler.use（styles）	在当前Styler上设置样式，可能使用Styler.export的样式。
工具函数
使用选项

describe_option（pat [，_print_desc]）	打印一个或多个注册选项的说明。
reset_option（pat）	将一个或多个选项重置为其默认值。
get_option（pat）	检索指定选项的值。
set_option（pat，value）	设置指定选项的值。
option_context（\ * args）	上下文管理器临时设置与语句上下文中的选项。
"""