"""Escopo de variável e ordem de pesquisa de variável do Python.
LEGB: Local -> Incorporado -> Global -> Integrado
global - declara ou define uma variável global
não local - use uma variável de um escopo envolvente"""
x = 100


def foo():
    global x
    x = 200

    def bar():
        x = 300
        print(x)

    bar()
    print(x)


foo()
print(x)
