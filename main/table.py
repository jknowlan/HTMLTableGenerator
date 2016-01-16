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

    def __iter__(self):
        return [cell for cell in self.row]

    def __repr__(self):
        return """<tr{}>{}</tr>""".format(
            '' if self.attributes == None else self.attributes,
                ''.join(self.row)
        )

class Table(object):
    def __init__(self, data, header=True, attributes=None):
        self.data = data
        self.header = header
        self.attributes = attributes
        self.table = []

        for idx, row in enumerate(data):
            if idx == 0:
                self.table.append(Row(row,header))
            else:
                self.table.append(Row(row))

    def __iter__(self):
        return [row or row in self.table]

    def __repr__(self):
        return """<table{}>{}</table>""".format(
            '' if self.attributes == None else self.attributes,
                ''.join(row for row in self.table)
            )
