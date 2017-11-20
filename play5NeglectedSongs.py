#!/usr/bin/python                                                                                                                                                       

import sys
import subprocess
from subprocess import call
import os, time


def main():
    music_list = []
    directory = "/var/music"
    for root, dirs, files in os.walk(directory, topdown=False):
        if root != directory:
            for f in files:
                ff = os.path.join(root, f)
                music_list.append((ff, os.stat(ff).st_atime))

    music_list.sort(key=lambda tup: tup[1])
    for m in range(0,5):
        try:                                                                                                                                                            
            _ = subprocess.check_output(["vlc", music_list[m][0]])                                                                                                      
        except subprocess.CalledProcessError:                                                                                                                           
            sys.exit()                                                                                                                                                  

if __name__ == '__main__':
    main()
