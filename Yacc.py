import ply.yacc as yacc
from Lexer import tokens, lexer


def p_programa(p):
    '''PROGRAMA : PROGRAM ID SEMICOLON VARS FUNC BLOQUE
                | PROGRAM ID SEMICOLON FUNC BLOQUE'''


def p_vars(p):
    '''VARS : VAR id_list COLON TIPO SEMICOLON
            | empty'''


def p_id_list(p):
    '''id_list : id_list COMMA ID array
               | ID array'''


def p_array(p):
    '''array : L_BRACKET CTE_I R_BRACKET
                    | empty'''


def p_tipo(p):
    '''TIPO : INT
            | FLOAT
            | CHAR'''


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
    '''ASIGNACION : ID array EQUAL EXPRESION SEMICOLON'''


def p_llamada(p):
    '''LLAMADA : FUNC_ESPECIAL L_PAREN exp_rep R_PAREN SEMICOLON
               | ID L_PAREN exp_rep R_PAREN SEMICOLON'''


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
    '''RELOP : GT
             | LT
             | EQ
             | LEQ
             | GEQ'''


def p_exp(p):
    '''EXP : TERMINO
           | TERMINO MASMENOS TERMINO'''


def p_masmenos(p):
    '''MASMENOS : PLUS
                | MINUS'''


def p_termino(p):
    '''TERMINO : FACTOR
               | FACTOR MULTDIV FACTOR'''


def p_multdiv(p):
    '''MULTDIV : MULT
               | DIV'''


def p_factor(p):
    '''FACTOR : L_PAREN EXPRESION R_PAREN
              | MASMENOS VAR_CTE
              | VAR_CTE'''


def p_var_cte(p):
    '''VAR_CTE : ID
               | CTE_I
               | CTE_F
               | CTE_CHAR'''


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Syntax error at '%s'" % p.value)


parser = yacc.yacc()


if __name__ == "__main__":
    data = input('file name:')
    with open(data, 'r') as data:
        parser.parse(data.read())
