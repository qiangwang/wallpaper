#!/usr/bin/env python

from pprint import pprint

import conf

#find wallpapers
import glob
papers = []
for path in conf.paths:
    for form in conf.formats:
        papers += glob.glob(path+'/*.'+form)
#pprint(papers)

import os
contexts = {}
for paper in papers:
    names = os.path.split(paper)
    fname = os.path.splitext(names[1])[0]
    if not names[0] in contexts.keys():
        contexts[names[0]] = []
    contexts[names[0]].append({'name':fname,'filename':paper}) 
pprint(contexts)

#generate confs
import dict_to_xml
dict_to_xml.doctype = conf.doctype
#for context in contexts.keys():
