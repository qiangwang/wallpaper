#!/usr/bin/env python

from xml.dom.minidom import DOMImplementation

class Dict_To_XML:

    def __init__(self):
        self.doctype = None
        self.indent = '    '
        self.name_sep = ' '
        self.attr_sep = '='
    
    def dict_to_xml(self,dic):
        if not isinstance(dic,dict):
            return None
        
        dom_impl = DOMImplementation()
        if self.doctype:
            doctype = dom_impl.createDocumentType(self.doctype[0],self.doctype[1],self.doctype[2])
        else:
            doctype = None
        
        if dic.keys():
            key = list(dic.keys())[0]
            doc = dom_impl.createDocument(key,None,doctype)
            root = doc.lastChild
            for ele in self.to_xml(doc,dic[key]):
                root.appendChild(ele)
        
        return doc.toprettyxml(indent=self.indent)
    
    def to_xml(self,doc,seq,alone=True):
        eles = []
        
        if isinstance(seq,dict):
            for key in list(seq.keys()):
                attrs = key.split(self.name_sep)
                ele = doc.createElement(attrs[0]) 
                for attr in attrs[1:]:
                    attr = attr.split(self.attr_sep)
                    ele.setAttribute(attr[0],attr[1])

                c_eles = self.to_xml(doc,seq[key])
                for c_ele in c_eles:
                    ele.appendChild(c_ele)
                eles.append(ele)
        elif isinstance(seq,list):
            for ele in seq:
                c_eles = self.to_xml(doc,ele,False)
                eles += c_eles
        else:
            seq = self.to_str(seq)
            if alone:
                ele = doc.createTextNode(seq)
            else:
                ele = doc.createComment(seq)
            eles.append(ele)
    
        return eles

    def to_str(self,var):
        if not isinstance(var,str):
            var = repr(var)

        return var

dx = Dict_To_XML()
print(dx.dict_to_xml({'a':1}))