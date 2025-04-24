import numpy as np


def calculate_sound_level(Lw, TL, F, A1, A2):
    """
    音源の音響パワーレベルLw、総合透過損失TL、音源側吸音面積A1、受音側吸音面積A2から、受音側の音圧レベルL2を計算する関数。

    パラメータ:
        Lw (float): 音源の音響パワーレベル [dB]
        TL (float): 総合透過損失 [dB]
        A1 (float): 音源側の吸音面積 [m^2]
        A2 (float): 受音側の吸音面積 [m^2]
        F (float): 間仕切りの面積 [m^2]

    戻り値:
        float: 受音側の音圧レベルL2 [dB]
    """
    L1 = Lw + 6 - 10 * np.log10(A1)
    L2 = L1 - (TL + 10 * np.log10(A2 / F))
    return L2

def transmission_loss_to_transmittance(R):
    """
    透過損失から透過率を計算する関数　
    単一値でもリストでも可能

    パラメータ:
        R (float または list of float): 透過損失 [dB]

    戻り値:
        float または list of float: 透過率
    """
    if isinstance(R, (list, np.ndarray)):
        return [10 ** (-r / 10) for r in R]
    else:
        return 10 ** (-R / 10)

def calculate_total_transmission_loss(tau_S_list):
    """
    各部位の(透過率, 面積)タプルのリストから総合透過損失（dB）を計算する関数

    パラメータ:
        tau_S_list (list of tuple): (透過率, 面積)のリスト

    戻り値:
        float: 総合透過損失 [dB]
    """
    return 10 * np.log10(1 / (sum(tau * S for tau, S in tau_S_list) / sum(S for _, S in tau_S_list)))


def calculate_diffuse_incident_transmission_loss(m, f):
    """
    材料の面密度と周波数から乱入射透過損失（dB）を計算する関数

    パラメータ:
        m (float): 材料の面密度 [kg/m^2]
        f (float): 入射音の周波数 [Hz]

    戻り値:
        float: 乱入射透過損失 TL [dB]
    """
    TL0 = 20 * np.log10(m * f) - 42.5
    TL = TL0 - 10 * np.log10(0.23 * TL0)
    return TL


def sabine_reverberation_time(V, A):
    """
    Sabineの式により残響時間を計算する関数

    パラメータ:
        V (float): 室容積 [m^3]
        A (float): 室内の総吸音面積 [m^2]

    戻り値:
        float: 残響時間 [秒]
    """
    return 0.16 * V / A

def total_absorption_coefficient(alpha_S_list):
    """
    各部位の(吸音率, 面積)タプルのリストから総合吸音率を計算する関数

    パラメータ:
        alpha_S_list (list of tuple): (吸音率, 面積)のリスト

    戻り値:
        float: 総合吸音率
    """
    return sum(alpha * S for alpha, S in alpha_S_list) / sum(S for _, S in alpha_S_list)