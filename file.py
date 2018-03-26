import os
for filename in os.listdir('C:\Fizal\photos\New Folder'):
    try:
        if os.path.exists(filename):
            info = os.stat(filename)
            print info.st_mtime
        else:
            print "File Not Found " + filename
    except:
        print filename