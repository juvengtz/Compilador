
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CHAR COLON COMMA CTE_CHAR CTE_F CTE_I CTE_S DIV DO ELSE EQ EQUAL FLOAT FOR FUNCTION GEQ GT ID IF INT LEQ LT L_BRACE L_BRACKET L_PAREN MAIN MEDIA MINUS MODA MULT OR PLOTXY PLUS PROGRAM READ REG RETURN R_BRACE R_BRACKET R_PAREN SEMICOLON THEN TO VAR VARIANZA VOID WHILE WRITEPROGRAMA : PROGRAM create_dirfunc ID  SEMICOLON vars2 func2 principalvars : VAR tipo  COLON id_list SEMICOLONvars2 : vars vars2\n             | emptyid_list : id_list COMMA ID addvar array\n               | ID addvar arrayarray : L_BRACKET CTE_I addDim R_BRACKET jumpAddr\n                    | emptytipo : INT current_type\n            | FLOAT current_type\n            | BOOL current_type\n            | CHAR current_typefunc : FUNCTION tipo_func ID addfunc L_PAREN params R_PAREN vars2 L_BRACE funcJump estatuto_rep R_BRACE endFuncfunc2 : func func2\n             | emptytipo_func : INT current_type\n                 | FLOAT current_type\n                 | CHAR current_type\n                 | BOOL current_type\n                 | VOID current_typeparams : tipo ID addvar updateParams params2\n             | emptyparams2 : COMMA tipo ID addvar updateParams params2\n            | emptyprincipal : MAIN start funcChange L_PAREN R_PAREN bloque endProcbloque : L_BRACE estatuto_rep R_BRACEestatuto_rep : estatuto estatuto_rep \n                     | emptyestatuto : asignacion\n                | condicion\n                | escritura\n                | llamada\n                | retorno\n                | lectura\n                | repeticionasignacion : ID stack_operand_id EQUAL stack_operator expOr np_asignacion SEMICOLON\n                    | var_dim EQUAL stack_operator expOr np_asignacion SEMICOLONllamada : ID llamadaEra L_PAREN fakebottom parm checkParamNum R_PAREN checkparentesis Gosubretorno : RETURN L_PAREN expOr np_return R_PAREN SEMICOLONlectura : READ L_PAREN ID np_read R_PAREN SEMICOLONescritura : WRITE L_PAREN escritura_rep R_PAREN SEMICOLONescritura_rep : escritura_rep COMMA escritura_aux\n                      | escritura_auxescritura_aux : CTE_S printString\n                         | expOr np_printcondicion : IF L_PAREN expOr R_PAREN GotoF THEN bloque else_auxelse_aux : ELSE Goto bloque end_if\n                   | end_ifrepeticion : WHILE addJump L_PAREN expOr R_PAREN GotoF DO bloque end_whileparm : expOr checkParam parm2\n            | emptyparm2 : COMMA expOr checkParam parm2\n            | emptyexpOr : expAnd checkAndOr OR stack_operator expOr\n             | expAnd checkAndOr expAnd : expresion checkAndOr AND stack_operator expAnd\n             | expresion checkAndOrexpresion : exp checkrelop reloprelop : GT stack_operator expresion\n             | LT stack_operator expresion\n             | EQ stack_operator expresion\n             | LEQ stack_operator expresion\n             | GEQ stack_operator expresion\n             | emptyexp : termino checkexp masmenos masmenos : PLUS stack_operator exp\n                | MINUS stack_operator exp\n                | emptytermino : factor checkterm multdivmultdiv : MULT stack_operator termino\n               | DIV stack_operator termino\n               | emptyfactor : L_PAREN fakebottom expOr R_PAREN checkparentesis\n              | var_ctevar_cte : ID stack_operand_id\n                | llamada\n               | CTE_I stack_operand_int\n               | CTE_F stack_operand_float\n               | CTE_CHAR stack_operand_char\n               | var_dimvar_dim : ID stack_operand_id L_BRACKET verDim fakebottom expOr cuadVer R_BRACKET checkparentesis verDimNum cuadVarDim  empty :create_dirfunc :current_type :addvar :addfunc :stack_operand_id :stack_operand_int :stack_operand_float :stack_operand_char :stack_operator :fakebottom :checkparentesis :checkAndOr :checkterm :checkexp :checkrelop :llamadaEra :np_asignacion :np_return :GotoF :Goto :end_if :end_while :addJump :endFunc :updateParams :funcJump :funcChange :np_print :printString :np_read :start :endProc :checkParam :checkParamNum :Gosub :addDim :jumpAddr :verDim :verDimNum :cuadVer :cuadVarDim :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,20,60,66,87,],[0,-1,-114,-25,-26,]),'ID':([2,3,16,17,18,19,23,24,25,26,27,28,29,30,31,32,33,36,37,38,39,40,46,56,61,68,70,71,72,73,74,75,76,87,91,92,93,94,95,97,100,101,102,103,104,124,125,129,130,131,133,145,152,154,161,162,164,165,166,167,168,171,172,175,176,178,189,192,193,194,195,196,197,198,199,200,201,202,203,204,208,210,212,215,230,232,234,235,238,241,244,246,],[-83,4,-84,-84,-84,-84,35,-84,-84,-84,-84,-84,42,-9,-10,-11,-12,-16,-17,-18,-19,-20,50,63,77,77,-29,-30,-31,-32,-33,-34,-35,-26,-91,112,112,112,123,-108,-91,-120,-92,112,-92,112,77,112,-92,112,112,112,184,112,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-41,-37,112,112,112,112,112,112,112,112,112,112,112,-39,-40,-36,-93,112,-103,-117,-46,-48,-104,-38,-49,-103,-47,]),'SEMICOLON':([4,41,42,47,50,51,53,58,64,86,99,106,107,108,109,110,111,112,113,114,115,116,117,132,135,136,137,138,139,140,141,142,143,144,153,158,163,169,170,173,174,177,180,181,185,190,210,214,216,217,218,219,220,221,222,223,224,225,226,229,230,237,238,242,245,],[5,45,-85,-82,-85,-6,-8,-82,-5,-119,-7,-94,-94,-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,-99,-55,-57,-82,-82,-82,-75,-77,-78,-79,178,-99,189,-58,-64,-65,-68,-69,-72,203,204,208,-93,-93,-73,-54,-56,-59,-60,-61,-62,-63,-66,-67,-70,-71,-93,-117,-121,-38,-123,-81,]),'VAR':([5,7,45,62,],[9,9,-2,9,]),'FUNCTION':([5,6,7,8,11,14,45,183,206,],[-82,13,-82,-4,13,-3,-2,-106,-13,]),'MAIN':([5,6,7,8,10,11,12,14,22,45,183,206,],[-82,-82,-82,-4,21,-82,-15,-3,-14,-2,-106,-13,]),'L_BRACE':([7,8,14,45,54,62,84,191,227,233,240,],[-82,-4,-3,-2,61,-82,97,61,61,-102,61,]),'INT':([9,13,49,127,],[16,24,16,16,]),'FLOAT':([9,13,49,127,],[17,25,17,17,]),'BOOL':([9,13,49,127,],[18,27,18,18,]),'CHAR':([9,13,49,127,],[19,26,19,19,]),'VOID':([13,],[28,]),'COLON':([15,16,17,18,19,30,31,32,33,],[29,-84,-84,-84,-84,-9,-10,-11,-12,]),'L_PAREN':([21,34,35,43,44,77,79,80,81,82,83,90,91,92,93,94,96,100,101,102,103,104,112,124,129,130,131,133,145,154,161,162,164,165,166,167,168,171,172,175,176,192,193,194,195,196,197,198,199,200,201,202,212,],[-113,-109,-86,48,49,-98,92,93,94,95,-105,102,-91,104,104,104,124,-91,-120,-92,104,-92,-98,104,104,-92,104,104,104,104,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,104,104,104,104,104,104,104,104,104,104,104,104,]),'COMMA':([41,42,47,50,51,53,58,63,64,85,86,98,99,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,135,136,137,138,139,140,141,142,143,146,147,156,163,169,170,173,174,177,179,184,188,190,207,210,214,216,217,218,219,220,221,222,223,224,225,226,228,229,230,231,237,238,239,242,245,],[46,-85,-82,-85,-6,-8,-82,-85,-5,-107,-119,127,-7,-94,-94,-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,145,-43,-111,-110,-55,-57,-82,-82,-82,-75,-77,-78,-79,-44,-45,-115,-58,-64,-65,-68,-69,-72,-42,-85,212,-93,-107,-93,-73,-54,-56,-59,-60,-61,-62,-63,-66,-67,-70,-71,127,-93,-117,-115,-121,-38,212,-123,-81,]),'L_BRACKET':([42,47,50,58,77,89,112,140,],[-85,52,-85,52,-87,101,-87,101,]),'R_PAREN':([48,49,55,57,63,85,98,102,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,128,131,135,136,137,138,139,140,141,142,143,146,147,148,149,150,155,156,157,159,163,169,170,173,174,177,179,184,187,188,190,207,210,211,213,214,216,217,218,219,220,221,222,223,224,225,226,228,229,230,231,236,237,238,239,242,243,245,],[54,-82,62,-22,-85,-107,-82,-92,134,-94,-94,-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,144,-43,-111,-110,-100,-112,-21,-24,-82,-55,-57,-82,-82,-82,-75,-77,-78,-79,-44,-45,180,181,182,-116,-115,-51,190,-58,-64,-65,-68,-69,-72,-42,-85,210,-82,-93,-107,-93,-50,-53,-73,-54,-56,-59,-60,-61,-62,-63,-66,-67,-70,-71,-82,-93,-117,-115,-23,-121,-38,-82,-123,-52,-81,]),'CTE_I':([52,91,92,93,94,100,101,102,103,104,124,129,130,131,133,145,154,161,162,164,165,166,167,168,171,172,175,176,192,193,194,195,196,197,198,199,200,201,202,212,],[59,-91,114,114,114,-91,-120,-92,114,-92,114,114,-92,114,114,114,114,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,114,114,114,114,114,114,114,114,114,114,114,114,]),'R_BRACKET':([59,65,106,107,108,109,110,111,112,113,114,115,116,117,135,136,137,138,139,140,141,142,143,163,169,170,173,174,177,186,190,209,210,214,216,217,218,219,220,221,222,223,224,225,226,229,230,237,238,242,245,],[-118,86,-94,-94,-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,-55,-57,-82,-82,-82,-75,-77,-78,-79,-58,-64,-65,-68,-69,-72,-122,-93,229,-93,-73,-54,-56,-59,-60,-61,-62,-63,-66,-67,-70,-71,-93,-117,-121,-38,-123,-81,]),'R_BRACE':([61,67,68,69,70,71,72,73,74,75,76,87,88,97,125,151,178,189,203,204,208,210,215,230,232,234,235,238,241,244,246,],[-82,87,-82,-28,-29,-30,-31,-32,-33,-34,-35,-26,-27,-108,-82,183,-41,-37,-39,-40,-36,-93,-103,-117,-46,-48,-104,-38,-49,-103,-47,]),'IF':([61,68,70,71,72,73,74,75,76,87,97,125,178,189,203,204,208,210,215,230,232,234,235,238,241,244,246,],[79,79,-29,-30,-31,-32,-33,-34,-35,-26,-108,79,-41,-37,-39,-40,-36,-93,-103,-117,-46,-48,-104,-38,-49,-103,-47,]),'WRITE':([61,68,70,71,72,73,74,75,76,87,97,125,178,189,203,204,208,210,215,230,232,234,235,238,241,244,246,],[80,80,-29,-30,-31,-32,-33,-34,-35,-26,-108,80,-41,-37,-39,-40,-36,-93,-103,-117,-46,-48,-104,-38,-49,-103,-47,]),'RETURN':([61,68,70,71,72,73,74,75,76,87,97,125,178,189,203,204,208,210,215,230,232,234,235,238,241,244,246,],[81,81,-29,-30,-31,-32,-33,-34,-35,-26,-108,81,-41,-37,-39,-40,-36,-93,-103,-117,-46,-48,-104,-38,-49,-103,-47,]),'READ':([61,68,70,71,72,73,74,75,76,87,97,125,178,189,203,204,208,210,215,230,232,234,235,238,241,244,246,],[82,82,-29,-30,-31,-32,-33,-34,-35,-26,-108,82,-41,-37,-39,-40,-36,-93,-103,-117,-46,-48,-104,-38,-49,-103,-47,]),'WHILE':([61,68,70,71,72,73,74,75,76,87,97,125,178,189,203,204,208,210,215,230,232,234,235,238,241,244,246,],[83,83,-29,-30,-31,-32,-33,-34,-35,-26,-108,83,-41,-37,-39,-40,-36,-93,-103,-117,-46,-48,-104,-38,-49,-103,-47,]),'EQUAL':([77,78,89,229,237,242,245,],[-87,91,100,-93,-121,-123,-81,]),'ELSE':([87,215,],[-26,233,]),'CTE_F':([91,92,93,94,100,101,102,103,104,124,129,130,131,133,145,154,161,162,164,165,166,167,168,171,172,175,176,192,193,194,195,196,197,198,199,200,201,202,212,],[-91,115,115,115,-91,-120,-92,115,-92,115,115,-92,115,115,115,115,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,115,115,115,115,115,115,115,115,115,115,115,115,]),'CTE_CHAR':([91,92,93,94,100,101,102,103,104,124,129,130,131,133,145,154,161,162,164,165,166,167,168,171,172,175,176,192,193,194,195,196,197,198,199,200,201,202,212,],[-91,116,116,116,-91,-120,-92,116,-92,116,116,-92,116,116,116,116,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,-91,116,116,116,116,116,116,116,116,116,116,116,116,]),'CTE_S':([93,145,],[120,120,]),'OR':([106,107,108,109,110,111,112,113,114,115,116,117,135,136,137,138,139,140,141,142,143,163,169,170,173,174,177,190,210,214,217,218,219,220,221,222,223,224,225,226,229,230,237,238,242,245,],[-94,-94,-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,161,-57,-82,-82,-82,-75,-77,-78,-79,-58,-64,-65,-68,-69,-72,-93,-93,-73,-56,-59,-60,-61,-62,-63,-66,-67,-70,-71,-93,-117,-121,-38,-123,-81,]),'AND':([107,108,109,110,111,112,113,114,115,116,117,136,137,138,139,140,141,142,143,163,169,170,173,174,177,190,210,214,218,219,220,221,222,223,224,225,226,229,230,237,238,242,245,],[-94,-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,162,-82,-82,-82,-75,-77,-78,-79,-58,-64,-65,-68,-69,-72,-93,-93,-73,-59,-60,-61,-62,-63,-66,-67,-70,-71,-93,-117,-121,-38,-123,-81,]),'GT':([108,109,110,111,112,113,114,115,116,117,137,138,139,140,141,142,143,170,173,174,177,190,210,214,223,224,225,226,229,230,237,238,242,245,],[-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,164,-82,-82,-75,-77,-78,-79,-65,-68,-69,-72,-93,-93,-73,-66,-67,-70,-71,-93,-117,-121,-38,-123,-81,]),'LT':([108,109,110,111,112,113,114,115,116,117,137,138,139,140,141,142,143,170,173,174,177,190,210,214,223,224,225,226,229,230,237,238,242,245,],[-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,165,-82,-82,-75,-77,-78,-79,-65,-68,-69,-72,-93,-93,-73,-66,-67,-70,-71,-93,-117,-121,-38,-123,-81,]),'EQ':([108,109,110,111,112,113,114,115,116,117,137,138,139,140,141,142,143,170,173,174,177,190,210,214,223,224,225,226,229,230,237,238,242,245,],[-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,166,-82,-82,-75,-77,-78,-79,-65,-68,-69,-72,-93,-93,-73,-66,-67,-70,-71,-93,-117,-121,-38,-123,-81,]),'LEQ':([108,109,110,111,112,113,114,115,116,117,137,138,139,140,141,142,143,170,173,174,177,190,210,214,223,224,225,226,229,230,237,238,242,245,],[-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,167,-82,-82,-75,-77,-78,-79,-65,-68,-69,-72,-93,-93,-73,-66,-67,-70,-71,-93,-117,-121,-38,-123,-81,]),'GEQ':([108,109,110,111,112,113,114,115,116,117,137,138,139,140,141,142,143,170,173,174,177,190,210,214,223,224,225,226,229,230,237,238,242,245,],[-97,-96,-95,-74,-87,-76,-88,-89,-90,-80,168,-82,-82,-75,-77,-78,-79,-65,-68,-69,-72,-93,-93,-73,-66,-67,-70,-71,-93,-117,-121,-38,-123,-81,]),'PLUS':([109,110,111,112,113,114,115,116,117,138,139,140,141,142,143,174,177,190,210,214,225,226,229,230,237,238,242,245,],[-96,-95,-74,-87,-76,-88,-89,-90,-80,171,-82,-75,-77,-78,-79,-69,-72,-93,-93,-73,-70,-71,-93,-117,-121,-38,-123,-81,]),'MINUS':([109,110,111,112,113,114,115,116,117,138,139,140,141,142,143,174,177,190,210,214,225,226,229,230,237,238,242,245,],[-96,-95,-74,-87,-76,-88,-89,-90,-80,172,-82,-75,-77,-78,-79,-69,-72,-93,-93,-73,-70,-71,-93,-117,-121,-38,-123,-81,]),'MULT':([110,111,112,113,114,115,116,117,139,140,141,142,143,190,210,214,229,230,237,238,242,245,],[-95,-74,-87,-76,-88,-89,-90,-80,175,-75,-77,-78,-79,-93,-93,-73,-93,-117,-121,-38,-123,-81,]),'DIV':([110,111,112,113,114,115,116,117,139,140,141,142,143,190,210,214,229,230,237,238,242,245,],[-95,-74,-87,-76,-88,-89,-90,-80,176,-75,-77,-78,-79,-93,-93,-73,-93,-117,-121,-38,-123,-81,]),'THEN':([134,160,],[-101,191,]),'DO':([182,205,],[-101,227,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'create_dirfunc':([2,],[3,]),'vars2':([5,7,62,],[6,14,84,]),'vars':([5,7,62,],[7,7,7,]),'empty':([5,6,7,11,47,49,58,61,62,68,98,125,131,137,138,139,188,228,239,],[8,12,8,12,53,57,53,69,8,69,128,69,157,169,173,177,213,128,213,]),'func2':([6,11,],[10,22,]),'func':([6,11,],[11,11,]),'tipo':([9,49,127,],[15,56,152,]),'principal':([10,],[20,]),'tipo_func':([13,],[23,]),'current_type':([16,17,18,19,24,25,26,27,28,],[30,31,32,33,36,37,38,39,40,]),'start':([21,],[34,]),'id_list':([29,],[41,]),'funcChange':([34,],[43,]),'addfunc':([35,],[44,]),'addvar':([42,50,63,184,],[47,58,85,207,]),'array':([47,58,],[51,64,]),'params':([49,],[55,]),'bloque':([54,191,227,240,],[60,215,235,244,]),'addDim':([59,],[65,]),'endProc':([60,],[66,]),'estatuto_rep':([61,68,125,],[67,88,151,]),'estatuto':([61,68,125,],[68,68,68,]),'asignacion':([61,68,125,],[70,70,70,]),'condicion':([61,68,125,],[71,71,71,]),'escritura':([61,68,125,],[72,72,72,]),'llamada':([61,68,92,93,94,103,124,125,129,131,133,145,154,192,193,194,195,196,197,198,199,200,201,202,212,],[73,73,113,113,113,113,113,73,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,]),'retorno':([61,68,125,],[74,74,74,]),'lectura':([61,68,125,],[75,75,75,]),'repeticion':([61,68,125,],[76,76,76,]),'var_dim':([61,68,92,93,94,103,124,125,129,131,133,145,154,192,193,194,195,196,197,198,199,200,201,202,212,],[78,78,117,117,117,117,117,78,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,]),'stack_operand_id':([77,112,],[89,140,]),'llamadaEra':([77,112,],[90,90,]),'addJump':([83,],[96,]),'updateParams':([85,207,],[98,228,]),'jumpAddr':([86,],[99,]),'stack_operator':([91,100,161,162,164,165,166,167,168,171,172,175,176,],[103,129,192,193,194,195,196,197,198,199,200,201,202,]),'expOr':([92,93,94,103,124,129,131,133,145,154,192,212,],[105,121,122,132,150,153,156,159,121,186,216,231,]),'expAnd':([92,93,94,103,124,129,131,133,145,154,192,193,212,],[106,106,106,106,106,106,106,106,106,106,106,217,106,]),'expresion':([92,93,94,103,124,129,131,133,145,154,192,193,194,195,196,197,198,212,],[107,107,107,107,107,107,107,107,107,107,107,107,218,219,220,221,222,107,]),'exp':([92,93,94,103,124,129,131,133,145,154,192,193,194,195,196,197,198,199,200,212,],[108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,223,224,108,]),'termino':([92,93,94,103,124,129,131,133,145,154,192,193,194,195,196,197,198,199,200,201,202,212,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,225,226,109,]),'factor':([92,93,94,103,124,129,131,133,145,154,192,193,194,195,196,197,198,199,200,201,202,212,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,]),'var_cte':([92,93,94,103,124,129,131,133,145,154,192,193,194,195,196,197,198,199,200,201,202,212,],[111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,]),'escritura_rep':([93,],[118,]),'escritura_aux':([93,145,],[119,179,]),'funcJump':([97,],[125,]),'params2':([98,228,],[126,236,]),'verDim':([101,],[130,]),'fakebottom':([102,104,130,],[131,133,154,]),'checkAndOr':([106,107,],[135,136,]),'checkrelop':([108,],[137,]),'checkexp':([109,],[138,]),'checkterm':([110,],[139,]),'stack_operand_int':([114,],[141,]),'stack_operand_float':([115,],[142,]),'stack_operand_char':([116,],[143,]),'printString':([120,],[146,]),'np_print':([121,],[147,]),'np_return':([122,],[148,]),'np_read':([123,],[149,]),'parm':([131,],[155,]),'np_asignacion':([132,153,],[158,185,]),'GotoF':([134,182,],[160,205,]),'relop':([137,],[163,]),'masmenos':([138,],[170,]),'multdiv':([139,],[174,]),'checkParamNum':([155,],[187,]),'checkParam':([156,231,],[188,239,]),'endFunc':([183,],[206,]),'cuadVer':([186,],[209,]),'parm2':([188,239,],[211,243,]),'checkparentesis':([190,210,229,],[214,230,237,]),'else_aux':([215,],[232,]),'end_if':([215,244,],[234,246,]),'Gosub':([230,],[238,]),'Goto':([233,],[240,]),'end_while':([235,],[241,]),'verDimNum':([237,],[242,]),'cuadVarDim':([242,],[245,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> PROGRAM create_dirfunc ID SEMICOLON vars2 func2 principal','PROGRAMA',7,'p_programa','Yacc.py',11),
  ('vars -> VAR tipo COLON id_list SEMICOLON','vars',5,'p_vars','Yacc.py',15),
  ('vars2 -> vars vars2','vars2',2,'p_vars2','Yacc.py',18),
  ('vars2 -> empty','vars2',1,'p_vars2','Yacc.py',19),
  ('id_list -> id_list COMMA ID addvar array','id_list',5,'p_id_list','Yacc.py',23),
  ('id_list -> ID addvar array','id_list',3,'p_id_list','Yacc.py',24),
  ('array -> L_BRACKET CTE_I addDim R_BRACKET jumpAddr','array',5,'p_array','Yacc.py',28),
  ('array -> empty','array',1,'p_array','Yacc.py',29),
  ('tipo -> INT current_type','tipo',2,'p_tipo','Yacc.py',33),
  ('tipo -> FLOAT current_type','tipo',2,'p_tipo','Yacc.py',34),
  ('tipo -> BOOL current_type','tipo',2,'p_tipo','Yacc.py',35),
  ('tipo -> CHAR current_type','tipo',2,'p_tipo','Yacc.py',36),
  ('func -> FUNCTION tipo_func ID addfunc L_PAREN params R_PAREN vars2 L_BRACE funcJump estatuto_rep R_BRACE endFunc','func',13,'p_func','Yacc.py',40),
  ('func2 -> func func2','func2',2,'p_func2','Yacc.py',43),
  ('func2 -> empty','func2',1,'p_func2','Yacc.py',44),
  ('tipo_func -> INT current_type','tipo_func',2,'p_tipo_func','Yacc.py',47),
  ('tipo_func -> FLOAT current_type','tipo_func',2,'p_tipo_func','Yacc.py',48),
  ('tipo_func -> CHAR current_type','tipo_func',2,'p_tipo_func','Yacc.py',49),
  ('tipo_func -> BOOL current_type','tipo_func',2,'p_tipo_func','Yacc.py',50),
  ('tipo_func -> VOID current_type','tipo_func',2,'p_tipo_func','Yacc.py',51),
  ('params -> tipo ID addvar updateParams params2','params',5,'p_params','Yacc.py',55),
  ('params -> empty','params',1,'p_params','Yacc.py',56),
  ('params2 -> COMMA tipo ID addvar updateParams params2','params2',6,'p_params2','Yacc.py',59),
  ('params2 -> empty','params2',1,'p_params2','Yacc.py',60),
  ('principal -> MAIN start funcChange L_PAREN R_PAREN bloque endProc','principal',7,'p_principal','Yacc.py',64),
  ('bloque -> L_BRACE estatuto_rep R_BRACE','bloque',3,'p_bloque','Yacc.py',67),
  ('estatuto_rep -> estatuto estatuto_rep','estatuto_rep',2,'p_estatuto_rep','Yacc.py',71),
  ('estatuto_rep -> empty','estatuto_rep',1,'p_estatuto_rep','Yacc.py',72),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','Yacc.py',76),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','Yacc.py',77),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','Yacc.py',78),
  ('estatuto -> llamada','estatuto',1,'p_estatuto','Yacc.py',79),
  ('estatuto -> retorno','estatuto',1,'p_estatuto','Yacc.py',80),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','Yacc.py',81),
  ('estatuto -> repeticion','estatuto',1,'p_estatuto','Yacc.py',82),
  ('asignacion -> ID stack_operand_id EQUAL stack_operator expOr np_asignacion SEMICOLON','asignacion',7,'p_asignacion','Yacc.py',87),
  ('asignacion -> var_dim EQUAL stack_operator expOr np_asignacion SEMICOLON','asignacion',6,'p_asignacion','Yacc.py',88),
  ('llamada -> ID llamadaEra L_PAREN fakebottom parm checkParamNum R_PAREN checkparentesis Gosub','llamada',9,'p_llamada','Yacc.py',92),
  ('retorno -> RETURN L_PAREN expOr np_return R_PAREN SEMICOLON','retorno',6,'p_retorno','Yacc.py',106),
  ('lectura -> READ L_PAREN ID np_read R_PAREN SEMICOLON','lectura',6,'p_lectura','Yacc.py',110),
  ('escritura -> WRITE L_PAREN escritura_rep R_PAREN SEMICOLON','escritura',5,'p_escritura','Yacc.py',114),
  ('escritura_rep -> escritura_rep COMMA escritura_aux','escritura_rep',3,'p_escritura_rep','Yacc.py',118),
  ('escritura_rep -> escritura_aux','escritura_rep',1,'p_escritura_rep','Yacc.py',119),
  ('escritura_aux -> CTE_S printString','escritura_aux',2,'p_escritura_aux','Yacc.py',123),
  ('escritura_aux -> expOr np_print','escritura_aux',2,'p_escritura_aux','Yacc.py',124),
  ('condicion -> IF L_PAREN expOr R_PAREN GotoF THEN bloque else_aux','condicion',8,'p_condicion','Yacc.py',128),
  ('else_aux -> ELSE Goto bloque end_if','else_aux',4,'p_else_aux','Yacc.py',132),
  ('else_aux -> end_if','else_aux',1,'p_else_aux','Yacc.py',133),
  ('repeticion -> WHILE addJump L_PAREN expOr R_PAREN GotoF DO bloque end_while','repeticion',9,'p_repeticion','Yacc.py',137),
  ('parm -> expOr checkParam parm2','parm',3,'p_parm','Yacc.py',143),
  ('parm -> empty','parm',1,'p_parm','Yacc.py',144),
  ('parm2 -> COMMA expOr checkParam parm2','parm2',4,'p_parm2','Yacc.py',147),
  ('parm2 -> empty','parm2',1,'p_parm2','Yacc.py',148),
  ('expOr -> expAnd checkAndOr OR stack_operator expOr','expOr',5,'p_expOr','Yacc.py',151),
  ('expOr -> expAnd checkAndOr','expOr',2,'p_expOr','Yacc.py',152),
  ('expAnd -> expresion checkAndOr AND stack_operator expAnd','expAnd',5,'p_expAnd','Yacc.py',155),
  ('expAnd -> expresion checkAndOr','expAnd',2,'p_expAnd','Yacc.py',156),
  ('expresion -> exp checkrelop relop','expresion',3,'p_expresion','Yacc.py',159),
  ('relop -> GT stack_operator expresion','relop',3,'p_relop','Yacc.py',163),
  ('relop -> LT stack_operator expresion','relop',3,'p_relop','Yacc.py',164),
  ('relop -> EQ stack_operator expresion','relop',3,'p_relop','Yacc.py',165),
  ('relop -> LEQ stack_operator expresion','relop',3,'p_relop','Yacc.py',166),
  ('relop -> GEQ stack_operator expresion','relop',3,'p_relop','Yacc.py',167),
  ('relop -> empty','relop',1,'p_relop','Yacc.py',168),
  ('exp -> termino checkexp masmenos','exp',3,'p_exp','Yacc.py',172),
  ('masmenos -> PLUS stack_operator exp','masmenos',3,'p_masmenos','Yacc.py',176),
  ('masmenos -> MINUS stack_operator exp','masmenos',3,'p_masmenos','Yacc.py',177),
  ('masmenos -> empty','masmenos',1,'p_masmenos','Yacc.py',178),
  ('termino -> factor checkterm multdiv','termino',3,'p_termino','Yacc.py',181),
  ('multdiv -> MULT stack_operator termino','multdiv',3,'p_multdiv','Yacc.py',185),
  ('multdiv -> DIV stack_operator termino','multdiv',3,'p_multdiv','Yacc.py',186),
  ('multdiv -> empty','multdiv',1,'p_multdiv','Yacc.py',187),
  ('factor -> L_PAREN fakebottom expOr R_PAREN checkparentesis','factor',5,'p_factor','Yacc.py',191),
  ('factor -> var_cte','factor',1,'p_factor','Yacc.py',192),
  ('var_cte -> ID stack_operand_id','var_cte',2,'p_var_cte','Yacc.py',196),
  ('var_cte -> llamada','var_cte',1,'p_var_cte','Yacc.py',197),
  ('var_cte -> CTE_I stack_operand_int','var_cte',2,'p_var_cte','Yacc.py',198),
  ('var_cte -> CTE_F stack_operand_float','var_cte',2,'p_var_cte','Yacc.py',199),
  ('var_cte -> CTE_CHAR stack_operand_char','var_cte',2,'p_var_cte','Yacc.py',200),
  ('var_cte -> var_dim','var_cte',1,'p_var_cte','Yacc.py',201),
  ('var_dim -> ID stack_operand_id L_BRACKET verDim fakebottom expOr cuadVer R_BRACKET checkparentesis verDimNum cuadVarDim','var_dim',11,'p_var_dim','Yacc.py',204),
  ('empty -> <empty>','empty',0,'p_empty','Yacc.py',208),
  ('create_dirfunc -> <empty>','create_dirfunc',0,'p_create_dirfunc','Yacc.py',280),
  ('current_type -> <empty>','current_type',0,'p_current_type','Yacc.py',287),
  ('addvar -> <empty>','addvar',0,'p_addvar','Yacc.py',293),
  ('addfunc -> <empty>','addfunc',0,'p_addfunc','Yacc.py',308),
  ('stack_operand_id -> <empty>','stack_operand_id',0,'p_stack_operand_id','Yacc.py',509),
  ('stack_operand_int -> <empty>','stack_operand_int',0,'p_stack_operand_int','Yacc.py',529),
  ('stack_operand_float -> <empty>','stack_operand_float',0,'p_stack_operand_float','Yacc.py',543),
  ('stack_operand_char -> <empty>','stack_operand_char',0,'p_stack_operand_char','Yacc.py',556),
  ('stack_operator -> <empty>','stack_operator',0,'p_stack_operator','Yacc.py',569),
  ('fakebottom -> <empty>','fakebottom',0,'p_fakebottom','Yacc.py',575),
  ('checkparentesis -> <empty>','checkparentesis',0,'p_checkparentesis','Yacc.py',580),
  ('checkAndOr -> <empty>','checkAndOr',0,'p_checkAndOr','Yacc.py',590),
  ('checkterm -> <empty>','checkterm',0,'p_checkterm','Yacc.py',611),
  ('checkexp -> <empty>','checkexp',0,'p_checkexp','Yacc.py',632),
  ('checkrelop -> <empty>','checkrelop',0,'p_checkrelop','Yacc.py',653),
  ('llamadaEra -> <empty>','llamadaEra',0,'p_llamdaEra','Yacc.py',674),
  ('np_asignacion -> <empty>','np_asignacion',0,'p_np_asignacion','Yacc.py',686),
  ('np_return -> <empty>','np_return',0,'p_np_return','Yacc.py',707),
  ('GotoF -> <empty>','GotoF',0,'p_GotoF','Yacc.py',720),
  ('Goto -> <empty>','Goto',0,'p_Goto','Yacc.py',732),
  ('end_if -> <empty>','end_if',0,'p_end_if','Yacc.py',741),
  ('end_while -> <empty>','end_while',0,'p_end_while','Yacc.py',748),
  ('addJump -> <empty>','addJump',0,'p_addJump','Yacc.py',757),
  ('endFunc -> <empty>','endFunc',0,'p_endFunc','Yacc.py',763),
  ('updateParams -> <empty>','updateParams',0,'p_updateParams','Yacc.py',781),
  ('funcJump -> <empty>','funcJump',0,'p_funcJump','Yacc.py',791),
  ('funcChange -> <empty>','funcChange',0,'p_funcChange','Yacc.py',799),
  ('np_print -> <empty>','np_print',0,'p_np_print','Yacc.py',805),
  ('printString -> <empty>','printString',0,'p_printString','Yacc.py',811),
  ('np_read -> <empty>','np_read',0,'p_np_read','Yacc.py',819),
  ('start -> <empty>','start',0,'p_start','Yacc.py',831),
  ('endProc -> <empty>','endProc',0,'p_endProc','Yacc.py',837),
  ('checkParam -> <empty>','checkParam',0,'p_checkParam','Yacc.py',843),
  ('checkParamNum -> <empty>','checkParamNum',0,'p_checkParamNum','Yacc.py',861),
  ('Gosub -> <empty>','Gosub',0,'p_Gosub','Yacc.py',870),
  ('addDim -> <empty>','addDim',0,'p_addDim','Yacc.py',888),
  ('jumpAddr -> <empty>','jumpAddr',0,'p_jumpAddr','Yacc.py',901),
  ('verDim -> <empty>','verDim',0,'p_verDim','Yacc.py',912),
  ('verDimNum -> <empty>','verDimNum',0,'p_verDimNum','Yacc.py',925),
  ('cuadVer -> <empty>','cuadVer',0,'p_cuadVer','Yacc.py',933),
  ('cuadVarDim -> <empty>','cuadVarDim',0,'p_cuadVarDim','Yacc.py',942),
]
