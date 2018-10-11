import Modelo.ply.yacc as yacc
from Modelo.analizadorLexico import *


def p_main(p):
    'MAIN : VAR SUBRUTINAS VARIABLES'
    print("main")

def p_subrutinas(p):
    'SUBRUTINAS : PROCEDURES'
    print("subrutina : procedure")

def p_subrutinas2(p):
    'SUBRUTINAS: FUNCTIONS'
    print("subrutina: function")

def p_subrutinas_empty(p):
    'SUBRUTINAS: empty'
    print("subrutina: lambda")

def p_variables(p):
    'VARIABLES: DEFVARIABLE'
    print("variable: defvariable")

def p_variables(p):
    'VARIABLES: empty'
    print("variable: lambda")

def p_procedures(p):
    'PROCEDURES: PROCEDURE NOMVARIABLE ABRIRPARENTESIS PARAMETRO CERRARPARENTESIS VAR DEFVARIABLE ABRIRLLAVE INSTRUCCIONES CERRARLLAVE'

def p_functions(p):
    'FUNCTIONS: FUNCTION TIPODATO NOMVARIABLE ABRIRPARENTESIS PARAMETRO CERRARPARENTESIS VAR DEFVARIABLE ABRIRLLAVE INSTRUCCIONES CERRARLLAVE RETURN NOMVARIABLE'

def p_defvariable(p):
    'DEFVARIABLE: TIPODATO NOMVARIABLE MASVARIABLES'

def p_defvariable2(p):
    'DEFVARIABLE: TIPODATO NOMVARIABLE ASIGNACION NUMERO MASVARIABLES'

def p_defvariable3(p):
    'DEFVARIABLE: TIPODATO NOMVARIABLE ASIGNACION NOMVARIABLE MASVARIABLES'

def p_defvariable4(p):
    'DEFVARIABLE: TIPODATO NOMVARIABLE OPERADORMATEMATICO NOMVARIABLE MASVARIABLES'

def p_parametro(p):
    'PARAMETRO: MODOPARAMETRO TIPODATO NOMVARIABLE MASPARAMETRO'

def p_parametro2(p):
    'PARAMETRO: MODOPARAMETRO TIPODATO ESTRUCTURA MASPARAMETRO'

def p_instrucciones(p):
    'INSTRUCCIONES: DEFVARIABLE'

def p_instrucciones2(p):
    'INSTRUCCIONES: ACCIONES'

def p_instrucciones3(p):
    'INSTRUCCIONES: INSTRUCCIONCON'

def p_instrucciones4(p):
    'INSTRUCCIONES: EMPTY'

def p_masvariables(p):
    'MASVARIABLES: COMA DEFVARIABLE'

def p_masvariables2(p):
    'MASVARIABLES: EMPTY'

