from sound_insulation import *
from loudA import exe_a_weighting
from plot import plot_3_loudness_curves
import pandas as pd
import numpy as np

# 吸音率データベース
absorption_data_constant = {
    "パイルカーペット": {125: 0.09, 250: 0.1, 500: 0.2, 1000: 0.25, 2000: 0.3, 4000: 0.4},
    
    "壁クロス張り(コンクリート下地)": {125: 0.03, 250: 0.03, 500: 0.03, 1000: 0.04, 2000: 0.06, 4000: 0.08},
}

absorption_data = {
    'グラスウール': {'16-24': {25: {
                                    0: {125: 0.1, 250: 0.3, 500: 0.6, 1000: 0.7, 2000: 0.8, 4000: 0.85},
                                    40: {125: 0.15, 250: 0.4, 500: 0.7, 1000: 0.85, 2000: 0.9, 4000: 0.95},
                                    100: {125: 0.22, 250: 0.57, 500: 0.83, 1000: 0.82, 2000: 0.9, 4000: 0.9},
                                    300: {125: 0.65,  250: 0.7, 500: 0.75, 1000: 0.8, 2000: 0.75, 4000: 0.85}
                                },
                            50: {
                                    0: {125: 0.2, 250: 0.65, 500: 0.9, 1000: 0.85, 2000: 0.8, 4000: 0.85},
                                    40: {125: 0.25, 250: 0.8, 500: 0.95, 1000: 0.9, 2000: 0.85, 4000: 0.9},
                                    100: {125: 0.45, 250: 0.97, 500: 0.99, 1000: 0.85, 2000: 0.8, 4000: 0.92},
                                    300: {125: 0.75, 250: 0.85, 500: 0.85, 1000: 0.8, 2000: 0.8, 4000: 0.85}
                                },
                            100: {
                                    0: {125: 0.6, 250: 0.95, 500: 0.95, 1000: 0.85, 2000: 0.8, 4000: 0.9}
                                }
                            },
                    '32-48': {25: {
                                     0: {125: 0.12, 250: 0.3, 500: 0.65, 1000: 0.8, 2000: 0.85, 4000: 0.85},
                                    40: {125: 0.12, 250: 0.45, 500: 0.85, 1000: 0.9, 2000: 0.85, 4000: 0.9},
                                    100: {125: 0.25, 250: 0.7, 500: 0.9, 1000: 0.85, 2000: 0.85, 4000: 0.9}
                                },
                            50: {
                                    0: {125: 0.2, 250: 0.65, 500: 0.95, 1000: 0.9, 2000: 0.8, 4000: 0.85},
                                    40: {125: 0.28, 250: 0.9, 500: 0.95, 1000: 0.87, 2000: 0.85, 4000: 0.94}
                                }
                            },
                    '32-40': {100: {
                                    0: {125: 0.7, 250: 1.0, 500: 0.98, 1000: 0.85, 2000: 0.7, 4000: 0.8},
                                    40: {125: 0.78, 250: 1.0, 500: 0.99, 1000: 0.94, 2000: 0.9, 4000: 0.9},
                                    100: {125: 0.8, 250: 1.0, 500: 0.99, 1000: 0.93, 2000: 0.84, 4000: 0.84}
                                    }
                              }
                    },
    'ロックウール': {'40-140': {25: {
                                    0: {125: 0.1, 250: 0.3, 500: 0.7, 1000: 0.8, 2000: 0.8, 4000: 0.85},
                                    40: {125: 0.2, 250: 0.65, 500: 0.9, 1000: 0.85, 2000: 0.8, 4000: 0.8},
                                    100: {125: 0.35, 250: 0.65, 500: 0.9, 1000: 0.85, 2000: 0.85, 4000: 0.8},
                                    300: {125: 0.65, 250: 0.85, 500: 0.85, 1000: 0.8, 2000: 0.8, 4000: 0.85}
                                    },
                            50: {
                                0: {125: 0.2, 250: 0.65, 500: 0.95, 1000: 0.9, 2000: 0.85, 4000: 0.9},
                                40: {125: 0.35, 250: 0.85, 500: 0.95, 1000: 0.9, 2000: 0.85, 4000: 0.85},
                                100: {125: 0.55, 250: 0.9, 500: 0.95, 1000: 0.9, 2000: 0.85, 4000: 0.85},
                                300: {125: 0.75,250: 0.95, 500: 0.95, 1000: 0.85, 2000: 0.85, 4000: 0.9}
                                }
                            }
               }
    }


# 透過損失データベース
insulation_data = {
    "コンクリート": {
        "120": {125: 30, 250: 35, 500: 40, 1000: 45, 2000: 50, 4000: 55},
        "150": {125: 35, 250: 40, 500: 45, 1000: 50, 2000: 55, 4000: 60}
    },
    "ドア": {125: 11, 250: 13, 500: 16, 1000: 21, 2000: 25, 4000: 23},
    "開口": {125: 0, 250: 0, 500: 0, 1000: 0, 2000: 0, 4000: 0}
}

# 音源室と受音室の吸音の設定
# 面積の計算
floor_area = 5 * 5  # m^2
wall_area = 5 * 2.3 * 3  # m^2
door_area = 1 * 2  # m^2
wall_adjacent_area = 5 * 2.3  - door_area
ceiling_area = 5 * 5  # m^2

def select_material_absorption(material_name):
    if material_name in ["グラスウール", "ロックウール"]:
        density_keys = list(absorption_data[material_name].keys())
        print(f"{material_name}の密度候補:", density_keys)
        density = input("密度を選んで入力してください: ")

        thickness_keys = list(absorption_data[material_name][density].keys())
        print("厚さ候補:", thickness_keys)
        thickness = int(input("厚さ[mm]を選んで入力してください: "))

        air_layer_keys = list(absorption_data[material_name][density][thickness].keys())
        print("空気層厚さ候補:", air_layer_keys)
        air_layer = int(input("空気層厚さ[mm]を選んで入力してください: "))

        absorption = absorption_data[material_name][density][thickness][air_layer]
    else:
        absorption = absorption_data[material_name]
    return absorption


def get_user_parameters():
    print("天井の材料候補:", list(absorption_data.keys()))
    ceiling_material = input("天井の材料名を選んで入力してください: ")
    ceiling_abs = select_material_absorption(ceiling_material)

    print("パネルの材料候補:", list(absorption_data.keys()))
    panel_material = input("パネルの材料名を選んで入力してください: ")
    panel_abs = select_material_absorption(panel_material)

    absorption_area = float(input("パネルの設置面積[m^2]を入力してください: "))
    adjacent_wall_thickness = int(input("隣接壁の厚さ[m^2]を入力してください 120 or 150: "))
    return ceiling_abs, panel_abs, absorption_area, adjacent_wall_thickness


def calculate_dB(
    power_level_db, # 1. 音源の設定
    frequency_hz, 
    ceiling_abs, 
    panel_abs, 
    absorption_area, 
    adjacent_wall_thickness, 
    open=False  # デフォルトはFalse（ドア閉）
    ):

    # 2. 音源室の吸音力算出
    # 吸音率と面積のデータから音源室の吸音力を算出
    A1 = sound_abs = calculate_total_transmission_loss([
        (absorption_data_constant["パイルカーペット"][frequency_hz], floor_area),
        (absorption_data_constant["壁クロス張り(コンクリート下地)"][frequency_hz], wall_area + wall_adjacent_area - absorption_area),
        (ceiling_abs[frequency_hz], ceiling_area),
        (panel_abs[frequency_hz], absorption_area)
        ])
        

    # 3. 音源室の平均音圧レベル算出
    L1 = power_level_db + 6 - 10 * np.log10(A1)

    # 4. 遮音領域の設定
    # 透過率の計算
    wall_rate = 10 ** (-1 * insulation_data["コンクリート"][str(adjacent_wall_thickness)][frequency_hz] / 10)
    door_rate = 10 ** (-1 * insulation_data["ドア"][frequency_hz] / 10)
    opening_rate = 1

    # 透過率の合計
    if open == True:
        insulation_loss = calculate_total_transmission_loss([
                            (wall_rate, wall_area),
                            (opening_rate, door_area)
                            ])
    else:
        insulation_loss = calculate_total_transmission_loss([
                            (wall_rate, wall_area),
                            (door_rate, door_area)
                            ])

    # 5. 受音室の吸音力算出（音源室と同様）
    A2 = A1

    # 6. 受音室の平均音圧レベル算出
    L2 = L1 - (insulation_loss + 10 * np.log10(A2 / wall_adjacent_area))
    
    a_waiting = exe_a_weighting(frequency_hz)
    
    # 7. A特性音圧レベル算出
    L3 = L2 + a_waiting
    
    # 8. 等ラウドネス曲線にプロット（ダミー）
    points = [(frequency_hz, power_level_db), (frequency_hz, L1), (frequency_hz, L2)]
    plot_3_loudness_curves(points)
    
    result = pd.DataFrame({
        'L1': [L1],
        'L2': [L2],
        'L3': [L3],
        'A1': [A1],
        'insulation_loss': [insulation_loss],
    })
    return result


def main():
    frequency_hz = float(input("周波数[Hz]を入力してください（125, 250, 500, 1000, 2000, 4000 のいずれか）: "))
    ceiling_abs, panel_abs, absorption_area, adjacent_wall = get_user_parameters()
    power_level_db = float(input("音源のパワーレベル[dB]を入力してください: "))
    open = False
    
    # 音源室と受音室の吸音力算出
    result = calculate_dB(power_level_db, frequency_hz, ceiling_abs, panel_abs, absorption_area, adjacent_wall, open)
    
    # 結果の表示
    print(result)

if __name__ == "__main__":
    main()



# 9. 音の出力（ダミー: 実装例）

