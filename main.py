from flask import Flask, render_template, request, jsonify
import numpy as np
import simpleaudio as sa
import os

app = Flask(__name__)

def volume_to_amplitude(volume_percent):
    """
    音量パーセンテージ（0-100）を振幅（0-0.9）に変換
    対数カーブを使用して、より自然な音量変化を実現
    """
    # 0-100を-40dB-0dBの範囲に変換（対数スケール）
    if volume_percent == 0:
        return 0
    db = -40 * (1 - (volume_percent / 100)) 
    # デシベルを振幅に変換（最大0.9）
    return min(10 ** (db / 20.0), 0.9)

def generate_tone(frequency=440.0, duration=1.0, volume=50):
    rate = 48000  # サンプリングレート
    # ナイキスト周波数を超えないようにチェック
    if frequency > rate/2:
        raise ValueError(f"周波数が高すぎます。{rate/2}Hz以下にしてください。")
    
    t = np.linspace(0., duration, int(rate*duration))
    # 音量パーセンテージを振幅に変換
    amplitude = volume_to_amplitude(volume)
    
    x = amplitude * np.sin(2.0 * np.pi * frequency * t)
    
    # フェードイン/アウトを適用して、クリック音を防ぐ
    fade_duration = 0.01  # 10ミリ秒
    fade_length = int(fade_duration * rate)
    fade_in = np.linspace(0, 1, fade_length)
    fade_out = np.linspace(1, 0, fade_length)
    x[:fade_length] *= fade_in
    x[-fade_length:] *= fade_out
    
    # 16ビット整数に変換
    audio = (x * 32767).astype(np.int16)
    return audio, rate

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_sound():
    try:
        frequency = float(request.form.get('frequency', 440.0))
        duration = float(request.form.get('duration', 1.0))
        volume = float(request.form.get('volume', 50.0))
        
        audio, rate = generate_tone(frequency, duration, volume)
        play_obj = sa.play_buffer(audio, 1, 2, rate)
        play_obj.wait_done()
        
        return jsonify({'status': 'success'})
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    if not os.path.exists('templates'):
        os.makedirs('templates')
    app.run(debug=True)
