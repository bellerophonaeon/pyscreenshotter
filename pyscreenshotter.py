import PIL
import os
import datetime
import time
import random
import paramiko
import pyscreenshot as ImageGrab

paramiko.util.log_to_file('./paramiko.log')


if __name__ == "__main__":
    subname = 'sundreams-'
    for directory, subdirectories, files in os.walk('.'):
        for file in files:
            if subname in file:
                if '.jpg' in file:
                    print 'Deleting ' + os.path.join(directory, file)
                    os.remove(os.path.join(directory, file))
    while 1:
        # fullscreen screenshot
        im=ImageGrab.grab()
        filename = subname + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.jpg'
        im.save(filename)

        # set up sftp link
        host = ""
        port = 22
        transport = paramiko.Transport((host, port))
        password = ""
        username = ""
        print "opening connection"
        transport.connect(username = username, password = password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        print sftp
        # Upload
        filepath = filename
        localpath = filename
        print filename
        sftp.put(localpath, filepath)
        print "file uploaded"
        sftp.close()
        transport.close()

        time.sleep(random.randint(30,90))