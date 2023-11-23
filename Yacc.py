import ply.yacc as yacc
import sys
from Lexer import tokens, lexer
from Cubo_Semantico import *
from Cuadruplo import *


def p_programa(p):
    '''PROGRAMA : PROGRAM create_dirfunc ID  SEMICOLON vars2 func2 principal'''


def p_vars(p):
    '''vars : VAR tipo  COLON id_list SEMICOLON'''
    
def p_vars2(p):
    '''vars2 : vars vars2
             | empty'''


def p_id_list(p):
    '''id_list : id_list COMMA ID addvar array
               | ID addvar array'''


def p_array(p):
    '''array : L_BRACKET CTE_I R_BRACKET
                    | empty'''


def p_tipo(p):
    '''tipo : INT current_type
            | FLOAT current_type
            | BOOL current_type
            | CHAR current_type'''


def p_func(p):
    '''func : FUNCTION tipo_func ID addfunc L_PAREN params R_PAREN vars2 L_BRACE funcJump estatuto_rep R_BRACE endFunc'''

def p_func2(p):
    '''func2 : func func2
             | empty'''

def p_tipo_func(p):
    '''tipo_func : INT current_type
                 | FLOAT current_type
                 | CHAR current_type
                 | BOOL current_type
                 | VOID current_type'''


def p_params(p):
    '''params : tipo ID addvar updateParams params2
             | empty'''
    
def p_params2(p):
    '''params2 : COMMA tipo ID addvar updateParams params2
            | empty'''


def p_principal(p):
    '''principal : MAIN start funcChange L_PAREN R_PAREN bloque endProc'''

def p_bloque(p):
    '''bloque : L_BRACE estatuto_rep R_BRACE'''


def p_estatuto_rep(p):
    '''estatuto_rep : estatuto estatuto_rep 
                     | empty'''


def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura
                | llamada
                | retorno
                | lectura
                | repeticion
                | repeticion2'''


def p_asignacion(p):
    '''asignacion : ID stack_operand_id array EQUAL stack_operator expOr np_asignacion SEMICOLON'''


def p_llamada(p):
    '''llamada : ID llamadaEra L_PAREN fakebottom parm checkParamNum R_PAREN checkparentesis Gosub'''
    

#def p_func_especial(p):
#   '''func_especial : media
#                     | moda
#                     | varianza
#                     | reg
#                     | plotxy'''
    



def p_retorno(p):
    '''retorno : RETURN L_PAREN expOr np_return R_PAREN SEMICOLON'''


def p_lectura(p):
    '''lectura : READ L_PAREN ID np_read R_PAREN SEMICOLON'''


def p_escritura(p):
    '''escritura : WRITE L_PAREN escritura_rep R_PAREN SEMICOLON'''


def p_escritura_rep(p):
    '''escritura_rep : escritura_rep COMMA escritura_aux
                      | escritura_aux'''


def p_escritura_aux(p):
    '''escritura_aux : CTE_S printString
                         | expOr np_print'''


def p_condicion(p):
    '''condicion : IF L_PAREN expOr R_PAREN GotoF THEN bloque else_aux'''


def p_else_aux(p):
    '''else_aux : ELSE Goto bloque end_if
                   | end_if'''


def p_repeticion(p):
    '''repeticion : WHILE addJump L_PAREN expOr R_PAREN GotoF bloque end_while'''

def p_repeticion2(p):
    ''' repeticion2 : FOR ID EQUAL expOr TO expOr DO bloque'''

def p_parm(p):
    '''parm : expOr checkParam parm2
            | empty'''

def p_parm2(p):
    '''parm2 : COMMA expOr checkParam parm2
            | empty'''

def p_expOr(p):
    '''expOr : expAnd checkAndOr OR stack_operator expOr
             | expAnd checkAndOr '''

def p_expAnd(p):
    '''expAnd : expresion checkAndOr AND stack_operator expAnd
             | expresion checkAndOr'''

def p_expresion(p):
    '''expresion : exp checkrelop relop'''


def p_relop(p):
    '''relop : GT stack_operator expresion
             | LT stack_operator expresion
             | EQ stack_operator expresion
             | LEQ stack_operator expresion
             | GEQ stack_operator expresion
             | empty'''


def p_exp(p):
    '''exp : termino checkexp masmenos '''


def p_masmenos(p):
    '''masmenos : PLUS stack_operator exp
                | MINUS stack_operator exp
                | empty'''

def p_termino(p):
    '''termino : factor checkterm multdiv'''


def p_multdiv(p):
    '''multdiv : MULT stack_operator termino
               | DIV stack_operator termino
               | empty'''


def p_factor(p):
    '''factor : L_PAREN fakebottom expOr R_PAREN checkparentesis
              | var_cte'''


def p_var_cte(p):
    '''var_cte : ID stack_operand_id
                | llamada
               | CTE_I stack_operand_int
               | CTE_F stack_operand_float
               | CTE_CHAR stack_operand_char'''


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if p is not None:
        print("Syntax error in line " + str(p.lineno) + " " + str(p.value))
        sys.exit()
    else:
        print("Syntax error: p is None")
    print("Parsing stack:")
    for s in parser.symstack:
        print(s)
    print("dirFunc")
    print(dirFunc)
    print("Quadruples")
    print(Quadruples)
    print("Constants")
    print(Constants)
    
# GLOBAL VARIABLES


Operands_Stack = []
Operators_Stack = []

JumpStack = []

Quadruples = []
Constants = {}


CurrentFunc = 'global'
CurrentType = 'void'
CurrentID = ''
ReturnT = 0
ParamCount = 0
ParamPointer = 0
CallFunc = ''

dirFunc = {}
Quadruples.append(['GOTO', None, None, None])

# Directions
global_int = 1000
global_float = 2000
global_char = 3000
global_bool = 4000
local_int = 5000
local_float = 6000
local_char = 7000
local_bool = 8000
const_int = 9000
const_float = 10000
const_char = 11000
const_bool = 12000
temp_int = 13000
temp_float = 14000
temp_char = 15000
temp_bool = 16000
stringMemory = 17000

# Semantics


def p_create_dirfunc(p):
    'create_dirfunc :'
    global CurrentFunc, CurrentType
    dirFunc[CurrentFunc] = {'type': CurrentType,
                                'vars': {}, 'parameters': [], 'Start_dir': 0, 'size': 0}


def p_current_type(p):
    'current_type :'
    global CurrentType
    CurrentType = p[-1]


def p_addvar(p):
    'addvar :'
    global CurrentFunc, CurrentType, CurrentID
    CurrentID = p[-1]
    if CurrentID in dirFunc[CurrentFunc]['vars']:
        print('Variable already declared')
        sys.exit()
    else:
        if CurrentFunc == 'global':
            address = p_get_global_Mem(CurrentType)
        else:
            address = p_get_local_Mem(CurrentType)
        dirFunc[CurrentFunc]['vars'][CurrentID] = {
            'name': CurrentID, 'type': CurrentType, 'dir': address, 'size': 0}

def p_addfunc(p):
    'addfunc :'
    global CurrentFunc, CurrentType, CurrentID, ReturnT
    ReturnT = 0
    CurrentFunc = p[-1]
    if CurrentFunc in dirFunc:
        print('Function already declared')
        sys.exit()
    else:
        dirFunc[CurrentFunc] = {'type': CurrentType,
                              'vars': {}, 'parameters': [], 'dir': 0, 'size': 0}

def p_get_global_Mem(type):
    global global_int, global_float, global_char, global_bool
    if type == 'int':
        if global_int < 2000:
            global_int += 1
            return global_int
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'float':
        if global_float < 3000:
            global_float += 1
            return global_float
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'char':
        if global_char < 4000:
            global_char += 1
            return global_char
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'bool':
        if global_bool < 5000:
            global_bool += 1
            return global_bool
        else:
            print('Stack overflow')
            sys.exit()


def p_get_local_Mem(type):
    global local_int, local_float, local_char, local_bool
    if type == 'int':
        if local_int < 6000:
            local_int += 1
            return local_int
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'float':
        if local_float < 7000:
            local_float += 1
            return local_float
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'char':
        if local_char < 8000:
            local_char += 1
            return local_char
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'bool':
        if local_bool < 9000:
            local_bool += 1
            return local_bool
        else:
            print('Stack overflow')
            sys.exit()

def p_get_const_Mem(type):
    global const_int, const_float, const_char, const_bool, stringMemory
    if type == 'int':
        if const_int < 10000:
            const_int += 1
            return const_int
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'float':
        if const_float < 11000:
            const_float += 1
            return const_float
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'char':
        if const_char < 12000:
            const_char += 1
            return const_char
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'bool':
        if const_bool < 13000:
            const_bool += 1
            return const_bool
    elif type == 'string':
        if stringMemory < 18000:
            stringMemory += 1
            return stringMemory
        else:
            print('Stack overflow')
            sys.exit()

def p_get_temp_Mem(type):
    global temp_int, temp_float, temp_char, temp_bool
    if type == 'int':
        if temp_int < 14000:
            temp_int += 1
            return temp_int
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'float':
        if temp_float < 15000:
            temp_float += 1
            return temp_float
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'char':
        if temp_char < 16000:
            temp_char += 1
            return temp_char
        else:
            print('Stack overflow')
            sys.exit()
    elif type == 'bool':
        if temp_bool < 17000:
            temp_bool += 1
            return temp_bool
        else:
            print('Stack overflow')
            sys.exit()



def p_stack_operand_id(p):
    'stack_operand_id :'
    global Operands_Stack, Operators_Stack, dirFunc, CurrentFunc

    var_name = p[-1]
    if var_name in dirFunc[CurrentFunc]['vars']:
        var_info = dirFunc[CurrentFunc]['vars'][var_name]
    elif var_name in dirFunc['global']['vars']:
        var_info = dirFunc['global']['vars'][var_name]
    else:
        print('Variable not declared: ' + var_name + ' in ' + CurrentFunc)
        sys.exit()

    var_type = var_info.get('type')
    var_address = var_info.get('dir')

    Operands_Stack.append({'name': var_name, 'type': var_type, 'dir': var_address, 'size': 0})



def p_stack_operand_int(p):
    'stack_operand_int :'
    global Operands_Stack, Constants
    idName = p[-1]
    address = p_get_const_Mem('int')
    if p[-1] not in Constants:
        Constants[idName] = {'dir': address, 'type': 'int'}
    Operands_Stack.append({'name': idName, 'type': 'int', 'dir': address, 'size': 0})



def p_stack_operand_float(p):
    'stack_operand_float :'
    global Operands_Stack, Constants
    idName = p[-1]
    address = p_get_const_Mem('float')
    if p[-1] not in Constants:
        Constants[idName] = {'dir': address, 'type': 'float'}
    Operands_Stack.append({'name': idName, 'type': 'float', 'dir': address, 'size': 0})


def p_stack_operand_char(p):
    'stack_operand_char :'
    global Operands_Stack, Constants
    idName = p[-1]
    address = p_get_const_Mem('char')
    if p[-1] not in Constants:
        Constants[idName] = {'dir': address, 'type': 'char'}
    Operands_Stack.append({'name': idName, 'type': 'char', 'dir': address, 'size': 0})

def p_stack_operator(p):
    'stack_operator :'
    global Operators_Stack
    Operators_Stack.append(p[-1])
    print("Operator parsed:", p[-1])

def p_fakebottom(p):
    'fakebottom :'
    global Operators_Stack
    Operators_Stack.append('(')

def p_checkparentesis(p):
    'checkparentesis :'
    global Operators_Stack
    if Operators_Stack[-1] == '(':
        Operators_Stack.pop()
    else:
        print('Parentesis mismatch')
        sys.exit()

def p_checkAndOr(p):
    'checkAndOr :'
    global Operators_Stack, Operators_Stack, Quadruples
    if Operators_Stack:
        if Operators_Stack[-1] == '&' or Operators_Stack[-1] == '|':
            right_operand = Operands_Stack.pop()
            left_operand = Operands_Stack.pop()
            operator = Operators_Stack.pop()
            cubo_semantico = CuboSemantico()  
            result_type = cubo_semantico.get_type(left_operand['type'], right_operand['type'], operator)
            if result_type != 'error':
                address = p_get_temp_Mem(result_type)
                Operands_Stack.append({'name': 'temp', 'type': result_type, 'dir': address, 'size': 0})
                Quadruples.append([operator, left_operand['dir'],
                                right_operand['dir'], address])
            else:
                print('Type mismatch 1')
                sys.exit()

def p_checkterm(p):
    'checkterm :'
    global Operators_Stack, Operators_Stack, Quadruples
    if Operators_Stack:
        if Operators_Stack[-1] == '*' or Operators_Stack[-1] == '/':
            right_operand = Operands_Stack.pop()
            left_operand = Operands_Stack.pop()
            operator = Operators_Stack.pop()
            cubo_semantico = CuboSemantico()  
            result_type = cubo_semantico.get_type(left_operand['type'], right_operand['type'], operator)
            if result_type != 'error':
                address = p_get_temp_Mem(result_type)
                Operands_Stack.append({'name': 'temp', 'type': result_type, 'dir': address, 'size': 0})
                Quadruples.append([operator, left_operand['dir'],
                                right_operand['dir'], address])
            else:
                print('Type mismatch 2')
                sys.exit()
        

def p_checkexp(p):
    'checkexp :'
    global Operators_Stack, Operators_Stack, Quadruples
    if Operators_Stack: 
        if Operators_Stack[-1] == '+' or Operators_Stack[-1] == '-':
            right_operand = Operands_Stack.pop()
            left_operand = Operands_Stack.pop()
            operator = Operators_Stack.pop()
            cubo_semantico = CuboSemantico()  
            result_type = cubo_semantico.get_type(left_operand['type'], right_operand['type'], operator)
            if result_type != 'error':
                address = p_get_temp_Mem(result_type)
                Operands_Stack.append({'name': 'temp', 'type': result_type, 'dir': address, 'size': 0})
                Quadruples.append([operator, left_operand['dir'],
                                right_operand['dir'], address])
            else:
                print('Type mismatch 3')
                sys.exit()


def p_checkrelop(p):
    'checkrelop :'
    global Operators_Stack, Operators_Stack, Quadruples
    if Operators_Stack:
        if Operators_Stack[-1] == '<' or Operators_Stack[-1] == '>' or Operators_Stack[-1] == '<=' or Operators_Stack[-1] == '>=' or Operators_Stack[-1] == '==':
            right_operand = Operands_Stack.pop()
            left_operand = Operands_Stack.pop()
            operator = Operators_Stack.pop()
            cubo_semantico = CuboSemantico()
            print(left_operand['type'], right_operand['type'], operator)
            result_type = cubo_semantico.get_type(left_operand['type'], right_operand['type'], operator)
            print(result_type)
            if result_type != 'error':
                address = p_get_temp_Mem(result_type)
                Operands_Stack.append({'name': 'temp', 'type': result_type, 'dir': address, 'size': 0})
                Quadruples.append([operator, left_operand['dir'],
                                right_operand['dir'], address])
            else:
                print('Type mismatch 4')
                sys.exit()


def p_llamdaEra(p):
    'llamadaEra :'
    global Operands_Stack, Operators_Stack, Quadruples, CurrentFunc, dirFunc, CallFunc
    CallFunc = p[-1]
    if p[-1] in dirFunc:
        Quadruples.append(['ERA', None, None, CallFunc])
    else:
        print('Function not declared')
        sys.exit()


def p_np_asignacion(p):
    'np_asignacion :'
    global Operands_Stack, Operators_Stack, Quadruples, CurrentFunc, dirFunc
    if Operators_Stack[-1] == '=':
        Operators_Stack.pop()
        operando = Operands_Stack.pop()
        right_operand = operando['dir']
        right_type = operando['type']
        idOperand = Operands_Stack.pop()
        left_operand = idOperand['dir']
        left_type = idOperand['type']
        cubo_semantico = CuboSemantico()  
        result_type = cubo_semantico.get_type(left_type, right_type, '=')
        
        if result_type != 'error':
            Quadruples.append(['=', right_operand, None, left_operand])
        else:
            print('Type mismatch 5')
            sys.exit()

def p_np_return(p):
    'np_return :'
    global Operands_Stack, Operators_Stack, Quadruples, CurrentFunc, dirFunc, ReturnT
    right_operand = Operands_Stack.pop()
    result_type = dirFunc[CurrentFunc]['type']
    if right_operand['type'] == result_type:
        ReturnT = 1
        Quadruples.append(['return', None, None, right_operand['dir']])
    else:
        print(CurrentFunc)
        print(dirFunc)
        print('Type mismatch 6')
        sys.exit()

def p_GotoF(p):
    'GotoF :'
    global Operands_Stack, Operators_Stack, Quadruples, JumpStack
    result = Operands_Stack.pop()
    if result['type'] == 'bool':
        Quadruples.append(['GotoF', result, None, None])
        JumpStack.append(len(Quadruples) - 1)
    else:
        print('Type mismatch 7')
        sys.exit()

def p_Goto(p):
    'Goto :'
    global Operands_Stack, Operators_Stack, Quadruples, JumpStack
    Quadruples.append(['Goto', None, None, None])
    false = JumpStack.pop()
    JumpStack.append(len(Quadruples) - 1)
    Quadruples[false][3] = len(Quadruples)

def p_end_if(p):
    'end_if :'
    global Operands_Stack, Operators_Stack, Quadruples, JumpStack
    end = JumpStack.pop()
    Quadruples[end][3] = len(Quadruples)

def p_end_while(p):
    'end_while :'
    global Operands_Stack, Operators_Stack, Quadruples, JumpStack
    end = JumpStack.pop()
    ret = JumpStack.pop()
    Quadruples.append(['Goto', None, None, ret])
    Quadruples[end][3] = len(Quadruples)

def p_addJump(p):
    'addJump :'
    global Operands_Stack, Operators_Stack, Quadruples, JumpStack
    JumpStack.append(len(Quadruples))


def p_endFunc(p):
    'endFunc :'
    global Operands_Stack, Operators_Stack, Quadruples, JumpStack, ReturnT, CurrentFunc, dirFunc
    result_type = dirFunc[CurrentFunc]['type']
    
    if result_type != 'void' and ReturnT == 0:
        print('Function has to return a value')
        sys.exit()
    
    if result_type == 'void' and ReturnT == 1:
        print('Function should not have a return')
        sys.exit()
    
    Quadruples.append(['ENDFUNC', None, None, None])
    ReturnT = 0


def p_updateParams(p):
    'updateParams :'
    global dirFunc, CurrentFunc, CurrentType, CurrentID, ParamCount
    var = dirFunc[CurrentFunc]['vars'][CurrentID]
    address = var.get('dir')
    tipo = var.get('type')
    dirFunc[CurrentFunc]['parameters'].append([tipo, address])
    ParamCount += 1

def p_funcJump(p):
    'funcJump :'
    global dirFunc,Quadruples, CurrentFunc, ParamCount
    dirFunc[CurrentFunc]['dir'] = len(Quadruples)
    dirFunc[CurrentFunc]['size'] += ParamCount
    ParamCount = 0

def p_funcChange(p):
    'funcChange :'
    global CurrentFunc
    CurrentFunc = 'global'

def p_np_print(p):
    'np_print :'
    global Operands_Stack, Quadruples
    result = Operands_Stack.pop()
    Quadruples.append(['PRINT',None,None,result['dir']])

def p_printString(p):
    'printString :'
    global Operands_Stack, Quadruples
    address = p_get_const_Mem('string')
    Constants[p[-1]] = {'dir': address, 'type': 'string'}
    Quadruples.append(['PRINT',None,None,address])

def p_np_read(p):
    'np_read :'
    global dirFunc, CurrentFunc, Quadruples
    variable_name = p[-1]
    if variable_name not in dirFunc[CurrentFunc]['vars']:
        print('Variable not declared')
        sys.exit()
    else:
        address = dirFunc[CurrentFunc]['vars'][variable_name]['dir']
        Quadruples.append(['READ', None, None, address])


def p_start(p):
    'start :'
    global Quadruples
    if not Quadruples:
        Quadruples.append([None, None, None, None])
    Quadruples[0][3] = len(Quadruples)

def p_endProc(p):
    'endProc :'
    global Operands_Stack, Operators_Stack, Quadruples, JumpStack
    Quadruples.append(['ENDPROC', None, None, None])

def p_checkParam(p):
    'checkParam :'
    global Operands_Stack, Quadruples, CallFunc, ParamPointer, dirFunc

    arg = Operands_Stack.pop()
    argType = arg['type']
    paramType, paramAddr = dirFunc[CallFunc]['parameters'][ParamPointer]

    if argType == paramType:
        argAddr = arg['dir']
        Quadruples.append(['PARAM', None, argAddr, paramAddr])
        ParamPointer += 1
    else:
        print('Parameter types do not match')

def p_checkParamNum(p):
    'checkParamNum :'
    global Operands_Stack, Quadruples, CallFunc, ParamPointer, dirFunc
    if (ParamPointer != len(dirFunc[CallFunc]['parameters'])):
        print('Number of parameters does not match')
        sys.exit()

def p_Gosub(p):
    'Gosub :'
    global Operands_Stack, Quadruples, CallFunc, ParamPointer, dirFunc

    Quadruples.append(['GOSUB', None, None, CallFunc])

    tipo = dirFunc[CallFunc].get('type')
    if tipo != 'void':
        dirResult = dirFunc[CallFunc].get('dir')
        nextDir = p_get_temp_Mem(tipo)
        Quadruples.append(['=', dirResult, None, nextDir])
        Operands_Stack.append({'name': 'temp', 'type': tipo, 'dir': nextDir, 'size': 0})

    ParamPointer = 0
        


parser = yacc.yacc()


if __name__ == "__main__":
   # data = input('file name:')
    with open("./test1.txt", 'r') as data:
        parser.parse(data.read())
        print(dirFunc)
        print(Quadruples)
        print(Constants)
