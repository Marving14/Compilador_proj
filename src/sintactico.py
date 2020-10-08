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

def p_program(p):
    '''program = block'''
    p[0] = program(p[1], "program")

def p_constAssignmentList1(p):
    '''constAssignmentList : ID = NUMBER'''
    print("constAssignmentList 1")

def p_constAssignmentList2(p):
    '''constAssignmentList : constAssignmentList, ID = NUMBER'''
    print("constAssignmentList 2")

def p_varDecl1(p):
    '''varDecl : VAR ID ;'''
    print("varDecl 1")

def p_varDecl2(p):
    '''varDecl : empty'''
    print("varDecl empty")




def p_(p):
    ''' = '''


def p_(p):
    ''' = '''

def p_(p):
    ''' = '''

def p_(p):
    ''' = '''

def p_(p):
    ''' = '''

def p_(p):
    ''' = '''







