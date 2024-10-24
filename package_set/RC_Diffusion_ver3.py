# In[]
from RC_lib import RC_calc_lib as rc
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[]

# 離散時間ステップ
dt = 0.001  # サンプリング間隔 (秒)

schedule = np.array([dt*i for i in range(10000000)])
current = np.array([0.0]+[50.0]*4999999+[0.0]*5000000)

# RC回路のパラメータ 抵抗 (Ω) コンデンサ容量 (F)
R1, C1 = 20*1e-3, 20000
R2, C2 = 15*1e-3, 1700
R_dc = 1*1e-3

# 離散化された微分方程式を解く
M = np.zeros(len(schedule))
Vc1, Vc2, Vout = M.copy(), M.copy(), M.copy()

coulomb_count = M.copy()
FCC = 50.0
soc = M.copy()
coulomb_counter = 0


# In[]

for step in tqdm(range(1, len(schedule))):
    
    coulomb_counter += current[step] * dt / 3600
    
    coulomb_count[step] = coulomb_counter
    soc[step] = coulomb_counter / FCC

    rc_lib1 = rc.RC(Vc=Vc1[step-1], R=R1, C=C1, dt=dt, I=current[step])
    rc_lib2 = rc.RC(Vc=Vc2[step-1], R=R2, C=C2, dt=dt, I=current[step])
    
    Vc1[step] = rc_lib1.differential_equation()
    Vc2[step] = rc_lib2.differential_equation()
    
    Vdc = R_dc * current[step]
    
    Vout[step] = Vc1[step] + Vc2[step] + Vdc

# In[]

plt.figure(figsize=(12, 8))
#plt.plot(schedule, coulomb_count, label='coulomb_count', color='red')
#plt.plot(schedule, soc, label='SOC', color='yellow')
plt.plot(schedule, Vc1, label='Charging1', color='orange', ls='--')
plt.plot(schedule, Vc2, label='Charging2', color='orange')
plt.plot(schedule, Vout, label='Charging', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Capacitor Charging and Discharging')
plt.legend()
plt.grid(True)
plt.show()
