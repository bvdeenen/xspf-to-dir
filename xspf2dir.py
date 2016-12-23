#!/usr/bin/env python3

import sys,os,json,xmltodict,subprocess, shutil
import urllib, urlparse

def p(f, dest, d="/Users/mjv", mount="mac"):
    with open(f) as fd:                     
        doc =xmltodict.parse(fd.read())
        for i,x in enumerate(doc['playlist']['trackList']['track']):
            f=x['location']
urllib.url2pathname(urlparse.urlparse('file:///home/user/some%20file.txt').path)
'/home/user/some file.txt'

            n,e = os.path.splitext(f)
            dst = os.path.join(dest, "%03d-%s.mp3" %(i, os.path.basename(n)))
            src = os.path.join(mount, os.path.relpath(f,d))
            if e == ".mp3":
                shutil.copyfile(src, dst)
            else:
                convert_m4a(src, dst)

def convert_m4a(f,mp3):
    n,e = os.path.splitext(f)
    cmd=["ffmpeg","-v","5","-y","-i",f,"-acodec","libmp3lame","-ac","2","-ab","192k",mp3]
    ret = subprocess.run(cmd)
    if ret == 0:
        return mp3
    else:
        print(cmd, ret)
        return None




if __name__ == '__main__':
    p(sys.argv[1], sys.argv[2])

