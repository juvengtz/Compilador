import ply.yacc as yacc
from Lexer import tokens, lexer
from Cubo_Semantico import *
from Cuadruplo import *


def p_programa(p):
    '''PROGRAMA : PROGRAM create_dirfunc ID SEMICOLON VARS FUNC BLOQUE
                | PROGRAM create_dirfunc ID SEMICOLON FUNC BLOQUE'''


def p_vars(p):
    '''VARS : VAR addvar id_list COLON TIPO SEMICOLON
            | empty'''


def p_id_list(p):
    '''id_list : id_list COMMA ID array
               | ID array'''


def p_array(p):
    '''array : L_BRACKET CTE_I R_BRACKET
                    | empty'''


def p_tipo(p):
    '''TIPO : INT current_type
            | FLOAT current_type
            | CHAR current_type'''


def p_func(p):
    '''FUNC : FUNCTION TIPO ID L_PAREN PARMS R_PAREN VARS BLOQUE'''


def p_parms(p):
    '''PARMS : TIPO ID id_list
             | empty'''


def p_bloque(p):
    '''BLOQUE : L_BRACE ESTATUTO_rep R_BRACE'''


def p_estatuto_rep(p):
    '''ESTATUTO_rep : ESTATUTO_rep ESTATUTO
                     | ESTATUTO'''


def p_estatuto(p):
    '''ESTATUTO : ASIGNACION
                | CONDICION
                | ESCRITURA
                | LLAMADA
                | RETORNO
                | LECTURA
                | REPETICION'''


def p_asignacion(p):
    '''ASIGNACION : ID array EQUAL EXPRESION np_asignacion SEMICOLON'''


def p_llamada(p):
    '''LLAMADA : FUNC_ESPECIAL L_PAREN exp_rep R_PAREN SEMICOLON
               | ID L_PAREN exp_rep R_PAREN np_llamada SEMICOLON'''


def p_exp_rep(p):
    '''exp_rep : exp_rep COMMA EXPRESION
                | EXPRESION'''


def p_func_especial(p):
    '''FUNC_ESPECIAL : MEDIA
                     | MODA
                     | VARIANZA
                     | REG
                     | PLOTXY'''


def p_retorno(p):
    '''RETORNO : RETURN L_PAREN EXPRESION R_PAREN SEMICOLON'''


def p_lectura(p):
    '''LECTURA : READ L_PAREN id_list R_PAREN SEMICOLON'''


def p_escritura(p):
    '''ESCRITURA : WRITE L_PAREN escritura_rep R_PAREN SEMICOLON'''


def p_escritura_rep(p):
    '''escritura_rep : escritura_rep COMMA escritura_aux
                      | escritura_aux'''


def p_escritura_aux(p):
    '''escritura_aux : CTE_S
                         | EXPRESION'''


def p_condicion(p):
    '''CONDICION : IF L_PAREN EXPRESION R_PAREN BLOQUE else_aux'''


def p_else_aux(p):
    '''else_aux : ELSE BLOQUE
                   | empty'''


def p_repeticion(p):
    '''REPETICION : WHILE L_PAREN EXPRESION R_PAREN BLOQUE
                  | FOR ID EQUAL EXPRESION TO EXPRESION DO BLOQUE'''


def p_expresion(p):
    '''EXPRESION : EXP
                 | EXP RELOP EXP'''


def p_relop(p):
    '''RELOP : GT stack_operator
             | LT stack_operator
             | EQ stack_operator
             | LEQ stack_operator
             | GEQ stack_operator'''


def p_exp(p):
    '''EXP : TERMINO
           | TERMINO MASMENOS TERMINO'''


def p_masmenos(p):
    '''MASMENOS : PLUS stack_operator
                | MINUS stack_operator'''


def p_termino(p):
    '''TERMINO : FACTOR
               | FACTOR MULTDIV FACTOR'''


def p_multdiv(p):
    '''MULTDIV : MULT stack_operator
               | DIV stack_operator'''


def p_factor(p):
    '''FACTOR : L_PAREN stack_operator EXPRESION R_PAREN stack_operator
              | MASMENOS VAR_CTE
              | VAR_CTE'''


def p_var_cte(p):
    '''VAR_CTE : ID stack_operand_id
               | CTE_I stack_operand_int
               | CTE_F stack_operand_float
               | CTE_CHAR stack_operand_char'''


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Syntax error at '%s'" % p.value)
# GLOBAL VARIABLES


Operands_Stack = []
Operators_Stack = []
Types = []

JumpStack = []

Quadruples = []
Constants = []


CurrentFunc = None
CurrentType = None
CurrentID = None

dirFunc = {}

# Semantics


def p_create_dirfunc(p):
    'create_dirfunc :'
    global CurrentFunc, CurrentType
    if CurrentFunc in dirFunc:
        print('Function already declared')
    else:
        dirFunc[CurrentFunc] = {'type': CurrentType,
                                'vars': {}, 'dir': None, 'size': 0}


def p_current_type(p):
    'current_type :'
    global CurrentType
    CurrentType = p[-1]


def p_addvar(p):
    'addvar :'
    global CurrentFunc, CurrentType, CurrentID
    if CurrentID in dirFunc[CurrentFunc]['vars']:
        print('Variable already declared')
    else:
        dirFunc[CurrentFunc]['vars'][CurrentID] = {
            'name': CurrentID, 'type': CurrentType, 'dir': None, 'size': 0}


def p_stack_operand_id(p):
    'stack_operand_id :'
    global Operands_Stack, CurrentFunc, CurrentID
    if CurrentID in dirFunc[CurrentFunc]['vars']:
        Operands_Stack.append(dirFunc[CurrentFunc]['vars'][CurrentID]['dir'])
        Types.append(dirFunc[CurrentFunc]['vars'][CurrentID]['type'])
    else:
        print('Variable not declared')


def p_stack_operand_int(p):
    'stack_operand_int :'
    global Operands_Stack, Constants
    Operands_Stack.append(Constants[p[-1]])
    Types.append('int')


def p_stack_operand_float(p):
    'stack_operand_float :'
    global Operands_Stack, Constants
    Operands_Stack.append(Constants[p[-1]])
    Types.append('float')


def p_stack_operand_char(p):
    'stack_operand_char :'
    global Operands_Stack, Constants
    Operands_Stack.append(Constants[p[-1]])
    Types.append('char')


def p_stack_operator(p):
    'stack_operator :'
    global Operators_Stack
    Operators_Stack.append(p[-1])

def p_checkterm(p):
    'checkterm :'
    global Operators_Stack
    if Operators_Stack[-1] == '*' or Operators_Stack[-1] == '/':
        right_operand = Operands_Stack.pop()
        right_type = Types.pop()
        left_operand = Operands_Stack.pop()
        left_type = Types.pop()
        operator = Operators_Stack.pop()
        result_type = CuboSemantico[left_type][right_type][operator]
        if result_type != 'error':
            result = 'temp' + str(len(Constants))
            Constants.append(result_type)
            Operands_Stack.append(result)
            Types.append(result_type)
            Quadruples.append([operator, left_operand,
                               right_operand, result])
        else:
            print('Type mismatch')
        

def p_checkexp(p):
    'checkexp :'
    global Operators_Stack
    if Operators_Stack[-1] == '+' or Operators_Stack[-1] == '-':
        right_operand = Operands_Stack.pop()
        right_type = Types.pop()
        left_operand = Operands_Stack.pop()
        left_type = Types.pop()
        operator = Operators_Stack.pop()
        result_type = CuboSemantico[left_type][right_type][operator]
        if result_type != 'error':
            result = 'temp' + str(len(Constants))
            Constants.append(result_type)
            Operands_Stack.append(result)
            Types.append(result_type)
            Quadruples.append([operator, left_operand,
                               right_operand, result])
        else:
            print('Type mismatch')


def p_np_llamada(p):
    'np_llamada :'
    global Operands_Stack, Operators_Stack, Quadruples, CurrentFunc, dirFunc
    if p[-1] in dirFunc:
        if dirFunc[p[-1]]['type'] != 'void':
            print('Function has to return a value')
        else:
            Quadruples.append(['ERA', p[-1], None, None])
            Quadruples.append(['GOSUB', p[-1], None, None])
            Quadruples.append(['ENDPROC', None, None, None])
    else:
        print('Function not declared')


def p_np_asignacion(p):
    'np_asignacion :'
    global Operands_Stack, Operators_Stack, Quadruples, Types
    if Operators_Stack[-1] == '=':
        Operators_Stack.pop()
        right_operand = Operands_Stack.pop()
        right_type = Types.pop()
        left_operand = Operands_Stack.pop()
        left_type = Types.pop()
        result_type = CuboSemantico[left_type][right_type]['=']
        if result_type != 'error':
            Quadruples.append(['=', right_operand, None, left_operand])
        else:
            print('Type mismatch')
    else:
        print('Operator mismatch')


def p_np_condicion(p):
    'np_condicion :'
    global Operands_Stack, Operators_Stack, Quadruples, JumpStack
    if Operators_Stack[-1] == '==':
        Operators_Stack.pop()
        right_operand = Operands_Stack.pop()
        right_type = Types.pop()
        left_operand = Operands_Stack.pop()
        left_type = Types.pop()
        result_type = CuboSemantico[left_type][right_type]['==']
        if result_type != 'error':
            Quadruples.append(['GOTOF', left_operand, None, None])
            JumpStack.append(len(Quadruples)-1)
        else:
            print('Type mismatch')


def p_np_condicion2(p):
    'np_condicion2 :'
    global Operands_Stack, Operators_Stack, Quadruples, JumpStack
    Quadruples.append(['GOTO', None, None, None])
    false = JumpStack.pop()
    JumpStack.append(len(Quadruples)-1)
    Quadruples[false][3] = len(Quadruples)


parser = yacc.yacc()


if __name__ == "__main__":
    data = input('file name:')
    with open(data, 'r') as data:
        parser.parse(data.read())
        print(dirFunc)
        print(Quadruples)
        print(Constants)
