
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '1C64F2692BB7292F92A79B203BF74531'
    
_lr_action_items = {'DIVISION':([9,10,12,14,20,21,22,23,24,],[16,-13,-11,-14,-10,-9,-12,16,16,]),'RPAREN':([9,10,12,14,17,20,21,22,23,24,],[-8,-13,-11,-14,22,-10,-9,-12,-6,-7,]),'ADDITION':([9,10,12,13,14,17,20,21,22,23,24,],[-8,-13,-11,18,-14,18,-10,-9,-12,-6,-7,]),'EQUALS':([5,],[8,]),'FLOAT_LITERAL':([8,11,15,16,18,19,],[10,10,10,10,10,10,]),'SUBTRACTION':([9,10,12,13,14,17,20,21,22,23,24,],[-8,-13,-11,19,-14,19,-10,-9,-12,-6,-7,]),'LPAREN':([8,11,15,16,18,19,],[11,11,11,11,11,11,]),'MULTIPLICATION':([9,10,12,14,20,21,22,23,24,],[15,-13,-11,-14,-10,-9,-12,15,15,]),'ID':([0,4,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,],[5,5,14,-8,-13,14,-11,-5,-14,14,14,14,14,-10,-9,-12,-6,-7,]),'$end':([0,1,2,3,4,6,7,9,10,12,13,14,20,21,22,23,24,],[-15,-2,0,-1,-15,-4,-3,-8,-13,-11,-5,-14,-10,-9,-12,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([8,11,18,19,],[9,9,23,24,]),'multStatements':([0,4,],[1,7,]),'start':([0,],[2,]),'program':([0,],[3,]),'statement':([0,4,],[4,4,]),'factor':([8,11,15,16,18,19,],[12,12,20,21,12,12,]),'expression':([8,11,],[13,17,]),'Empty':([0,4,],[6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> program','start',1,'p_start','parse_ula.py',37),
  ('program -> multStatements','program',1,'p_program','parse_ula.py',41),
  ('multStatements -> statement multStatements','multStatements',2,'p_multStatements','parse_ula.py',45),
  ('multStatements -> Empty','multStatements',1,'p_multStatememts_empty','parse_ula.py',49),
  ('statement -> ID EQUALS expression','statement',3,'p_statement','parse_ula.py',52),
  ('expression -> expression ADDITION term','expression',3,'p_expression_plus','parse_ula.py',56),
  ('expression -> expression SUBTRACTION term','expression',3,'p_expression_minus','parse_ula.py',60),
  ('expression -> term','expression',1,'p_expression_term','parse_ula.py',64),
  ('term -> term DIVISION factor','term',3,'p_term_div','parse_ula.py',68),
  ('term -> term MULTIPLICATION factor','term',3,'p_term_mult','parse_ula.py',72),
  ('term -> factor','term',1,'p_term_factor','parse_ula.py',76),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parse_ula.py',84),
  ('factor -> FLOAT_LITERAL','factor',1,'p_factor_float','parse_ula.py',89),
  ('factor -> ID','factor',1,'p_factor_ID','parse_ula.py',93),
  ('Empty -> <empty>','Empty',0,'p_empty','parse_ula.py',105),
]
