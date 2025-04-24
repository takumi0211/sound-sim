import numpy as np
import sounddevice as sd

class SoundGenerator:
    def __init__(self):
        self.sample_rate = 44100
        self.calibration_factor = 1.0
        self.base_amplitude = 0.5

    def generate_sound(self, frequency, db_level, duration=1.0):
        # 時間配列の生成
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        
        # dBからAmplitudeへの変換
        amplitude = self.base_amplitude * (10 ** (db_level / 20))
        
        # 正弦波の生成（窓関数を適用）
        window = np.hanning(len(t))
        signal = amplitude * np.sin(2 * np.pi * frequency * t) * window
        
        # 信号の正規化
        signal = np.clip(signal, -1, 1)
        
        # 音の再生
        sd.play(signal, self.sample_rate)
        sd.wait()

    def stop_sound(self):
        sd.stop()

# テスト用
if __name__ == "__main__":
    generator = SoundGenerator()
    generator.generate_sound(200, 30, 1.0)