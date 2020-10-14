import ply.yacc as yacc
import os
import codecs
import re
from lexico import tokens
from sys import stdin 

#evitar errores radious 
precedence = (
    ('right', 'ID', 'PROGRAM', 'MAIN', 'IF', 'WHILE', 'FOR', 'TO'),
    ('right', 'PROCEDURE', 'MODULE', 'RETURN'),
    ('right', 'VAR', 'INT', 'FLOAT', 'CHAR', 'VOID'),
    ('right', 'ASSIGN', 'READ', 'WRITE'),
    ('right', 'UPDATE'),
    ('left', 'NE'),
    ('left', 'LESS', 'GREATER', 'LESS_EQ', 'GREATER_EQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'ODD'),
    ('left', 'LPARENT', 'RPARENT')
)

def p_program(p):
    '''program : block'''
    print("program")
   # p[0] = program(p[1], "program")

def p_block(p):
    '''block : constDecl varDecl procDecl statement'''
    print("block")

def p_constDecl(p):
    '''constDecl : CONST constAssignmentList SEMMICOLOM'''
    print("constDecl")

def p_constDeclEmpty(p):
    '''constDecl : empty'''
    print("Nulo")

def p_constAssignmentList1(p):
    '''constAssignmentList : ID ASSIGN NUMBER'''
    print("constAssignmentList 1")

def p_constAssignmentList2(p):
    '''constAssignmentList : constAssignmentList COMMA ID ASSIGN NUMBER'''
    print("constAssignmentList 2")

def p_varDecl1(p):
    '''varDecl : VAR ID SEMMICOLOM'''
    print("varDecl 1")

def p_varDeclEmpty(p):
    '''varDecl : empty'''
    print("varDecl empty")

def p_identList1(p):
    '''identList : ID'''
    print("identList 1")

def p_identList2(p):
    '''identList : identList COMMA ID'''
    print("IdentList 2")

def p_procDecl1(p):
    '''procDecl : procDecl PROCEDURE ID SEMMICOLOM block SEMMICOLOM '''
    print("procDecl1")
def p_procDeclEmpty(p):
    '''procDecl : empty'''
    print("nulo")

def p_statement1(p):
    '''statement : ID UPDATE expression'''
    print("statement 1")

def p_statement2(p):
    '''statement : CALL ID'''
    print("statement 2 - call")

def p_statement4(p):
    '''statement : IF condition THEN statement'''
    print("Statement 4 - if")

def p_statement5(p):
    '''statement : WHILE condition DO statement'''
    print("Statement 5 - while")

def p_statementEmpty(p):
    '''statement : empty'''
    print("nullo statement")

def p_statementList1(p):
    '''statementList : statement'''
    print("Statement list 1")

def p_statementList2(p):
    '''statementList : statementList SEMMICOLOM statement'''
    print("Statement list 2")

def p_condition1(p):
    '''condition : ODD expression'''
    print("condition 1")

def p_condition2(p):
    '''condition : expression relation expression'''
    print("condition 2")

def p_relation1(p):
    '''relation : ASSIGN'''
    print("relation 1 - ASSIGN")

def p_relation2(p):
    '''relation : NE'''
    print("relation 2 - NE")

def p_relation3(p):
    '''relation : LESS'''
    print("relation 3")

def p_relation4(p):
    '''relation : LESS_EQ'''
    print("relation 4")

def p_relation5(p):
    '''relation : GREATER'''
    print("relation 5")

def p_relation6(p):
    '''relation : GREATER_EQ'''
    print("relation 6")

def p_relation7(p):
    '''relation : COMPARE'''
    print("relation 7")


def p_expression1(p):
    '''expression : term'''
    print("expression 1")

def p_expression2(p):
    '''expression : addingOperator term'''
    print("expression 2")

def p_expression3(p):
    '''expression : expression addingOperator term'''
    print("expression 3")

def p_addingOperator1(p):
    '''addingOperator : PLUS'''
    print("addingOperator 1")
    
def p_addingOperator2(p):
    '''addingOperator : MINUS'''
    print("addingOperator 2")

def p_term1(p):
    '''term : factor'''
    print("term 1")

def p_term2(p):
    '''term : term multiplyingOperator factor'''
    print("term 2")

def p_multiplyingOperator1(p):
    '''multiplyingOperator : TIMES'''
    print("multiplyingOperator 1")

def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVIDE'''
    print("multiplyingOperator 2")


def p_factor1(p):
    '''factor : ID'''
    print("factor 1")

def p_factor2(p):
    '''factor : NUMBER'''
    print("factor 2") 

def p_factor3(p):
    '''factor : LPARENT expression RPARENT'''
    print("factor 3")

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print("Error de sintaxis", p)
    print("Error en linea: "+ str(p.lineno))


"""
def p_(p):
    ''' : '''
"""



def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont)+ ". " + file)
        cont = cont + 1
    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break 

    print("Has escogido \"%s\" \n" %files[int(numArchivo)-1] )

    return files[int(numArchivo)-1]

directorio = 'C:/Users/bryan/Documents/compiladores/Compilador_proj/test/'
archivo = buscarFicheros(directorio)
#combinar directorio con resultado de pruebas
test = directorio + archivo
#Leer las pruebas 
fp = codecs.open(test, "r", "utf-8")
#leer archivo y 
cadena = fp.read()
fp.close() 

parser = yacc.yacc()
result = parser.parse(cadena)

print(result)





