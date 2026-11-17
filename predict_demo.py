# 从刚才写好的predict.py脚本里导入predict预测函数
from predict import predict
# 构造一条模拟居民随访记录字典，包含模型需要的全部原始输入特征
record = {"height_cm": 165, "weight_kg": 78, "waist_cm": 96, "sbp": 142, "dbp": 88,
          "smoking_status": "current", "drinking_freq": "occasional", "exercise_min_week": 60,
          "sleep_hours": 6.5, "veg_fruit_daily": 0, "family_history_dm": "yes",
          "hypertension_dx": 1, "hyperlipidemia_dx": 1, "gdm_history": 0,
          "polyuria": 0, "polydipsia": 0, "weight_loss_unexplained": 0,
          "gender": "M", "age": 58}
# 调用predict函数，传入这条随访记录，得到糖尿病阳性风险概率，保留4位小数
re = round(predict(record),4)
print(re)