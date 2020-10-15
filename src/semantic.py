#variable para el codigo de nodos
txt= " "


#contador en funcion
cont=0
def incrementarContador():
    global cont 
    cont +=1
    return "%d" %cont

class Nodo():
    pass


class program(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class block(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class constDecl(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class constDeclEmpty(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class constAssignmentList1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class constAssignmentList2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class varDecl1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class varDeclEmpty(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class identList1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class identList2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class procDecl1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class procDeclEmpty(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class statement1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class statement2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class statement4(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class statement5(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class statementEmpty(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class statementList1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class statementList2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class condition1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class condition2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class relation1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class relation2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class relation3(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class relation4(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class relation5(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class relation6(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class relation7(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class expression1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class expression2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class expression3(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class addingOperator1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class addingOperator2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class term1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class term2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class multiplyingOperator1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class multiplyingOperator2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class factor1(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class factor2(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class factor3(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

class empty(Nodo):
    def __init__(self,name):
        self.name = name

    def traducir(self):
        global txt
        id = incrementarContador()

        return id

