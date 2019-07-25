from PyQt4 import QtGui, QtCore
import xml.etree.ElementTree as ET
import pandas
import sys
import os
import random

class MirGui(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MirGui, self).__init__(parent)
        self.mz_file = None
        self.tolerance = None
        self.output = None
        self.output_filename = None
        self.init_gui()

    def init_gui(self):
        self.mz_file = QtGui.QPushButton('Select m/z list .csv file...')
        self.tolerance = QtGui.QLineEdit('Tolerance (+/- Da)')
        self.output = QtGui.QPushButton('Select output directory...')
        self.output_filename = QtGui.QLineEdit('Output Filename')
        generate = QtGui.QPushButton('Generate Filter List')

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.mz_file, 1, 0)
        grid.addWidget(self.tolerance, 2, 0)
        grid.addWidget(self.output, 3, 0)
        grid.addWidget(self.output_filename, 4, 0)
        grid.addWidget(generate, 5, 0)
        self.setLayout(grid)

        self.center()
        self.setWindowTitle('Bruker flexImaging Filter List Generator')
        self.show()

        QtCore.QObject.connect(self.mz_file, QtCore.SIGNAL('clicked()'), self.get_csv_file)
        QtCore.QObject.connect(self.output, QtCore.SIGNAL('clicked()'), self.get_output_directory)
        QtCore.QObject.connect(generate, QtCore.SIGNAL('clicked()'), self.generate_filter_list)

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def get_csv_file(self):
        self.mz_file.setText(str(QtGui.QFileDialog.getOpenFileName(self, 'Open File', 'C:\\')).replace('/', '\\'))

    def get_output_directory(self):
        self.output.setText(str(QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory',
                                                                       'C:\\')).replace('/', '\\'))

    def write_mir(self, mz_list, tolerance, output):
        mir_object = ET.Element('ImagingResults', {'flexImagingVersion': '4.1.116.257', 'last_modified': ''})
        for mz in mz_list:
            attrib_dict = {'Type': 'PkFilter',
                           'Name': str(mz),
                           'Color': '#' + '%06x' % random.randint(0, 0xFFFFFF),
                           'Show': '0',
                           'MinIntensity': '0',
                           'IntensityThreshold': '100',
                           'AbsIntens': '0',
                           'LogScale': '0',
                           'MinMass': str(mz - tolerance),
                           'MaxMass': str(mz + tolerance),
                           'Integrate': '0',
                           'UsePercentile': '0',
                           'IntensityPercentile': '0.95',
                           'FindMass': '0',
                           'RelMass': '0'}
            result_object = ET.SubElement(mir_object, 'Result', attrib_dict)
            mir_object.append(result_object)
        mir_tree = ET.ElementTree(mir_object)
        mir_tree.write(os.path.join(output, str(self.output_filename.text())) + '.mir', method='xml')

    def generate_filter_list(self):
        mz_list = pandas.read_csv(str(self.mz_file.text()), usecols=['mz'])['mz'].values.tolist()
        self.write_mir(mz_list, float(self.tolerance.text()), str(self.output.text()))

def main():
    app = QtGui.QApplication(sys.argv)
    gui = MirGui()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
