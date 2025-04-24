# 吸音率データベース
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

absorption_data_constant = {
    "パイルカーペット": {125: 0.09, 250: 0.1, 500: 0.2, 1000: 0.25, 2000: 0.3, 4000: 0.4},
    
    "壁クロス張り(コンクリート下地)": {125: 0.03, 250: 0.03, 500: 0.03, 1000: 0.04, 2000: 0.06, 4000: 0.08},
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


from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from exe import *
import os

from sound import SoundGenerator

sound_generator = SoundGenerator()

app = Flask(__name__)
app.static_folder = '.'  # 現在のディレクトリを静的ファイルのルートとして設定

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-main', methods=['GET'])
def run_main():
    result = main()
    return jsonify({'result': result})

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # フォームデータの取得
        frequency_hz = float(request.form['frequency'])
        power_level_db = float(request.form['power_level'])
        
        # 天井材料の情報取得
        ceiling_material = request.form['ceiling_material']
        ceiling_density = request.form['ceiling_density']
        ceiling_thickness = int(request.form['ceiling_thickness'])
        ceiling_air_layer = int(request.form['ceiling_air_layer'])
        
        # パネル材料の情報取得
        panel_material = request.form['panel_material']
        panel_density = request.form['panel_density']
        panel_thickness = int(request.form['panel_thickness'])
        panel_air_layer = int(request.form['panel_air_layer'])
        
        # その他のパラメータ
        absorption_area = float(request.form['absorption_area'])
        wall_thickness = int(request.form['wall_thickness'])
        door_open = request.form.get('door_open') == 'true'  # セレクトボックスの値を取得

        # 吸音率データの取得
        ceiling_abs = absorption_data[ceiling_material][ceiling_density][ceiling_thickness][ceiling_air_layer]
        panel_abs = absorption_data[panel_material][panel_density][panel_thickness][panel_air_layer]

        # 音響計算の実行
        result = calculate_dB(
            power_level_db=power_level_db,
            frequency_hz=frequency_hz,
            ceiling_abs=ceiling_abs,
            panel_abs=panel_abs,
            absorption_area=absorption_area,
            adjacent_wall_thickness=wall_thickness,
            open=door_open  # ドアの開閉状態を渡す
        )

        # 結果の整形
        data = {
            '音源の音圧レベル': f"{power_level_db:.1f} dB",
            '音源室の音圧レベル': f"{result['L1'].iloc[0]:.1f} dB",
            '受音室の音圧レベル': f"{result['L2'].iloc[0]:.1f} dB",
            '受音室のA特性騒音レベル': f"{result['L3'].iloc[0]:.1f} dB",
            '吸音力': f"{result['A1'].iloc[0]:.2f} m²",
            '遮音損失': f"{result['insulation_loss'].iloc[0]:.1f} dB",
        }

        # グラフの画像URLを返す
        chart_url = '/output/loudness_curves.png'
        a_weighting_url = f'/output/a_weighting_{int(frequency_hz)}Hz.png'

        return jsonify({
            'success': True,
            'data': data,
            'chartUrl': chart_url,
            'aWeightingUrl': a_weighting_url
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/play-sound', methods=['POST'])
def play_sound():
    data = request.json
    type_ = data['type']
    frequency = float(data['frequency'])
    db_str = data['db'].split()[0]
    db = float(db_str)
    
    # 音を生成して再生
    sound_generator.generate_sound(frequency=frequency, db_level=db, duration=1.0)
    
    return jsonify({'success': True})

@app.route('/output/<path:filename>')
def serve_output(filename):
    return send_from_directory('output', filename)

if __name__ == '__main__':
    if not os.path.exists('templates'):
        os.makedirs('templates')
    app.run(debug=True, host='0.0.0.0', port=5001)

