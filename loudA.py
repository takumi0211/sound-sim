import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib import pyplot as plt
import japanize_matplotlib
import os

def a_weighting(frequencies):
    """
    A特性重み付けを計算する関数。

    Args:
        frequencies (np.ndarray or float): 周波数（Hz）の配列または単一の値。

    Returns:
        np.ndarray or float: A特性重み付け（dB）の配列または単一の値。
    """
    frequencies = np.array(frequencies)
    numerator = np.power(12194, 2) * np.power(frequencies, 4)
    denominator = (
        (np.power(frequencies, 2) + np.power(20.6, 2))
        * np.sqrt(
            (np.power(frequencies, 2) + np.power(107.7, 2))
            * (np.power(frequencies, 2) + np.power(737.9, 2))
        )
        * (np.power(frequencies, 2) + np.power(12194, 2))
    )
    ra = numerator / denominator
    return 20 * np.log10(ra) + 2.00

def exe_a_weighting(freq_point):
    """
    指定した周波数でA特性カーブを描画し、画像として保存するメイン関数。

    Args:
        freq_point (float): プロットしたい周波数（Hz）
    """
    freqs = np.logspace(np.log10(10), np.log10(20000), 500)
    A = a_weighting(freqs)
    plt.figure(figsize=(10, 6))
    plt.semilogx(freqs, A, label='A特性音圧レベルの重みづけ')
    # 入力周波数点を赤い点で描画
    A_point = a_weighting(freq_point)
    plt.scatter([freq_point], A_point, color='red', label=f'{freq_point} Hz: {A_point:.2f} dB')
    plt.xlabel('周波数 [Hz]')
    plt.ylabel('レスポンス [dB]')
    plt.title('A特性音圧レベルの重みづけグラフ')
    plt.legend()
    plt.grid(True, which='both')
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, f'a_weighting_{int(freq_point)}Hz.png')
    plt.savefig(save_path)
    print(f'画像を{save_path}に保存しました')
    
    return A_point    

if __name__ == "__main__":
    freq_point = float(input("プロットしたい周波数をHzで入力してください（例: 1000）: "))
    exe_a_weighting(freq_point)
