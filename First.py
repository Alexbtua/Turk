from zipfile import ZipFile
import datatime




inputfile = "loc.txt"
outputfile = "log.txt"



fi = open(inputfile, mode='r', encoding='latina_1')
fo = open(outputfile, mode='a', encoding= 'latina_1')

zip = ZipFile('.zip', 'w')    # name now funk
for x in fi:
    zip.write(fi)

zip.close()






fo.write()
fi.close()
fo.close()