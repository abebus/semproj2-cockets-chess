# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chess.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self._77 = QtWidgets.QPushButton(self.centralwidget)
        self._77.setMaximumSize(QtCore.QSize(35, 35))
        self._77.setText("")
        self._77.setObjectName("_77")
        self.gridLayout.addWidget(self._77, 2, 6, 1, 1)
        self._41 = QtWidgets.QPushButton(self.centralwidget)
        self._41.setMaximumSize(QtCore.QSize(35, 35))
        self._41.setText("")
        self._41.setObjectName("_41")
        self.gridLayout.addWidget(self._41, 8, 3, 1, 1)
        self.d = QtWidgets.QPushButton(self.centralwidget)
        self.d.setMaximumSize(QtCore.QSize(35, 35))
        self.d.setFlat(True)
        self.d.setObjectName("d")
        self.gridLayout.addWidget(self.d, 0, 3, 1, 1)
        self._83 = QtWidgets.QPushButton(self.centralwidget)
        self._83.setMaximumSize(QtCore.QSize(35, 35))
        self._83.setText("")
        self._83.setObjectName("_83")
        self.gridLayout.addWidget(self._83, 6, 7, 1, 1)
        self.c = QtWidgets.QPushButton(self.centralwidget)
        self.c.setEnabled(True)
        self.c.setMaximumSize(QtCore.QSize(35, 35))
        self.c.setFlat(True)
        self.c.setObjectName("c")
        self.gridLayout.addWidget(self.c, 0, 2, 1, 1)
        self._14 = QtWidgets.QPushButton(self.centralwidget)
        self._14.setMaximumSize(QtCore.QSize(35, 35))
        self._14.setText("")
        self._14.setObjectName("_14")
        self.gridLayout.addWidget(self._14, 5, 0, 1, 1)
        self._21 = QtWidgets.QPushButton(self.centralwidget)
        self._21.setMaximumSize(QtCore.QSize(35, 35))
        self._21.setText("")
        self._21.setObjectName("_21")
        self.gridLayout.addWidget(self._21, 8, 1, 1, 1)
        self._28 = QtWidgets.QPushButton(self.centralwidget)
        self._28.setMaximumSize(QtCore.QSize(35, 35))
        self._28.setText("")
        self._28.setObjectName("_28")
        self.gridLayout.addWidget(self._28, 1, 1, 1, 1)
        self._47 = QtWidgets.QPushButton(self.centralwidget)
        self._47.setMaximumSize(QtCore.QSize(35, 35))
        self._47.setText("")
        self._47.setObjectName("_47")
        self.gridLayout.addWidget(self._47, 2, 3, 1, 1)
        self._34 = QtWidgets.QPushButton(self.centralwidget)
        self._34.setMaximumSize(QtCore.QSize(35, 35))
        self._34.setText("")
        self._34.setObjectName("_34")
        self.gridLayout.addWidget(self._34, 5, 2, 1, 1)
        self._3 = QtWidgets.QPushButton(self.centralwidget)
        self._3.setMaximumSize(QtCore.QSize(35, 35))
        self._3.setFlat(True)
        self._3.setObjectName("_3")
        self.gridLayout.addWidget(self._3, 6, 8, 1, 1)
        self._12 = QtWidgets.QPushButton(self.centralwidget)
        self._12.setMaximumSize(QtCore.QSize(35, 35))
        self._12.setText("")
        self._12.setObjectName("_12")
        self.gridLayout.addWidget(self._12, 7, 0, 1, 1)
        self._37 = QtWidgets.QPushButton(self.centralwidget)
        self._37.setMaximumSize(QtCore.QSize(35, 35))
        self._37.setText("")
        self._37.setObjectName("_37")
        self.gridLayout.addWidget(self._37, 2, 2, 1, 1)
        self._58 = QtWidgets.QPushButton(self.centralwidget)
        self._58.setMaximumSize(QtCore.QSize(35, 35))
        self._58.setText("")
        self._58.setObjectName("_58")
        self.gridLayout.addWidget(self._58, 1, 4, 1, 1)
        self._25 = QtWidgets.QPushButton(self.centralwidget)
        self._25.setMaximumSize(QtCore.QSize(35, 35))
        self._25.setText("")
        self._25.setObjectName("_25")
        self.gridLayout.addWidget(self._25, 4, 1, 1, 1)
        self._85 = QtWidgets.QPushButton(self.centralwidget)
        self._85.setMaximumSize(QtCore.QSize(35, 35))
        self._85.setText("")
        self._85.setObjectName("_85")
        self.gridLayout.addWidget(self._85, 4, 7, 1, 1)
        self._38 = QtWidgets.QPushButton(self.centralwidget)
        self._38.setMaximumSize(QtCore.QSize(35, 35))
        self._38.setText("")
        self._38.setObjectName("_38")
        self.gridLayout.addWidget(self._38, 1, 2, 1, 1)
        self._72 = QtWidgets.QPushButton(self.centralwidget)
        self._72.setMaximumSize(QtCore.QSize(35, 35))
        self._72.setText("")
        self._72.setObjectName("_72")
        self.gridLayout.addWidget(self._72, 7, 6, 1, 1)
        self._6 = QtWidgets.QPushButton(self.centralwidget)
        self._6.setMaximumSize(QtCore.QSize(35, 35))
        self._6.setFlat(True)
        self._6.setObjectName("_6")
        self.gridLayout.addWidget(self._6, 3, 8, 1, 1)
        self._35 = QtWidgets.QPushButton(self.centralwidget)
        self._35.setEnabled(True)
        self._35.setMaximumSize(QtCore.QSize(35, 35))
        self._35.setText("")
        self._35.setObjectName("_35")
        self.gridLayout.addWidget(self._35, 4, 2, 1, 1)
        self._67 = QtWidgets.QPushButton(self.centralwidget)
        self._67.setMaximumSize(QtCore.QSize(35, 35))
        self._67.setText("")
        self._67.setObjectName("_67")
        self.gridLayout.addWidget(self._67, 2, 5, 1, 1)
        self._57 = QtWidgets.QPushButton(self.centralwidget)
        self._57.setMaximumSize(QtCore.QSize(35, 35))
        self._57.setText("")
        self._57.setObjectName("_57")
        self.gridLayout.addWidget(self._57, 2, 4, 1, 1)
        self.f = QtWidgets.QPushButton(self.centralwidget)
        self.f.setMaximumSize(QtCore.QSize(35, 35))
        self.f.setFlat(True)
        self.f.setObjectName("f")
        self.gridLayout.addWidget(self.f, 0, 5, 1, 1)
        self._17 = QtWidgets.QPushButton(self.centralwidget)
        self._17.setMaximumSize(QtCore.QSize(35, 35))
        self._17.setText("")
        self._17.setObjectName("_17")
        self.gridLayout.addWidget(self._17, 2, 0, 1, 1)
        self._33 = QtWidgets.QPushButton(self.centralwidget)
        self._33.setMaximumSize(QtCore.QSize(35, 35))
        self._33.setText("")
        self._33.setObjectName("_33")
        self.gridLayout.addWidget(self._33, 6, 2, 1, 1)
        self._32 = QtWidgets.QPushButton(self.centralwidget)
        self._32.setMaximumSize(QtCore.QSize(35, 35))
        self._32.setText("")
        self._32.setObjectName("_32")
        self.gridLayout.addWidget(self._32, 7, 2, 1, 1)
        self._16 = QtWidgets.QPushButton(self.centralwidget)
        self._16.setMaximumSize(QtCore.QSize(35, 35))
        self._16.setText("")
        self._16.setObjectName("_16")
        self.gridLayout.addWidget(self._16, 3, 0, 1, 1)
        self._63 = QtWidgets.QPushButton(self.centralwidget)
        self._63.setMaximumSize(QtCore.QSize(35, 35))
        self._63.setText("")
        self._63.setObjectName("_63")
        self.gridLayout.addWidget(self._63, 6, 5, 1, 1)
        self._61 = QtWidgets.QPushButton(self.centralwidget)
        self._61.setMaximumSize(QtCore.QSize(35, 35))
        self._61.setText("")
        self._61.setObjectName("_61")
        self.gridLayout.addWidget(self._61, 8, 5, 1, 1)
        self.corner = QtWidgets.QPushButton(self.centralwidget)
        self.corner.setMaximumSize(QtCore.QSize(35, 35))
        self.corner.setText("")
        self.corner.setFlat(True)
        self.corner.setObjectName("corner")
        self.gridLayout.addWidget(self.corner, 0, 8, 1, 1)
        self._46 = QtWidgets.QPushButton(self.centralwidget)
        self._46.setMaximumSize(QtCore.QSize(35, 35))
        self._46.setText("")
        self._46.setObjectName("_46")
        self.gridLayout.addWidget(self._46, 3, 3, 1, 1)
        self.a = QtWidgets.QPushButton(self.centralwidget)
        self.a.setEnabled(True)
        self.a.setMaximumSize(QtCore.QSize(35, 35))
        self.a.setFlat(True)
        self.a.setObjectName("a")
        self.gridLayout.addWidget(self.a, 0, 0, 1, 1)
        self._78 = QtWidgets.QPushButton(self.centralwidget)
        self._78.setMaximumSize(QtCore.QSize(35, 35))
        self._78.setText("")
        self._78.setObjectName("_78")
        self.gridLayout.addWidget(self._78, 1, 6, 1, 1)
        self._56 = QtWidgets.QPushButton(self.centralwidget)
        self._56.setMaximumSize(QtCore.QSize(35, 35))
        self._56.setText("")
        self._56.setObjectName("_56")
        self.gridLayout.addWidget(self._56, 3, 4, 1, 1)
        self._84 = QtWidgets.QPushButton(self.centralwidget)
        self._84.setMaximumSize(QtCore.QSize(35, 35))
        self._84.setText("")
        self._84.setObjectName("_84")
        self.gridLayout.addWidget(self._84, 5, 7, 1, 1)
        self._81 = QtWidgets.QPushButton(self.centralwidget)
        self._81.setMaximumSize(QtCore.QSize(35, 35))
        self._81.setText("")
        self._81.setObjectName("_81")
        self.gridLayout.addWidget(self._81, 8, 7, 1, 1)
        self._15 = QtWidgets.QPushButton(self.centralwidget)
        self._15.setMaximumSize(QtCore.QSize(35, 35))
        self._15.setText("")
        self._15.setObjectName("_15")
        self.gridLayout.addWidget(self._15, 4, 0, 1, 1)
        self._45 = QtWidgets.QPushButton(self.centralwidget)
        self._45.setMaximumSize(QtCore.QSize(35, 35))
        self._45.setText("")
        self._45.setObjectName("_45")
        self.gridLayout.addWidget(self._45, 4, 3, 1, 1)
        self._51 = QtWidgets.QPushButton(self.centralwidget)
        self._51.setMaximumSize(QtCore.QSize(35, 35))
        self._51.setText("")
        self._51.setObjectName("_51")
        self.gridLayout.addWidget(self._51, 8, 4, 1, 1)
        self._31 = QtWidgets.QPushButton(self.centralwidget)
        self._31.setMaximumSize(QtCore.QSize(35, 35))
        self._31.setText("")
        self._31.setObjectName("_31")
        self.gridLayout.addWidget(self._31, 8, 2, 1, 1)
        self._54 = QtWidgets.QPushButton(self.centralwidget)
        self._54.setMaximumSize(QtCore.QSize(35, 35))
        self._54.setText("")
        self._54.setObjectName("_54")
        self.gridLayout.addWidget(self._54, 5, 4, 1, 1)
        self._66 = QtWidgets.QPushButton(self.centralwidget)
        self._66.setMaximumSize(QtCore.QSize(35, 35))
        self._66.setText("")
        self._66.setObjectName("_66")
        self.gridLayout.addWidget(self._66, 3, 5, 1, 1)
        self._7 = QtWidgets.QPushButton(self.centralwidget)
        self._7.setMaximumSize(QtCore.QSize(35, 35))
        self._7.setFlat(True)
        self._7.setObjectName("_7")
        self.gridLayout.addWidget(self._7, 2, 8, 1, 1)
        self._87 = QtWidgets.QPushButton(self.centralwidget)
        self._87.setMaximumSize(QtCore.QSize(35, 35))
        self._87.setText("")
        self._87.setObjectName("_87")
        self.gridLayout.addWidget(self._87, 2, 7, 1, 1)
        self._26 = QtWidgets.QPushButton(self.centralwidget)
        self._26.setMaximumSize(QtCore.QSize(35, 35))
        self._26.setText("")
        self._26.setObjectName("_26")
        self.gridLayout.addWidget(self._26, 3, 1, 1, 1)
        self.g = QtWidgets.QPushButton(self.centralwidget)
        self.g.setMaximumSize(QtCore.QSize(35, 35))
        self.g.setFlat(True)
        self.g.setObjectName("g")
        self.gridLayout.addWidget(self.g, 0, 6, 1, 1)
        self._55 = QtWidgets.QPushButton(self.centralwidget)
        self._55.setMaximumSize(QtCore.QSize(35, 35))
        self._55.setText("")
        self._55.setObjectName("_55")
        self.gridLayout.addWidget(self._55, 4, 4, 1, 1)
        self._13 = QtWidgets.QPushButton(self.centralwidget)
        self._13.setMaximumSize(QtCore.QSize(35, 35))
        self._13.setText("")
        self._13.setObjectName("_13")
        self.gridLayout.addWidget(self._13, 6, 0, 1, 1)
        self._24 = QtWidgets.QPushButton(self.centralwidget)
        self._24.setMaximumSize(QtCore.QSize(35, 35))
        self._24.setText("")
        self._24.setObjectName("_24")
        self.gridLayout.addWidget(self._24, 5, 1, 1, 1)
        self._5 = QtWidgets.QPushButton(self.centralwidget)
        self._5.setMaximumSize(QtCore.QSize(35, 35))
        self._5.setFlat(True)
        self._5.setObjectName("_5")
        self.gridLayout.addWidget(self._5, 4, 8, 1, 1)
        self._82 = QtWidgets.QPushButton(self.centralwidget)
        self._82.setMaximumSize(QtCore.QSize(35, 35))
        self._82.setText("")
        self._82.setObjectName("_82")
        self.gridLayout.addWidget(self._82, 7, 7, 1, 1)
        self._73 = QtWidgets.QPushButton(self.centralwidget)
        self._73.setMaximumSize(QtCore.QSize(35, 35))
        self._73.setText("")
        self._73.setObjectName("_73")
        self.gridLayout.addWidget(self._73, 6, 6, 1, 1)
        self._52 = QtWidgets.QPushButton(self.centralwidget)
        self._52.setMaximumSize(QtCore.QSize(35, 35))
        self._52.setText("")
        self._52.setObjectName("_52")
        self.gridLayout.addWidget(self._52, 7, 4, 1, 1)
        self._65 = QtWidgets.QPushButton(self.centralwidget)
        self._65.setMaximumSize(QtCore.QSize(35, 35))
        self._65.setText("")
        self._65.setObjectName("_65")
        self.gridLayout.addWidget(self._65, 4, 5, 1, 1)
        self.h = QtWidgets.QPushButton(self.centralwidget)
        self.h.setMaximumSize(QtCore.QSize(35, 35))
        self.h.setFlat(True)
        self.h.setObjectName("h")
        self.gridLayout.addWidget(self.h, 0, 7, 1, 1)
        self._4 = QtWidgets.QPushButton(self.centralwidget)
        self._4.setMaximumSize(QtCore.QSize(35, 35))
        self._4.setFlat(True)
        self._4.setObjectName("_4")
        self.gridLayout.addWidget(self._4, 5, 8, 1, 1)
        self._53 = QtWidgets.QPushButton(self.centralwidget)
        self._53.setMaximumSize(QtCore.QSize(35, 35))
        self._53.setText("")
        self._53.setObjectName("_53")
        self.gridLayout.addWidget(self._53, 6, 4, 1, 1)
        self._36 = QtWidgets.QPushButton(self.centralwidget)
        self._36.setMaximumSize(QtCore.QSize(35, 35))
        self._36.setText("")
        self._36.setObjectName("_36")
        self.gridLayout.addWidget(self._36, 3, 2, 1, 1)
        self._71 = QtWidgets.QPushButton(self.centralwidget)
        self._71.setMaximumSize(QtCore.QSize(35, 35))
        self._71.setText("")
        self._71.setObjectName("_71")
        self.gridLayout.addWidget(self._71, 8, 6, 1, 1)
        self._75 = QtWidgets.QPushButton(self.centralwidget)
        self._75.setMaximumSize(QtCore.QSize(35, 35))
        self._75.setText("")
        self._75.setObjectName("_75")
        self.gridLayout.addWidget(self._75, 4, 6, 1, 1)
        self._43 = QtWidgets.QPushButton(self.centralwidget)
        self._43.setMaximumSize(QtCore.QSize(35, 35))
        self._43.setText("")
        self._43.setObjectName("_43")
        self.gridLayout.addWidget(self._43, 6, 3, 1, 1)
        self._27 = QtWidgets.QPushButton(self.centralwidget)
        self._27.setMaximumSize(QtCore.QSize(35, 35))
        self._27.setText("")
        self._27.setObjectName("_27")
        self.gridLayout.addWidget(self._27, 2, 1, 1, 1)
        self._62 = QtWidgets.QPushButton(self.centralwidget)
        self._62.setMaximumSize(QtCore.QSize(35, 35))
        self._62.setText("")
        self._62.setObjectName("_62")
        self.gridLayout.addWidget(self._62, 7, 5, 1, 1)
        self._22 = QtWidgets.QPushButton(self.centralwidget)
        self._22.setMaximumSize(QtCore.QSize(35, 35))
        self._22.setText("")
        self._22.setObjectName("_22")
        self.gridLayout.addWidget(self._22, 7, 1, 1, 1)
        self._48 = QtWidgets.QPushButton(self.centralwidget)
        self._48.setMaximumSize(QtCore.QSize(35, 35))
        self._48.setText("")
        self._48.setObjectName("_48")
        self.gridLayout.addWidget(self._48, 1, 3, 1, 1)
        self._42 = QtWidgets.QPushButton(self.centralwidget)
        self._42.setMaximumSize(QtCore.QSize(35, 35))
        self._42.setText("")
        self._42.setObjectName("_42")
        self.gridLayout.addWidget(self._42, 7, 3, 1, 1)
        self.b = QtWidgets.QPushButton(self.centralwidget)
        self.b.setEnabled(True)
        self.b.setMaximumSize(QtCore.QSize(35, 35))
        self.b.setFlat(True)
        self.b.setObjectName("b")
        self.gridLayout.addWidget(self.b, 0, 1, 1, 1)
        self._1 = QtWidgets.QPushButton(self.centralwidget)
        self._1.setMaximumSize(QtCore.QSize(35, 35))
        self._1.setFlat(True)
        self._1.setObjectName("_1")
        self.gridLayout.addWidget(self._1, 8, 8, 1, 1)
        self._74 = QtWidgets.QPushButton(self.centralwidget)
        self._74.setMaximumSize(QtCore.QSize(35, 35))
        self._74.setText("")
        self._74.setObjectName("_74")
        self.gridLayout.addWidget(self._74, 5, 6, 1, 1)
        self._8 = QtWidgets.QPushButton(self.centralwidget)
        self._8.setMaximumSize(QtCore.QSize(35, 35))
        self._8.setFlat(True)
        self._8.setObjectName("_8")
        self.gridLayout.addWidget(self._8, 1, 8, 1, 1)
        self._64 = QtWidgets.QPushButton(self.centralwidget)
        self._64.setMaximumSize(QtCore.QSize(35, 35))
        self._64.setText("")
        self._64.setObjectName("_64")
        self.gridLayout.addWidget(self._64, 5, 5, 1, 1)
        self.e = QtWidgets.QPushButton(self.centralwidget)
        self.e.setMaximumSize(QtCore.QSize(35, 35))
        self.e.setFlat(True)
        self.e.setObjectName("e")
        self.gridLayout.addWidget(self.e, 0, 4, 1, 1)
        self._44 = QtWidgets.QPushButton(self.centralwidget)
        self._44.setMaximumSize(QtCore.QSize(35, 35))
        self._44.setText("")
        self._44.setObjectName("_44")
        self.gridLayout.addWidget(self._44, 5, 3, 1, 1)
        self._23 = QtWidgets.QPushButton(self.centralwidget)
        self._23.setMaximumSize(QtCore.QSize(35, 35))
        self._23.setText("")
        self._23.setObjectName("_23")
        self.gridLayout.addWidget(self._23, 6, 1, 1, 1)
        self._2 = QtWidgets.QPushButton(self.centralwidget)
        self._2.setMaximumSize(QtCore.QSize(35, 35))
        self._2.setFlat(True)
        self._2.setObjectName("_2")
        self.gridLayout.addWidget(self._2, 7, 8, 1, 1)
        self._86 = QtWidgets.QPushButton(self.centralwidget)
        self._86.setMaximumSize(QtCore.QSize(35, 35))
        self._86.setText("")
        self._86.setObjectName("_86")
        self.gridLayout.addWidget(self._86, 3, 7, 1, 1)
        self._76 = QtWidgets.QPushButton(self.centralwidget)
        self._76.setMaximumSize(QtCore.QSize(35, 35))
        self._76.setText("")
        self._76.setObjectName("_76")
        self.gridLayout.addWidget(self._76, 3, 6, 1, 1)
        self._88 = QtWidgets.QPushButton(self.centralwidget)
        self._88.setMaximumSize(QtCore.QSize(35, 35))
        self._88.setText("")
        self._88.setObjectName("_88")
        self.gridLayout.addWidget(self._88, 1, 7, 1, 1)
        self._18 = QtWidgets.QPushButton(self.centralwidget)
        self._18.setMaximumSize(QtCore.QSize(35, 35))
        self._18.setText("")
        self._18.setObjectName("_18")
        self.gridLayout.addWidget(self._18, 1, 0, 1, 1)
        self._11 = QtWidgets.QPushButton(self.centralwidget)
        self._11.setMaximumSize(QtCore.QSize(35, 35))
        self._11.setText("")
        self._11.setObjectName("_11")
        self.gridLayout.addWidget(self._11, 8, 0, 1, 1)
        self._68 = QtWidgets.QPushButton(self.centralwidget)
        self._68.setMaximumSize(QtCore.QSize(35, 35))
        self._68.setText("")
        self._68.setObjectName("_68")
        self.gridLayout.addWidget(self._68, 1, 5, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chat_history = QtWidgets.QTextEdit(self.centralwidget)
        self.chat_history.setReadOnly(True)
        self.chat_history.setObjectName("chat_history")
        self.verticalLayout.addWidget(self.chat_history)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_emojis = QtWidgets.QPushButton(self.centralwidget)
        self.btn_emojis.setMaximumSize(QtCore.QSize(35, 35))
        self.btn_emojis.setObjectName("btn_emojis")
        self.horizontalLayout_2.addWidget(self.btn_emojis)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.btn_send_msg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_msg.setMaximumSize(QtCore.QSize(50, 35))
        self.btn_send_msg.setObjectName("btn_send_msg")
        self.horizontalLayout_2.addWidget(self.btn_send_msg)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ============================================================

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.d.setText(_translate("MainWindow", "d"))
        self.c.setText(_translate("MainWindow", "c"))
        self._3.setText(_translate("MainWindow", "3"))
        self._6.setText(_translate("MainWindow", "6"))
        self.f.setText(_translate("MainWindow", "f"))
        self.a.setText(_translate("MainWindow", "a"))
        self._7.setText(_translate("MainWindow", "7"))
        self.g.setText(_translate("MainWindow", "g"))
        self._5.setText(_translate("MainWindow", "5"))
        self.h.setText(_translate("MainWindow", "h"))
        self._4.setText(_translate("MainWindow", "4"))
        self.b.setText(_translate("MainWindow", "b"))
        self._1.setText(_translate("MainWindow", "1"))
        self._8.setText(_translate("MainWindow", "8"))
        self.e.setText(_translate("MainWindow", "e"))
        self._2.setText(_translate("MainWindow", "2"))
        self.btn_emojis.setText(_translate("MainWindow", ":)"))
        self.btn_send_msg.setText(_translate("MainWindow", "Send"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
