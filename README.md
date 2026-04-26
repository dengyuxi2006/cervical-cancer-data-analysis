# cervical-cancer-data-analysis
# 宫颈癌近距离放疗临床数据分析项目
## 项目简介
本项目以宫颈癌近距离放疗患者临床随访数据为研究基础，使用 Python 完成全流程数据分析，包含原始数据读取、数据清洗与特征构建、描述性统计、可视化绘图、逻辑回归预测模型搭建与模型性能评估。
依托 LaTeX 完成分析报告排版，结合 GitHub Pages 搭建项目在线展示网页，完整复现数据分析标准研究流程。

## 技术工具
- 数据处理：Pandas、NumPy
- 可视化绘图：Matplotlib、Seaborn
- 机器学习模型：Scikit-learn（逻辑回归）
- 报告撰写：LaTeX
- 在线展示：GitHub Pages

## 数据分析流程
1. 数据读取：导入 Excel 临床数据集，核对样本与变量信息
2. 数据预处理：整合多疗程放疗总剂量、筛选核心临床特征、删除缺失样本
3. 统计可视化：绘制基线特征分布图、变量相关性热力图
4. 模型构建：以 PFS 预后状态为标签，构建二分类预测模型
5. 模型评估：通过 ROC 曲线、AUC、混淆矩阵综合评价模型效果

## 实验结果展示
### 1. 人群基线分布
![年龄分布](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/age_dist.png)
![肿瘤分期分布](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/stage_dist.png)

### 2. 变量相关性分析
![相关性热力图](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/corr_heatmap.png)

### 3. 预测模型评估
![ROC曲线](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/roc_curve.png)
![混淆矩阵](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/confusion_matrix.png)

## 项目文件说明
- 全部 Python 代码：分段式独立脚本，可逐段复现运行
- 原始数据：临床患者 Excel 数据集
- 输出结果：5 张标准化分析图表
- 分析报告：LaTeX 源文件 + 最终 PDF 文档

## 总结
本项目完成了临床医疗数据从预处理、统计分析到机器学习建模的全链条实践，探究了放疗剂量、临床指标与患者肿瘤预后的关联，数据分析流程完整、结果清晰，满足课程设计与项目展示要求。
