"""predict.py —— 输入一条随访记录（dict），输出风险分"""
import json
import joblib
import pandas as pd
# 加载之前保存的完整Pipeline（包含预处理+随机森林模型）
model = joblib.load('model.pkl')
# 加载特征清单，拿到建模时要求的全部特征列名（json文件用json.load）
with open('feature_cols.json', 'r', encoding='utf-8') as f:
    feature_cols = json.load(f)
# 定义预测函数：输入是单条随访字典，返回值是float类型的阳性风险概率
def predict(record:dict)->float:
    # 把单条字典记录转为DataFrame，模型只能接收DataFrame格式输入
    df = pd.DataFrame([record])
    # 手动计算BMI，和训练时逻辑保持一致：BMI=体重kg/(身高m)^2
    df['bmi'] = df['weight_kg'] / (df['height_cm']/100)**2
    # 重新对齐列：强制按照训练时的特征顺序，缺少的列自动填充为空，交给流水线里的填充器处理
    df = df.reindex(columns=feature_cols)
    # predict_proba输出[阴性概率,阳性概率]，取第1列（阳性概率），转为浮点数返回
    return float(model.predict_proba(df)[:,1][0])