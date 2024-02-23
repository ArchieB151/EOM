# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:30:17 2023

@author: mcwt12
"""
import matplotlib.pyplot as plt
import sys

import numpy as np
import os
import importlib
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.dockarea as dockarea
from PyQt5.QtWidgets import QMessageBox

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time
import datetime
from random import randint


import serial
import serial.tools.list_ports

from PyQt5.QtGui import QFont

class EOMslider(QtGui.QMainWindow):

    def __init__(self, parent):
        QtGui.QMainWindow.__init__(self)
        self.parentGui = parent
        #self.sampling_rate = 250
        self.initUI()

    def initUI(self):
        
        #setting placeholder values for the various parameters

        
        #GUI
        self.area = dockarea.DockArea()
        self.setCentralWidget(self.area)
        self.resize(100,100)
        self.setWindowTitle('Adiabatic')
        self.createDocks()
        
    def createDocks(self):
            self.d1 = dockarea.Dock("AWG", size=(300,200))
            self.d1.hideTitleBar()

            self.carrierfreq = 1
            self.modfreq = 2
            self.modamp = 3
            self.halfwavevolt = 4
            
            #######################################################################
            ## w1: modify and read variables
            #######################################################################
    
            self.w1 = pg.LayoutWidget()
            self.label_w1 = QtGui.QLabel('EOM peaks')
            self.label_w1.setFont(QFont('Helvetica', 10))
            self.label_w1.setAlignment(QtCore.Qt.AlignCenter)
            
            self.Carrierfreqlabel = QtGui.QLabel('Carrier freq')
            self.Carrierfreqlabel.setAlignment(QtCore.Qt.AlignCenter)
            self.CarrierfreqLE = QtGui.QLineEdit(str(self.carrierfreq))
            
            self.Modfreqlabel = QtGui.QLabel('Modulation freq')
            self.Modfreqlabel.setAlignment(QtCore.Qt.AlignCenter)
            self.ModfreqLE = QtGui.QLineEdit(str(self.modfreq))
            
            self.Modamplabel = QtGui.QLabel(r'$V_{m}$')
            self.Modamplabel.setAlignment(QtCore.Qt.AlignCenter)
            self.Modampslider =  QtGui.QSlider()
            
            self.halfwavevoltlabel = QtGui.QLabel(r'$V_{\pi}$')
            self.halfwavevoltlabel.setAlignment(QtCore.Qt.AlignCenter)
            self.halfwavevoltLE = QtGui.QLineEdit(str(self.halfwavevolt))
         
            
            self.figure = plt.figure(facecolor='ghostwhite', frameon = True, figsize=(10,8))
            self.canvas = FigureCanvas(self.figure)
            ax = self.figure.add_subplot(111)
            self.figure.subplots_adjust(0.05, 0.4, 0.95, 0.95) # left,bottom,right,top 
            ax.tick_params(left = False, labelleft=False)
            ax.set_xlabel('Frequency')
            

            self.w1.addWidget(self.canvas, row=0, col=3, rowspan=4)
            self.w1.addWidget(self.Carrierfreqlabel, row=0, col=0)
            self.w1.addWidget(self.CarrierfreqLE, row=0, col=1)
            self.w1.addWidget(self.Modfreqlabel, row=1, col=0)
            self.w1.addWidget(self.ModfreqLE, row=1, col=1)
            self.w1.addWidget(self.halfwavevoltlabel, row=2, col=0)
            self.w1.addWidget(self.halfwavevoltLE, row=2, col=1)
            self.w1.addWidget(self.Modamplabel, row = 3, col= 0)
            self.w1.addWidget(self.Modampslider, row = 3, col= 1, colspan=2)
            
            #self.w1.addWidget(self.load_files_btn, row = 1,col=0, colspan=3)
            
            self.d1.addWidget(self.w1, row=0, col=0)
         