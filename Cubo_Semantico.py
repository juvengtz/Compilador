class CuboSemantico:
    def __init__(self):

        self.cube = {
            'int': {
                'int': {
                    '+': 'int',
                    '-': 'int',
                    '*': 'int',
                    '/': 'int',
                    '>': 'bool',
                    '<': 'bool',
                    '>=': 'bool',
                    '<=': 'bool',
                    '==': 'bool',
                    '!=': 'bool'
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float',
                    '>': 'bool',
                    '<': 'bool',
                    '>=': 'bool',
                    '<=': 'bool',
                    '==': 'bool',
                    '!=': 'bool'
                },
                'char': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'error',
                    '!=': 'error'
                },
                'bool': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'error',
                    '!=': 'error'
                }
            },
            'float': {
                'int': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float',
                    '>': 'bool',
                    '<': 'bool',
                    '>=': 'bool',
                    '<=': 'bool',
                    '==': 'bool',
                    '!=': 'bool'
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float',
                    '>': 'bool',
                    '<': 'bool',
                    '>=': 'bool',
                    '<=': 'bool',
                    '==': 'bool',
                    '!=': 'bool'
                },
                'char': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'error',
                    '!=': 'error'
                },
                'bool': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'error',
                    '!=': 'error'
                }
            },
            'char': {
                'int': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'error',
                    '!=': 'error'
                },
                'float': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'error',
                    '!=': 'error'
                },
                'char': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'bool',
                    '!=': 'bool'
                },
                'bool': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'bool',
                    '!=': 'bool'
                }
            },
            'bool': {
                'int': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'error',
                    '!=': 'error'
                },
                'float': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'error',
                    '!=': 'error'
                },
                'char': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'error',
                    '<': 'error',
                    '>=': 'error',
                    '<=': 'error',
                    '==': 'bool',
                    '!=': 'bool'
                },
                'bool': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '>': 'bool',
                    '<': 'bool',
                    '>=': 'bool',
                    '<=': 'bool',
                    '==': 'bool',
                    '!=': 'bool'
                }
            }
        }

    def get_type(self, type1, type2, operator):
        return self.cube[type1][type2][operator]
