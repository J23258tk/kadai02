import random

results = [] # 出た目を保存する空のリストを用意

for i in range(10):
    x = random.randint(1,6)
    results.append(x)  #出た数字をリストに追加
    print(str(i+1)+"回目："+str(x))

average = sum(results) / len(results) # 出目の合計を回数で割って平均を求める
print("平均値：" + str(average))

# 期待される出力結果例
"""
1回目：4
2回目：1
3回目：1
4回目：5
5回目：1
6回目：1
7回目：5
8回目：6
9回目：4
10回目：6
平均値：3.4
"""
