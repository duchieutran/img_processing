from PyQt6 import QtCore, QtGui, QtWidgets
import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 429)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.buttondecode = QtWidgets.QPushButton(parent=self.centralwidget)
        self.buttondecode.setGeometry(QtCore.QRect(30, 280, 91, 31))
        self.buttondecode.setObjectName("buttondecode")
        self.buttonresset = QtWidgets.QPushButton(parent=self.centralwidget)
        self.buttonresset.setGeometry(QtCore.QRect(150, 280, 91, 31))
        self.buttonresset.setObjectName("buttonresset")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 91, 21))
        self.label_2.setObjectName("label_2")
        self.nhap_duong_dan = QtWidgets.QLineEdit(parent=self.groupBox)
        self.nhap_duong_dan.setGeometry(QtCore.QRect(90, 20, 271, 20))
        self.nhap_duong_dan.setObjectName("nhap_duong_dan")
        self.link_path = QtWidgets.QRadioButton(parent=self.groupBox)
        self.link_path.setGeometry(QtCore.QRect(0, 50, 80, 18))
        self.link_path.setObjectName("link_path")
        self.link_url = QtWidgets.QRadioButton(parent=self.groupBox)
        self.link_url.setGeometry(QtCore.QRect(80, 50, 80, 18))
        self.link_url.setObjectName("link_url")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 60, 361, 201))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.hien_thi_qrcode = QtWidgets.QLabel(parent=self.groupBox_2)
        self.hien_thi_qrcode.setGeometry(QtCore.QRect(16, 23, 150, 150))
        self.hien_thi_qrcode.setText("")
        self.hien_thi_qrcode.setObjectName("hien_thi_qrcode")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 150, 381, 101))
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(0, 30, 81, 21))
        self.checkBox.setObjectName("checkBox")
        self.lam_sang = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.lam_sang.setGeometry(QtCore.QRect(90, 30, 101, 21))
        self.lam_sang.setObjectName("lam_sang")
        self.histogram = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.histogram.setGeometry(QtCore.QRect(290, 30, 81, 21))
        self.histogram.setObjectName("histogram")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.checkBox_4.setGeometry(QtCore.QRect(200, 30, 67, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.value = QtWidgets.QDoubleSpinBox(parent=self.groupBox_3)
        self.value.setGeometry(QtCore.QRect(40, 70, 62, 22))
        self.value.setObjectName("value")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(0, 70, 51, 21))
        self.label_4.setObjectName("label_4")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(440, 260, 361, 121))
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.label_3.setObjectName("label_3")
        self.data = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.data.setGeometry(QtCore.QRect(50, 30, 311, 21))
        self.data.setReadOnly(True)
        self.data.setObjectName("data")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_5.setObjectName("label_5")
        self.data_2 = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.data_2.setGeometry(QtCore.QRect(80, 70, 281, 21))
        self.data_2.setReadOnly(True)
        self.data_2.setObjectName("data_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 320, 351, 20))
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # khu vực xử lý sự kiện
        self.buttondecode.clicked.connect(self.decode_qrcode)
        self.buttonresset.clicked.connect(self.reset_decode)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ĐỌC MÃ QRCODE"))
        self.buttondecode.setText(_translate("MainWindow", "DECODE"))
        self.buttonresset.setText(_translate("MainWindow", "RESET"))
        self.groupBox.setTitle(_translate("MainWindow", "Khu Vực Nhập "))
        self.label_2.setText(_translate("MainWindow", "Nhập đường dẫn : "))
        self.link_path.setText(_translate("MainWindow", "Link_Path"))
        self.link_url.setText(_translate("MainWindow", "URL"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Khu vực hiển thị QRCODE"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tính năng bổ sung"))
        self.checkBox.setText(_translate("MainWindow", "Lọc Nhiễu"))
        self.lam_sang.setText(_translate("MainWindow", "Làm Sáng / tối"))
        self.histogram.setText(_translate("MainWindow", "Histogram"))
        self.checkBox_4.setText(_translate("MainWindow", "Làm Mịn"))
        self.label_4.setText(_translate("MainWindow", "Value : "))
        self.groupBox_4.setTitle(_translate("MainWindow", "Khu vực hiển thị dữ liệu"))
        self.label_3.setText(_translate("MainWindow", "Data : "))
        self.label_5.setText(_translate("MainWindow", "Chất Lượng : "))


    def decode_qrcode(self):
        duong_dan = None
        if not self.link_path.isChecked() and not self.link_url.isChecked():
            self.lineEdit.setText("Vui lòng chọn một trong hai loại đường dẫn!")
            return
        if self.link_path.isChecked():
            file_path = self.nhap_duong_dan.text()
            duong_dan = cv.imread(file_path)
            if duong_dan is None:
                self.lineEdit.setText("Không thể đọc ảnh")
                return
        elif self.link_url.isChecked():
            url = self.nhap_duong_dan.text()
            try:
                response = requests.get(url)
                response.raise_for_status()
                image_array = np.frombuffer(response.content, np.uint8)
                duong_dan = cv.imdecode(image_array, cv.IMREAD_COLOR)
            except requests.RequestException as e:
                self.lineEdit.setText("Không thể đọc ảnh")


        #chỗ bên dưới test

        if self.lam_sang.isChecked():
            duong_dan = self.gamma(duong_dan, self.value.value())

        if self.histogram.isChecked():
            duong_dan = self.equalize_histogram(duong_dan)
        
        if self.checkBox_4.isChecked():
            duong_dan = self.img_filter(duong_dan)
        
        if self.checkBox.isChecked():
            duong_dan = self.denoise_image(duong_dan)


        # ------------------------------------------------------------------------------

        if duong_dan is not None:
            decoded_data, img_decoded = self.de_qrcode(duong_dan)

            if img_decoded is not None:
                height, width, channel = img_decoded.shape
                bytes_per_line = 3 * width
                q_img = QtGui.QImage(img_decoded.data, width, height, bytes_per_line,
                                     QtGui.QImage.Format.Format_RGB888).rgbSwapped()

                pixmap = QtGui.QPixmap.fromImage(q_img)
                self.hien_thi_qrcode.setPixmap(pixmap)
                self.hien_thi_qrcode.setScaledContents(True)

            if decoded_data:
                self.data.setText(decoded_data)
            else:
                self.data.setText("Không tìm thấy mã QR")
        else:
            self.lineEdit.setText("Vui lòng nhập đường dẫn ảnh.")


    def de_qrcode(self, img):
        if img is None:
            self.lineEdit.setText("Không thể đọc được ảnh, vui lòng kiểm tra lại đường dẫn!")
            return None, None

        rows, cols, _ = img.shape
        agel = 0
        for barcode in decode(img):
            if barcode.type != 'QRCODE':
                continue

            if barcode.orientation == 'DOWN':
                agel = 180
            elif barcode.orientation == 'RIGHT':
                agel = 90
            elif barcode.orientation == 'LEFT':
                agel = -90

        center = ((cols - 1) / 2, (rows - 1) / 2)
        m = cv.getRotationMatrix2D(center, agel, 1)
        img_rotated = cv.warpAffine(img, m, (cols, rows))

        decoded_data = None
        for barcode in decode(img_rotated):
            if barcode.type == 'QRCODE':
                decoded_data = barcode.data.decode('utf-8')
                break

        if decoded_data:
            Point = np.array(barcode.polygon, np.int32)
            if len(Point) == 4:  # Kiểm tra số lượng điểm cạnh
                aspect_ratio = (Point[2][0] - Point[0][0]) / (Point[2][1] - Point[0][1])
                quality = "Tốt" if 0.9 <= aspect_ratio <= 1.1 else "Trung Bình"

                self.data_2.setText(quality)

                pts1 = np.float32([Point[0], Point[3], Point[1], Point[2]])
                pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

                M = cv.getPerspectiveTransform(pts1, pts2)
                img_decoded = cv.warpPerspective(img_rotated, M, (300, 300))
                return decoded_data, img_decoded
            else:
                self.data_2.setText("Không tốt")
                return None, None
        else:
            self.data.setText("Không tìm thấy mã QR trong ảnh!")
            self.data_2.setText("N/A")
            return None, None


    # hàm histogram
    def equalize_histogram(self, image):
        # Chuyển đổi ảnh sang không gian màu YUV
        yuv_img = cv.cvtColor(image, cv.COLOR_BGR2YUV)
        # Chuyển đổi tuple thành list
        yuv_planes = list(cv.split(yuv_img))
        yuv_planes[0] = cv.equalizeHist(yuv_planes[0])
        # Ghép các kênh YUV lại
        equalized_yuv_img = cv.merge(yuv_planes)
        equalized_img = cv.cvtColor(equalized_yuv_img, cv.COLOR_YUV2BGR)
        return equalized_img


    # hàm xử lý nhiễu
    def denoise_image(self, image):
        # Áp dụng bộ lọc Gaussian Blur để xử lý nhiễu
        denoised_img = cv.GaussianBlur(image, (5, 5), 0)
        return denoised_img


    #Hàm gamma
    def gamma(self, img, g):
        img_gam = np.float32(img) / 255
        img_gam = np.power(img_gam, g) * 255
        return np.uint8(img_gam)


    #làm mịn ảnhh
    def img_filter(self, img):
        kernel = np.ones((3, 3), np.float32) / 9
        img_filtered = cv.filter2D(img, -1, kernel)
        return np.uint8(img_filtered)

    def reset_decode(self) :
        self.nhap_duong_dan.clear()
        self.lineEdit.clear()
        self.data.clear()
        self.data_2.clear()

        # Reset radio buttons
        self.link_path.setChecked(False)
        self.link_url.setChecked(False)

        # Reset checkboxes
        self.checkBox.setChecked(False)
        self.lam_sang.setChecked(False)
        self.histogram.setChecked(False)
        self.checkBox_4.setChecked(False)

        # Reset double spin box
        self.value.setValue(0)

        # Reset image display
        self.hien_thi_qrcode.clear()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
