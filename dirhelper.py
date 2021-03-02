#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:06:50 2021

@author: archit

Module to view the structure of directories in the dataset and extract tar files
"""
import os


def list_contents(directory=".", *include_types):
    file_list = []
    os.chdir(directory)
    if len(include_types) == 0:
        return os.listdir(directory)
    else:
        for t in include_types:
            for f in os.listdir(directory):
                if f.endswith(t):
                    file_list.append(f)
                    
    return file_list

def dir_structure(directory="."):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' '*4*level
        print("{}{}".format(indent, os.path.basename(root)))
        subindent = ' '*4*(level+1)
        for f in files:
            print("{}{}".format(subindent, f))

