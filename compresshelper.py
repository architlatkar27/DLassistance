#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 23:04:13 2021

@author: archit
"""

import os
import tarfile
import zipfile

def extract(path, destination="", compression='r'):
    if ".zip" in path:
        extract_zip(path, compression)
    elif ".tar" in path:
        extract_tar(path, compression)
    else:
        print("Unknown compression type, pls check other sources")

# def extract_all(dirpath, compression='r'):
#     for x in os.listdir(dirpath):
#         if x.endswith(("tar", "zip")):
#             extract(os.path.join(dirpath, x))

def extract_tar(tar_path, compression='r'):
    exdir = os.path.dirname(tar_path)
    exfolder = os.path.basename(tar_path)
    exfolder = exfolder[0:exfolder.find(".")]
    exfolder = os.path.join(exdir, exfolder)
    os.mkdir(exfolder)
    with tarfile.open(tar_path) as tf:
        tf.extractall(exfolder)
        tf.close()
    print("Done!")
    

def extract_zip(zip_path, compression='r'):
    exdir = os.path.dirname(zip_path)
    exfolder = os.path.basename(zip_path)
    exfolder = exfolder[0:exfolder.find(".")]
    exfolder = os.path.join(exdir, exfolder)
    os.mkdir(exfolder)
    with zipfile.ZipFile(zip_path, compression) as zf:
        zf.extractall(exfolder)
        zf.close()
    print("Done!")

extract("/home/archit/TestExtract/exampractice.zip")
extract("/home/archit/TestExtract/Cupertino-Catalina.tar.xz")