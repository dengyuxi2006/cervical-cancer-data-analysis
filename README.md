# 宫颈癌近距离放疗预后分析项目

## 项目简介
本项目基于宫颈癌患者临床数据，使用 Python 实现全流程数据分析，包括数据读取、预处理、统计分析、可视化、预测模型构建与模型评估。
使用 LaTeX 生成完整分析报告，并通过 GitHub Pages 搭建在线展示网页。

## 技术工具
- Python
- Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- LaTeX (TeXworks)
- GitHub Pages

## 项目结构
- code/：Python 数据分析代码
- images/：结果可视化图片
- report/：LaTeX 源码与 PDF 报告
- data_clean_v2.xlsx：原始临床数据

## 数据分析流程
1. 数据读取
2. 数据预处理（计算总剂量、缺失值处理、特征筛选）
3. 描述统计与可视化
4. 构建逻辑回归预后预测模型
5. 模型性能评估（ROC、AUC、混淆矩阵）

## 结果展示
![年龄分布](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/images/age_dist.png)
![肿瘤分期](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/images/stage_dist.png)
![相关性热力图](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/images/corr_heatmap.png)
![ROC曲线](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/images/roc_curve.png)
![混淆矩阵](https://raw.githubusercontent.com/dengyuxi2006/cervical-cancer-data-analysis/main/images/confusion_matrix.png)

## 总结
本项目完成了临床医疗数据的全流程分析实践，包含数据处理、统计建模、可视化展示、报告撰写与项目在线发布。
