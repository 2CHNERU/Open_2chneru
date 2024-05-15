# In[]
import tqdm
import RC_model
import numpy as np
import matplotlib.pyplot as plt

# In[]
# パラメータ
R1 = 1000  # 1段目の抵抗値 (Ω)
C1 = 100* 1e-6  # 1段目のコンデンサ容量 (F)
R2 = 2000  # 2段目の抵抗値 (Ω)
C2 = 100* 1e-6  # 2段目のコンデンサ容量 (F)

# In[]
# 初期値
param1, param2 = [R1, C1], [R2, C2]
Vini1, Vini2 = 0, 0
dT = 10 * 1e-3

# オブジェクト
circuit_obj1 = RC_model.RC_class(param1, dT, Vini1)
circuit_obj2 = RC_model.RC_class(param2, dT, Vini2)

# In[]
# 入力電流の生成（pulse波形）
time = np.linspace(0, 6, num=600)
Current = np.zeros_like(time)
Current[100:300] = 0.1  # pulseの開始と終了インデックスを指定

# In[]
# シミュレーションループ
Voltage = np.zeros_like(time)
V_circuit1, V_circuit2 = Voltage.copy(), Voltage.copy()

for t in range(1, len(time)):
    V_1 = circuit_obj1.simulate_rc_series(dI_dt=Current[t])
    V_2 = circuit_obj2.simulate_rc_series(dI_dt=Current[t])
    
    Voltage[t], V_circuit1[t], V_circuit2[t] = V_1 + V_2, V_1, V_2


# In[]
# 電圧波形のプロット
fig, ax1 = plt.subplots(figsize=(10,8))

color1 = 'tab:red'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)', color=color1)
ax1.plot(time, V_circuit1, color='orange', label='Voltage1 (V)', ls='-.')
ax1.plot(time, V_circuit2, color=color1, label='Voltage2 (V)')
ax1.tick_params(axis='y', labelcolor=color1)

# 電流波形のプロット
ax2 = ax1.twinx()
color2 = 'tab:blue'
ax2.set_ylabel('Current (A)', color=color2)
ax2.plot(time, Current, color=color2, label='Current (A)')
ax2.tick_params(axis='y', labelcolor=color2)

plt.grid(True)

plt.title('2-Stage RC Series Circuit Simulation with Pulse Input')
fig.tight_layout()
plt.show()
