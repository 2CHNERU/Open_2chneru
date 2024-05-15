# -*- coding: utf-8 -*-

class RC_class:
    
    def __init__(self, param, dT, Vini):
        
        [self.R, self.C] = param
        self.dT, self.Vb = dT, Vini
        self.coulomb = 0
    
    
    def simulate_rc_series(self, dI_dt):
        
        # 微分方程式
        dVc_dt = (self.R * dI_dt - self.Vb) / (self.R * self.C)
        
        # オイラー法
        self.V = self.Vb + dVc_dt * self.dT

        self.Vb = self.V
        
        return self.V

