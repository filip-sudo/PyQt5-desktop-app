from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        # MAIN WINDOW

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # LABEL FINANCIJE

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 50, 200, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")

        # BUTTON "NOVI UNOS"

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 200, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.novi_unos_win)

        # BUTTON "PREGLED"

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 400, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pregled_win)

        # MENU BAR

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 26))
        self.menubar.setObjectName("menubar")
        self.menuDatoteka = QtWidgets.QMenu(self.menubar)
        self.menuDatoteka.setObjectName("menuDatoteka")
        self.menuOpcije = QtWidgets.QMenu(self.menubar)
        self.menuOpcije.setObjectName("menuOpcije")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuDatoteka.addAction(self.actionSave)
        self.menuOpcije.addAction(self.actionCopy)
        self.menuOpcije.addAction(self.actionPaste)
        self.menubar.addAction(self.menuDatoteka.menuAction())
        self.menubar.addAction(self.menuOpcije.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Župa Uznesenja Blažene Djevice Marije, Zlatar"))
        self.label.setText(_translate("MainWindow", "Financije"))
        self.pushButton.setText(_translate("MainWindow", "Novi Unos"))
        self.pushButton_2.setText(_translate("MainWindow", "Pregled"))
        self.menuDatoteka.setTitle(_translate("MainWindow", "Datoteka"))
        self.actionSave.setText(_translate("MainWindow", "Spremi"))
        self.actionSave.setStatusTip(
            _translate("MainWindow", "Spremanje izmjena"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Kopiraj"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Kopiranje"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWIndow", "Zaljepi"))
        self.actionPaste.setStatusTip(
            _translate("MainWindow", "Zaljepi kopirano"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.menuOpcije.setTitle(_translate("MainWindow", "Opcije"))

    def novi_unos_win(self):
        self.NoviUnos = QtWidgets.QWidget()
        self.ui = Ui_NoviUnos()
        self.ui.setupUi(self.NoviUnos)
        self.NoviUnos.show()

    def pregled_win(self):
        self.Pregled = QtWidgets.QWidget()
        self.ui = Ui_Pregled()
        self.ui.setupUi(self.Pregled)
        self.Pregled.show()


class Ui_NoviUnos(object):

    def setupUi(self, NoviUnos):
        NoviUnos.setObjectName("NoviUnos")
        NoviUnos.resize(1280, 720)

        # Button Primitci

        self.pushButton = QtWidgets.QPushButton(NoviUnos)
        self.pushButton.setGeometry(QtCore.QRect(390, 200, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Unos_Primitci_win)

        # Button Izdatci

        self.pushButton_2 = QtWidgets.QPushButton(NoviUnos)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 400, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Unos_Izdatci_win)

        # Lable

        self.label = QtWidgets.QLabel(NoviUnos)
        self.label.setGeometry(QtCore.QRect(475, 50, 330, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(NoviUnos)
        QtCore.QMetaObject.connectSlotsByName(NoviUnos)

    def retranslateUi(self, NoviUnos):
        _translate = QtCore.QCoreApplication.translate
        NoviUnos.setWindowTitle(_translate("NoviUnos", "Novi Unos"))
        self.pushButton.setText(_translate("NoviUnos", "Primitci"))
        self.pushButton_2.setText(_translate("NoviUnos", "Izdatci"))
        self.label.setText(_translate("NoviUnos", "Novi Unos za:"))

    def Unos_Primitci_win(self):
        self.Unos_Primitci = QtWidgets.QWidget()
        self.ui = Ui_Unos_Primitci()
        self.ui.setupUi(self.Unos_Primitci)
        self.Unos_Primitci.show()

    def Unos_Izdatci_win(self):
        self.Unos_Izdatci = QtWidgets.QWidget()
        self.ui = Ui_Unos_Izdatci()
        self.ui.setupUi(self.Unos_Izdatci)
        self.Unos_Izdatci.show()


class Ui_Unos_Primitci(object):
    def setupUi(self, Unos_Primitci):
        Unos_Primitci.setObjectName("Unos_Primitci")
        Unos_Primitci.resize(1280, 720)

        # Combo box

        self.comboBox = QtWidgets.QComboBox(Unos_Primitci)
        self.comboBox.setGeometry(QtCore.QRect(230, 110, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        for i in range(0, 20):
            self.comboBox.addItem("")

        # Combo box 2

        self.comboBox2 = QtWidgets.QComboBox(Unos_Primitci)
        self.comboBox2.setGeometry(QtCore.QRect(650, 110, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox2.setFont(font)
        self.comboBox2.setObjectName("comboBox2")

        self.comboBox.currentIndexChanged.connect(self.combobox_check)

        # Lable_Iznos

        self.label_Iznos = QtWidgets.QLabel(Unos_Primitci)
        self.label_Iznos.setGeometry(QtCore.QRect(380, 290, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(44)
        font.setBold(False)
        font.setWeight(50)
        self.label_Iznos.setFont(font)
        self.label_Iznos.setObjectName("label_Iznos")

        # Lable_kn

        self.label_kn = QtWidgets.QLabel(Unos_Primitci)
        self.label_kn.setGeometry(QtCore.QRect(840, 290, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_kn.setFont(font)
        self.label_kn.setObjectName("label_kn")

        # Lable_Ukupno

        self.label_Ukupno = QtWidgets.QLabel(Unos_Primitci)
        self.label_Ukupno.setGeometry(QtCore.QRect(750, 600, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_Ukupno.setFont(font)
        self.label_Ukupno.setObjectName("label_Ukupno")

        # Button

        self.pushButton = QtWidgets.QPushButton(Unos_Primitci)
        self.pushButton.setGeometry(QtCore.QRect(390, 400, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.unos)

        # Line Edit

        self.lineEdit = QtWidgets.QLineEdit(Unos_Primitci)
        self.lineEdit.setGeometry(QtCore.QRect(530, 290, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.onlyDouble = QDoubleValidator()
        self.lineEdit.setValidator(self.onlyDouble)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        # Reset Button

        self.pushButton2 = QtWidgets.QPushButton(Unos_Primitci)
        self.pushButton2.setGeometry(QtCore.QRect(0, 670, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.reset)

        self.retranslateUi(Unos_Primitci)
        QtCore.QMetaObject.connectSlotsByName(Unos_Primitci)

    def retranslateUi(self, Unos_Primitci):
        _translate = QtCore.QCoreApplication.translate
        Unos_Primitci.setWindowTitle(
            _translate("Unos_Primitci", "Unos primitaka"))
        self.comboBox.setItemText(
            0, _translate("Unos_Primitci", "Redovita milostinja"))
        self.comboBox.setItemText(1, _translate(
            "Unos_Primitci", "Darovi prigodom blagoslova obitelji"))
        self.comboBox.setItemText(2, _translate(
            "Unos_Primitci", "Pristojbe prigodom podjeljivanja sakramenata i blagoslovina"))
        self.comboBox.setItemText(3, _translate(
            "Unos_Primitci", "Darovi kod krštenja i prve pričesti"))
        self.comboBox.setItemText(4, _translate(
            "Unos_Primitci", "Uredske pristojbe"))
        self.comboBox.setItemText(5, _translate(
            "Unos_Primitci", "Namjenski darovi za crkvu"))
        self.comboBox.setItemText(6, _translate(
            "Unos_Primitci", "Namjenska milostinja"))
        self.comboBox.setItemText(7, _translate(
            "Unos_Primitci", "Namjenske kolekte"))
        self.comboBox.setItemText(8, _translate(
            "Unos_Primitci", "Binacije i trinacije"))
        self.comboBox.setItemText(9, _translate(
            "Unos_Primitci", "Kolektivne misne nakane"))
        self.comboBox.setItemText(10, _translate(
            "Unos_Primitci", "Zaručnički tečaj"))
        self.comboBox.setItemText(11, _translate(
            "Unos_Primitci", "Prilog za prijevoz hodočasnika"))
        self.comboBox.setItemText(12, _translate(
            "Unos_Primitci", "Društveni prilozi"))
        self.comboBox.setItemText(13, _translate(
            "Unos_Primitci", "Prihodi od ekonomije župe"))
        self.comboBox.setItemText(14, _translate(
            "Unos_Primitci", "Vjerski tisak"))
        self.comboBox.setItemText(15, _translate(
            "Unos_Primitci", "Doprinos svećenika za domačinstvo"))
        self.comboBox.setItemText(16, _translate(
            "Unos_Primitci", "Pomoć UZUK-a za uzdržavanje svećenika"))
        self.comboBox.setItemText(17, _translate(
            "Unos_Primitci", "Izvanredne pomoći koje župa dobiva od NDS-a ili uz dopuštenje NDS-a"))
        self.comboBox.setItemText(18, _translate(
            "Unos_Primitci", "Novčani darovi za župni caritas"))
        self.comboBox.setItemText(19, _translate(
            "Unos_Primitci", "Maslinove grančice(Caritas, Misije)"))
        self.label_Iznos.setText(_translate("Unos_Primitci", "Iznos"))
        self.label_kn.setText(_translate("Unos_Primitci", "kn"))
        self.label_Ukupno.setText(_translate(
            "Unos_Primitci", "Ukupni iznos: "))
        self.pushButton.setText(_translate("Unos_Primitci", "Unesi"))
        self.pushButton2.setText(_translate("Unos_Primitci", "Reset"))

    def combobox_check(self):
        self.comboBox2.clear()
        if self.comboBox.currentText() == "Pristojbe prigodom podjeljivanja sakramenata i blagoslovina":
            self.comboBox2.clear()
            for i in range(0, 3):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Potvrda")
            self.comboBox2.setItemText(1, "Vjenčanja")
            self.comboBox2.setItemText(2, "Sprovodi")
        if self.comboBox.currentText() == "Darovi kod krštenja i prve pričesti":
            self.comboBox2.clear()
            for i in range(0, 2):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Krštenje")
            self.comboBox2.setItemText(1, "Prva Pričest")
        if self.comboBox.currentText() == "Namjenski darovi za crkvu":
            self.comboBox2.clear()
            for i in range(0, 4):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Izgradnja i obnova")
            self.comboBox2.setItemText(1, "Razne škrabice")
            self.comboBox2.setItemText(2, "Lukno, redovina...")
            self.comboBox2.setItemText(3, "Obiteljski dar")
        if self.comboBox.currentText() == "Namjenska milostinja":
            self.comboBox2.clear()
            for i in range(0, 4):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Božji grob")
            self.comboBox2.setItemText(1, "Petrov novčić")
            self.comboBox2.setItemText(2, "Misijska nedjelja")
            self.comboBox2.setItemText(3, "Nedjelja Caritasa")
        if self.comboBox.currentText() == "Društveni prilozi":
            self.comboBox2.clear()
            for i in range(0, 4):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Država")
            self.comboBox2.setItemText(1, "Županija")
            self.comboBox2.setItemText(2, "Grad ili Općina")
            self.comboBox2.setItemText(3, "Razni donatori")
        if self.comboBox.currentText() == "Prihodi od ekonomije župe":
            self.comboBox2.clear()
            for i in range(0, 4):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Zakupi i najamnine")
            self.comboBox2.setItemText(1, "Od prodaje nabožnih predmeta")
            self.comboBox2.setItemText(2, "Lučice/dušice")
            self.comboBox2.setItemText(3, "Kamate")
        if self.comboBox.currentText() == "Pomoć UZUK-a za uzdržavanje svećenika":
            self.comboBox2.clear()
            for i in range(0, 2):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Pomoć za nagradu")
            self.comboBox2.setItemText(1, "Dekanska nagrada")

    def unos(self):
        lista = [0, 1, 4, 8, 9, 10,
                 11, 14, 15, 17, 18, 19]
        value = (self.lineEdit.text())
        for i in range(0, 12):
            if self.comboBox.currentIndex() == lista[i]:
                f = open("Unos_Prihodi_QB", "r")
                pisanje = f.readlines()
                value = float(value) + float(pisanje[i])
                pisanje[i] = str(value) + "\n"
                f.close()
                f = open("Unos_Prihodi_QB", "w")
                f.writelines(pisanje)
                f.close()
        if self.comboBox.currentIndex() == 2:
            for i in range(0, 3):
                if self.comboBox2.currentIndex() == i:
                    f = open("Unos_Prihodi_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Prihodi_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 3:
            for i in range(3, 5):
                if self.comboBox2.currentIndex() == i-3:
                    f = open("Unos_Prihodi_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Prihodi_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 5:
            for i in range(5, 9):
                if self.comboBox2.currentIndex() == i-5:
                    f = open("Unos_Prihodi_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Prihodi_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 6:
            for i in range(9, 13):
                if self.comboBox2.currentIndex() == i-9:
                    f = open("Unos_Prihodi_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Prihodi_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 7:
            for i in range(13, 14):
                if self.comboBox2.currentIndex() == i-13:
                    f = open("Unos_Prihodi_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Prihodi_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 12:
            for i in range(14, 18):
                if self.comboBox2.currentIndex() == i-14:
                    f = open("Unos_Prihodi_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Prihodi_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 13:
            for i in range(18, 22):
                if self.comboBox2.currentIndex() == i-18:
                    f = open("Unos_Prihodi_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Prihodi_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 16:
            for i in range(22, 24):
                if self.comboBox2.currentIndex() == i-22:
                    f = open("Unos_Prihodi_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Prihodi_QB2", "w")
                    f.writelines(pisanje)
                    f.close()

    def reset(self):
        for i in range(0, 12):
            f = open("Unos_Prihodi_QB", "r")
            pisanje = f.readlines()
            pisanje[i] = "0.00\n"
            f.close()
            f = open("Unos_Prihodi_QB", "w")
            f.writelines(pisanje)
            f.close()
        for i in range(0, 24):
            f = open("Unos_Prihodi_QB2", "r")
            pisanje = f.readlines()
            pisanje[i] = "0.00\n"
            f.close()
            f = open("Unos_Prihodi_QB2", "w")
            f.writelines(pisanje)
            f.close()


class Ui_Unos_Izdatci(object):
    def setupUi(self, Unos_Izdatci):
        Unos_Izdatci.setObjectName("Unos_Izdatci")
        Unos_Izdatci.resize(1280, 720)

        # Combo box

        self.comboBox = QtWidgets.QComboBox(Unos_Izdatci)
        self.comboBox.setGeometry(QtCore.QRect(230, 110, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        for i in range(0, 16):
            self.comboBox.addItem("")

        # Combo box 2

        self.comboBox2 = QtWidgets.QComboBox(Unos_Izdatci)
        self.comboBox2.setGeometry(QtCore.QRect(650, 110, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox2.setFont(font)
        self.comboBox2.setObjectName("comboBox2")
        for i in range(0, 2):
            self.comboBox2.addItem("")
        self.comboBox2.setItemText(0, "Nagrada župniku")
        self.comboBox2.setItemText(1, "Nagrada župnom vikaru / supsidijaru")

        self.comboBox.currentIndexChanged.connect(self.combobox_check)

        # Lable_Iznos

        self.label_Iznos = QtWidgets.QLabel(Unos_Izdatci)
        self.label_Iznos.setGeometry(QtCore.QRect(380, 290, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(44)
        font.setBold(False)
        font.setWeight(50)
        self.label_Iznos.setFont(font)
        self.label_Iznos.setObjectName("label_Iznos")

        # Lable_kn

        self.label_kn = QtWidgets.QLabel(Unos_Izdatci)
        self.label_kn.setGeometry(QtCore.QRect(840, 290, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_kn.setFont(font)
        self.label_kn.setObjectName("label_kn")

        # Lable_Ukupno

        self.label_Ukupno = QtWidgets.QLabel(Unos_Izdatci)
        self.label_Ukupno.setGeometry(QtCore.QRect(750, 600, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_Ukupno.setFont(font)
        self.label_Ukupno.setObjectName("label_Ukupno")

        # Button

        self.pushButton = QtWidgets.QPushButton(Unos_Izdatci)
        self.pushButton.setGeometry(QtCore.QRect(390, 400, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.unos)

        # Line Edit

        self.lineEdit = QtWidgets.QLineEdit(Unos_Izdatci)
        self.lineEdit.setGeometry(QtCore.QRect(530, 290, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.onlyDouble = QDoubleValidator()
        self.lineEdit.setValidator(self.onlyDouble)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        # Reset Button

        self.pushButton2 = QtWidgets.QPushButton(Unos_Izdatci)
        self.pushButton2.setGeometry(QtCore.QRect(0, 670, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.reset)

        self.retranslateUi(Unos_Izdatci)
        QtCore.QMetaObject.connectSlotsByName(Unos_Izdatci)

    def retranslateUi(self, Unos_Izdatci):
        _translate = QtCore.QCoreApplication.translate
        Unos_Izdatci.setWindowTitle(
            _translate("Unos_Izdatci", "Unos izdataka"))
        self.comboBox.setItemText(
            0, _translate("Unos_Izdatci", "Nagrada svećenicima u župi"))
        self.comboBox.setItemText(1, _translate(
            "Unos_Izdatci", "Nagrade za pomoć u blagoslovu obitelji"))
        self.comboBox.setItemText(2, _translate(
            "Unos_Izdatci", "Prigodne nagrade"))
        self.comboBox.setItemText(3, _translate(
            "Unos_Izdatci", "Nagrade ostalim crkvenim suradnicima"))
        self.comboBox.setItemText(4, _translate(
            "Unos_Izdatci", "Potrebe bogoslužja"))
        self.comboBox.setItemText(5, _translate(
            "Unos_Izdatci", "Potrebe pastorala"))
        self.comboBox.setItemText(6, _translate(
            "Unos_Izdatci", "Režijski troškovi za crkvu i župnu kuću, vjeronaučnu dvoranu..."))
        self.comboBox.setItemText(7, _translate(
            "Unos_Izdatci", "Troškovi za župnu kuću i domaćinstvo"))
        self.comboBox.setItemText(8, _translate(
            "Unos_Izdatci", "Redovito održavanje crkvenih zgrada"))
        self.comboBox.setItemText(9, _translate(
            "Unos_Izdatci", "Veći radovi na crkvenim zgradama ili novogradnje"))
        self.comboBox.setItemText(10, _translate(
            "Unos_Izdatci", "Obveze župe prema Nadbiskupiji"))
        self.comboBox.setItemText(11, _translate(
            "Unos_Izdatci", "Vizitacijske pristojbe"))
        self.comboBox.setItemText(12, _translate(
            "Unos_Izdatci", "Za župe povjerene redovnicima"))
        self.comboBox.setItemText(13, _translate(
            "Unos_Izdatci", "Novčani izdaci župnog Caritasa"))
        self.comboBox.setItemText(14, _translate(
            "Unos_Izdatci", "Porez na dobit"))
        self.comboBox.setItemText(15, _translate(
            "Unos_Izdatci", "PDV"))
        self.label_Iznos.setText(_translate("Unos_Izdatci", "Iznos"))
        self.label_kn.setText(_translate("Unos_Izdatci", "kn"))
        self.label_Ukupno.setText(_translate(
            "Unos_Izdatci", "Ukupni iznos: "))
        self.pushButton.setText(_translate("Unos_Izdatci", "Unesi"))
        self.pushButton2.setText(_translate("Unos_Izdatci", "Reset"))

    def combobox_check(self):
        self.comboBox2.clear()
        if self.comboBox.currentText() == "Nagrada svećenicima u župi":
            self.comboBox2.clear()
            for i in range(0, 2):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Nagrada župniku")
            self.comboBox2.setItemText(
                1, "Nagrada župnom vikaru / supsidijaru")
        if self.comboBox.currentText() == "Nagrade ostalim crkvenim suradnicima":
            self.comboBox2.clear()
            for i in range(0, 4):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Orguljaš/zborovođa")
            self.comboBox2.setItemText(1, "Zvonar/sakristan")
            self.comboBox2.setItemText(2, "Domaćica")
            self.comboBox2.setItemText(3, "Čistaćica")
        if self.comboBox.currentText() == "Potrebe bogoslužja":
            self.comboBox2.clear()
            for i in range(0, 4):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(
                0, "Liturgijsko ruho i posuđe, predmeti za liturgiju")
            self.comboBox2.setItemText(
                1, "Hostije, misno vino, svijeće, tamjan")
            self.comboBox2.setItemText(
                2, "Uređenje crkve, cvijeće, sredstva za čišćenje itd.")
            self.comboBox2.setItemText(
                3, "Opremanje crkve (slike, kipovi, tehnički uređaji, namještaj ...")
        if self.comboBox.currentText() == "Potrebe pastorala":
            self.comboBox2.clear()
            for i in range(0, 7):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(
                0, "Troškovi organiziranja župnih slavlja")
            self.comboBox2.setItemText(
                1, "Troškovi za minstrante, pjevače, ŽEV, ŽPV itd.")
            self.comboBox2.setItemText(
                2, "Opremanje dvorane i katehetska pomagala")
            self.comboBox2.setItemText(
                3, "Troškovi uredskog poslovanja: materijal i pribor, poštarina, bankovne naknade itd.")
            self.comboBox2.setItemText(
                4, "Troškovi župnih tiskovina, interneta, mrežne stranice itd.")
            self.comboBox2.setItemText(
                5, "Troškovi prijevoza u pastoralne svrhe")
            self.comboBox2.setItemText(6, "Troškovi prijevoza hodočasnika")
        if self.comboBox.currentText() == "Režijski troškovi za crkvu i župnu kuću, vjeronaučnu dvoranu...":
            self.comboBox2.clear()
            for i in range(0, 8):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Voda, KN, NUV")
            self.comboBox2.setItemText(1, "Struja")
            self.comboBox2.setItemText(2, "Plin")
            self.comboBox2.setItemText(3, "Loživo ulje, drva i dr.")
            self.comboBox2.setItemText(4, "Telefon, internet, faks")
            self.comboBox2.setItemText(5, "Odvoz otpada")
            self.comboBox2.setItemText(6, "Naknade za župne grobove")
            self.comboBox2.setItemText(7, "RTV pristojba")
        if self.comboBox.currentText() == "Troškovi za župnu kuću i domaćinstvo":
            self.comboBox2.clear()
            for i in range(0, 4):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Prehrana, kućne potrepštine itd.")
            self.comboBox2.setItemText(1, "Sredstva, pribor za čišćenje itd.")
            self.comboBox2.setItemText(
                2, "Uređaji: nabava pećnice, hladnjaka itd.")
            self.comboBox2.setItemText(3, "Namještaj - nabava")
        if self.comboBox.currentText() == "Redovito održavanje crkvenih zgrada":
            self.comboBox2.clear()
            for i in range(0, 3):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(
                0, "Sitniji popravci, servisiranje uređaja itd.")
            self.comboBox2.setItemText(
                1, "Osiguranje zgrada kod osigura. kuće itd.")
            self.comboBox2.setItemText(2, "Uređenje okoliša")
        if self.comboBox.currentText() == "Veći radovi na crkvenim zgradama ili novogradnje":
            self.comboBox2.clear()
            for i in range(0, 2):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Župna crkva i kapele")
            self.comboBox2.setItemText(1, "Župni dvor, dvorana")
        if self.comboBox.currentText() == "Obveze župe prema Nadbiskupiji":
            self.comboBox2.clear()
            for i in range(0, 11):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Obiteljski dar")
            self.comboBox2.setItemText(1, "Mirovinski fond-ONS")
            self.comboBox2.setItemText(2, "Binacije i trinacije")
            self.comboBox2.setItemText(3, "Kolektivne nakane")
            self.comboBox2.setItemText(
                4, "Pristojbe od vjenčanja, sprovoda, krizme i drugih potvrda")
            self.comboBox2.setItemText(5, "Misijska nedjelja")
            self.comboBox2.setItemText(6, "Božji grob")
            self.comboBox2.setItemText(7, "Petrov novčić")
            self.comboBox2.setItemText(8, "Nedjelja Caritasa")
            self.comboBox2.setItemText(
                9, "Nedjelja solidarnosti i zajedništva s Crkvom i ljudima u BiH")
            self.comboBox2.setItemText(
                10, "Maslinove grančice(Caritas, Misije)")
        if self.comboBox.currentText() == "Vizitacijske pristojbe":
            self.comboBox2.clear()
            for i in range(0, 1):
                self.comboBox2.addItem("")
            self.comboBox2.setItemText(0, "Arhiđ. ili Dek.")

    def unos(self):
        lista = [1, 2, 12, 13, 14,
                 15]
        value = (self.lineEdit.text())
        for i in range(0, 6):
            if self.comboBox.currentIndex() == lista[i]:
                f = open("Unos_Izdatci_QB", "r")
                pisanje = f.readlines()
                value = float(value) + float(pisanje[i])
                pisanje[i] = str(value) + "\n"
                f.close()
                f = open("Unos_Izdatci_QB", "w")
                f.writelines(pisanje)
                f.close()
        if self.comboBox.currentIndex() == 0:
            for i in range(0, 2):
                if self.comboBox2.currentIndex() == i:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 3:
            for i in range(2, 6):
                if self.comboBox2.currentIndex() == i-2:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 4:
            for i in range(6, 10):
                if self.comboBox2.currentIndex() == i-6:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 5:
            for i in range(10, 17):
                if self.comboBox2.currentIndex() == i-10:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 6:
            for i in range(17, 25):
                if self.comboBox2.currentIndex() == i-17:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 7:
            for i in range(25, 29):
                if self.comboBox2.currentIndex() == i-25:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 8:
            for i in range(29, 32):
                if self.comboBox2.currentIndex() == i-29:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 9:
            for i in range(32, 34):
                if self.comboBox2.currentIndex() == i-32:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 10:
            for i in range(34, 45):
                if self.comboBox2.currentIndex() == i-34:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()
        if self.comboBox.currentIndex() == 11:
            for i in range(45, 46):
                if self.comboBox2.currentIndex() == i-45:
                    f = open("Unos_Izdatci_QB2", "r")
                    pisanje = f.readlines()
                    value = float(value) + float(pisanje[i])
                    pisanje[i] = str(value) + "\n"
                    f.close()
                    f = open("Unos_Izdatci_QB2", "w")
                    f.writelines(pisanje)
                    f.close()

    def reset(self):
        for i in range(0, 6):
            f = open("Unos_Izdatci_QB", "r")
            pisanje = f.readlines()
            pisanje[i] = "0.00\n"
            f.close()
            f = open("Unos_Izdatci_QB", "w")
            f.writelines(pisanje)
            f.close()
        for i in range(0, 46):
            f = open("Unos_Izdatci_QB2", "r")
            pisanje = f.readlines()
            pisanje[i] = "0.00\n"
            f.close()
            f = open("Unos_Izdatci_QB2", "w")
            f.writelines(pisanje)
            f.close()


class Ui_Pregled(object):
    def setupUi(self, Pregled):
        Pregled.setObjectName("Pregled")
        Pregled.resize(1280, 720)

        # Button Primitci

        self.pushButton = QtWidgets.QPushButton(Pregled)
        self.pushButton.setGeometry(QtCore.QRect(565, 180, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # Button Izdatci

        self.pushButton_2 = QtWidgets.QPushButton(Pregled)
        self.pushButton_2.setGeometry(QtCore.QRect(565, 310, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        # Lable

        self.label = QtWidgets.QLabel(Pregled)
        self.label.setGeometry(QtCore.QRect(450, 20, 480, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Pregled)
        QtCore.QMetaObject.connectSlotsByName(Pregled)

    def retranslateUi(self, Pregled):
        _translate = QtCore.QCoreApplication.translate
        Pregled.setWindowTitle(_translate("Pregled", "Pregled"))
        self.pushButton.setText(_translate("Pregled", "Primitci"))
        self.pushButton_2.setText(_translate("Pregled", "Izdatci"))
        self.label.setText(_translate("Pregled", "Pregled za:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
