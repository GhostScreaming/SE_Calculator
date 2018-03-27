# -*- coding: utf-8 -*-

"""
Module implementing Cal.
"""
import math
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from Ui_cal import Ui_Calculator


class Cal(QWidget, Ui_Calculator):
    """
    Class documentation goes here.
    """
    
    """
    Some necessary value are defined here.
    """

    num1 = 0               #记录第一个操作数
    num2 = 0               #记录第二个操作数
    text1 = ""              #第一个操作数的字符，也可能是错误提示信息
    text2 = ""              #第二个操作数的字符
    
    '''
    记录当前状态。
    0表示之前没有计算结果，正在输入第一个计算数，
    1表示正在输入第二个计算数
    2表示之前已经有计算结果，或者输出了错误信息
    3表示对第二个操作数进行了一元运算(平方等)，禁止再输入数字
    '''
    signal = 0               
    digit = 0                 #记录有多少可以退格的位
    counter = 0             #记录有多少小数点
    sum = 0                  #记录运算数的结果
    op = ""                   #记录将要执行的运算符
    m_sum = 0             #记录M操作的数字

    
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Cal, self).__init__(parent)
        self.setupUi(self)
        
        """
        Create necesssary slot function
        """
        self.pushButton_0.clicked.connect(self.show_text)
        self.pushButton_1.clicked.connect(self.show_text)
        self.pushButton_2.clicked.connect(self.show_text)
        self.pushButton_3.clicked.connect(self.show_text)
        self.pushButton_4.clicked.connect(self.show_text)
        self.pushButton_5.clicked.connect(self.show_text)
        self.pushButton_6.clicked.connect(self.show_text)
        self.pushButton_7.clicked.connect(self.show_text)
        self.pushButton_8.clicked.connect(self.show_text)
        self.pushButton_9.clicked.connect(self.show_text)
        self.pushButton_Point.clicked.connect(self.show_text)
        self.pushButton_Plus.clicked.connect(self.show_text)
        self.pushButton_Substract.clicked.connect(self.show_text)
        self.pushButton_Multiply.clicked.connect(self.show_text)
        self.pushButton_Divide.clicked.connect(self.show_text)
        self.pushButton_Equal.clicked.connect(self.show_text)
        self.pushButton_Module.clicked.connect(self.show_text)
        self.pushButton_Reciprocal.clicked.connect(self.show_text)
        self.pushButton_Square.clicked.connect(self.show_text)
        self.pushButton_Opposite.clicked.connect(self.show_text)
        self.pushButton_Evolution.clicked.connect(self.show_text)
        self.pushButton_Backspace.clicked.connect(self.show_text)
        self.pushButton_C.clicked.connect(self.show_text)
        self.pushButton_CE.clicked.connect(self.show_text)
        self.pushButton_MC.clicked.connect(self.show_text)
        self.pushButton_MR.clicked.connect(self.show_text)
        self.pushButton_MS.clicked.connect(self.show_text)
        self.pushButton_M_Substract.clicked.connect(self.show_text)
        self.pushButton_M_Plus.clicked.connect(self.show_text)
        self.pushButton_Pi.clicked.connect(self.show_text)
        self.pushButton_Ln.clicked.connect(self.show_text)
        self.pushButton_Sin.clicked.connect(self.show_text)
        self.pushButton_Cos.clicked.connect(self.show_text)



    
    @pyqtSlot()
    def show_text(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.plainTextEdit.setPlainText(self.text1 + ' ' + self.op + ' ' + self.text2)
     
    @pyqtSlot()
    def error_report(self,  error):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.op = ""
        self.text1 = error
        self.text2 = ""
        self.num1 = 0
        self.num2 = 0
        self.sum = 0
        self.digit = 0
        self.counter = 0
        self.signal = 2
      
     
    @pyqtSlot()
    def evaluate(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.op == "+":
            self.sum = self.num1 + self.num2
        elif self.op == "-":
            self.sum = self.num1 - self.num2
        elif self.op == "×":
            self.sum = self.num1 * self.num2
        elif self.op == "/":
            if self.num2 == 0:
                error = "Zero can't be divisor!"
                self.error_report(error)
                return
            else:
                self.sum = self.num1 / self.num2
        elif self.op == "%":
            if (self.num1.is_integer() and self.num2.is_integer()):
                self.sum = self.num1 % self.num2
            else:
                error = "Please enter interger as operands."
                self.error_report(error)
                return
        self.num1 = self.sum
        self.num2 = 0
        self.text2 = ""
        self.counter = 0
        self.signal = 1
        self.op = ""
        self.sum = float(self.sum)
        if self.sum.is_integer():
            self.text1 = str(int(self.sum))
        else:
            self.text1 = str(self.sum)
   
   
    @pyqtSlot()
    def on_pushButton_MC_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.text1 = ""
        self.text2 = ""
        self.num1 = 0
        self.num2 = 0
        self.sum = 0
        self.op = ""
        self.counter = 0
        self.signal = 1
        self.counter = 0
        self.m_sum = 0
    
    @pyqtSlot()
    def on_pushButton_MR_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.num1 = float(self.m_sum)
        if self.num1 != 0:
            if(self.m_sum.is_integer()):
                self.text1 = str(int(self.m_sum))
            else:
                self.text1 = str(self.m_sum)
        else:
            self.text1 = '0'
        self.op = ""
        self.text2 = ""
        self.num2 = 0
        self.sum = 0
        self.signal = 2
        self.counter = 0
        self.digit = 0
    
    @pyqtSlot()
    def on_pushButton_M_Substract_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self. signal == 2:
            if self.text1 != ""and self.text1[0] < 'A':
                self.num1 = float(self.text1)
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.evaluate()
            else:
                error = "Incomplete expression!"
                self.error_report(error)
                return
        self.m_sum = self.m_sum - self.num1
        self.counter = 0
        self.signal = 2
        self.digit = 0
    
    @pyqtSlot()
    def on_pushButton_M_Plus_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self. signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.evaluate()
            else:
                error = "Incomplete expression!"
                self.error_report(error)
                return
        self.m_sum = self.m_sum + self.num1
        self.counter = 0
        self.signal = 2
        self.digit = 0

            
    
    @pyqtSlot()
    def on_pushButton_MS_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
            else:
                error = "Only valid number can be stored!"
                self.error_report(error)
                return
        else:
            if self.text2 != "" and self.text2[0] < 'A':
                self.num2 = float(self.text2)
                self.evaluate()
            else:
                error = "Only valid number can be stored!"
                self.error_report(error)
                return
        self.m_sum = self.num1
        self.counter = 0
        self.signal = 2
        self.digit = 0
    
    @pyqtSlot()
    def on_pushButton_CE_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0:
            self.text1 = ""
            self.num1 = 0
            self.digit = 0
            self.counter = 0
        elif self.signal == 1:
            self.text2 = ""
            self.num2 = 0
            self.digit = 0
            self.counter = 0
        elif self.signal == 2:
            self.text1 = ""
            self.num1 = 0
            self.digit = 0
            self.counter = 0
            self.signal = 0
        elif self.signal == 3:
            self.text2 = ""
            self.num2 = 0
            self.digit =0
            self.counter =0
            self.signal =1
    
    @pyqtSlot()
    def on_pushButton_C_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.op = ""
        self.text1 = ""
        self.text2 = ""
        self.num1 = 0
        self.num2 = 0
        self.sum = 0
        self.digit = 0
        self.counter = 0
        self.signal = 0
    
    @pyqtSlot()
    def on_pushButton_Backspace_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.digit > 0:
            if self.signal == 0:
                if self.text1[-1] == '.':
                    self.counter =0
                self.text1 = self.text1[:-1]
            elif self.signal == 1:
                if self.text2[-1] == '.':
                    self.counter =0
                self.text2 = self.text2[:-1]
    
    @pyqtSlot()
    def on_pushButton_Divide_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0  or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                self.signal = 1
                self.counter = 0
                self.op = "/"
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.evaluate()
                self.op = "/"
                self.digit = 0

    
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "7"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "7"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "7"
            self.digit = self.digit + 1
    
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "5"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "5"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "5"
            self.digit = self.digit + 1
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "4"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "4"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "4"
            self.digit = self.digit + 1
    
    @pyqtSlot()
    def on_pushButton_Opposite_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                self.num1 = - self.num1
                if self.num1.is_integer():
                    self.text1 = str(int(self.num1))
                else:
                    self.text1 = str(self.num1)
                self.signal = 2
                self.counter = 0
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.num2 = -self.num2
                if self.num2.is_integer():
                    self.text2 = str(int(self.num2))
                else:
                    self.text2 = str(self.num2)
                self.signal =3
                self.counter = 0
                self.digit = 0
    
    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "1"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "1"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "1"
            self.digit = self.digit + 1
    
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "8"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "8"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "8"
            self.digit = self.digit + 1
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "2"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "2"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "2"
            self.digit = self.digit + 1
    
    @pyqtSlot()
    def on_pushButton_0_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "0"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "0"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "0"
            self.digit = self.digit + 1

    
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "9"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "9"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "9"
            self.digit = self.digit + 1
    
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "6"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "6"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "6"
            self.digit = self.digit + 1
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 2:
            self.text1 = "3"
            self.num1 = 0
            self.signal = 0
            self.digit = self.digit + 1
        elif self.signal == 0:
            self.text1 = self.text1 + "3"
            self.digit = self.digit + 1
        elif self.signal == 1:
            self.text2 = self.text2 + "3"
            self.digit = self.digit + 1
    
    @pyqtSlot()
    def on_pushButton_Point_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.counter == 0:
            if self.signal == 2:
                self.text1 = "."
                self.num1 = 0
                self.signal = 0
                self.digit = self.digit + 1
            elif self.signal == 0:
                self.text1 = self.text1 + "."
                self.digit = self.digit + 1
            elif self.signal == 1:
                self.text2 = self.text2 + "."
                self.digit = self.digit + 1
            self.counter = 1

    
    @pyqtSlot()
    def on_pushButton_Multiply_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0  or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                self.signal = 1
                self.counter = 0
                self.op = "×"
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.evaluate()
                self.op = "×"
                self.digit = 0
    
    @pyqtSlot()
    def on_pushButton_Substract_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                self.signal = 1
                self.counter = 0
                self.op = "-"
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.evaluate()
                self.op = "-"
                self.digit = 0
    
    @pyqtSlot()
    def on_pushButton_Plus_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                self.signal = 1
                self.counter = 0
                self.op = "+"
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.evaluate()
                self.op = "+"
                self.digit = 0
            
                
        
        
    
    @pyqtSlot()
    def on_pushButton_Equal_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.sum = float(self.text1)
                if self.sum.is_integer():
                    self.text1 = str(int(self.sum))
                else:
                    self.text1 = str(self.sum)
                self.num1 = float(self.text1)
                self.signal = 2
                self.counter = 0
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.evaluate()
                self.op = ""
                self.signal = 2
                self.digit = 0



    
    @pyqtSlot()
    def on_pushButton_Square_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                self.num1 = self.num1 * self.num1
                if self.num1.is_integer():
                    self.text1 = str(int(self.num1))
                else:
                    self.text1 = str(self.num1)
                self.counter = 0
                self.signal = 2
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.num2 = self.num2 * self.num2
                if self.num2.is_integer():
                    self.text2 = str(int(self.num2))
                else:
                    self.text2 = str(self.num2)
                self.signal =3
                self.counter = 0
                self.digit = 0

    
    @pyqtSlot()
    def on_pushButton_Evolution_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                if self.num1 >= 0:
                    self.num1 = math.sqrt(self.num1)
                    if self.num1.is_integer():
                        self.text1 = str(int(self.num1))
                    else:
                        self.text1 = str(self.num1)
                else:
                    error = "Negative number can't do evolution!"
                    self.error_report(error)
                    return
                self.counter = 0
                self.signal = 2
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                if self.num2 >= 0:
                    self.num2 = math.sqrt(self.num2)
                    if self.num2.is_integer():
                        self.text2 = str(int(self.num2))
                    else:
                        self.text2 = str(self.num2)
                    self.counter = 0
                    self.signal = 3
                    self.digit = 0
                else:
                    error = "Negative number can't do evolution!"
                    self.error_report(error)
                    return
    
    @pyqtSlot()
    def on_pushButton_Module_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0  or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                self.signal = 1
                self.op = "%"
                self.counter = 0
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.evaluate()
                self.op = "%"
                self.digit = 0
    
    @pyqtSlot()
    def on_pushButton_Reciprocal_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                if self.num1 != 0:
                    self.num1 = 1 / self.num1
                    if self.num1.is_integer():
                        self.text1 = str(int(self.num1))
                    else:
                        self.text1 = str(self.num1)
                    self.counter = 0
                    self.signal = 2
                    self.digit = 0
                else:
                    error = "Zero has no reciprocal!"
                    self.error_report(error)
                    return
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                if self.num2 != 0:
                    self.num2 = 1 / self.num2
                    if self.num2.is_integer():
                        self.text2 = str(int(self.num2))
                    else:
                        self.text2 = str(self.num2)
                    self.counter = 0
                    self.signal = 3
                    self.digit = 0
                else:
                    error = "Zero has no reciprocal!"
                    self.error_report(error)
                    return
                
    @pyqtSlot()
    def on_pushButton_Pi_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0:
            if self.text1 == "":
                self.text1 = "3.1415926535898"
                self.num1 = float(self.text1)
                self.signal = 2
        elif self.signal == 1:
            if self.text2 == "":
                self.text2 = "3.1415926535898"
                self.num2 = float(self.text1)
                self.signal = 3
        elif self.signal == 2:
            self.text1 = "3.1415926535898"
            self.num1 = float(self.text1)
            self.signal = 2        
            
    @pyqtSlot()
    def on_pushButton_Ln_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                if self.num1 > 0:
                    self.num1 = math.log(self.num1)
                    if self.num1.is_integer():
                        self.text1 = str(int(self.num1))
                    else:
                        self.text1 = str(self.num1)
                    self.signal = 2
                    self.counter = 0
                    self.digit = 0
                else:
                    error = "Use positive number as input!"
                    self.error_report(error)
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                if self.num2 > 0:
                    self.num2 = math.sin(self.num2)
                    if self.num2.is_integer():
                        self.text2 = str(int(self.num2))
                    else:
                        self.text2 = str(self.num2)
                    self.signal =3
                    self.counter = 0
                    self.digit = 0
                else:
                    error = "Use positive number as input!"
                    self.error_report(error)        
        
    @pyqtSlot()
    def on_pushButton_Sin_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                self.num1 = math.sin(self.num1)
                if self.num1.is_integer():
                    self.text1 = str(int(self.num1))
                else:
                    self.text1 = str(self.num1)
                self.signal = 2
                self.counter = 0
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.num2 = math.sin(self.num2)
                if self.num2.is_integer():
                    self.text2 = str(int(self.num2))
                else:
                    self.text2 = str(self.num2)
                self.signal =3
                self.counter = 0
                self.digit = 0
        
    @pyqtSlot()
    def on_pushButton_Cos_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError        
        if self.signal == 0 or self.signal == 2:
            if self.text1 != "" and self.text1[0] < 'A':
                self.num1 = float(self.text1)
                self.num1 = math.cos(self.num1)
                if self.num1.is_integer():
                    self.text1 = str(int(self.num1))
                else:
                    self.text1 = str(self.num1)
                self.signal = 2
                self.counter = 0
                self.digit = 0
        else:
            if self.text2 != "":
                self.num2 = float(self.text2)
                self.num2 = math.cos(self.num2)
                if self.num2.is_integer():
                    self.text2 = str(int(self.num2))
                else:
                    self.text2 = str(self.num2)
                self.signal =3
                self.counter = 0
                self.digit = 0
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Cal = Cal()
    Cal.show()
    sys.exit(app.exec_())
