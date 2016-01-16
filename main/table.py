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
                    '' if self.attributes == None
                    else self.attributes, self.value
                )
        else:
            return """<td{}>{}</td>""".format(
                    '' if self.attributes == None
                    else self.attributes, self.value
                )

class Row(object):
    def __init__(self, row, header=False, attributes=None):
        if not header:
            self.cells = [Cell(value) for value in row]
        else:
            self.cells = [Cell(value,header=True) for value in row]
        self.attributes = attributes
        self.header = header

    def __iter__(self):
        for cell in self.cells:
            yield cell

    def __repr__(self):
        return """<tr{}>{}</tr>""".format(
            '' if self.attributes == None else self.attributes,
                ''.join(str(cell) for cell in self.cells)
        )

class Table(object):
    def __init__(self, data, header=True, attributes=None):
        self.data = data
        self.header = header
        self.attributes = attributes
        self.rows = []

        for idx, row in enumerate(data):
            if idx == 0:
                self.rows.append(Row(row,header))
            else:
                self.rows.append(Row(row))

    def __iter__(self):
        for row in self.rows:
            yield row

    def __repr__(self):
        return """<table{}>{}</table>""".format(
            '' if self.attributes == None else self.attributes,
                ''.join(str(row) for row in self.rows)
            )
