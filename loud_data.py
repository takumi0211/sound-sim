"""
このファイルは等ラウドネス曲線のデータ処理を行うスクリプトです。
ISO 226:2003規格に基づく等ラウドネス曲線のデータを生成し、
CSVファイルとして保存します。

機能：
- 各フォン値のデータファイルの読み込み
- データの結合と整理
- 10フォン刻みでの補間処理
- 完成したデータセットのCSV保存
"""

import pandas as pd
import numpy as np
import os

# データディレクトリのパス
data_dir = 'data'

# 基準となるデータの読み込みと初期設定
df = pd.read_csv(os.path.join(data_dir, '0 Phons.csv'), 
                sep='\t', decimal=',', names=['frequency', 'phon_0'])

# 全てのフォンデータを結合
for file in sorted(os.listdir(data_dir)):
    if file.endswith('Phons.csv') and not file.startswith('0'):
        phon = int(file.split()[0])
        temp_df = pd.read_csv(os.path.join(data_dir, file), 
                            sep='\t', decimal=',',
                            names=['frequency', f'phon_{phon}'])
        df = pd.merge(df, temp_df, on='frequency', how='outer')

# 周波数でソートし、10フォン刻みで補間
df = df.sort_values('frequency')
phon_columns = [col for col in df.columns if col.startswith('phon_')]
phon_values = np.array([int(col.split('_')[1]) for col in phon_columns])

# 補間用の新しいデータフレーム作成
interpolated_df = pd.DataFrame({'frequency': df['frequency']})

# 既存のフォン値を追加
for col in phon_columns:
    interpolated_df[col] = df[col]

# 10フォン刻みで補間
for phon in range(0, max(phon_values) + 1, 10):
    if f'phon_{phon}' not in interpolated_df.columns:
        # 上下のフォン値を見つける
        lower_phon = max([p for p in phon_values if p < phon])
        upper_phon = min([p for p in phon_values if p > phon])
        
        # 線形補間で新しい曲線を生成
        weight = (phon - lower_phon) / (upper_phon - lower_phon)
        interpolated_df[f'phon_{phon}'] = (
            df[f'phon_{lower_phon}'] + 
            (df[f'phon_{upper_phon}'] - df[f'phon_{lower_phon}']) * weight
        )

# 列を順番に並び替え
phon_columns = [col for col in interpolated_df.columns if col.startswith('phon_')]
phon_values = sorted([int(col.split('_')[1]) for col in phon_columns])
ordered_columns = ['frequency'] + [f'phon_{phon}' for phon in phon_values]
interpolated_df = interpolated_df[ordered_columns]

# データを保存
output_file = 'data/complete_loudness_curves.csv'
interpolated_df.to_csv(output_file, index=False)
