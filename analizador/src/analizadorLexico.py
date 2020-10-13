import ply.lex as lex
import re
import codecs
import os
import sys


tokens = ['ID','PLUS','MINUS','NUMBER','TIMES','DIVIDE','ODD','ASSIGN',
    'NE','LESS','GREATER','LPARENT','RPARENT','COMMA','SEMMICOLOM','DOT',
    'UPDATE'
]

reservadas = {
    'begin':'BEGIN',
    'end':'END',
    'if':'IF',
    'else':'ELSE',
    'then':'THEN',
    'while':'WHILE',
    'do':'DO',
    'call':'CALL',
    'procedure':'PROCEDURE',
    'out':'OUT',
    'in':'IN'
}


tokens = tokens + list(reservadas.values())

# definir lo que hay dentro de los tokens

t_ignore = '\t'

t_PLUS = r'\+'
t_ASSIGN = r'='
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_NE = r'<>'
t_LESS = r'<'
t_GREATER = r'>'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='


def t_ID(t):
    r' [a-zA-Z_] [a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper() 
        t.type = t.value 

    return t 

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass 

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("caracter no reconocido en el lenguaje: '%s'"% t.value[0])
    t.lexer.skip(1)

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

directorio = 'C:/Users/bryan/Documents/Compiladores/Tareas/analizador/test/'
archivo = buscarFicheros(directorio)
#combinar directorio con resultado de pruebas
test = directorio + archivo
#Leer las pruebas 
fp = codecs.open(test, "r", "utf-8")

#leer archivo y 
cadena = fp.read()
fp.close() 

analizador = lex.lex()

analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : break
    print(tok)


