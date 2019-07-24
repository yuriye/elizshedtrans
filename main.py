from PyQt5 import QtWidgets, uic, QtCore
import sys
import converter.convert as cvt
import traceback


class ScheduleConverter(QtWidgets.QMainWindow):
    ui: QtWidgets.QMainWindow

    def __init__(self):
        super(ScheduleConverter, self).__init__()
        self.ui = uic.loadUi("mainwin.ui")
        self.ui.fileSelectButton.clicked.connect(self.file_select)
        self.ui.templateFileSelectButton.clicked.connect(self.template_select)
        self.ui.convertButton.clicked.connect(self.convert_schedule)

    def file_select(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать файл', 'C:\\YandexDisk\\МФЦ\\Табели\\Елизово\\', 'Excel файлы (*.xlsx)')[0]
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.ui.fileNameEdit.setText(filename)
        self.ui.sheetSelector.addItems(cvt.get_sheetNames(filename))
        QtWidgets.QApplication.restoreOverrideCursor()

    def template_select(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать файл', 'C:\\data\\', 'Excel файлы (*.xlsx)')[0]
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.ui.templateFileNameEdit.setText(filename)
        QtWidgets.QApplication.restoreOverrideCursor()

    def convert_schedule(self):
        try:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            cvt.convert(self.ui.fileNameEdit.text(), self.ui.sheetSelector.currentText(), self.ui.templateFileNameEdit.text())
        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())
            sys.exit(app.exec())
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()


app = QtWidgets.QApplication([])
application = ScheduleConverter()
application.ui.show()
sys.exit(app.exec())
