import zipfile
import time
# import os
# import shutil
# import sys

inputfile = "location.txt"
outputfile = "log.txt"

f1 = open(inputfile, mode='r', encoding='utf_8')
f2 = open(outputfile, mode='a', encoding='utf_8')
name_zip = str(time.strftime("%Y%m%d-%H%M%S")) + ".zip"
zip_archive = zipfile.ZipFile(name_zip, 'w')
for num, line in enumerate(f1, 1):
    zip_archive.write(line.strip(), compress_type=zipfile.ZIP_DEFLATED)

zip_archive.close()

f1.close()
f2.close()
