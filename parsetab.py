
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CHAR COLON COMMA CTE_CHAR CTE_F CTE_I CTE_S DIV DO ELSE EQ EQUAL FLOAT FOR FUNCTION GEQ GT ID IF INT LEQ LT L_BRACE L_BRACKET L_PAREN MEDIA MINUS MODA MULT PLOTXY PLUS PROGRAM READ REG RETURN R_BRACE R_BRACKET R_PAREN SEMICOLON TO VAR VARIANZA WHILE WRITEPROGRAMA : PROGRAM create_dirfunc ID SEMICOLON VARS FUNC BLOQUE\n                | PROGRAM create_dirfunc ID SEMICOLON FUNC BLOQUEVARS : VAR addvar id_list COLON TIPO SEMICOLON\n            | emptyid_list : id_list COMMA ID array\n               | ID arrayarray : L_BRACKET CTE_I R_BRACKET\n                    | emptyTIPO : INT current_type\n            | FLOAT current_type\n            | CHAR current_typeFUNC : FUNCTION TIPO ID L_PAREN PARMS R_PAREN VARS BLOQUEPARMS : TIPO ID id_list\n             | emptyBLOQUE : L_BRACE ESTATUTO_rep R_BRACEESTATUTO_rep : ESTATUTO_rep ESTATUTO\n                     | ESTATUTOESTATUTO : ASIGNACION\n                | CONDICION\n                | ESCRITURA\n                | LLAMADA\n                | RETORNO\n                | LECTURA\n                | REPETICIONASIGNACION : ID array EQUAL EXPRESION np_asignacion SEMICOLONLLAMADA : FUNC_ESPECIAL L_PAREN exp_rep R_PAREN SEMICOLON\n               | ID L_PAREN exp_rep R_PAREN np_llamada SEMICOLONexp_rep : exp_rep COMMA EXPRESION\n                | EXPRESIONFUNC_ESPECIAL : MEDIA\n                     | MODA\n                     | VARIANZA\n                     | REG\n                     | PLOTXYRETORNO : RETURN L_PAREN EXPRESION R_PAREN SEMICOLONLECTURA : READ L_PAREN id_list R_PAREN SEMICOLONESCRITURA : WRITE L_PAREN escritura_rep R_PAREN SEMICOLONescritura_rep : escritura_rep COMMA escritura_aux\n                      | escritura_auxescritura_aux : CTE_S\n                         | EXPRESIONCONDICION : IF L_PAREN EXPRESION R_PAREN BLOQUE else_auxelse_aux : ELSE BLOQUE\n                   | emptyREPETICION : WHILE L_PAREN EXPRESION R_PAREN BLOQUE\n                  | FOR ID EQUAL EXPRESION TO EXPRESION DO BLOQUEEXPRESION : EXP\n                 | EXP RELOP EXPRELOP : GT stack_operator\n             | LT stack_operator\n             | EQ stack_operator\n             | LEQ stack_operator\n             | GEQ stack_operatorEXP : TERMINO\n           | TERMINO MASMENOS TERMINOMASMENOS : PLUS stack_operator\n                | MINUS stack_operatorTERMINO : FACTOR\n               | FACTOR MULTDIV FACTORMULTDIV : MULT stack_operator\n               | DIV stack_operatorFACTOR : L_PAREN stack_operator EXPRESION R_PAREN stack_operator\n              | MASMENOS VAR_CTE\n              | VAR_CTEVAR_CTE : ID stack_operand_id\n               | CTE_I stack_operand_int\n               | CTE_F stack_operand_float\n               | CTE_CHAR stack_operand_charempty :create_dirfunc :current_type :addvar :stack_operand_id :stack_operand_int :stack_operand_float :stack_operand_char :stack_operator :np_llamada :np_asignacion :np_condicion :np_condicion2 :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,12,19,48,],[0,-2,-1,-15,]),'ID':([2,3,8,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,36,45,46,47,48,49,51,54,55,56,57,58,59,62,65,67,72,75,76,90,93,98,100,101,102,103,104,105,106,107,109,110,111,112,113,120,128,135,136,137,138,139,142,143,144,145,147,148,149,150,151,154,156,157,159,163,165,],[-70,4,-72,29,43,44,-71,-71,-71,29,-17,-18,-19,-20,-21,-22,-23,-24,60,-9,-10,-11,-15,-16,66,66,66,66,66,43,66,92,66,-77,66,-77,-77,66,128,66,66,66,-77,-77,-77,-77,-77,66,66,-77,-77,-56,-57,66,43,-49,-50,-51,-52,-53,-60,-61,-69,-37,-26,-35,-36,-45,66,-25,-27,-42,-44,-43,-46,]),'SEMICOLON':([4,16,17,18,45,46,47,66,70,71,73,74,77,78,79,91,96,97,99,108,114,115,116,119,121,122,123,130,132,134,140,141,155,162,],[5,-71,-71,-71,-9,-10,-11,-73,-47,-54,-58,-64,-74,-75,-76,126,-79,-65,-78,-63,-66,-67,-68,145,147,148,149,154,156,-48,-55,-59,-77,-62,]),'VAR':([5,129,],[8,8,]),'FUNCTION':([5,6,9,126,],[10,10,-4,-3,]),'L_BRACE':([7,9,11,48,118,124,126,129,153,158,161,164,],[13,-4,13,-15,13,13,-3,-69,13,13,-12,13,]),'INT':([10,61,64,],[16,16,16,]),'FLOAT':([10,61,64,],[17,17,17,]),'CHAR':([10,61,64,],[18,18,18,]),'IF':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[30,30,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'WRITE':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[31,31,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'RETURN':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[33,33,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'READ':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[34,34,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'WHILE':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[35,35,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'FOR':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[36,36,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'MEDIA':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[37,37,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'MODA':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[38,38,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'VARIANZA':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[39,39,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'REG':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[40,40,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'PLOTXY':([13,20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[41,41,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'R_BRACE':([20,21,22,23,24,25,26,27,28,48,49,144,145,147,148,149,150,154,156,157,159,163,165,],[48,-17,-18,-19,-20,-21,-22,-23,-24,-15,-16,-69,-37,-26,-35,-36,-45,-25,-27,-42,-44,-43,-46,]),'L_PAREN':([29,30,31,32,33,34,35,37,38,39,40,41,44,51,54,55,56,57,59,65,67,75,76,90,98,100,101,102,103,104,105,106,107,109,110,111,112,113,120,135,136,137,138,139,142,143,151,],[51,54,55,56,57,58,59,-30,-31,-32,-33,-34,64,67,67,67,67,67,67,67,-77,-77,-77,67,67,67,67,-77,-77,-77,-77,-77,67,67,-77,-77,-56,-57,67,-49,-50,-51,-52,-53,-60,-61,67,]),'L_BRACKET':([29,43,92,],[52,52,52,]),'EQUAL':([29,50,53,60,117,],[-69,65,-8,90,-7,]),'COLON':([42,43,53,63,92,117,127,],[61,-69,-8,-6,-69,-7,-5,]),'COMMA':([42,43,53,63,66,68,69,70,71,73,74,77,78,79,82,83,84,85,86,88,92,97,108,114,115,116,117,127,133,134,140,141,146,152,155,162,],[62,-69,-8,-6,-73,100,-29,-47,-54,-58,-64,-74,-75,-76,120,-39,-40,-41,100,62,-69,-65,-63,-66,-67,-68,-7,-5,-28,-48,-55,-59,-38,62,-77,-62,]),'R_PAREN':([43,53,63,64,66,68,69,70,71,73,74,77,78,79,81,82,83,84,85,86,87,88,89,92,94,95,97,108,114,115,116,117,127,131,133,134,140,141,146,152,155,162,],[-69,-8,-6,-69,-73,99,-29,-47,-54,-58,-64,-74,-75,-76,118,119,-39,-40,-41,121,122,123,124,-69,129,-14,-65,-63,-66,-67,-68,-7,-5,155,-28,-48,-55,-59,-38,-13,-77,-62,]),'ELSE':([48,144,],[-15,158,]),'PLUS':([51,54,55,56,57,59,65,66,67,71,73,74,75,76,77,78,79,90,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,120,135,136,137,138,139,141,142,143,151,155,162,],[75,75,75,75,75,75,75,-73,-77,75,-58,-64,-77,-77,-74,-75,-76,75,-65,75,75,75,-77,-77,-77,-77,-77,75,-63,75,-77,-77,-56,-57,-66,-67,-68,75,-49,-50,-51,-52,-53,-59,-60,-61,75,-77,-62,]),'MINUS':([51,54,55,56,57,59,65,66,67,71,73,74,75,76,77,78,79,90,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,120,135,136,137,138,139,141,142,143,151,155,162,],[76,76,76,76,76,76,76,-73,-77,76,-58,-64,-77,-77,-74,-75,-76,76,-65,76,76,76,-77,-77,-77,-77,-77,76,-63,76,-77,-77,-56,-57,-66,-67,-68,76,-49,-50,-51,-52,-53,-59,-60,-61,76,-77,-62,]),'CTE_I':([51,52,54,55,56,57,59,65,67,72,75,76,90,98,100,101,102,103,104,105,106,107,109,110,111,112,113,120,135,136,137,138,139,142,143,151,],[77,80,77,77,77,77,77,77,-77,77,-77,-77,77,77,77,77,-77,-77,-77,-77,-77,77,77,-77,-77,-56,-57,77,-49,-50,-51,-52,-53,-60,-61,77,]),'CTE_F':([51,54,55,56,57,59,65,67,72,75,76,90,98,100,101,102,103,104,105,106,107,109,110,111,112,113,120,135,136,137,138,139,142,143,151,],[78,78,78,78,78,78,78,-77,78,-77,-77,78,78,78,78,-77,-77,-77,-77,-77,78,78,-77,-77,-56,-57,78,-49,-50,-51,-52,-53,-60,-61,78,]),'CTE_CHAR':([51,54,55,56,57,59,65,67,72,75,76,90,98,100,101,102,103,104,105,106,107,109,110,111,112,113,120,135,136,137,138,139,142,143,151,],[79,79,79,79,79,79,79,-77,79,-77,-77,79,79,79,79,-77,-77,-77,-77,-77,79,79,-77,-77,-56,-57,79,-49,-50,-51,-52,-53,-60,-61,79,]),'CTE_S':([55,120,],[84,84,]),'MULT':([66,73,74,77,78,79,97,108,114,115,116,155,162,],[-73,110,-64,-74,-75,-76,-65,-63,-66,-67,-68,-77,-62,]),'DIV':([66,73,74,77,78,79,97,108,114,115,116,155,162,],[-73,111,-64,-74,-75,-76,-65,-63,-66,-67,-68,-77,-62,]),'GT':([66,70,71,73,74,77,78,79,97,108,114,115,116,140,141,155,162,],[-73,102,-54,-58,-64,-74,-75,-76,-65,-63,-66,-67,-68,-55,-59,-77,-62,]),'LT':([66,70,71,73,74,77,78,79,97,108,114,115,116,140,141,155,162,],[-73,103,-54,-58,-64,-74,-75,-76,-65,-63,-66,-67,-68,-55,-59,-77,-62,]),'EQ':([66,70,71,73,74,77,78,79,97,108,114,115,116,140,141,155,162,],[-73,104,-54,-58,-64,-74,-75,-76,-65,-63,-66,-67,-68,-55,-59,-77,-62,]),'LEQ':([66,70,71,73,74,77,78,79,97,108,114,115,116,140,141,155,162,],[-73,105,-54,-58,-64,-74,-75,-76,-65,-63,-66,-67,-68,-55,-59,-77,-62,]),'GEQ':([66,70,71,73,74,77,78,79,97,108,114,115,116,140,141,155,162,],[-73,106,-54,-58,-64,-74,-75,-76,-65,-63,-66,-67,-68,-55,-59,-77,-62,]),'TO':([66,70,71,73,74,77,78,79,97,108,114,115,116,125,134,140,141,155,162,],[-73,-47,-54,-58,-64,-74,-75,-76,-65,-63,-66,-67,-68,151,-48,-55,-59,-77,-62,]),'DO':([66,70,71,73,74,77,78,79,97,108,114,115,116,134,140,141,155,160,162,],[-73,-47,-54,-58,-64,-74,-75,-76,-65,-63,-66,-67,-68,-48,-55,-59,-77,164,-62,]),'R_BRACKET':([80,],[117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'create_dirfunc':([2,],[3,]),'VARS':([5,129,],[6,153,]),'FUNC':([5,6,],[7,11,]),'empty':([5,29,43,64,92,129,144,],[9,53,53,95,53,9,159,]),'BLOQUE':([7,11,118,124,153,158,164,],[12,19,144,150,161,163,165,]),'addvar':([8,],[14,]),'TIPO':([10,61,64,],[15,91,93,]),'ESTATUTO_rep':([13,],[20,]),'ESTATUTO':([13,20,],[21,49,]),'ASIGNACION':([13,20,],[22,22,]),'CONDICION':([13,20,],[23,23,]),'ESCRITURA':([13,20,],[24,24,]),'LLAMADA':([13,20,],[25,25,]),'RETORNO':([13,20,],[26,26,]),'LECTURA':([13,20,],[27,27,]),'REPETICION':([13,20,],[28,28,]),'FUNC_ESPECIAL':([13,20,],[32,32,]),'id_list':([14,58,128,],[42,88,152,]),'current_type':([16,17,18,],[45,46,47,]),'array':([29,43,92,],[50,63,127,]),'exp_rep':([51,56,],[68,86,]),'EXPRESION':([51,54,55,56,57,59,65,90,98,100,120,151,],[69,81,85,69,87,89,96,125,131,133,85,160,]),'EXP':([51,54,55,56,57,59,65,90,98,100,101,120,151,],[70,70,70,70,70,70,70,70,70,70,134,70,70,]),'TERMINO':([51,54,55,56,57,59,65,90,98,100,101,107,120,151,],[71,71,71,71,71,71,71,71,71,71,71,140,71,71,]),'MASMENOS':([51,54,55,56,57,59,65,71,90,98,100,101,107,109,120,151,],[72,72,72,72,72,72,72,107,72,72,72,72,72,72,72,72,]),'FACTOR':([51,54,55,56,57,59,65,90,98,100,101,107,109,120,151,],[73,73,73,73,73,73,73,73,73,73,73,73,141,73,73,]),'VAR_CTE':([51,54,55,56,57,59,65,72,90,98,100,101,107,109,120,151,],[74,74,74,74,74,74,74,108,74,74,74,74,74,74,74,74,]),'escritura_rep':([55,],[82,]),'escritura_aux':([55,120,],[83,146,]),'PARMS':([64,],[94,]),'stack_operand_id':([66,],[97,]),'stack_operator':([67,75,76,102,103,104,105,106,110,111,155,],[98,112,113,135,136,137,138,139,142,143,162,]),'RELOP':([70,],[101,]),'MULTDIV':([73,],[109,]),'stack_operand_int':([77,],[114,]),'stack_operand_float':([78,],[115,]),'stack_operand_char':([79,],[116,]),'np_asignacion':([96,],[130,]),'np_llamada':([99,],[132,]),'else_aux':([144,],[157,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> PROGRAM create_dirfunc ID SEMICOLON VARS FUNC BLOQUE','PROGRAMA',7,'p_programa','Yacc.py',8),
  ('PROGRAMA -> PROGRAM create_dirfunc ID SEMICOLON FUNC BLOQUE','PROGRAMA',6,'p_programa','Yacc.py',9),
  ('VARS -> VAR addvar id_list COLON TIPO SEMICOLON','VARS',6,'p_vars','Yacc.py',13),
  ('VARS -> empty','VARS',1,'p_vars','Yacc.py',14),
  ('id_list -> id_list COMMA ID array','id_list',4,'p_id_list','Yacc.py',18),
  ('id_list -> ID array','id_list',2,'p_id_list','Yacc.py',19),
  ('array -> L_BRACKET CTE_I R_BRACKET','array',3,'p_array','Yacc.py',23),
  ('array -> empty','array',1,'p_array','Yacc.py',24),
  ('TIPO -> INT current_type','TIPO',2,'p_tipo','Yacc.py',28),
  ('TIPO -> FLOAT current_type','TIPO',2,'p_tipo','Yacc.py',29),
  ('TIPO -> CHAR current_type','TIPO',2,'p_tipo','Yacc.py',30),
  ('FUNC -> FUNCTION TIPO ID L_PAREN PARMS R_PAREN VARS BLOQUE','FUNC',8,'p_func','Yacc.py',34),
  ('PARMS -> TIPO ID id_list','PARMS',3,'p_parms','Yacc.py',38),
  ('PARMS -> empty','PARMS',1,'p_parms','Yacc.py',39),
  ('BLOQUE -> L_BRACE ESTATUTO_rep R_BRACE','BLOQUE',3,'p_bloque','Yacc.py',43),
  ('ESTATUTO_rep -> ESTATUTO_rep ESTATUTO','ESTATUTO_rep',2,'p_estatuto_rep','Yacc.py',47),
  ('ESTATUTO_rep -> ESTATUTO','ESTATUTO_rep',1,'p_estatuto_rep','Yacc.py',48),
  ('ESTATUTO -> ASIGNACION','ESTATUTO',1,'p_estatuto','Yacc.py',52),
  ('ESTATUTO -> CONDICION','ESTATUTO',1,'p_estatuto','Yacc.py',53),
  ('ESTATUTO -> ESCRITURA','ESTATUTO',1,'p_estatuto','Yacc.py',54),
  ('ESTATUTO -> LLAMADA','ESTATUTO',1,'p_estatuto','Yacc.py',55),
  ('ESTATUTO -> RETORNO','ESTATUTO',1,'p_estatuto','Yacc.py',56),
  ('ESTATUTO -> LECTURA','ESTATUTO',1,'p_estatuto','Yacc.py',57),
  ('ESTATUTO -> REPETICION','ESTATUTO',1,'p_estatuto','Yacc.py',58),
  ('ASIGNACION -> ID array EQUAL EXPRESION np_asignacion SEMICOLON','ASIGNACION',6,'p_asignacion','Yacc.py',62),
  ('LLAMADA -> FUNC_ESPECIAL L_PAREN exp_rep R_PAREN SEMICOLON','LLAMADA',5,'p_llamada','Yacc.py',66),
  ('LLAMADA -> ID L_PAREN exp_rep R_PAREN np_llamada SEMICOLON','LLAMADA',6,'p_llamada','Yacc.py',67),
  ('exp_rep -> exp_rep COMMA EXPRESION','exp_rep',3,'p_exp_rep','Yacc.py',71),
  ('exp_rep -> EXPRESION','exp_rep',1,'p_exp_rep','Yacc.py',72),
  ('FUNC_ESPECIAL -> MEDIA','FUNC_ESPECIAL',1,'p_func_especial','Yacc.py',76),
  ('FUNC_ESPECIAL -> MODA','FUNC_ESPECIAL',1,'p_func_especial','Yacc.py',77),
  ('FUNC_ESPECIAL -> VARIANZA','FUNC_ESPECIAL',1,'p_func_especial','Yacc.py',78),
  ('FUNC_ESPECIAL -> REG','FUNC_ESPECIAL',1,'p_func_especial','Yacc.py',79),
  ('FUNC_ESPECIAL -> PLOTXY','FUNC_ESPECIAL',1,'p_func_especial','Yacc.py',80),
  ('RETORNO -> RETURN L_PAREN EXPRESION R_PAREN SEMICOLON','RETORNO',5,'p_retorno','Yacc.py',84),
  ('LECTURA -> READ L_PAREN id_list R_PAREN SEMICOLON','LECTURA',5,'p_lectura','Yacc.py',88),
  ('ESCRITURA -> WRITE L_PAREN escritura_rep R_PAREN SEMICOLON','ESCRITURA',5,'p_escritura','Yacc.py',92),
  ('escritura_rep -> escritura_rep COMMA escritura_aux','escritura_rep',3,'p_escritura_rep','Yacc.py',96),
  ('escritura_rep -> escritura_aux','escritura_rep',1,'p_escritura_rep','Yacc.py',97),
  ('escritura_aux -> CTE_S','escritura_aux',1,'p_escritura_aux','Yacc.py',101),
  ('escritura_aux -> EXPRESION','escritura_aux',1,'p_escritura_aux','Yacc.py',102),
  ('CONDICION -> IF L_PAREN EXPRESION R_PAREN BLOQUE else_aux','CONDICION',6,'p_condicion','Yacc.py',106),
  ('else_aux -> ELSE BLOQUE','else_aux',2,'p_else_aux','Yacc.py',110),
  ('else_aux -> empty','else_aux',1,'p_else_aux','Yacc.py',111),
  ('REPETICION -> WHILE L_PAREN EXPRESION R_PAREN BLOQUE','REPETICION',5,'p_repeticion','Yacc.py',115),
  ('REPETICION -> FOR ID EQUAL EXPRESION TO EXPRESION DO BLOQUE','REPETICION',8,'p_repeticion','Yacc.py',116),
  ('EXPRESION -> EXP','EXPRESION',1,'p_expresion','Yacc.py',120),
  ('EXPRESION -> EXP RELOP EXP','EXPRESION',3,'p_expresion','Yacc.py',121),
  ('RELOP -> GT stack_operator','RELOP',2,'p_relop','Yacc.py',125),
  ('RELOP -> LT stack_operator','RELOP',2,'p_relop','Yacc.py',126),
  ('RELOP -> EQ stack_operator','RELOP',2,'p_relop','Yacc.py',127),
  ('RELOP -> LEQ stack_operator','RELOP',2,'p_relop','Yacc.py',128),
  ('RELOP -> GEQ stack_operator','RELOP',2,'p_relop','Yacc.py',129),
  ('EXP -> TERMINO','EXP',1,'p_exp','Yacc.py',133),
  ('EXP -> TERMINO MASMENOS TERMINO','EXP',3,'p_exp','Yacc.py',134),
  ('MASMENOS -> PLUS stack_operator','MASMENOS',2,'p_masmenos','Yacc.py',138),
  ('MASMENOS -> MINUS stack_operator','MASMENOS',2,'p_masmenos','Yacc.py',139),
  ('TERMINO -> FACTOR','TERMINO',1,'p_termino','Yacc.py',143),
  ('TERMINO -> FACTOR MULTDIV FACTOR','TERMINO',3,'p_termino','Yacc.py',144),
  ('MULTDIV -> MULT stack_operator','MULTDIV',2,'p_multdiv','Yacc.py',148),
  ('MULTDIV -> DIV stack_operator','MULTDIV',2,'p_multdiv','Yacc.py',149),
  ('FACTOR -> L_PAREN stack_operator EXPRESION R_PAREN stack_operator','FACTOR',5,'p_factor','Yacc.py',153),
  ('FACTOR -> MASMENOS VAR_CTE','FACTOR',2,'p_factor','Yacc.py',154),
  ('FACTOR -> VAR_CTE','FACTOR',1,'p_factor','Yacc.py',155),
  ('VAR_CTE -> ID stack_operand_id','VAR_CTE',2,'p_var_cte','Yacc.py',159),
  ('VAR_CTE -> CTE_I stack_operand_int','VAR_CTE',2,'p_var_cte','Yacc.py',160),
  ('VAR_CTE -> CTE_F stack_operand_float','VAR_CTE',2,'p_var_cte','Yacc.py',161),
  ('VAR_CTE -> CTE_CHAR stack_operand_char','VAR_CTE',2,'p_var_cte','Yacc.py',162),
  ('empty -> <empty>','empty',0,'p_empty','Yacc.py',166),
  ('create_dirfunc -> <empty>','create_dirfunc',0,'p_create_dirfunc','Yacc.py',195),
  ('current_type -> <empty>','current_type',0,'p_current_type','Yacc.py',205),
  ('addvar -> <empty>','addvar',0,'p_addvar','Yacc.py',211),
  ('stack_operand_id -> <empty>','stack_operand_id',0,'p_stack_operand_id','Yacc.py',221),
  ('stack_operand_int -> <empty>','stack_operand_int',0,'p_stack_operand_int','Yacc.py',231),
  ('stack_operand_float -> <empty>','stack_operand_float',0,'p_stack_operand_float','Yacc.py',238),
  ('stack_operand_char -> <empty>','stack_operand_char',0,'p_stack_operand_char','Yacc.py',245),
  ('stack_operator -> <empty>','stack_operator',0,'p_stack_operator','Yacc.py',252),
  ('np_llamada -> <empty>','np_llamada',0,'p_np_llamada','Yacc.py',258),
  ('np_asignacion -> <empty>','np_asignacion',0,'p_np_asignacion','Yacc.py',272),
  ('np_condicion -> <empty>','np_condicion',0,'p_np_condicion','Yacc.py',290),
  ('np_condicion2 -> <empty>','np_condicion2',0,'p_np_condicion2','Yacc.py',307),
]
