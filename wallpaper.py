#!/usr/bin/env python

from pprint import pprint

#template


#conf
entrance = '/usr/share/gnome-background-properties/wall_paper.xml'
doctype = ['wallpapers',None,'gnome-wp-list.dtd'}
auto_only = True

paths = ['/usr/share/backgrounds/*']
context = 'context.xml'
formats = ['jpg','png']

#find wallpapers
import glob
papers = []
for path in paths:
    for form in formats:
        papers += glob.glob(path+'/*.'+form)
#pprint(papers)

import os
context = {}
for paper in papers:
    names = os.path.split(paper)
    fname = os.path.splitext(names[1])[0]
    if not names[0] in context.keys():
        context[names[0]] = []
    context[names[0]].append({'name':fname,'filename':paper}) 
#pprint(context)

#generate confs
