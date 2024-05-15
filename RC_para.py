import numpy as np
import matplotlib.pyplot as plt


# 2段のRC直列回路のシミュレーション関数
def simulate_rc_series():
    
    global V0, R1, C1, R2, C2, I, time
    
    num_steps = len(time)
    
    dt = time[1] - time[0]  # 時間間隔を計算
    
    V_result = np.zeros(num_steps)  # 電圧の配列を初期化
    V_result[0] = V0  # 初期電圧を設定

    # 1段目のRC回路の差分方程式を解く
    for i in range(1, num_steps):
        V1 = V_result[i-1] + (1 / (R1 * C1)) * (I[i-1] * dt - (V_result[i-1] / R1) * dt)

        # 2段目のRC回路の差分方程式を解く
        V_result[i] = V1 + (1 / (R2 * C2)) * ((V1 - V_result[i-1]) / dt - (V1 / R2) * dt) * dt
        
    return V_result


# パラメータ
V0 = 0  # 初期電圧 (V)
R1 = 1 * 1e+3  # 1段目の抵抗値 (Ω)
C1 = 10 * 1e-6  # 1段目のコンデンサ容量 (F)
R2 = 2 * 1e+3  # 2段目の抵抗値 (Ω)
C2 = 10 * 1e-6  # 2段目のコンデンサ容量 (F)

# 入力電流の生成（pulse波形）
time = np.linspace(0, 10, num=1000)
I = np.zeros_like(time)
I[100:300] = 0.1  # pulseの開始と終了インデックスを指定

# シミュレーションの実行
V = simulate_rc_series()

# 電圧波形のプロット
fig, ax1 = plt.subplots(figsize=(10,8))

color = 'tab:red'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)', color=color)
ax1.plot(time, V, color=color, label='Voltage (V)')
ax1.tick_params(axis='y', labelcolor=color)

# 電流波形のプロット
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Current (A)', color=color)
ax2.plot(time, I, color=color, label='Current (A)')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('2-Stage RC Series Circuit Simulation with Pulse Input')
fig.tight_layout()
plt.show()
