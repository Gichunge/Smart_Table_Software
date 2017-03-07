from distutils.core import setup
import py2exe

setup(console=['APCS.py'])
setup(console=[
    {'script': "APCS.py",
     "icon_resources": [(0, "book_icon.ico")]
     }])
