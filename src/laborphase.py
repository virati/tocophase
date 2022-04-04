#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:20:37 2020

@author: virati
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


class trajector:
    t = []
    
    def __init__(self,scaler=0.0001):
        self.t = np.linspace(0,50,50*1000)
        self.scaler = scaler
                
        self.import_FHR()
        self.import_IUP()

        
    def import_IUP(self):
        self.IUP = np.sin(self.t * np.pi * 2 * 0.03 + 0.2) + np.random.normal(0,0.5*self.scaler,size=self.t.shape)
        
    def import_FHR(self):
        self.FHR = 0.01*np.sin(self.t * np.pi * 2 * 0.5) + np.random.normal(0,0.1*self.scaler,size=self.t.shape)
        
        center=7
        width=1
        decel_gaussian = (1/(width * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((self.t - center)/width)**2)
        
        self.FHR = self.FHR - (decel_gaussian)
        
        
    def plot_ts(self):
        plt.figure()
        plt.plot(self.t,self.IUP)
        plt.plot(self.t,self.FHR)
        
    def plot_phase(self):
        plt.figure()
        plt.plot(self.IUP[::10],self.FHR[::10])
        plt.xlim((-2,2))
        plt.ylim((-2,2))
        
        
if __name__=='__main__':
    baby1 = trajector(0.01)
    baby1.plot_ts()
    baby1.plot_phase()