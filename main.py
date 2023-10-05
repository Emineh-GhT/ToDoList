from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import database #database.py khodm

class TODOList(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('design.ui', None)
        self.ui.show()

        self.ui.btn_add.clicked.connect(self.addNewTaskToDatabase)
        self.ReadFromDatabase()

    def ReadFromDatabase(self):
        results = database.getAll()

        for i in range(len(results)): #ezafe kardan be ui

            new_checkbox_done = QCheckBox()
            
            new_title = QLabel() 
            new_title.setText(results[i][1])

            new_priority = QLabel() 
            if results[i][6] == 1: #soton 7 db
                new_priority.setText("Important")
                new_priority.setStyleSheet("color: red;")
            elif results[i][6] == 0: #soton 7 db
                new_priority.setText("Unimportant")
                new_priority.setStyleSheet("color: black;")
            new_btn_description = QPushButton() 
            new_btn_description.setText('❗️')
            new_btn_delete = QPushButton() 
            new_btn_delete.setText('❌')

            if results[i][3] == 0: #done nashode
                new_checkbox_done.setChecked(False)
                self.ui.gridLayout_reminder.addWidget(new_checkbox_done, i, 0)
                new_checkbox_done.clicked.connect(partial(self.updateDone, results[i], new_checkbox_done))
                self.ui.gridLayout_reminder.addWidget(new_title, i, 1)
                self.ui.gridLayout_reminder.addWidget(new_priority, i, 2)
                self.ui.gridLayout_reminder.addWidget(new_btn_description, i, 3)
                new_btn_description.clicked.connect(partial(self.InfoDescription, results[i]))
                self.ui.gridLayout_reminder.addWidget(new_btn_delete, i, 4)
                new_btn_delete.clicked.connect(partial(self.DeleteFromDatabase, results[i]))
                          
            elif results[i][3] == 1: #done shode
                new_checkbox_done.setChecked(True)
                self.ui.gridLayout_done.addWidget(new_checkbox_done, i, 0)
                new_checkbox_done.clicked.connect(partial(self.updateDone, results[i], new_checkbox_done))
                self.ui.gridLayout_done.addWidget(new_title, i, 1)
                self.ui.gridLayout_done.addWidget(new_priority, i, 2)
                self.ui.gridLayout_done.addWidget(new_btn_description, i, 3)
                new_btn_description.clicked.connect(partial(self.InfoDescription, results[i]))
                self.ui.gridLayout_done.addWidget(new_btn_delete, i, 4)
                new_btn_delete.clicked.connect(partial(self.DeleteFromDatabase, results[i]))
                

    def addNewTaskToDatabase(self):
        done = 0
        title = self.ui.tb_title.text()
        description = self.ui.tb_description.text()
        if self.ui.RB_important.isChecked():
            priority = 1
        elif  self.ui.RB_unimportant.isChecked():
            priority = 0
        time = self.ui.tb_time.text()
        date = self.ui.tb_date.text()

        database.add(title, description, done, time, date, priority)
        self.ReadFromDatabase()

        self.ui.tb_title.setText('')
        self.ui.tb_description.setText('')
        self.ui.tb_time.setText('')
        self.ui.tb_date.setText('')
 
    def InfoDescription(self, i):
        msg = QMessageBox()
        msg.setWindowTitle('Description')
        msg.setText(f'Title : {i[1]}\nDescription : {i[2]}\nTime : {i[4]}\nDate : {i[5]}')
        msg.exec()

    def DeleteFromDatabase(self , i): 
        database.removeTask(i[0])
        self.clearLayout(self.ui.gridLayout_done)
        self.clearLayout(self.ui.gridLayout_reminder)
        self.ReadFromDatabase()
        
    def updateDone(self, i, new_checkbox_done):
        
        if new_checkbox_done.isChecked() == True:
            database.DoneUpdate(i[0] , 1)
            self.clearLayout(self.ui.gridLayout_reminder)
               
        elif new_checkbox_done.isChecked() == False:
            database.DoneUpdate(i[0] , 0)
            self.clearLayout(self.ui.gridLayout_done)
            
        self.ReadFromDatabase()

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()  


app = QApplication([])
window = TODOList()
app.exec()