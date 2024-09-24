# In[]
import os
import subprocess
import ltspice
import matplotlib.pyplot as plt

# In[]
# LTSPICEのコマンド
ltspice_exe = r'C:\Users\yukih\AppData\Local\Programs\ADI\LTspice\LTspice.exe'
circuit_file = r'D:\CraftRed\Simulation_spice\LTspicedata\python_test\python_test1.asc'

# LTSPICEのシミュレーションをコマンドラインで実行
subprocess.run([ltspice_exe, '-Run', circuit_file])

# RAWファイルを読み込み解析
raw_file = circuit_file.replace('.asc', '.raw')
lt = ltspice.Ltspice(raw_file)
lt.parse()

# 時間と波形データの取得
time = lt.getTime()
voltage_out = lt.getData('V(n002)')

# データのプロット
plt.plot(time, voltage_out)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.title('V(n002) vs Time')
plt.grid(True)
plt.show()