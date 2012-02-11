#!/usr/bin/env python

#@todo:dtd declaration,attribute,comment

from xml.dom.minidom import Document

def dic_to_xml(dic):
    if not isinstance(dic,dict):
        return
    doc = Document()
    if dic.keys():
        key = dic.keys()[0]
        root = doc.createElement(key)
        for ele in to_xml(doc,dic[key]):
            root.appendChild(ele)
        doc.appendChild(root)
    return doc.toprettyxml(indent='    ')

def to_xml(doc,seq):
    eles = []
    
    if isinstance(seq,dict):
        for key in seq.keys():
            ele = doc.createElement(key) 
            c_eles = to_xml(doc,seq[key])
            for c_ele in c_eles:
                ele.appendChild(c_ele)
            eles.append(ele)
    elif isinstance(seq,list):
        for ele in seq:
            c_eles = to_xml(doc,ele)
            eles += c_eles
    else:
        if not isinstance(seq,str):
            seq = repr(seq)
        ele = doc.createTextNode(seq)
        eles.append(ele)
    
    return eles
