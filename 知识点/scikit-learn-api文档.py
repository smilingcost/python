# -*- coding: utf-8 -*-
from sklearn.linear_model import LinearRegression
"""
sklearn.base: Base classes and utility functions（基类和效用函数）
所有估计量的基类。
基础类
base.BaseEstimator	scikit学习中所有估计的基础类
base.ClassifierMixin	所有分类器的混合类在scikit学习
base.ClusterMixin	所有聚类估计器的混合类在scikit学习中
base.RegressorMixin	所有回归估计器的混合类在scikit学习
base.TransformerMixin	所有变压器的混合类在scikit学习

函数
base.clone(estimator[, safe])	构造具有相同参数的新估计器


sklearn.cluster: Clustering（聚类）
该sklearn.cluster模块收集流行的无监督聚类算法。
用户指南：有关详细信息，请参阅“ 集群”部分。
类
cluster.AffinityPropagation([damping, ...])	执行亲和度传播数据聚类
cluster.AgglomerativeClustering([...])	集聚聚类
cluster.Birch([threshold, branching_factor, ...])	实现Birch聚类算法
cluster.DBSCAN([eps, min_samples, metric, ...])	从矢量阵列或距离矩阵执行DBSCAN聚类
cluster.FeatureAgglomeration([n_clusters, ...])	聚集特征
cluster.KMeans([n_clusters, init, n_init, ...])	K均值聚类
cluster.MiniBatchKMeans([n_clusters, init, ...])	小批量K均值聚类
cluster.MeanShift([bandwidth, seeds, ...])	使用平坦内核的平均移位聚类
cluster.SpectralClustering([n_clusters, ...])	将聚类应用于对规范化拉普拉斯算子的投影

函数
cluster.estimate_bandwidth(X[, quantile, ...])	估计与平均移位算法一起使用的带宽
cluster.k_means(X, n_clusters[, init, ...])	K均值聚类算法
cluster.ward_tree(X[, connectivity, ...])	基于特征矩阵的区域聚类
cluster.affinity_propagation(S[, ...])	执行亲和度传播数据聚类
cluster.dbscan(X[, eps, min_samples, ...])	从矢量阵列或距离矩阵执行DBSCAN聚类
cluster.mean_shift(X[, bandwidth, seeds, ...])	使用平坦的内核执行数据的平均移位聚类
cluster.spectral_clustering(affinity[, ...])	将聚类应用于对规范化拉普拉斯算子的投影


sklearn.cluster.bicluster: Biclustering（双聚类）
光谱双聚类算法。
作者：Kemal Eren许可证：BSD 3条款
用户指南：有关详细信息，请参阅Biclustering部分。
类
SpectralBiclustering([n_clusters, method, ...])	光谱双聚类（Kluger，2003）
SpectralCoclustering([n_clusters, ...])	光谱共聚焦算法（Dhillon，2001）


sklearn.covariance: Covariance Estimators（协方差估计）
该sklearn.covariance模块包括方法和算法，以鲁棒地估计给定一组点的特征的协方差。定义为协方差的倒数的精度矩阵也被估计。协方差估计与高斯图形模型的理论密切相关。
用户指南：有关详细信息，请参见协方差估计部分。
covariance.EmpiricalCovariance([...])	最大似然协方差估计
covariance.EllipticEnvelope([...])	用于检测高斯分布数据集中异常值的对象
covariance.GraphLasso([alpha, mode, tol, ...])	具有l1惩罚估计量的稀疏逆协方差估计
covariance.GraphLassoCV([alphas, ...])	稀疏逆协方差与交叉验证的l1罚款的选择
covariance.LedoitWolf([store_precision, ...])	LedoitWolf估计
covariance.MinCovDet([store_precision, ...])	最小协方差决定因素（MCD）：协方差的robust估计
covariance.OAS([store_precision, ...])	Oracle近似收缩估计
covariance.ShrunkCovariance([...])	协变量估计与收缩
covariance.empirical_covariance(X[, ...])	计算最大似然协方差估计
covariance.ledoit_wolf(X[, assume_centered, ...])	估计缩小的Ledoit-Wolf协方差矩阵
covariance.shrunk_covariance(emp_cov[, ...])	计算对角线上收缩的协方差矩阵
covariance.oas(X[, assume_centered])	使用Oracle近似收缩算法估计协方差
covariance.graph_lasso(emp_cov, alpha[, ...])	l1惩罚协方差估计


sklearn.model_selection: Model Selection（模型选择）
用户指南：请参阅交叉验证：评估估计器性能，调整估计器的超参数和 学习曲线部分以获取更多详细信息。
分割器类
model_selection.KFold([n_splits, shuffle, ...])	K-折叠交叉验证器
model_selection.GroupKFold([n_splits])	具有非重叠组的K-fold迭代器变体
model_selection.StratifiedKFold([n_splits, ...])	分层K-折叠交叉验证器
model_selection.LeaveOneGroupOut()	离开一组交叉验证器
model_selection.LeavePGroupsOut(n_groups)	离开P组交叉验证器
model_selection.LeaveOneOut()	一次性交叉验证器
model_selection.LeavePOut(p)	Leave-P-Out交叉验证器
model_selection.ShuffleSplit([n_splits, ...])	随机置换交叉验证器
model_selection.GroupShuffleSplit([...])	随机组 - 交叉验证迭代器
model_selection.StratifiedShuffleSplit([...])	分层ShuffleSplit交叉验证器
model_selection.PredefinedSplit(test_fold)	预定义分裂交叉验证器
model_selection.TimeSeriesSplit([n_splits])	时间序列交叉验证器

分割函数
model_selection.train_test_split(\*arrays, ...)	将阵列或矩阵拆分成随机列和测试子集
model_selection.check_cv([cv, y, classifier])	用于构建交叉验证器的输入检查器实用程序

超参数优化
model_selection.GridSearchCV(estimator, ...)	对估计器的指定参数值进行详尽搜索
model_selection.RandomizedSearchCV(...[, ...])	随机搜索超参数
model_selection.ParameterGrid(param_grid)	每个参数的网格具有离散数量的值
model_selection.ParameterSampler(...[, ...])	发电机对从给定分布采样的参数
model_selection.fit_grid_point(X, y, ...[, ...])	适合一组参数

模型验证
model_selection.cross_val_score(estimator, X)	通过交叉验证评估分数
model_selection.cross_val_predict(estimator, X)	为每个输入数据点生成交叉验证的估计
model_selection.permutation_test_score(...)	评估具有置换的交叉验证分数的意义
model_selection.learning_curve(estimator, X, y)	学习曲线
model_selection.validation_curve(estimator, ...)	验证曲线


sklearn.datasets: Datasets（数据集）
该sklearn.datasets模块包括用于加载数据集的实用程序，包括加载和获取流行参考数据集的方法。它还具有一些人工数据生成器。
用户指南：有关详细信息，请参阅数据集加载实用程序部分。
装载机
datasets.clear_data_home([data_home])	删除数据家庭缓存的所有内容
datasets.get_data_home([data_home])	返回scikit-learn数据目录的路径
datasets.fetch_20newsgroups([data_home, ...])	加载20个新闻组数据集中的文件名和数据
datasets.fetch_20newsgroups_vectorized([...])	加载20个新闻组数据集并将其转换为tf-idf向量
datasets.load_boston([return_X_y])	加载并返回波士顿房价数据集（回归）
datasets.load_breast_cancer([return_X_y])	加载并返回乳腺癌威斯康星数据集（分类）
datasets.load_diabetes([return_X_y])	加载并返回糖尿病数据集（回归）
datasets.load_digits([n_class, return_X_y])	加载并返回数字数据集（分类）
datasets.load_files(container_path[, ...])	加载具有子文件夹名称类别的文本文件
datasets.load_iris([return_X_y])	加载并返回虹膜数据集（分类）
datasets.fetch_lfw_pairs([subset, ...])	在野外（LFW）对数据集中的标记面的装载程序
datasets.fetch_lfw_people([data_home, ...])	野外（LFW）人物数据集中的标记面的装载程序
datasets.load_linnerud([return_X_y])	加载并返回linnerud数据集（多元回归）
datasets.mldata_filename(dataname)	转换mldata.org文件名中的数据集的原始名称
datasets.fetch_mldata(dataname[, ...])	获取mldata.org数据集
datasets.fetch_olivetti_faces([data_home, ...])	Olivetti的装载机面向AT＆T的数据集
datasets.fetch_california_housing([...])	来自StatLib的加州住房数据集的装载机
datasets.fetch_covtype([data_home, ...])	加载封面类型数据集，必要时下载
datasets.fetch_kddcup99([subset, shuffle, ...])	加载并返回kddcup 99数据集（分类）
datasets.fetch_rcv1([data_home, subset, ...])	加载RCV1 multilabel数据集，必要时下载
datasets.load_mlcomp(name_or_id[, set_, ...])	加载从http://mlcomp.org下载的数据集
datasets.load_sample_image(image_name)	加载单个样本图像的numpy数组
datasets.load_sample_images()	加载样品图像进行图像处理
datasets.fetch_species_distributions([...])	来自Phillips等的物种分布数据集的装载机
datasets.load_svmlight_file(f[, n_features, ...])	将svmlight / libsvm格式的数据集加载到稀疏的CSR矩阵中
datasets.load_svmlight_files(files[, ...])	从SVMlight格式的多个文件加载数据集
datasets.dump_svmlight_file(X, y, f[, ...])	以svmlight / libsvm文件格式转储数据集

样本生成器
datasets.make_blobs([n_samples, n_features, ...])	生成用于聚类的各向同性高斯斑点
datasets.make_classification([n_samples, ...])	生成随机n类分类问题
datasets.make_circles([n_samples, shuffle, ...])	在2d中制作一个包含较小圆的大圆
datasets.make_friedman1([n_samples, ...])	产生“Friedman＃1”回归问题
datasets.make_friedman2([n_samples, noise, ...])	产生“Friedman＃2”回归问题
datasets.make_friedman3([n_samples, noise, ...])	产生“Friedman＃3”回归问题
datasets.make_gaussian_quantiles([mean, ...])	通过分位数生成各向同性高斯和标签样本
datasets.make_hastie_10_2([n_samples, ...])	生成Hastie等人使用的二进制分类数据
datasets.make_low_rank_matrix([n_samples, ...])	生成具有钟形奇异值的大多数低阶矩阵
datasets.make_moons([n_samples, shuffle, ...])	使两个交错半圈
datasets.make_multilabel_classification([...])	产生一个随机多标签分类问题
datasets.make_regression([n_samples, ...])	产生随机回归问题
datasets.make_s_curve([n_samples, noise, ...])	生成S曲线数据集
datasets.make_sparse_coded_signal(n_samples, ...)	生成信号作为字典元素的稀疏组合
datasets.make_sparse_spd_matrix([dim, ...])	产生一个稀疏的对称确定正矩阵
datasets.make_sparse_uncorrelated([...])	生成稀疏不相关设计的随机回归问题
datasets.make_spd_matrix(n_dim[, random_state])	产生一个随机对称，正定矩阵
datasets.make_swiss_roll([n_samples, noise, ...])	生成瑞士卷数据集
datasets.make_biclusters(shape, n_clusters)	生成一个具有恒定块对角线结构的阵列，用于二聚体
datasets.make_checkerboard(shape, n_clusters)	生成具有块棋盘结构的数组，用于双向聚集


sklearn.decomposition: Matrix Decomposition（矩阵分解）
该sklearn.decomposition模块包括矩阵分解算法，其中包括PCA，NMF或ICA。该模块的大多数算法可以被认为是降维技术。
用户指南：有关详细信息，请参阅组件中的分解信号（矩阵分解问题）部分。
decomposition.PCA([n_components, copy, ...])	主成分分析（PCA）
decomposition.IncrementalPCA([n_components, ...])	增量主成分分析（IPCA）
decomposition.ProjectedGradientNMF(\*args, ...)	非负矩阵因子分解（NMF）
decomposition.KernelPCA([n_components, ...])	内核主成分分析（KPCA）
decomposition.FactorAnalysis([n_components, ...])	因子分析（FA）
decomposition.FastICA([n_components, ...])	FastICA：独立分量分析的快速算法。
decomposition.TruncatedSVD([n_components, ...])	使用截断的SVD（也称为LSA）进行尺寸缩小
decomposition.NMF([n_components, init, ...])	非负矩阵因子分解（NMF）
decomposition.SparsePCA([n_components, ...])	稀疏主成分分析（SparsePCA）
decomposition.MiniBatchSparsePCA([...])	小批量稀疏主成分分析
decomposition.SparseCoder(dictionary[, ...])	稀疏编码
decomposition.DictionaryLearning([...])	词典学习
decomposition.MiniBatchDictionaryLearning([...])	小批量字典学习
decomposition.LatentDirichletAllocation([...])	潜在的Dirichlet分配与在线变分贝叶斯算法
decomposition.fastica(X[, n_components, ...])	执行快速独立成分分析
decomposition.dict_learning(X, n_components, ...)	解决词典学习矩阵分解问题
decomposition.dict_learning_online(X[, ...])	在线解决词典学习矩阵分解问题
decomposition.sparse_encode(X, dictionary[, ...])	稀疏编码


sklearn.dummy: Dummy estimators（虚拟估计）
用户指南：有关详细信息，请参阅模型评估：量化预测部分的质量部分。

dummy.DummyClassifier([strategy, ...])	DummyClassifier是使用简单规则进行预测的分类器
dummy.DummyRegressor([strategy, constant, ...])	DummyRegressor是使用简单规则进行预测的倒数


sklearn.ensemble: Ensemble Methods（集成方法）
该sklearn.ensemble模块包括用于分类，回归和异常检测的基于集成的方法。
用户指南：有关详细信息，请参阅“ 集成方法”部分。
ensemble.AdaBoostClassifier([...])	一个AdaBoost分类器
ensemble.AdaBoostRegressor([base_estimator, ...])	AdaBoost回归器
ensemble.BaggingClassifier([base_estimator, ...])	Bagging分类器
ensemble.BaggingRegressor([base_estimator, ...])	Bagging回归器
ensemble.ExtraTreesClassifier([...])	一个额外的树分类器
ensemble.ExtraTreesRegressor([n_estimators, ...])	一个额外的树回归器
ensemble.GradientBoostingClassifier([loss, ...])	梯度提升分类
ensemble.GradientBoostingRegressor([loss, ...])	渐变提升回归
ensemble.IsolationForest([n_estimators, ...])	隔离森林算法
ensemble.RandomForestClassifier([...])	随机森林分类器
ensemble.RandomTreesEmbedding([...])	一个完全随机的树的集成
ensemble.RandomForestRegressor([...])	随机森林回归器
ensemble.VotingClassifier(estimators[, ...])	软投票/多数规则分类器

部分依赖
树组合的部分依赖图
ensemble.partial_dependence.partial_dependence(...)	部分依赖target_variables
ensemble.partial_dependence.plot_partial_dependence(...)	部分依赖图features


sklearn.exceptions: Exceptions and warnings（异常和警告）
该sklearn.exceptions模块包括在scikit学习中使用的所有自定义警告和错误类。
exceptions.NotFittedError	如果在拟合前使用估计器，则提升异常类
exceptions.ChangedBehaviorWarning	用于通知用户任何行为变化的警告类
exceptions.ConvergenceWarning	捕捉收敛问题的自定义警告
exceptions.DataConversionWarning	警告用于通知代码中发生的隐式数据转换
exceptions.DataDimensionalityWarning	自定义警告，以通知数据维度的潜在问题
exceptions.EfficiencyWarning	用于通知用户效率低下的警告
exceptions.FitFailedWarning	如果在拟合估计器时出现错误，则使用警告类
exceptions.NonBLASDotWarning	点操作不使用BLAS时使用的警告
exceptions.UndefinedMetricWarning	度量无效时使用的警告


sklearn.feature_extraction: Feature Extraction（特征提取）
该sklearn.feature_extraction模块处理原始数据的特征提取。它目前包括从文本和图像中提取特征的方法。
用户指南：有关详细信息，请参阅特征提取部分。
feature_extraction.DictVectorizer([dtype, ...])	将特征值映射列表转换为向量
feature_extraction.FeatureHasher([...])	实现哈希功能，又称哈希技巧

从图像
该sklearn.feature_extraction.image子模块收集实用程序从图像中提取特征。
feature_extraction.image.img_to_graph(img[, ...])	像素到像素梯度连接的图形
feature_extraction.image.grid_to_graph(n_x, n_y)	像素到像素连接的图形
feature_extraction.image.extract_patches_2d(...)	将2D图像重新整理成一组补丁
feature_extraction.image.reconstruct_from_patches_2d(...)	从所有补丁重构图像
feature_extraction.image.PatchExtractor([...])	从图像集中提取补丁


从文本
该sklearn.feature_extraction.text子模块收集实用程序从文本文档建立特征向量。
feature_extraction.text.CountVectorizer([...])	将文本文档的集合转换为令牌计数矩阵
feature_extraction.text.HashingVectorizer([...])	将文本文档的集合转换为令牌发生的矩阵
feature_extraction.text.TfidfTransformer([...])	将计数矩阵转换为标准化的tf或tf-idf表示
feature_extraction.text.TfidfVectorizer([...])	将原始文档的集合转换为TF-IDF功能的矩阵


sklearn.feature_selection: Feature Selection（特征选择）
该sklearn.feature_selection模块实现特征选择算法。它目前包括单变量筛选方法和递归特征消除算法。
用户指南：有关详细信息，请参阅功能选择部分。
feature_selection.GenericUnivariateSelect([...])	具有可配置策略的单变量特征选择器
feature_selection.SelectPercentile([...])	根据最高分数百分位数选择功能
feature_selection.SelectKBest([score_func, k])	根据k最高分选择功能
feature_selection.SelectFpr([score_func, alpha])	过滤器：根据FPR测试选择低于alpha的p值
feature_selection.SelectFdr([score_func, alpha])	过滤器：为估计的错误发现率选择p值
feature_selection.SelectFromModel(estimator)	元变压器，用于根据重要性权重选择特征
feature_selection.SelectFwe([score_func, alpha])	过滤器：选择对应于同系误差率的p值
feature_selection.RFE(estimator[, ...])	功能排序与递归功能消除
feature_selection.RFECV(estimator[, step, ...])	功能排序与递归功能消除和交叉验证选择最佳数量的功能
feature_selection.VarianceThreshold([threshold])	功能选择器可删除所有低方差特征
feature_selection.chi2(X, y)	计算每个非负特征和类之间的平方统计
feature_selection.f_classif(X, y)	计算提供的样本的方差分析F值
feature_selection.f_regression(X, y[, center])	单变量线性回归测试
feature_selection.mutual_info_classif(X, y)	估计离散目标变量的互信息
feature_selection.mutual_info_regression(X, y)	估计连续目标变量的互信息


sklearn.gaussian_process: Gaussian Processes（高斯过程）
该sklearn.gaussian_process模块实现了基于高斯过程的回归和分类。
用户指南：有关详细信息，请参阅高斯过程部分。
gaussian_process.GaussianProcessRegressor([...])	高斯过程回归（GPR）
gaussian_process.GaussianProcessClassifier([...])	基于拉普拉斯逼近的高斯过程分类（GPC）
内核:
gaussian_process.kernels.Kernel	所有内核的基类
gaussian_process.kernels.Sum(k1, k2)	两个内核k1和k2的和核k1 + k2
gaussian_process.kernels.Product(k1, k2)	两个内核k1和k2的产品内核k1 * k2
gaussian_process.kernels.Exponentiation(...)	通过给定指数来指定内核
gaussian_process.kernels.ConstantKernel([...])	恒定内核
gaussian_process.kernels.WhiteKernel([...])	白内核
gaussian_process.kernels.RBF([length_scale, ...])	径向基函数核（又称平方指数核）
gaussian_process.kernels.Matern([...])	Matern 内核.
gaussian_process.kernels.RationalQuadratic([...])	理性二次内核
gaussian_process.kernels.ExpSineSquared([...])	正弦平方内核
gaussian_process.kernels.DotProduct([...])	Dot-Product内核
gaussian_process.kernels.PairwiseKernel([...])	在sklearn.metrics.pairwise中的内核包装器
gaussian_process.kernels.CompoundKernel(kernels)	内核由一组其他内核组成
gaussian_process.kernels.Hyperparameter	内核超参数的指定形式为namedtuple


sklearn.isotonic: Isotonic regression（等式回归）
用户指南：有关详细信息，请参阅等渗回归部分。
isotonic.IsotonicRegression([y_min, y_max, ...])	等渗回归模型
isotonic.isotonic_regression(y[, ...])	求解等渗回归模型:
isotonic.check_increasing(x, y)	确定y是否与x单调相关


sklearn.kernel_approximation Kernel Approximation（内核近似）
该sklearn.kernel_approximation模块基于傅里叶变换实现几个近似核特征图。
用户指南：有关更多详细信息，请参阅内核近似部分。
kernel_approximation.AdditiveChi2Sampler([...])	加性chi2核的近似特征图
kernel_approximation.Nystroem([kernel, ...])	使用训练数据的子集近似一个内核映射
kernel_approximation.RBFSampler([gamma, ...])	通过其傅立叶变换的Monte Carlo近似近似RBF核的特征图
kernel_approximation.SkewedChi2Sampler([...])	通过其傅立叶变换的蒙特卡罗近似近似的“偏斜卡方”核的特征图


sklearn.kernel_ridge Kernel Ridge Regression（内核岭回归）
模块sklearn.kernel_ridge实现内核脊回归。
用户指南：有关更多详细信息，请参阅Kernel ridge回归部分。
kernel_ridge.KernelRidge([alpha, kernel, ...])	内核岭回归


sklearn.discriminant_analysis: Discriminant Analysis（判别分析）
线性判别分析和二次判别分析
用户指南：有关详细信息，请参阅线性和二次判别分析部分。
discriminant_analysis.LinearDiscriminantAnalysis([...])	线性判别分析
discriminant_analysis.QuadraticDiscriminantAnalysis([...])	二次判别分析


sklearn.linear_model: Generalized Linear Models（广义线性模型）
该sklearn.linear_model模块实现广义线性模型。它包括利用最小角度回归和坐标下降计算的岭回归，贝叶斯回归，套索和弹性网估计。它还实现随机梯度下降相关算法。
用户指南：有关详细信息，请参阅“ 广义线性模型”一节。
linear_model.ARDRegression([n_iter, tol, ...])	贝叶斯ARD回归
linear_model.BayesianRidge([n_iter, tol, ...])	贝叶斯脊回归
linear_model.ElasticNet([alpha, l1_ratio, ...])	线性回归与组合L1和L2先验作为正则化器
linear_model.ElasticNetCV([l1_ratio, eps, ...])	弹性网模型沿正则化路径迭代拟合
linear_model.HuberRegressor([epsilon, ...])	线性回归模型，对离群值是robust
linear_model.Lars([fit_intercept, verbose, ...])	最小角度回归模型
linear_model.LarsCV([fit_intercept, ...])	交叉验证的最小二乘回归模型
linear_model.Lasso([alpha, fit_intercept, ...])	线性模型训练用L1作为矫正器（又名拉索）
linear_model.LassoCV([eps, n_alphas, ...])	拉索线性模型，沿正则化路径迭代拟合
linear_model.LassoLars([alpha, ...])	Lasso模型也适合最小角度回归
linear_model.LassoLarsCV([fit_intercept, ...])	使用LARS算法进行交叉验证的Lasso
linear_model.LassoLarsIC([criterion, ...])	Lasso模型适合Lars使用BIC或AIC进行型号选择
linear_model.LinearRegression([...])	普通最小二乘线性回归
linear_model.LogisticRegression([penalty, ...])	Logistic回归（又名logit，MaxEnt）分类器
linear_model.LogisticRegressionCV([Cs, ...])	Logistic回归CV（又名logit，MaxEnt）分类器
linear_model.MultiTaskLasso([alpha, ...])	用L1 / L2混合规范训练的多任务Lasso模型作为正则化器
linear_model.MultiTaskElasticNet([alpha, ...])	用L1 / L2混合规范训练的多任务ElasticNet模型作为正则化程序
linear_model.MultiTaskLassoCV([eps, ...])	多任务L1 / L2 Lasso内置交叉验证
linear_model.MultiTaskElasticNetCV([...])	多任务L1 / L2 ElasticNet内置交叉验证
linear_model.OrthogonalMatchingPursuit([...])	正交匹配追踪模型（OMP）
linear_model.OrthogonalMatchingPursuitCV([...])	交叉验证的正交匹配追踪模型（OMP）
linear_model.PassiveAggressiveClassifier([...])	被动侵略分类器
linear_model.PassiveAggressiveRegressor([C, ...])	被动侵略者
linear_model.Perceptron([penalty, alpha, ...])	在“ 用户指南”中阅读更多内容。
linear_model.RandomizedLasso([alpha, ...])	随机拉索
linear_model.RandomizedLogisticRegression([...])	随机逻辑回归
linear_model.RANSACRegressor([...])	RANSAC（RANdom SAmple Consensus）算法
linear_model.Ridge([alpha, fit_intercept, ...])	具有l2正则化的线性最小二乘法
linear_model.RidgeClassifier([alpha, ...])	分类器使用Ridge回归
linear_model.RidgeClassifierCV([alphas, ...])	里奇分类器内置交叉验证
linear_model.RidgeCV([alphas, ...])	里奇回归与内置交叉验证
linear_model.SGDClassifier([loss, penalty, ...])	线性分类器（SVM，逻辑回归，ao）与SGD训练
linear_model.SGDRegressor([loss, penalty, ...])	通过使用SGD最小化正则化经验损失拟合的线性模型
linear_model.TheilSenRegressor([...])	Theil-Sen估计：强大的多变量回归模型
linear_model.lars_path(X, y[, Xy, Gram, ...])	使用LARS算法计算最小角度回归或套索路径[1]
linear_model.lasso_path(X, y[, eps, ...])	计算具有坐标下降的Lasso路径
linear_model.lasso_stability_path(X, y[, ...])	基于随机拉索估计的稳定性路径
linear_model.logistic_regression_path(X, y)	为正则化参数列表计算逻辑回归模型
linear_model.orthogonal_mp(X, y[, ...])	正交匹配追踪（OMP）
linear_model.orthogonal_mp_gram(Gram, Xy[, ...])	革命正交匹配追踪（OMP）


sklearn.manifold: Manifold Learning（歧管学习）
该sklearn.manifold模块实现数据嵌入技术。
用户指南：有关详细信息，请参阅歧管学习部分。
manifold.LocallyLinearEmbedding([...])	局部线性嵌入
manifold.Isomap([n_neighbors, n_components, ...])	Isomap嵌入
manifold.MDS([n_components, metric, n_init, ...])	多维缩放
manifold.SpectralEmbedding([n_components, ...])	用于非线性维数降低的光谱嵌入
manifold.TSNE([n_components, perplexity, ...])	t分布随机相邻嵌入
manifold.locally_linear_embedding(X, ...[, ...])	对数据进行局部线性嵌入分析
manifold.spectral_embedding(adjacency[, ...])	将样本投影在拉普拉斯算子的第一个特征向量上


sklearn.metrics: Metrics（指标）
有关详细信息，请参阅模型评估：量化用户指南的预测部分的质量部分和成对度量度，亲和力和内核部分。
该sklearn.metrics模块包括分数函数，性能度量和成对度量和距离计算。
选型接口
有关详细信息，请参阅评分参数：定义用户指南的模型评估规则部分。
metrics.make_scorer(score_func[, ...])	从表现指标或损失函数中取得记分员
metrics.get_scorer(scoring)

分类度量
有关详细信息，请参阅用户指南的“ 分类指标”部分。
metrics.accuracy_score(y_true, y_pred[, ...])	准确度分级得分
metrics.auc(x, y[, reorder])	曲线下的计算面积（AUC）使用梯形规则
metrics.average_precision_score(y_true, y_score)	从预测分数计算平均精度（AP）
metrics.brier_score_loss(y_true, y_prob[, ...])	计算Brier分数
metrics.classification_report(y_true, y_pred)	构建一个显示主要分类指标的文本报告
metrics.cohen_kappa_score(y1, y2[, labels, ...])	科恩的kappa：衡量标注者间协议的统计
metrics.confusion_matrix(y_true, y_pred[, ...])	计算混淆矩阵来评估分类的准确性
metrics.f1_score(y_true, y_pred[, labels, ...])	计算F1分数，也称为平衡F分数或F度量
metrics.fbeta_score(y_true, y_pred, beta[, ...])	计算F-beta分数
metrics.hamming_loss(y_true, y_pred[, ...])	计算平均汉明损失
metrics.hinge_loss(y_true, pred_decision[, ...])	平均铰链损失（非正规化）
metrics.jaccard_similarity_score(y_true, y_pred)	Jaccard相似系数得分
metrics.log_loss(y_true, y_pred[, eps, ...])	对数损失，又称物流损失或交叉熵损失
metrics.matthews_corrcoef(y_true, y_pred[, ...])	计算二进制类的马修斯相关系数（MCC）
metrics.precision_recall_curve(y_true, ...)	计算不同概率阈值的 precision-recall 对
metrics.precision_recall_fscore_support(...)	计算每个课程的precision，recall，F度量和支持
metrics.precision_score(y_true, y_pred[, ...])	计算precision
metrics.recall_score(y_true, y_pred[, ...])	计算recall
metrics.roc_auc_score(y_true, y_score[, ...])	曲线下的计算面积（AUC）来自预测分数
metrics.roc_curve(y_true, y_score[, ...])	计算接收器工作特性（ROC）
metrics.zero_one_loss(y_true, y_pred[, ...])	零分类损失

回归指标
有关详细信息，请参阅用户指南的“回归指标”部分。
metrics.explained_variance_score(y_true, y_pred)	解释方差回归分数函数
metrics.mean_absolute_error(y_true, y_pred)	平均绝对误差回归损失
metrics.mean_squared_error(y_true, y_pred[, ...])	均方误差回归损失
metrics.median_absolute_error(y_true, y_pred)	中值绝对误差回归损失
metrics.r2_score(y_true, y_pred[, ...])	R^2（测定系数）回归分数函数

多标签排名指标
有关更多详细信息，请参阅用户指南的“ 多标签排名指标”部分。
metrics.coverage_error(y_true, y_score[, ...])	覆盖误差测量
metrics.label_ranking_average_precision_score(...)	计算基于排名的平均精度
metrics.label_ranking_loss(y_true, y_score)	计算排名损失量

聚类指标

有关详细信息，请参阅用户指南的群集性能评估部分。
该sklearn.metrics.cluster子模块包含了聚类分析的结果评价指标。有两种形式的评估：
监督，它为每个样本使用地面真值类别值。
无监督，不对和衡量模型本身的“质量”。
metrics.adjusted_mutual_info_score(...)	两个集群之间调整的相互信息
metrics.adjusted_rand_score(labels_true, ...)	兰德指数调整机会
metrics.calinski_harabaz_score(X, labels)	计算Calinski和Harabaz得分
metrics.completeness_score(labels_true, ...)	给定一个地面真相的集群标签的完整度量
metrics.fowlkes_mallows_score(labels_true, ...)	测量一组点的两个聚类的相似度
metrics.homogeneity_completeness_v_measure(...)	一次计算同质性和完整性和V-Measure分数
metrics.homogeneity_score(labels_true, ...)	给出了一个地面事实的集群标签的均匀性度量
metrics.mutual_info_score(labels_true, ...)	两个集群之间的相互信息
metrics.normalized_mutual_info_score(...)	两个集群之间的归一化互信息
metrics.silhouette_score(X, labels[, ...])	计算所有样本的平均轮廓系数
metrics.silhouette_samples(X, labels[, metric])	计算每个样本的剪影系数
metrics.v_measure_score(labels_true, labels_pred)	V-measure集群标签给出了一个基本的真相

二聚体指标
有关详细信息，请参阅用户指南的Biclustering评估部分。
metrics.consensus_score(a, b[, similarity])	两组双核的相似性

成对指标
有关更多详细信息，请参阅用户指南的“ 成对度量度，亲和力和内核”部分。
metrics.pairwise.additive_chi2_kernel(X[, Y])	计算X和Y中观测值之间的加性卡方核
metrics.pairwise.chi2_kernel(X[, Y, gamma])	计算指数卡方核X和Y
metrics.pairwise.distance_metrics()	pairwise_distances的有效指标
metrics.pairwise.euclidean_distances(X[, Y, ...])	考虑X（和Y = X）的行作为向量，计算每对向量之间的距离矩阵
metrics.pairwise.kernel_metrics()	pairwise_kernels的有效指标
metrics.pairwise.linear_kernel(X[, Y])	计算X和Y之间的线性内核
metrics.pairwise.manhattan_distances(X[, Y, ...])	计算X和Y中向量之间的L1距离
metrics.pairwise.pairwise_distances(X[, Y, ...])	从矢量数组X和可选Y计算距离矩阵
metrics.pairwise.pairwise_kernels(X[, Y, ...])	计算阵列X和可选阵列Y之间的内核
metrics.pairwise.polynomial_kernel(X[, Y, ...])	计算X和Y之间的多项式内核
metrics.pairwise.rbf_kernel(X[, Y, gamma])	计算X和Y之间的rbf（高斯）内核
metrics.pairwise.sigmoid_kernel(X[, Y, ...])	计算X和Y之间的S形内核
metrics.pairwise.cosine_similarity(X[, Y, ...])	计算X和Y中样本之间的余弦相似度
metrics.pairwise.cosine_distances(X[, Y])	计算X和Y中样本之间的余弦距离
metrics.pairwise.laplacian_kernel(X[, Y, gamma])	计算X和Y之间的拉普拉斯核
metrics.pairwise_distances(X[, Y, metric, ...])	从矢量数组X和可选Y计算距离矩阵
metrics.pairwise_distances_argmin(X, Y[, ...])	计算一点与一组点之间的最小距离
metrics.pairwise_distances_argmin_min(X, Y)	计算一点与一组点之间的最小距离
metrics.pairwise.paired_euclidean_distances(X, Y)	计算X与Y之间的配对欧氏距离
metrics.pairwise.paired_manhattan_distances(X, Y)	计算X和Y中向量之间的L1距离
metrics.pairwise.paired_cosine_distances(X, Y)	计算X和Y之间的配对余弦距离
metrics.pairwise.paired_distances(X, Y[, metric])	计算X和Y之间的配对距离


sklearn.mixture: Gaussian Mixture Models（高斯混合模型）
该sklearn.mixture模块实现混合建模算法。
用户指南：有关详细信息，请参阅高斯混合模型部分。
mixture.GaussianMixture([n_components, ...])	高斯混合
mixture.BayesianGaussianMixture([...])	高斯混合变分贝叶斯估计


sklearn.multiclass: Multiclass and multilabel classification（多类和多标签分类）
多类和多标签分类策略
该模块实现了多类学习算法：
one-vs-the-rest / one-vs-all
one-vs-one
纠错输出代码
该模块中提供的估计量是元估计器：它们需要在其构造函数中提供基本估计器。例如，可以使用这些估计器将二进制分类器或回归器转换为多类分类器。也可以将这些估计器与多类估计器一起使用，希望它们的准确性或运行时性能得到改善。
scikit-learn中的所有分类器实现多类分类; 您只需要使用此模块即可尝试使用自定义多类策略。
一对一的元分类器也实现了一个predict_proba方法，只要这种方法由基类分类器实现即可。该方法在单个标签和多重标签的情况下返回类成员资格的概率。注意，在多重标签的情况下，概率是给定样本落在给定类中的边际概率。因此，在多标签情况下，这些概率在一个给定样本的所有可能的标签的总和不会和为1，因为他们在单个标签的情况下做的。
用户指南：有关详细信息，请参阅多类和多标签算法部分。
multiclass.OneVsRestClassifier(estimator[, ...])	One-vs-the-rest (OvR) 多类/多标签策略
multiclass.OneVsOneClassifier(estimator[, ...])	One-vs-one 多类策略
multiclass.OutputCodeClassifier(estimator[, ...])	（错误校正）输出代码多类策略


sklearn.multioutput: Multioutput regression and classification（多输出回归和分类）
该模块实现多输出回归和分类。
该模块中提供的估计量是元估计器：它们需要在其构造函数中提供基本估计器。元估计器将单输出估计器扩展到多输出估计器。
用户指南：有关详细信息，请参阅多类和多标签算法部分。
multioutput.MultiOutputRegressor(estimator)	多目标回归
multioutput.MultiOutputClassifier(estimator)	多目标分类


sklearn.naive_bayes: Naive Bayes（朴素贝叶斯）
该sklearn.naive_bayes模块实现朴素贝叶斯算法。这些是基于应用贝叶斯定理与强（天真）特征独立假设的监督学习方法。
用户指南：有关详细信息，请参阅“ 朴素贝叶斯”部分。
naive_bayes.GaussianNB([priors])	高斯朴素贝叶斯（GaussianNB）
naive_bayes.MultinomialNB([alpha, ...])	朴素贝叶斯分类器多项式模型
naive_bayes.BernoulliNB([alpha, binarize, ...])	朴素贝叶斯分类器多变量伯努利模型


sklearn.neighbors: Nearest Neighbors（最近邻）
该sklearn.neighbors模块实现了k-最近邻居算法。
用户指南：有关更多详细信息，请参阅最近邻居部分。
neighbors.NearestNeighbors([n_neighbors, ...])	无监督学习者实施邻居搜索
neighbors.KNeighborsClassifier([...])	执行k-最近邻居的分类器投票
neighbors.RadiusNeighborsClassifier([...])	分类器在给定半径内的邻居中执行投票
neighbors.KNeighborsRegressor([n_neighbors, ...])	基于k最近邻的回归
neighbors.RadiusNeighborsRegressor([radius, ...])	基于固定半径内的邻居的回归
neighbors.NearestCentroid([metric, ...])	最重心分类器
neighbors.BallTree	BallTree用于快速泛化N点问题
neighbors.KDTree	KDTree用于快速泛化的N点问题
neighbors.LSHForest([n_estimators, radius, ...])	使用LSH森林执行近似最近邻搜索
neighbors.DistanceMetric	DistanceMetric类
neighbors.KernelDensity([bandwidth, ...])	核密度估计
neighbors.kneighbors_graph(X, n_neighbors[, ...])	计算X中k个邻居的（加权）图
neighbors.radius_neighbors_graph(X, radius)	计算X中的点的邻居的（加权）图


sklearn.neural_network: Neural network models（神经网络模型）
该sklearn.neural_network模块包括基于神经网络的模型。
用户指南：有关详细信息，请参阅神经网络模型（受监督）和神经网络模型（无监督）部分。
neural_network.BernoulliRBM([n_components, ...])	伯努利限制玻尔兹曼机（RBM）
neural_network.MLPClassifier([...])	多层感知器分类器
neural_network.MLPRegressor([...])	多层感知器回归


sklearn.calibration: Probability Calibration（概率校准）
校准预测概率。
用户指南：有关详细信息，请参阅概率校准部分。
calibration.CalibratedClassifierCV([...])	等渗回归或乙状结构的概率校准
calibration.calibration_curve(y_true, y_prob)	计算校准曲线的真实和预测概率

sklearn.cross_decomposition: Cross decomposition（交叉分解）
用户指南：有关详细信息，请参阅交叉分解部分。
cross_decomposition.PLSRegression([...])	PLS回归
cross_decomposition.PLSCanonical([...])	PLSCanonical实现了原始Wold算法的2块规范PLS [Tenenhaus 1998] p.204，在[Wegelin 2000]中被称为PLS-C2A
cross_decomposition.CCA([n_components, ...])	CCA规范相关分析
cross_decomposition.PLSSVD([n_components, ...])	部分最小二乘SVD


sklearn.pipeline: Pipeline（管道）
该sklearn.pipeline模块实现实用程序来构建复合估计器，作为变换链和估计器链。
pipeline.Pipeline(steps)	最终估计量的变换管道
pipeline.FeatureUnion(transformer_list[, ...])	连接多个变压器对象的结果
pipeline.make_pipeline(\*steps)	从给定的估计量构建管道
pipeline.make_union(\*transformers)	从给定的变压器构造一个FeatureUnion

sklearn.preprocessing: Preprocessing and Normalization（预处理和规范化）
该sklearn.preprocessing模块包括缩放，定心，归一化，二值化和插补方法。
用户指南：有关详细信息，请参阅预处理数据部分。
preprocessing.Binarizer([threshold, copy])	根据阈值对数据进行二值化（将特征值设置为0或1）
preprocessing.FunctionTransformer([func, ...])	从任意可调用的构造一个变压器
preprocessing.Imputer([missing_values, ...])	用于完成缺失值的插补变压器
preprocessing.KernelCenterer	中心一个内核矩阵
preprocessing.LabelBinarizer([neg_label, ...])	以一对一的方式对标签进行二值化
preprocessing.LabelEncoder	在0和n_classes-1之间编码标签
preprocessing.MultiLabelBinarizer([classes, ...])	在迭代迭代和多标签格式之间进行转换
preprocessing.MaxAbsScaler([copy])	按每个特征的最大绝对值进行缩放
preprocessing.MinMaxScaler([feature_range, copy])	通过将每个功能缩放到给定范围来转换功能
preprocessing.Normalizer([norm, copy])	将样品归一化为单位范数
preprocessing.OneHotEncoder([n_values, ...])	使用一个单一的一个K方案来编码分类整数特征
preprocessing.PolynomialFeatures([degree, ...])	生成多项式和交互特征
preprocessing.RobustScaler([with_centering, ...])	使用对异常值可靠的统计信息来缩放特征
preprocessing.StandardScaler([copy, ...])	通过删除平均值和缩放到单位方差来标准化特征
preprocessing.add_dummy_feature(X[, value])	增强数据集，带有额外的虚拟功能
preprocessing.binarize(X[, threshold, copy])	数组式或scipy.sparse矩阵的布尔阈值
preprocessing.label_binarize(y, classes[, ...])	以 one-vs-all 的方式对标签进行二值化
preprocessing.maxabs_scale(X[, axis, copy])	将每个特征缩放到[-1,1]范围，而不破坏稀疏度
preprocessing.minmax_scale(X[, ...])	通过将每个功能缩放到给定范围来转换功能
preprocessing.normalize(X[, norm, axis, ...])	将输入向量分别缩放到单位范数（向量长度）
preprocessing.robust_scale(X[, axis, ...])	沿着任何轴标准化数据集
preprocessing.scale(X[, axis, with_mean, ...])	沿着任何轴标准化数据集


sklearn.random_projection: Random projection（随机投影）
随机投影变压器
随机投影是一种简单且计算有效的方法，通过交易控制的精确度（作为附加方差）来减少数据的维度，以实现更快的处理时间和更小的模型大小。
控制随机投影矩阵的维数和分布，以保留数据集的任意两个样本之间的成对距离。
随机投影效率背后的主要理论结果是 Johnson-Lindenstrauss lemma（引用维基百科）：
在数学方面，Johnson-Lindenstrauss引理是从高维度到低维度欧几里德空间的低失真嵌入点的结果。引理指出，高维度空间中的一小部分点可以嵌入到较低维度的空间中，使得点之间的距离几乎保持不变。用于嵌入的地图至少为Lipschitz，甚至可以被视为正交投影。
用户指南：有关详细信息，请参阅随机投影部分。
random_projection.GaussianRandomProjection([...])	通过高斯随机投影降低维数
random_projection.SparseRandomProjection([...])	通过稀疏随机投影降低维数
random_projection.johnson_lindenstrauss_min_dim(...)	找到一个“安全”数量的组件随机投影到


sklearn.semi_supervised Semi-Supervised Learning（半监督学习）
该sklearn.semi_supervised模块实现半监督学习算法。这些算法使用少量的标记数据和大量未标记的分类任务数据。该模块包括标签传播。
用户指南：有关详细信息，请参阅半监督部分。
semi_supervised.LabelPropagation([kernel, ...])	标签传播分类器
semi_supervised.LabelSpreading([kernel, ...])	用于半监督学习的LabelSpread模型


sklearn.svm: Support Vector Machines（支持向量机）
该sklearn.svm模块包括支持向量机算法。
用户指南：有关详细信息，请参阅支持向量机部分。
评估者

svm.SVC([C, kernel, degree, gamma, coef0, ...])	C支持向量分类
svm.LinearSVC([penalty, loss, dual, tol, C, ...])	线性支持向量分类
svm.NuSVC([nu, kernel, degree, gamma, ...])	Nu支持向量分类
svm.SVR([kernel, degree, gamma, coef0, tol, ...])	Epsilon支持向量回归
svm.LinearSVR([epsilon, tol, C, loss, ...])	线性支持向量回归
svm.NuSVR([nu, C, kernel, degree, gamma, ...])	Nu支持向量回归
svm.OneClassSVM([kernel, degree, gamma, ...])	无监督异常检测
svm.l1_min_c(X, y[, loss, fit_intercept, ...])	返回C的最低边界，使得对于C（l1_min_C，无穷大），模型保证不为空

低级方法
svm.libsvm.fit	使用libsvm（低级方法）训练模型
svm.libsvm.decision_function	预测余量（这是libsvm的名称是predict_values）
svm.libsvm.predict	给定模型预测X的目标值（低级方法）
svm.libsvm.predict_proba	预测概率
svm.libsvm.cross_validation	交叉验证程序的绑定（低级程序）


sklearn.tree: Decision Trees（决策树）
该sklearn.tree模块包括用于分类和回归的基于决策树的模型。
用户指南：有关详细信息，请参阅决策树部分。
tree.DecisionTreeClassifier([criterion, ...])	决策树分类器
tree.DecisionTreeRegressor([criterion, ...])	决策树倒数
tree.ExtraTreeClassifier([criterion, ...])	一个非常随机的树分类器
tree.ExtraTreeRegressor([criterion, ...])	一个非常随机的树倒数
tree.export_graphviz	以DOT格式导出决策树

sklearn.utils: Utilities（工具）
该sklearn.utils模块包括各种实用程序。
开发人员指南：有关详细信息，请参阅实用程序开发人员页面。
utils.check_random_state(seed)	将种子转换成np.random.RandomState实例
utils.estimator_checks.check_estimator(Estimator)	检查估计是否符合scikit学习惯例
utils.resample(\*arrays, \*\*options)	以一致的方式重新采样数组或稀疏矩阵
utils.shuffle(\*arrays, \*\*options)	以一致的方式排列数组或稀疏矩阵

最近弃用
要在0.19中删除
lda.LDA([solver, shrinkage, priors, ...])	别名 sklearn.discriminant_analysis.LinearDiscriminantAnalysis.
qda.QDA([priors, reg_param, ...])	别名 sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.
datasets.load_lfw_pairs(\*args, \*\*kwargs)	DEPRECATED：函数'load_lfw_pairs'已经在0.17中被弃用，将在0.19中删除。请改用fetch_lfw_pairs（download_if_missing = False）
datasets.load_lfw_people(\*args, \*\*kwargs)	DEPRECATED：函数'load_lfw_people'在0.17中已被弃用，将在0.19中删除。请改用fetch_lfw_people（download_if_missing = False）

在0.20中删除
grid_search.ParameterGrid(param_grid)	每个参数的网格具有离散数量的值
grid_search.ParameterSampler(...[, random_state])	发电机对从给定分布采样的参数
grid_search.GridSearchCV(estimator, param_grid)	对估计器的指定参数值进行详尽搜索
grid_search.RandomizedSearchCV(estimator, ...)	随机搜索超参数
cross_validation.LeaveOneOut(n)	一次性交叉验证迭代器
cross_validation.LeavePOut(n, p)	Leave-P-Out交叉验证迭代器
cross_validation.KFold(n[, n_folds, ...])	K-fold交叉验证迭代器
cross_validation.LabelKFold(labels[, n_folds])	具有非重叠标签的K-fold迭代器变体
cross_validation.LeaveOneLabelOut(labels)	Leave-One-Label_Out交叉验证迭代器
cross_validation.LeavePLabelOut(labels, p)	Leave-P-Label_Out交叉验证迭代器
cross_validation.LabelShuffleSplit(labels[, ...])	Shuffle-Labels-Out交叉验证迭代器
cross_validation.StratifiedKFold(y[, ...])	分层K-折叠交叉验证迭代器
cross_validation.ShuffleSplit(n[, n_iter, ...])	随机置换交叉验证迭代器
cross_validation.StratifiedShuffleSplit(y[, ...])	分层ShuffleSplit交叉验证迭代器
cross_validation.PredefinedSplit(test_fold)	预定义的分割交叉验证迭代器
decomposition.RandomizedPCA(\*args, \*\*kwargs)	主成分分析（PCA）使用随机SVD
gaussian_process.GaussianProcess(\*args, \*\*kwargs)	遗留高斯过程模型类
mixture.GMM(\*args, \*\*kwargs)	传统高斯混合模型
mixture.DPGMM(\*args, \*\*kwargs)	Dirichlet过程高斯混合模型
mixture.VBGMM(\*args, \*\*kwargs)	高斯混合模型的变分推理
grid_search.fit_grid_point(X, y, estimator, ...)	适合一组参数
learning_curve.learning_curve(estimator, X, y)	学习曲线
learning_curve.validation_curve(estimator, ...)	验证曲线
cross_validation.cross_val_predict(estimator, X)	为每个输入数据点生成交叉验证的估计
cross_validation.cross_val_score(estimator, X)	通过交叉验证评估分数
cross_validation.check_cv(cv[, X, y, classifier])	输入检查器实用程序以用户友好的方式构建简历
cross_validation.permutation_test_score(...)	评估具有置换的交叉验证分数的意义
cross_validation.train_test_split(\*arrays, ...)	将阵列或矩阵拆分成随机列和测试子集