import ply.lex as lex
import re
import codecs
import os
import sys


reservadas = ['MAIN','PROGRAM','VAR','INT','FLOAT','CHAR','MODULE','VOID',
'RETURN','READ','WRITE','ELSE','THEN','WHILE','DO','PROCEDURE','OUT','IN','TO',
'LINE','CIRCLE','ARC','POINT','PENUP','PENDOWN','COLOR','SIZE','CLEAR', 'IF', 'FOR']

tokens = reservadas + ['ID','PLUS','MINUS','NUMBER','TIMES','DIVIDE','ODD','ASSIGN','COMMENT',
'NE','LESS','LESS_EQ','GREATER','GREATER_EQ','LPARENT','RPARENT','COMMA','SEMMICOLOM','DOT',
'UPDATE','LBRACE','RBRACE','COMPARE']



t_ignore = '\t '

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE  = r'<>'
t_LESS = r'<'
t_LESS_EQ = r'<='
t_GREATER = r'>'
t_GREATER_EQ = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_DOT = r'\.'
t_SEMMICOLOM = r';'
t_UPDATE = r':='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMPARE = r'=='

def t_ID(t):
    r'[a-zA-Z_] [a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

# handles new line (\n) error
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'%%.*'
    pass

# Number casts any number to integer
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_CHAR(t):
    r'[a-zA-Z0-9]'
    t.value = chr(t.value)
    return t

def t_error(t):
    print('*** caracter no reconocido en el lenguaje: ' + t.value[0])
    t.lexer.skip(1)

# testing code

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

    print("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]
"""
"""
# Working dir in lap
#directorio = 'C:/Users/bryan/Documents/Compiladores/Tareas/Proj/test/'

# working dir in pc 
directorio = 'C:/Users/bryan/Documents/compiladores/Compilador_proj/test/'

archivo = buscarFicheros(directorio)
#combinar directorio con resultado de pruebas
test = directorio + archivo
#Leer las pruebas 
fp = codecs.open(test, "r", "utf-8")
#leer archivo y 
cadena = fp.read()
fp.close()
"""

#analizador = lex.lex()

#analizador.input(cadena)
"""
while True:
    tok = analizador.token()
    if not tok : break
    print(tok)"""

