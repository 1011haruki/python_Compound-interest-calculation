import matplotlib.pyplot as plt
import japanize_matplotlib

11

# ユーザーからの入力
monthly_amount = float(input("毎月積み立て額(円):"))
annual_interest_rate = float(input("金利(%):"))
years = int(input("継続年数(年):"))

# 結果を保存するリスト
results = []

# 毎月積み立て額で複利計算を行う
for year in range(1, years + 1):
    months = year * 12
    future_value = 0
    for month in range(1, months + 1):
        future_value = (future_value + monthly_amount) * (1 + annual_interest_rate / 100 / 12)
    
    # 年ごとの結果を保存
    results.append((year, future_value))

# 年数と評価価格のリストを準備
years_list = [result[0] for result in results]
values_list = [result[1] for result in results]

# グラフの作成
fig, ax = plt.subplots()
bars = ax.bar(years_list, values_list, color='skyblue', edgecolor='black')
ax.set_title('積み立てニーサ複利シミュレーション', fontsize=14, fontweight='bold')
ax.set_xlabel('年数', fontsize=12)
ax.set_ylabel('評価価格 (円)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)  # グリッド線を追加

# 各バーの上に値を表示
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'¥{height:,.0f}', 
            ha='center', va='bottom', fontsize=10, color='black')

# 軸の範囲を自動調整
ax.autoscale_view()

plt.show()
