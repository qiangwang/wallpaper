#!/usr/bin/env python

from xml.dom.minidom import DOMImplementation,Document

doctype = [None,None,None]
indent = '    '
name_sep = ' '
attr_sep = '='

def dic_to_xml(dic):
    if not isinstance(dic,dict):
        return
    dom_impl = DOMImplementation()
    doc = dom_impl.createDocument(doctype=doc_impl.createDocumentType(doctype[0],doctype[1],doctype[2])))
    if dic.keys():
        key = dic.keys()[0]
        root = doc.createElement(key)
        for ele in to_xml(doc,dic[key]):
            root.appendChild(ele)
        doc.appendChild(root)
    return doc.toprettyxml(indent=indent)

def to_xml(doc,seq,alone=True):
    eles = []
    
    if isinstance(seq,dict):
        for key in seq.keys():
            attrs = key.split(name_sep)
            ele = doc.createElement(attrs[0]) 
            for attr in attrs[1:]:
                attr = attr.split(attr_sep)
                ele.setAttribute(attr[0],attr[1])

            c_eles = to_xml(doc,seq[key])
            for c_ele in c_eles:
                ele.appendChild(c_ele)
            eles.append(ele)
    elif isinstance(seq,list):
        for ele in seq:
            c_eles = to_xml(doc,ele,False)
            eles += c_eles
    else:
        seq = to_str(seq)
        if alone:
            ele = doc.createTextNode(seq)
        else:
            ele = doc.createComment(seq)
        eles.append(ele)
    
    return eles

def to_str(var):
    if not isinstance(var,str):
        var = repr(var)
    return var

