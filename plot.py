"""
このファイルは等ラウドネス曲線のプロットを行うメインスクリプトです。
2つの入力点（周波数とdB）を受け取り、ISO 226:2003の等ラウドネス曲線と共に
その点を通る推定等ラウドネス曲線を描画します。

機能：
- 2つの入力点の対話的な入力受付
- 等ラウドネス曲線の表示
- 入力点を通る推定等ラウドネス曲線の計算と表示
- 1kHz位置でのdB値の表示
"""

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.interpolate import interp1d
import os

def plot_3_loudness_curves(points):
    # pointsは必ず3点であることを前提とする
    if len(points) != 3:
        raise ValueError('pointsは3つの(周波数, dB)タプルである必要があります')
    names = ['音源', '音源室', '受音室']
    # データ読み込みと初期設定
    df = pd.read_csv('data/complete_loudness_curves.csv')
    plt.figure(figsize=(10, 6))
    plt.semilogx()
    plt.grid(True, alpha=0.3)
    
    # 既存の等ラウドネス曲線をプロット
    phon_columns = [col for col in df.columns if col.startswith('phon_')]
    freq_1k_idx = np.abs(df['frequency'] - 1000).argmin()
    
    for i, col in enumerate(phon_columns):
        phon = int(col.split('_')[1])
        plt.plot(df['frequency'], df[col], 'r-', alpha=0.5, 
                label='ISO 226:2003 等ラウドネス曲線' if i == 0 else None)
        plt.annotate(f'{int(df[col].iloc[freq_1k_idx])}', 
                    xy=(1000, df[col].iloc[freq_1k_idx]),
                    xytext=(-15, 0), textcoords='offset points',
                    fontsize=9, color='red', alpha=0.7, va='center', ha='right')
    
    # 入力点ごとに処理
    colors = ['b', 'g', 'm', 'c', 'y', 'k']
    for idx, (freq, db) in enumerate(points):
        color = colors[idx % len(colors)]
        name = names[idx]
        # フォン値の推定
        phon_values = np.array([int(col.split('_')[1]) for col in phon_columns])
        freq_idx = np.abs(df['frequency'] - freq).argmin()
        db_values = df.loc[freq_idx, phon_columns].values
        
        # 補間曲線の計算
        interpolator = interp1d(db_values, phon_values)
        estimated_phon = float(interpolator(db))
        
        # 新しい曲線の生成
        curve_interpolator = interp1d(phon_values, 
                                    df[phon_columns].values, 
                                    axis=1)
        new_curve = curve_interpolator(estimated_phon)
        
        # プロット
        plt.plot(df['frequency'], new_curve, f'{color}-', linewidth=2,
                label=f'{name}の推定等ラウドネス曲線 ({estimated_phon:.1f} phon)')
        plt.plot(freq, db, f'{color}o', markersize=10,
                label=f'{name} ({freq:.1f} Hz, {db:.1f} dB)')
    
    # グラフの設定
    plt.xlabel('周波数 (Hz)')
    plt.ylabel('音圧レベル (dB SPL)')
    plt.title('等ラウドネス曲線 (ISO 226:2003)')
    plt.xlim(20, 20000)
    plt.ylim(-10, 130)
    plt.legend(loc='lower left', bbox_to_anchor=(0.01, 0.01))
    plt.tight_layout()
    # 画像として保存
    
    os.makedirs('output', exist_ok=True)
    save_path = f'output/loudness_curves.png'
    plt.savefig(save_path)
    plt.close()
    print(f'画像を{save_path}に保存しました')
    



def plot_loudness_curves(points):
    # データ読み込みと初期設定
    df = pd.read_csv('data/complete_loudness_curves.csv')
    plt.figure(figsize=(10, 6))
    plt.semilogx()
    plt.grid(True, alpha=0.3)
    
    # 既存の等ラウドネス曲線をプロット
    phon_columns = [col for col in df.columns if col.startswith('phon_')]
    freq_1k_idx = np.abs(df['frequency'] - 1000).argmin()
    
    for i, col in enumerate(phon_columns):
        phon = int(col.split('_')[1])
        plt.plot(df['frequency'], df[col], 'r-', alpha=0.5, 
                label='ISO 226:2003 等ラウドネス曲線' if i == 0 else None)
        plt.annotate(f'{int(df[col].iloc[freq_1k_idx])}', 
                    xy=(1000, df[col].iloc[freq_1k_idx]),
                    xytext=(-15, 0), textcoords='offset points',
                    fontsize=9, color='red', alpha=0.7, va='center', ha='right')
    
    # 入力点ごとに処理
    colors = ['b', 'g', 'm', 'c', 'y', 'k']
    for idx, (freq, db) in enumerate(points):
        color = colors[idx % len(colors)]
        # フォン値の推定
        phon_values = np.array([int(col.split('_')[1]) for col in phon_columns])
        freq_idx = np.abs(df['frequency'] - freq).argmin()
        db_values = df.loc[freq_idx, phon_columns].values
        
        # 補間曲線の計算
        interpolator = interp1d(db_values, phon_values)
        estimated_phon = float(interpolator(db))
        
        # 新しい曲線の生成
        curve_interpolator = interp1d(phon_values, 
                                    df[phon_columns].values, 
                                    axis=1)
        new_curve = curve_interpolator(estimated_phon)
        
        # プロット
        plt.plot(df['frequency'], new_curve, f'{color}-', linewidth=2,
                label=f'推定等ラウドネス曲線 ({estimated_phon:.1f} phon)')
        plt.plot(freq, db, f'{color}o', markersize=10,
                label=f'入力点 ({freq:.1f} Hz, {db:.1f} dB)')
    
    # グラフの設定
    plt.xlabel('周波数 (Hz)')
    plt.ylabel('音圧レベル (dB SPL)')
    plt.title('等ラウドネス曲線 (ISO 226:2003)')
    plt.xlim(20, 20000)
    plt.ylim(-10, 130)
    plt.legend(loc='lower left', bbox_to_anchor=(0.01, 0.01))
    plt.tight_layout()
    # 画像として保存
    
    os.makedirs('output', exist_ok=True)
    save_path = f'output/loudness_curves.png'
    plt.savefig(save_path)
    plt.close()
    print(f'画像を{save_path}に保存しました')

if __name__ == "__main__":
    points = []
    n = int(input("入力点の個数を入力してください: "))
    for i in range(n):
        print(f"\n{i+1}つ目の入力点の値を入力してください:")
        freq = float(input("周波数(Hz)を入力してください: "))
        db = float(input("音圧レベル(dB)を入力してください: "))
        points.append((freq, db))
    plot_loudness_curves(points)