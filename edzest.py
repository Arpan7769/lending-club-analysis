#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 19:17:37 2022

@author: arpanshrivastava
"""
import seaborn as sns
import pandas as pd
accept=pd.read_csv('accepted_2007_to_2018Q4.csv')
reject=pd.read_csv('rejected_2007_to_2018Q4.csv')
class EDA:
    
    def __init__(self, data): 
        self.data=data
        pass  
    def heatmap(self,d):
        return sns.heatmap(d, cmap="flare", annot=True)
    def cp(self, xv,data):
        return sns.countplot(x=xv, data=data, order = data[xv].value_counts().index, palette='flare')
    
       