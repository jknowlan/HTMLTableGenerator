import re
import pprint as pp

__version__ = '0.1.0'

class Attributes(object):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def __repr__(self):
        attr_lst = [str(key)+'='+'"'+str(value)+'"'
                    for key,value in self.attributes.items()]
        return ' '.join(attr_lst)

class Cell(object):
    def __init__(self, value, header=False, attributes=None):
        self.value = value
        self.attributes = attributes
        self.header = header

    def __repr__(self):
        if self.header:
            return """<th{}>{}</th>""".format(
                    '' if self.attributes == None else self.attributes, value
                )
        else:
            return """<td{}>{}</td>""".format(
                    '' if self.attributes == None else self.attributes, value
                )

class Row(object):
    def __init__(self, row, header=False, attributes=None):
        if not header:
            self.row = [Cell(value) for value in row]
        else:
            self.row = [Cell(value,header=True) for value in row]
        self.attributes = attributes
        self.header = header

    def __repr__(self):
        return """<tr{}>{}</tr>""".format(
            '' if self.attributes == None else self.attributes,
                ''.join(self.row)
        )

class Table(object):
    def __init__(self,)
