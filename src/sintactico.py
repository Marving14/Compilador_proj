import ply.yacc as yacc
import os
import codecs
import re
from lexico import tokens
from sys import stdin 

#evitar errores radious 
precedence = (
    ('right', 'ID', 'PROGRAM', 'MAIN', ,'IF', 'WHILE', 'FOR' 'TO'),
    ('right', 'PROCEDURE', 'MODULE', 'RETURN'),
    ('right', 'VAR', 'INT', 'FLOAT', 'CHAR', 'VOID'),
    ('right', 'ASSIGN', 'READ', 'WRITE'),
    ('right', 'UPDATE'),
    ('left', 'NE'),
    ('left', 'LESS', 'GREATER'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'ODD'),
    ('left', 'LPARENT', 'RPARENT')
)





