# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
#pip install future
setup(
    windows = [{
        'script': 'simple_ocr_barcode_scanner_gui.py',
		'icon_resources': [(1, 'simple_ocr_barcode_scanner.ico')],
        'copyright': 'GNU General Public License v3.0',
		'name':'Simple OCR Barcode Scanner',
		'version':'1.0',
		'description':'Barcode scanner from image or folder',
		'author':'Xosé Brais Noya García',
    }],
    #options = {
        #'py2exe': {
            #'dll_excludes': ['libmmd.dll','mkl_rt.dll','libopenblas.TXA6YQSD3GCQQC22GEQ54J2UDCXDXHWN.gfortran-win_amd64.dll','svml_dispmd.dll']
        #}
    #},
)