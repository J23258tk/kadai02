import random

kaisuu = [10, 100, 1000, 10000, 1000000]  # 試行回数リスト

def roll_average(trial):
    total = 0  # サイコロの出目の合計値
    for n in range(trial):
        total += random.randint(1, 6)  # サイコロを1回振って出目を合計に足す
    average = total / trial  # 平均を計算
    return average  # 平均値を返す

# 各試行回数ごとの平均値を表示
for i in kaisuu:
    print(str(i) + "回試行の平均値：" + str(roll_average(i)))

# 期待される実行結果例
""" 
10回試行の平均値：3.9
100回試行の平均値：3.38
1000回試行の平均値：3.435
10000回試行の平均値：3.5103
1000000回試行の平均値：3.498772 
"""
