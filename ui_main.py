# Form implementation generated from reading ui file 'c:\Users\Mayhm\Desktop\py\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.firstFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.firstFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.firstFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.firstFrame.setObjectName("firstFrame")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.firstFrame)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.videoGroup = QtWidgets.QGroupBox(parent=self.firstFrame)
        self.videoGroup.setObjectName("videoGroup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.videoGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=self.videoGroup)
        self.widget.setMaximumSize(QtCore.QSize(550, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.videoDir = QtWidgets.QLineEdit(parent=self.widget)
        self.videoDir.setReadOnly(True)
        self.videoDir.setObjectName("videoDir")
        self.horizontalLayout_2.addWidget(self.videoDir)
        self.findVideoDir = QtWidgets.QPushButton(parent=self.widget)
        self.findVideoDir.setObjectName("findVideoDir")
        self.horizontalLayout_2.addWidget(self.findVideoDir)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(parent=self.videoGroup)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chooseVideoFormat = QtWidgets.QComboBox(parent=self.widget_2)
        self.chooseVideoFormat.setObjectName("chooseVideoFormat")
        self.chooseVideoFormat.addItem("")
        self.horizontalLayout_3.addWidget(self.chooseVideoFormat)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout_16.addWidget(self.videoGroup)
        self.verticalLayout.addWidget(self.firstFrame)
        self.secondFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.secondFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.secondFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.secondFrame.setObjectName("secondFrame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.secondFrame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.audioGroup = QtWidgets.QGroupBox(parent=self.secondFrame)
        self.audioGroup.setObjectName("audioGroup")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.audioGroup)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_4 = QtWidgets.QWidget(parent=self.audioGroup)
        self.widget_4.setMinimumSize(QtCore.QSize(550, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(550, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.chooseAudioFormat = QtWidgets.QComboBox(parent=self.widget_4)
        self.chooseAudioFormat.setObjectName("chooseAudioFormat")
        self.chooseAudioFormat.addItem("")
        self.horizontalLayout_8.addWidget(self.chooseAudioFormat)
        self.audioQuality = QtWidgets.QLineEdit(parent=self.widget_4)
        self.audioQuality.setMaximumSize(QtCore.QSize(100, 16777215))
        self.audioQuality.setObjectName("audioQuality")
        self.horizontalLayout_8.addWidget(self.audioQuality)
        self.horizontalLayout_7.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(parent=self.audioGroup)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.withAudio = QtWidgets.QRadioButton(parent=self.widget_6)
        self.withAudio.setAutoFillBackground(False)
        self.withAudio.setChecked(True)
        self.withAudio.setObjectName("withAudio")
        self.horizontalLayout_23.addWidget(self.withAudio)
        self.withoutAudio = QtWidgets.QRadioButton(parent=self.widget_6)
        self.withoutAudio.setObjectName("withoutAudio")
        self.horizontalLayout_23.addWidget(self.withoutAudio)
        self.horizontalLayout_7.addWidget(self.widget_6)
        self.horizontalLayout_10.addWidget(self.audioGroup)
        self.verticalLayout.addWidget(self.secondFrame)
        self.thirdFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.thirdFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.thirdFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.thirdFrame.setObjectName("thirdFrame")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.thirdFrame)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.subGroup = QtWidgets.QGroupBox(parent=self.thirdFrame)
        self.subGroup.setObjectName("subGroup")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.subGroup)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_7 = QtWidgets.QWidget(parent=self.subGroup)
        self.widget_7.setMinimumSize(QtCore.QSize(480, 0))
        self.widget_7.setMaximumSize(QtCore.QSize(480, 16777215))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.subDir = QtWidgets.QLineEdit(parent=self.widget_7)
        self.subDir.setReadOnly(True)
        self.subDir.setObjectName("subDir")
        self.horizontalLayout_12.addWidget(self.subDir)
        self.findSubDir = QtWidgets.QPushButton(parent=self.widget_7)
        self.findSubDir.setObjectName("findSubDir")
        self.horizontalLayout_12.addWidget(self.findSubDir)
        self.horizontalLayout_11.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(parent=self.subGroup)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.chooseSubFormat = QtWidgets.QComboBox(parent=self.widget_8)
        self.chooseSubFormat.setObjectName("chooseSubFormat")
        self.chooseSubFormat.addItem("")
        self.chooseSubFormat.addItem("")
        self.horizontalLayout_13.addWidget(self.chooseSubFormat)
        self.horizontalLayout_11.addWidget(self.widget_8)
        self.widget_5 = QtWidgets.QWidget(parent=self.subGroup)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.withSub = QtWidgets.QRadioButton(parent=self.widget_5)
        self.withSub.setChecked(True)
        self.withSub.setObjectName("withSub")
        self.horizontalLayout_9.addWidget(self.withSub)
        self.withoutSub = QtWidgets.QRadioButton(parent=self.widget_5)
        self.withoutSub.setObjectName("withoutSub")
        self.horizontalLayout_9.addWidget(self.withoutSub)
        self.horizontalLayout_11.addWidget(self.widget_5)
        self.horizontalLayout_15.addWidget(self.subGroup)
        self.verticalLayout.addWidget(self.thirdFrame)
        self.fourthFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.fourthFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fourthFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fourthFrame.setObjectName("fourthFrame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.fourthFrame)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.generalGroup = QtWidgets.QGroupBox(parent=self.fourthFrame)
        self.generalGroup.setObjectName("generalGroup")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.generalGroup)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_3 = QtWidgets.QWidget(parent=self.generalGroup)
        self.widget_3.setMaximumSize(QtCore.QSize(350, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.crfNum = QtWidgets.QLineEdit(parent=self.widget_3)
        self.crfNum.setObjectName("crfNum")
        self.horizontalLayout_5.addWidget(self.crfNum)
        self.preset = QtWidgets.QComboBox(parent=self.widget_3)
        self.preset.setObjectName("preset")
        self.preset.addItem("")
        self.preset.addItem("")
        self.preset.addItem("")
        self.preset.addItem("")
        self.preset.addItem("")
        self.preset.addItem("")
        self.preset.addItem("")
        self.preset.addItem("")
        self.preset.addItem("")
        self.horizontalLayout_5.addWidget(self.preset)
        self.horizontalLayout_4.addWidget(self.widget_3)
        self.frame_4 = QtWidgets.QFrame(parent=self.generalGroup)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.videoWidth = QtWidgets.QLineEdit(parent=self.frame_4)
        self.videoWidth.setObjectName("videoWidth")
        self.horizontalLayout_6.addWidget(self.videoWidth)
        self.videoHeight = QtWidgets.QLineEdit(parent=self.frame_4)
        self.videoHeight.setObjectName("videoHeight")
        self.horizontalLayout_6.addWidget(self.videoHeight)
        self.timeStart = QtWidgets.QLineEdit(parent=self.frame_4)
        self.timeStart.setObjectName("timeStart")
        self.horizontalLayout_6.addWidget(self.timeStart)
        self.timeEnd = QtWidgets.QLineEdit(parent=self.frame_4)
        self.timeEnd.setObjectName("timeEnd")
        self.horizontalLayout_6.addWidget(self.timeEnd)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.horizontalLayout_14.addWidget(self.generalGroup)
        self.verticalLayout.addWidget(self.fourthFrame)
        self.fifithFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.fifithFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fifithFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fifithFrame.setObjectName("fifithFrame")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.fifithFrame)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.outputGroup = QtWidgets.QGroupBox(parent=self.fifithFrame)
        self.outputGroup.setObjectName("outputGroup")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.outputGroup)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.widget_9 = QtWidgets.QWidget(parent=self.outputGroup)
        self.widget_9.setMaximumSize(QtCore.QSize(550, 16777215))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.outputDir = QtWidgets.QLineEdit(parent=self.widget_9)
        self.outputDir.setReadOnly(True)
        self.outputDir.setObjectName("outputDir")
        self.horizontalLayout_20.addWidget(self.outputDir)
        self.findOutputDir = QtWidgets.QPushButton(parent=self.widget_9)
        self.findOutputDir.setObjectName("findOutputDir")
        self.horizontalLayout_20.addWidget(self.findOutputDir)
        self.horizontalLayout_19.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(parent=self.outputGroup)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.execute = QtWidgets.QPushButton(parent=self.widget_10)
        self.execute.setObjectName("execute")
        self.horizontalLayout_21.addWidget(self.execute)
        self.horizontalLayout_19.addWidget(self.widget_10)
        self.horizontalLayout_22.addWidget(self.outputGroup)
        self.verticalLayout.addWidget(self.fifithFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.withoutAudio.clicked.connect(self.chooseAudioFormat.hide) # type: ignore
        self.withoutAudio.clicked.connect(self.audioQuality.hide) # type: ignore
        self.withAudio.clicked.connect(self.chooseAudioFormat.show) # type: ignore
        self.withAudio.clicked.connect(self.audioQuality.show) # type: ignore
        self.withoutSub.clicked.connect(self.subDir.hide) # type: ignore
        self.withoutSub.clicked.connect(self.findSubDir.hide) # type: ignore
        self.withoutSub.clicked.connect(self.chooseSubFormat.hide) # type: ignore
        self.withSub.clicked.connect(self.subDir.show) # type: ignore
        self.withSub.clicked.connect(self.findSubDir.show) # type: ignore
        self.withSub.clicked.connect(self.chooseSubFormat.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.videoGroup.setTitle(_translate("MainWindow", "Vídeo"))
        self.videoDir.setToolTip(_translate("MainWindow", "<html><head/><body><p>Diretório do vídeo</p></body></html>"))
        self.findVideoDir.setText(_translate("MainWindow", "Procurar"))
        self.chooseVideoFormat.setToolTip(_translate("MainWindow", "<html><head/><body><p>Formato do vídeo final</p></body></html>"))
        self.chooseVideoFormat.setItemText(0, _translate("MainWindow", "MP4"))
        self.audioGroup.setTitle(_translate("MainWindow", "Áudio"))
        self.chooseAudioFormat.setToolTip(_translate("MainWindow", "<html><head/><body><p>Formato do áudio final</p></body></html>"))
        self.chooseAudioFormat.setItemText(0, _translate("MainWindow", "AAC"))
        self.audioQuality.setToolTip(_translate("MainWindow", "<html><head/><body><p>Bitrate do áudio final</p></body></html>"))
        self.audioQuality.setText(_translate("MainWindow", "128k"))
        self.withAudio.setText(_translate("MainWindow", "C/Áudio"))
        self.withoutAudio.setText(_translate("MainWindow", "S/Áudio"))
        self.subGroup.setTitle(_translate("MainWindow", "Legenda"))
        self.subDir.setToolTip(_translate("MainWindow", "<html><head/><body><p>Diretório da legenda</p></body></html>"))
        self.findSubDir.setText(_translate("MainWindow", "Procurar"))
        self.chooseSubFormat.setToolTip(_translate("MainWindow", "<html><head/><body><p>Formato da legenda final</p></body></html>"))
        self.chooseSubFormat.setItemText(0, _translate("MainWindow", "SRT"))
        self.chooseSubFormat.setItemText(1, _translate("MainWindow", "ASS"))
        self.withSub.setText(_translate("MainWindow", "C/Legenda"))
        self.withoutSub.setText(_translate("MainWindow", "S/Legenda"))
        self.generalGroup.setTitle(_translate("MainWindow", "Geral"))
        self.crfNum.setToolTip(_translate("MainWindow", "<html><head/><body><p>CRF</p></body></html>"))
        self.crfNum.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.crfNum.setText(_translate("MainWindow", "18"))
        self.preset.setToolTip(_translate("MainWindow", "<html><head/><body><p>Preset de velocidade</p></body></html>"))
        self.preset.setItemText(0, _translate("MainWindow", "ultrafast"))
        self.preset.setItemText(1, _translate("MainWindow", "superfast"))
        self.preset.setItemText(2, _translate("MainWindow", "veryfast"))
        self.preset.setItemText(3, _translate("MainWindow", "faster"))
        self.preset.setItemText(4, _translate("MainWindow", "fast"))
        self.preset.setItemText(5, _translate("MainWindow", "medium"))
        self.preset.setItemText(6, _translate("MainWindow", "slow"))
        self.preset.setItemText(7, _translate("MainWindow", "slower"))
        self.preset.setItemText(8, _translate("MainWindow", "veryslow"))
        self.frame_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.videoWidth.setText(_translate("MainWindow", "1920"))
        self.videoHeight.setText(_translate("MainWindow", "1080"))
        self.timeStart.setToolTip(_translate("MainWindow", "<html><head/><body><p>Tempo de início para conversão</p></body></html>"))
        self.timeStart.setText(_translate("MainWindow", "00:00:00.000"))
        self.timeEnd.setToolTip(_translate("MainWindow", "<html><head/><body><p>Tempo de fim para conversão</p></body></html>"))
        self.timeEnd.setText(_translate("MainWindow", "00:00:00.000"))
        self.outputGroup.setTitle(_translate("MainWindow", "Saída"))
        self.outputDir.setToolTip(_translate("MainWindow", "<html><head/><body><p>Diretório de saída</p></body></html>"))
        self.findOutputDir.setText(_translate("MainWindow", "Procurar"))
        self.execute.setText(_translate("MainWindow", "Executar"))
