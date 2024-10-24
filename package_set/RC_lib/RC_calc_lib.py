# -*- coding: utf-8 -*-


class RC:

    def __init__(self, Vc, R, C, dt, I):
        self.Vc = Vc
        self.R = R
        self.C = C
        self.dt = dt
        self.I = I

    def differential_equation(self):

        dVc_dt = (self.I * self.R - self.Vc) / (self.R * self.C)  # 微分方程式
        Vc = self.Vc + dVc_dt * self.dt  # オイラー法
        
        return Vc
    
    
