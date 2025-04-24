"""
このファイルは等ラウドネス曲線の静的なプロット生成を行うスクリプトです。
ISO 226:2003規格に基づく等ラウドネス曲線を高品質な画像として保存します。

機能：
- 等ラウドネス曲線の描画（10フォン刻み）
- グラフの体裁設定（グリッド、軸ラベル、フォントサイズなど）
- 高解像度PNG画像として保存（300dpi）

出力：
- equal_loudness_contours.png：等ラウドネス曲線の画像ファイル
"""

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# データの読み込みとグラフ設定
df = pd.read_csv('data/complete_loudness_curves.csv')
plt.figure(figsize=(12, 8))
plt.rcParams['font.size'] = 12

# グラフの基本設定
plt.grid(True, which='both', linestyle='-', alpha=0.2)
plt.grid(True, which='minor', linestyle='-', alpha=0.1)
plt.semilogx()

# 等ラウドネス曲線のプロット
for phon in range(0, 101, 10):
    plt.plot(df['frequency'], df[f'phon_{phon}'], 'r-', 
             linewidth=1.5, label=f'{phon} phon')

# 軸の設定
plt.xlim(20, 20000)
plt.ylim(-10, 130)
plt.xticks([20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000],
           ['20', '50', '100', '200', '500', '1k', '2k', '5k', '10k', '20k'])
plt.yticks(np.arange(-10, 131, 10))

# ラベルと凡例の設定
plt.xlabel('Frequency (Hz)')
plt.ylabel('Sound Pressure Level (dB SPL)')
plt.title('Equal-loudness contours (ISO 226:2003)')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# グラフの保存と後処理
plt.savefig('equal_loudness_contours.png', dpi=300, bbox_inches='tight')
plt.close()