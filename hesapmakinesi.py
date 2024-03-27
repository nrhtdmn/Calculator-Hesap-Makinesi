import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setFixedSize(319, 400)  # Uygulama boyutunu ayarla
        self.setupUI()

    def setupUI(self):
        self.operator = ""
        self.text_Input = QLineEdit()
        self.text_Input.setFixedSize(300, 111)  # LineEdit'in boyutunu ayarla
        font = self.text_Input.font()
        font.setPointSize(font.pointSize() + 10)
        self.text_Input.setFont(font)
        self.text_Input.setAlignment(Qt.AlignRight)
        self.text_Input.setReadOnly(True)

        buttons = [
            ("7", 0, 0),
            ("8", 0, 1),
            ("9", 0, 2),
            ("+", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("-", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("*", 2, 3),
            ("0", 3, 0),
            ("C", 3, 1),
            ("=", 3, 2),
            ("/", 3, 3),
        ]

        grid_layout = QGridLayout()
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(70, 51)  # Buton boyutunu ayarla
            button.clicked.connect(lambda _, text=text: self.btnClick(text))
            grid_layout.addWidget(button, row, col)

        layout = QVBoxLayout()
        layout.addWidget(self.text_Input)
        layout.addLayout(grid_layout)
        self.setLayout(layout)

        # # QSS stil dosyasını yükle
        # style_file = QFile("tasarim_hesapmakinesi.qss")
        # style_file.open(QFile.ReadOnly | QFile.Text)
        # stream = QTextStream(style_file)
        # app.setStyleSheet(stream.readAll())

    def btnClick(self, text):
        if text == "=":
            try:
                result = str(eval(self.operator))
                self.text_Input.setText(result)
            except:
                self.text_Input.setText("Hata")
            self.operator = ""
        elif text == "C":
            self.operator = ""
            self.text_Input.setText("")
        else:
            self.operator += text
            self.text_Input.setText(self.operator)

    def keyPressEvent(self, event):
        key = event.text()
        if key.isdigit() or key in "+-*/":
            self.operator += key
            self.text_Input.setText(self.operator)
        elif key == "=" or event.key() == Qt.Key_Enter:
            try:
                result = str(eval(self.operator))
                self.text_Input.setText(result)
            except:
                self.text_Input.setText("Hata")
            self.operator = ""
        elif event.key() == Qt.Key_Backspace:
            self.operator = self.operator[:-1]
            self.text_Input.setText(self.operator)
        elif event.key() == Qt.Key_Escape:
            self.operator = ""
            self.text_Input.setText("")


css_style = """

/* Genel stil kuralları */
* {
  background-color: #333333; /* Mavi arka plan */
  color: #FFFFFF; /* Beyaz yazı */
}



QLineEdit {
  background-color: #ffffff; /* Başlangıçta arka plan rengi beyaz */
}

QLineEdit:!enabled {
  background-color: #ffff00; /* İçeriği dolu olan QLineEdit'in arka plan rengi sarı */
}
/* QLineEdit stil kuralları */
QLineEdit {
  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */
  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */
  /*padding: 6px; /* İçerik dolgusu */
  background-color: #ffffff; /* Arka plan rengi */
  color: #333333; /* Yazı rengi */
}

/* QLineEdit hover efekti */
QLineEdit:hover {
  border-color: #3498db; /* Kenarlık rengi */
}

/* QLineEdit odaklandığında */
QLineEdit:focus {
  border-color: #3498db; /* Kenarlık rengi */
}

/* LineEdit stil kuralları */
QLineEdit {
  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */
  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */
  background-color: #ffffff; /* Arka plan rengi */
}

/* LineEdit üzerine gelindiğinde */
QLineEdit:hover {
  background-color: #ffff00; /* Sarı arka plan rengi */
}




/* Butonların stil kuralları */
QPushButton, QToolButton {
  background-color:  #333333; /* Arka plan rengi */
  color: #ffffff; /* Yazı rengi beyaz */
  border: 1px solid #b3ff26; /* Kenarlık */
  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */
  padding: 8px 16px; /* Buton içeriği için dolgular */
  font: 22px;
  

}

/* Buton hover efekti */
QPushButton:hover, QToolButton:hover {
  background-color: #2980b9; /* Hover rengi */
  border-color: #2980b9; /* Kenarlık rengi */
}

/* Buton basılma efekti */
QPushButton:pressed, QToolButton:pressed {
  background-color: #1f618d; /* Basılma rengi */
  border-color: #1f618d; /* Kenarlık rengi */
}


/* GroupBox stil kuralları */
QGroupBox {
  border: 2px solid grey;/*#ccc;*/ /* Kenarlık rengi ve kalınlığı */
  border-radius: 6px; /* Kenarlık köşeleri yuvarlatma */
  padding: 6px; /* İçerik dolgusu */
  background-color: #333333; /* Arka plan rengi */
  color: #ffffff; /* Yazı rengi */
}

/* GroupBox üzerine gelindiğinde */
QGroupBox:hover {
  background-color: #ffff00; /* Sarı arka plan rengi */
color:#ffffff /* Yazı rengi */
}

/* CheckButton ve RadioButton stil kuralları */
QCheckBox, QRadioButton {
  color: #ffffff; /* Yazı rengi */
}

/* CheckButton ve RadioButton üzerine gelindiğinde */
QCheckBox:hover, QRadioButton:hover {
  background-color: #ffff00; /* Sarı arka plan rengi */
  color: black; /* Yazı rengi */
  border-radius: 3px; /* Kenarlık köşeleri yuvarlatma */
  /*padding: 1px; /* İçerik dolgusu */
}

/*--------------------------------------------------------------------*/

/* StackedWidget ileri ve geri butonlarının stil kuralları */
QStackedWidget &gt; QAbstractButton {
  background-color: #333333; /* Arka plan rengi ile aynı renk */
  border: none; /* Kenarlık yok */
  width: 0; /* Genişlik sıfır */
  height: 0; /* Yükseklik sıfır */
}

/* İleri ve geri butonlarının üzerine gelindiğinde */
QStackedWidget &gt; QAbstractButton:hover {
  background-color: #333333; /* Arka plan rengi ile aynı renk */
}

/* Butonların stil kuralları */
QPushButton {
  background-color: #333333; /* Arka plan rengi */
  color: #ffffff; /* Yazı rengi beyaz */
  font-family: Arial; /* Yazı tipi Arial */
  font-size: 14pt; /* Yazı boyutu 14 pt */
  font-weight: bold; /* Kalın yazı tipi */
  width: 70px; /* Genişlik */
  height: 51px; /* Yükseklik */
  border: none; /* Kenarlık yok */
}

/* Buton hover efekti */
QPushButton:hover {
  background-color: #2980b9; /* Hover rengi */
}
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.resize(319, 400)  # Uygulama boyutunu ayarla
    calculator.show()
    app.setStyleSheet(css_style)  # CSS stilini uygula
    sys.exit(app.exec_())
