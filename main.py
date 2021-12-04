import sys
from PyQt5 import QtWidgets, QtGui
from ddco_template import *
import subprocess
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        #sxelf.setFixedSize(1161,664)
        self.vvp_out_2.clicked.connect(self.getVVP2)
        self.gtkwave_2.clicked.connect(self.gtw2)
        self.gtkwave_3.clicked.connect(self.gtw3)
        self.vvp_out_3.clicked.connect(self.getVVP3)
        self.exit_btn.clicked.connect(self.exit_prog)
        self.vvp_n.clicked.connect(self.getVVPn)
        self.gtk_n.clicked.connect(self.gtwn)
       
    def getVVP2(self):
        os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_2.v && alacritty --hold -e vvp src/frequency_divider")


    def getVVP3(self):
        os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_3.v && alacritty --hold -e vvp src/frequency_divider")

    def gtw2(self):
        os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_2.v && vvp src/frequency_divider && gtkwave src/freqdiv.vcd")

    def gtw3(self):
        os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_3.v && vvp src/frequency_divider && gtkwave src/freqdiv.vcd")

    def getVVPn(self):
        n = int(self.lineEdit.text())
        if(n==0):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_0.v && alacritty --hold -e vvp src/frequency_divider")
        elif(n==1):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_1.v && alacritty --hold -e vvp src/frequency_divider")
        elif(n==2):
            self.err_label.setText("")
            getVVP2()
        elif(n==3):
            self.err_label.setText("")
            getVVP3()
        elif(n==4):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_4.v && alacritty --hold -e vvp src/frequency_divider")
        elif(n==5):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_5.v && alacritty --hold -e vvp src/frequency_divider")
        elif(n==6):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_6.v && alacritty --hold -e vvp src/frequency_divider")
        elif(n==7):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_7.v && alacritty --hold -e vvp src/frequency_divider")
        else:
            self.err_label.setText("Please enter a value between 1 to 7")
            self.err_label.setStyleSheet("color: red;")



    def gtwn(self):
        n = int(self.lineEdit.text())
        if(n==0):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_0.v && vvp src/frequency_divider && gtkwave src/freqdiv.vcd")
        elif(n==1):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_1.v && vvp src/frequency_divider && gtkwave src/freqdiv.vcd")
        elif(n==2):
            self.err_label.setText("")
            gtw2()
        elif(n==3):
            self.err_label.setText("")
            gtw3()
        elif(n==4):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_4.v")
            os.system("vvp src/frequency_divider")
            os.system("gtkwave src/freqdiv.vcd")
        elif(n==5):
            print(n)
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_5.v && vvp src/frequency_divider && gtkwave src/freqdiv.vcd")
        elif(n==6):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_6.v && vvp src/frequency_divider && gtkwave src/freqdiv.vcd")
        elif(n==7):
            self.err_label.setText("")
            os.system("iverilog -o src/frequency_divider src/frequency_divider.v src/frequency_divider_tb_7.v && vvp src/frequency_divider && gtkwave src/freqdiv.vcd")
        else:
            self.err_label.setText("Please enter a value between 1 to 7")
            self.err_label.setStyleSheet("color: red;")

    def exit_prog(self):
        sys.exit()

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.show()
app.exec()
