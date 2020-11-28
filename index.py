
#! charset UTF 8

from PyQt5 import QtWidgets, uic 
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QMainWindow, QDesktopWidget, QPushButton, QInputDialog, QLineEdit, QFileDialog, QAction
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys  # We need sys so that we can pass argv to QApplication
import json
import os
import time


# File selection window
# This is the file navigation window which will activate for file selection
class file_stream(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        #Load the UI Page 
        uic.loadUi('file_nav.ui', self)
       
        # Adding icons to the buttons
        # Gloabal size args
        self.size= QSize(29,29)
        self.bsize = QSize(74,74)

        # Icon for opening file explorer button 
        self.open_pacman_btn.setIcon(QIcon('images/file_select.png'))
        self.open_pacman_btn.setIconSize(self.size)

        # Listening for the btn to be clicked
        self.open_pacman_btn.clicked.connect(self.select_file)

        # Icon for sending file btn
        self.send_file_btn.setIcon(QIcon('images/send.png'))
        self.send_file_btn.setIconSize(self.bsize)
       
        # Listens for send button to be clicked
        self.send_file_btn.clicked.connect(self.send_file)

    # The process of opening file explorer and saving selected file to string.
    def select_file(self):

        self.file_url_input.setText(QFileDialog.getOpenFileName()[0])
        
    
    def status_loop(self):
        
        for i in self.pc_ip:
        
            with open('ip-ping/ping_{}.txt'.format(i), 'r') as file:
                
                data = file.read().replace('\n', '')

        
    def send_file(self):

        # user reference ID
        self.t_user_id = t_data

        # sending the file path
        self.t_packet = (self.file_url_input.text())

        # Initializing the system command
        os.system('scp ')
        
    

        
# Main QWindow
# Defining the start of the main window, this is the window that will always be visable
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page 
        uic.loadUi('form.ui', self)
        
        
        # Initializing icons
        # On / Off button
        self.size = QSize(49,49)
        self.start_btn.setIcon(QIcon('services/images/start.png'))
        self.start_btn.setIconSize(self.size)
        
        # Making the pause button checkable
        self.pause_btn.setCheckable(True)
        self.pause_btn.toggle()
        
        # Making the play button chckable
        self.play_btn.setCheckable(True)
        self.play_btn.toggle()

        # Making the start/stop btn checkable so we can keep track of wether it's been clicked or not
        self.start_btn.setCheckable(True)
        self.start_btn.toggle()
        
        # Play button
        self.play_btn.setIcon(QIcon('services/images/play.png'))
        self.play_btn.setIconSize(self.size)
        
        # Pause buttons
        self.pause_btn.setIcon(QIcon('services/images/pause.png'))
        self.pause_btn.setIconSize(self.size)
        
        # Pause buttons
        self.refresh_btn.setIcon(QIcon('services/images/refresh.png'))
        self.refresh_btn.setIconSize(self.size)
        
        # Blank out screens
        self.blank_btn.setIcon(QIcon('services/images/blank.png'))
        self.blank_btn.setIconSize(self.size)
        
        #  File menu Icon
        self.file_btn.setIcon(QIcon('services/images/file_transfer.png'))
        self.file_btn.setIconSize(self.size)
        
        # Interact icon
        self.interact_btn.setIcon(QIcon('services/images/interact.png'))
        self.interact_btn.setIconSize(self.size)

        # Screen share icon
        self.screen_share_btn.setIcon(QIcon('services/images/share_screen.png'))
        self.screen_share_btn.setIconSize(self.size)

        #++++++++++++++++++#
        # Global Variables #
        #++++++++++++++++++#
        
        # Contains the attribute reference name pause / play button [simplifies the code(Not necissary)] [global]
        
        # Contains the attribute reference name pause / play button [simplifies the code(Not necissary)] [global]
        self.pc_ = self.pc_select_box.currentText()
        
        
        # Reference for each PC's IP [basically converting a pc ID -> Numeric Value]
        self.pc_ip =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        
        
        ##############
        #  Startup/refresh # 
        ##############
        
        #-----------------------#
        # Event Listeners # 
        #-----------------------#
        
        # Listening for the pause button to be clicked [main window 'tab1'] 
        self.pause_btn.clicked.connect(self.pause_func)

        # Lisatening for the play button to be lcicked [main window 'tab1']
        self.play_btn.clicked.connect(self.play_func)
        
        # Listening for stopping and starting machines [main window 'tab1']
        #Setting the button to checkable 
        self.start_btn.clicked.connect(self.on_off_switch)
        
        # Listening for stopping and starting machines [main window 'tab1']
        #Setting the button to checkable 
        self.refresh_btn.clicked.connect(self.status_loop)
        
        # Listening for stopping and starting machines [main window 'tab1']
        #Setting the button to checkable 
        self.file_btn.clicked.connect(self.nav_open)

        self.blank_btn.clicked.connect(self.lock_pc)
        
        self.remote_btn_4.clicked.connect(self.remote_control_4)
        self.remote_btn_5.clicked.connect(self.remote_control_5)
        self.remote_btn_6.clicked.connect(self.remote_control_6)
        self.remote_btn_7.clicked.connect(self.remote_control_7)
        self.remote_btn_8.clicked.connect(self.remote_control_8)
        self.remote_btn_9.clicked.connect(self.remote_control_9)
        self.remote_btn_10.clicked.connect(self.remote_control_10)
        self.remote_btn_11.clicked.connect(self.remote_control_11)
        self.remote_btn_12.clicked.connect(self.remote_control_12)
        self.remote_btn_13.clicked.connect(self.remote_control_13)
        self.remote_btn_14.clicked.connect(self.remote_control_14)
        self.remote_btn_15.clicked.connect(self.remote_control_15)
        self.remote_btn_16.clicked.connect(self.remote_control_16)
        self.remote_btn_17.clicked.connect(self.remote_control_17)
        self.remote_btn_18.clicked.connect(self.remote_control_18)
        self.remote_btn_19.clicked.connect(self.remote_control_19)
        self.remote_btn_20.clicked.connect(self.remote_control_20)
        self.remote_btn_21.clicked.connect(self.remote_control_21)
        self.remote_btn_22.clicked.connect(self.remote_control_22)
        self.remote_btn_23.clicked.connect(self.remote_control_23)
        self.remote_btn_24.clicked.connect(self.remote_control_24)
        self.remote_btn_25.clicked.connect(self.remote_control_25)
        self.remote_btn_26.clicked.connect(self.remote_control_26)
        self.remote_btn_27.clicked.connect(self.remote_control_27)
        self.remote_btn_28.clicked.connect(self.remote_control_28)
        self.remote_btn_29.clicked.connect(self.remote_control_29)
        self.remote_btn_30.clicked.connect(self.remote_control_30)
        self.remote_btn_31.clicked.connect(self.remote_control_31)
        self.remote_btn_32.clicked.connect(self.remote_control_32)
        self.remote_btn_33.clicked.connect(self.remote_control_33)
        self.remote_btn_34.clicked.connect(self.remote_control_34)
        self.remote_btn_35.clicked.connect(self.remote_control_35)
        self.remote_btn_36.clicked.connect(self.remote_control_36)
        self.remote_btn_37.clicked.connect(self.remote_control_37)
        self.remote_btn_38.clicked.connect(self.remote_control_38)
        self.remote_btn_39.clicked.connect(self.remote_control_39)
        # self.remote_btn_40.clicked.connect(self.remote_control_40)
        
        
    #=================================================================#
    # This is will be all of the logic for the UI [Triggered by previous event handlsers]  #
    #=================================================================#
    
    def status_loop(self):
        
        for i in self.pc_ip:
            
            self.start_btn.setEnabled(False)
            self.refresh_btn.setEnabled(False)
            QtWidgets.QApplication.processEvents()    
            
            ##################################
            ## Second part of this function ##
            ##################################
        
        
            with open('/home/admin/OneLab-UI-Status/services/ip-ping/ping_{}.txt'.format(i), 'r') as file:
                
                data = file.read().replace('\n', '')
            
                currtent_machine = 'self.PC_{}'.format(i)
                current_label = 'self.label_{}'.format(i)
                        
                if data == 'True':
                    
                    eval(currtent_machine).setStyleSheet('background-color: lightgreen')
                    self.pixmap = QPixmap("/home/admin/OneLab-UI-Status/image-tracking/pc_{}.png".format(i))
                    self.pixmap.scaled(320 , 230)
                    eval(current_label).setPixmap(self.pixmap)
                    
                else:

                    eval(currtent_machine).setStyleSheet('background-color: red')
            
           # with open('/home/admin/OneLab-UI-Status/services/user-tracking/user_{}.txt'.format(i), 'r') as file:
                
                #self.user_data = file.read().replace('\n', '')
                #self.st_usr = 'self.display_name_{}'.format(i)

                # Set the label of each box to the name of the user
               # eval(self.st_usr).setText(self.user_data)

            self.start_btn.setEnabled(True)
            self.refresh_btn.setEnabled(True)
            continue 
    
    # This will pause all monitors and disable perifrials 
    def pause_func(self):
        
        # deactivating the pause button
        self.pause_btn.setEnabled(False)

        # Calling the thread that will handle sending the request to pause screens
        os.system('cd services/ && python run_disable.py & > /dev/null &')

    def play_func(self):
        
        # Resetting the pause button to active
        self.pause_btn.setEnabled(True)

        # Calling the thread the will handle re activating the perifrials
        os.system('cd services/ && python run_enable.py & > /dev/null')

    def lock_pc(self):

        self.pause_btn.setEnabled(False)

        os.system('cd services/ && python run_lock.py & /dev/null')

    # for tracking the status of the start button (checked or not checked)
    def on_off_switch(self):
        
        if self.start_btn.isChecked():
            
            # Setting pass until shutdown function is made
            print ('beep boop turned off')
            
        else:
            
            # If the button is not checked already this will call the status_loop function
            self.status_loop()
    
    # This function handles the looping part of check machines
    # I've separated this function set from the others in order to simplify the code. [GLOABAL]


    # Remote control
    def remote_control_4(self):
        os.system('echo 4 > services/remote_update/data.txt && cd services && ./remote_init.sh')
    def remote_control_5(self):
        os.system('echo 5 > services/remote_update/data.txt && cd services && ./remote_init.sh')
    def remote_control_6(self):
        os.system('echo 6 > services/remote_update/data.txt && cd services && ./remote_init.sh')
    def remote_control_7(self):
        os.system('echo 7 > services/remote_update/data.txt && cd services && ./remote_init.sh')
    def remote_control_8(self):
        os.system('echo 8 > services/remote_update/data.txt')
    def remote_control_9(self):
        os.system('echo 9 > services/remote_update/data.txt')
    def remote_control_10(self):
        os.system('echo 10 > services/remote_update/data.txt')
    def remote_control_11(self):
        os.system('echo 11 > services/remote_update/data.txt')
    def remote_control_12(self):
        os.system('echo 12 > services/remote_update/data.txt')
    def remote_control_13(self):
        os.system('echo 13 > services/remote_update/data.txt')
    def remote_control_14(self):
        os.system('echo 14 > services/remote_update/data.txt')
    def remote_control_15(self):
        os.system('echo 15 > services/remote_update/data.txt')
    def remote_control_16(self):
        os.system('echo 16 > services/remote_update/data.txt')
    def remote_control_17(self):
        os.system('echo 17 > services/remote_update/data.txt')
    def remote_control_18(self):
        os.system('echo 18 > services/remote_update/data.txt')
    def remote_control_19(self):
        os.system('echo 19 > services/remote_update/data.txt')
    def remote_control_20(self):
        os.system('echo 20 > services/remote_update/data.txt')
    def remote_control_21(self):
        os.system('echo 21 > services/remote_update/data.txt')
    def remote_control_22(self):
        os.system('echo 22 > services/remote_update/data.txt')
    def remote_control_23(self):
        os.system('echo 23 > services/remote_update/data.txt')
    def remote_control_24(self):
        os.system('echo 24 > services/remote_update/data.txt')
    def remote_control_25(self):
        os.system('echo 25 > services/remote_update/data.txt')
    def remote_control_26(self):
        os.system('echo 26 > services/remote_update/data.txt')
    def remote_control_27(self):
        os.system('echo 27 > services/remote_update/data.txt')
    def remote_control_28(self):
        os.system('echo 28 > services/remote_update/data.txt')
    def remote_control_29(self):
        os.system('echo 29 > services/remote_update/data.txt')
    def remote_control_30(self):
        os.system('echo 30 > services/remote_update/data.txt')
    def remote_control_31(self):
        os.system('echo 31 > services/remote_update/data.txt')
    def remote_control_32(self):
        os.system('echo 32 > services/remote_update/data.txt')
    def remote_control_33(self):
        os.system('echo 33 > services/remote_update/data.txt')
    def remote_control_34(self):
        os.system('echo 34 > services/remote_update/data.txt')
    def remote_control_35(self):
        os.system('echo 35 > services/remote_update/data.txt')
    def remote_control_36(self):
        os.system('echo 36 > services/remote_update/data.txt')
    def remote_control_37(self):
        os.system('echo 37 > services/remote_update/data.txt')
    def remote_control_38(self):
        os.system('echo 38 > services/remote_update/data.txt')
    def remote_control_39(self):
        os.system('echo 39 > services/remote_update/data.txt')
    #def remote_control_40(self):
        #os.system('echo 40 > services//remote_update.txt')
                    

    # Reciever for the start / stop button
    def stop_start(self):
        
        # Contains the attribute reference name [simplifies the code(Not necissary)]
        ss_btn = self.start_stop_btn
        
        # Function to change the color of the button when  it's selected.
        if ss_btn.isChecked():
            
            # Sets the button start / stop -> green when machine is turned on
            ss_btn.setStyleSheet("background-color: lightgreen") 
            
            # Sets the button pause / play -> green when machine is turned on
            self.pp_btn.setStyleSheet("background-color: lightgreen")
            
        else:
            
            # Sets color -> red when machine is turned off
            ss_btn.setStyleSheet("background-color: red")
            
            # Sets the button pause / play -> red when machine is turned on
            self.pp_btn.setStyleSheet("background-color: red")


    # Locking and unlocking student screens
    def pause_play(self):
        
        
        if self.pp_btn.isChecked():
            
            # Sets the button pause / play -> red when machine is paused
            self.pp_btn.setStyleSheet("background-color: red") 
            
            
        else:
            
            # Sets the button pause / play -> green when machine is turned on
            self.pp_btn.setStyleSheet("background-color: lightgreen")
            
            
    def nav_open(self):
            
        self.w = file_stream()
        self.w.show()
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':      
    main()
