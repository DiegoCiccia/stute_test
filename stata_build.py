import shutil
import os

version = "1.0.0"

source_dir = os.getcwd()
project = source_dir.split('\\')[-1]
destination_pkg = source_dir + "\\Stata\\dist\\"
try:
    os.mkdir(destination_pkg)
except:
    pass

build = [
    "ado\\stute_test.ado",
    "help\\stute_test.sthlp",
    "help\\stute_test.html",
    "pkg\\stata.toc",
    "pkg\\stute_test.pkg"
    ]
for v in build:
    shutil.copyfile(source_dir + "\\Stata\\" + v, destination_pkg + "\\" + v.split("\\")[1])
print("Version ", version, " packaged")