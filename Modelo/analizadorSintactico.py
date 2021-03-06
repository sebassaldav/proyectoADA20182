import Modelo.ply.yacc as yacc
from Modelo.analizadorLexico import *


def p_main(p):
    'MAIN : VAR SUBRUTINAS VARIABLES'
    print("main")

def p_subrutinas(p):
    'SUBRUTINAS : PROCEDURES'
    print("subrutina : procedure")

def p_subrutinas2(p):
    'SUBRUTINAS : FUNCTIONS'
    print("subrutina: function")

def p_subrutinas_empty(p):
    'SUBRUTINAS : EMPTY'
    print("subrutina: lambda")

def p_variables(p):
    'VARIABLES : DEFVARIABLE'
    print("variable: defvariable")

def p_variables1(p):
    'VARIABLES : EMPTY'
    print("variable: lambda")

def p_procedures(p):
    'PROCEDURES : PROCEDURE NOMVARIABLE ABRIRPARENTESIS PARAMETRO CERRARPARENTESIS VAR DEFVARIABLE ABRIRLLAVE INSTRUCCIONES CERRARLLAVE'

def p_functions(p):
    'FUNCTIONS : FUNCTION TIPODATO NOMVARIABLE ABRIRPARENTESIS PARAMETRO CERRARPARENTESIS VAR DEFVARIABLE ABRIRLLAVE INSTRUCCIONES CERRARLLAVE RETURN NOMVARIABLE'

def p_defvariable(p):
    'DEFVARIABLE : TIPODATO NOMVARIABLE MASVARIABLES'

def p_defvariable2(p):
    'DEFVARIABLE : TIPODATO NOMVARIABLE ASIGNACION NUMERO MASVARIABLES'

def p_defvariable3(p):
    'DEFVARIABLE : TIPODATO NOMVARIABLE ASIGNACION NOMVARIABLE MASVARIABLES'

def p_defvariable4(p):
    'DEFVARIABLE : TIPODATO NOMVARIABLE OPERADORMATEMATICO NOMVARIABLE MASVARIABLES'

def p_parametro(p):
    'PARAMETRO : MODOPARAMETRO TIPODATO NOMVARIABLE MASPARAMETRO'

def p_parametro2(p):
    'PARAMETRO : MODOPARAMETRO TIPODATO ESTRUCTURA MASPARAMETRO'

def p_instrucciones(p):
    'INSTRUCCIONES : DEFVARIABLE'

def p_instrucciones2(p):
    'INSTRUCCIONES : ACCIONES'

def p_instrucciones3(p):
    'INSTRUCCIONES : INSTRUCCIONCON'

def p_instrucciones4(p):
    'INSTRUCCIONES : EMPTY'

def p_masvariables(p):
    'MASVARIABLES : COMA DEFVARIABLE'

def p_masvariables2(p):
    'MASVARIABLES : EMPTY'

def p_masparametro(p):
    'MASPARAMETRO : COMA PARAMETRO'

def p_masparametro2(p):
    'MASPARAMETRO : EMPTY'

#EL COMENTADO ERA EL QUE HABIAMOS PENSADO, EL SIGUIENTE FUE LA FORMA MAS CLARA ES QUE LO ENTENDI :) :) :) PUES NO SE SI ESTA BIEN, FALTARIA PONER STACK, LIST ETC

#def p_estructura(p):
#    'ESTRUCTURA: TIPOESTRUCTURA ABRIRCORCHETE DIMENSION CERRARCORCHETE'

def p_estructura(p):
    'ESTRUCTURA : TIPOESTRUCTURA'

def p_tipoestructura(p):
    'TIPOESTRUCTURA : ARBOL ABRIRCORCHETE NUMERO NUMERO CERRARCORCHETE'

def p_tipoestructura2(p):
    'TIPOESTRUCTURA : GRAFO ABRIRCORCHETE NUMERO NUMERO CERRARCORCHETE'

def p_tipoestructura3(p):
    'TIPOESTRUCTURA : MATRIZ ABRIRCORCHETE DIMENSION CERRARCORCHETE'



def p_acciones(p):
    'ACCIONES : CONDICIONAL'

def p_acciones2(p):
    'ACCIONES : CICLO'

def p_acciones3(p):
    'ACCIONES : LLAMADOSUBRUTINA'

def p_acciones4(p):
    'ACCIONES : WRITE'

def p_acciones5(p):
    'ACCIONES : EMPTY'

def p_dimension(p):
    'DIMENSION : NUMERO MASNUMERO'

def p_condicional(p):
    'CONDICIONAL : IF ABRIRPARENTESIS CONDICION CERRARPARENTESIS THEN INSTRUCCIONES ENDIF'

def p_condicional2(p):
    'CONDICIONAL : IF ABRIRPARENTESIS CONDICION CERRARPARENTESIS THEN INSTRUCCIONES ELSE INSTRUCCIONES ENDIF'

def p_condicional3(p):
    'CONDICIONAL : IF ABRIRPARENTESIS CONDICION CERRARPARENTESIS OPERADORLOGICO ABRIRPARENTESIS CONDICION CERRARPARENTESIS THEN INSTRUCCIONES ENDIF'

def p_condicional4(p):
    'CONDICIONAL : IF ABRIRPARENTESIS CONDICION CERRARPARENTESIS OPERADORLOGICO ABRIRPARENTESIS CONDICION CERRARPARENTESIS THEN INSTRUCCIONES ELSE INSTRUCCIONES ENDIF'

def p_condicional5(p):
    'CONDICIONAL : CASE_OF NOMVARIABLE NUMERO DOSPUNTOS INSTRUCCIONES DEFAULT DOSPUNTOS INSTRUCCIONES ENDCASE'

def p_ciclo(p):
    'CICLO : FOR NOMVARIABLE ASIGNACION NOMVARIABLE TO NOMVARIABLE DO INSTRUCCIONES ENDFOR'

def p_ciclo2(p):
    'CICLO : FOR NUMERO ASIGNACION NUMERO TO NUMERO DO INSTRUCCIONES ENDFOR'

def p_ciclo3(p):
    'CICLO : FOR NOMVARIABLE ASIGNACION NOMVARIABLE TO NOMVARIABLE OPERADORLOGICO NOMVARIABLE DO INSTRUCCIONES ENDFOR'

def p_ciclo4(p):
    'CICLO : FOR NUMERO ASIGNACION NUMERO TO NUMERO OPERADORLOGICO NUMERO DO INSTRUCCIONES ENDFOR'

def p_ciclo5(p):
    'CICLO : FOR NOMVARIABLE ASIGNACION NUMERO TO NOMVARIABLE OPERADORLOGICO NOMVARIABLE DO INSTRUCCIONES ENDFOR'

def p_ciclo6(p):
    'CICLO : FOR NOMVARIABLE ASIGNACION NOMVARIABLE TO NOMVARIABLE OPERADORMATEMATICO NOMVARIABLE DO INSTRUCCIONES ENDFOR'

def p_ciclo7(p):
    'CICLO : FOR NUMERO ASIGNACION NUMERO TO NUMERO OPERADORMATEMATICO NUMERO DO INSTRUCCIONES ENDFOR'

def p_ciclo8(p):
    'CICLO : FOR NOMVARIABLE ASIGNACION NOMVARIABLE DOWNTO NOMVARIABLE INC NUMERO DO INSTRUCCIONES ENDFOR'

def p_ciclo9(p):
    'CICLO : FOR NUMERO ASIGNACION NUMERO DOWNTO NUMERO INC NUMERO DO INSTRUCCIONES ENDFOR'

def p_ciclo10(p):
    'CICLO : FOR NOMVARIABLE ASIGNACION NOMVARIABLE DOWNTO NOMVARIABLE INC NUMERO OPERADORLOGICO NOMVARIABLE DO INSTRUCCIONES ENDFOR'

def p_ciclo11(p):
    'CICLO : FOR NUMERO ASIGNACION NUMERO DOWNTO NUMERO INC NUMERO OPERADORLOGICO NUMERO DO INSTRUCCIONES ENDFOR'

def p_ciclo12(p):
    'CICLO : FOR NOMVARIABLE ASIGNACION NUMERO DOWNTO NOMVARIABLE INC NUMERO OPERADORLOGICO NOMVARIABLE DO INSTRUCCIONES ENDFOR'

def p_ciclo13(p):
    'CICLO : FOR NOMVARIABLE ASIGNACION NOMVARIABLE DOWNTO NOMVARIABLE INC NUMERO OPERADORMATEMATICO NOMVARIABLE DO INSTRUCCIONES ENDFOR'

def p_ciclo14(p):
    'CICLO : FOR NUMERO ASIGNACION NUMERO DOWNTO NUMERO INC NUMERO OPERADORMATEMATICO NUMERO DO INSTRUCCIONES ENDFOR'

def p_ciclo15(p):
    'CICLO : WHILE ABRIRPARENTESIS CONDICIONW CERRARPARENTESIS DO INSTRUCCIONES ENDWHILE'

def p_ciclo16(p):
    'CICLO : WHILE ABRIRPARENTESIS CONDICIONW CERRARPARENTESIS OPERADORLOGICO ABRIRPARENTESIS CONDICIONW CERRARPARENTESIS DO INSTRUCCIONES ENDWHILE'

def p_ciclo17(p):
    'CICLO : REPEAT INSTRUCCIONES UNTIL ABRIRPARENTESIS CONDICION CERRARPARENTESIS'

def p_ciclo18(p):
    'CICLO : FOREACH ABRIRPARENTESIS NOMVARIABLE TIPODATO DOSPUNTOS NOMVARIABLE CERRARPARENTESIS INSTRUCCIONES'

######################3 CREO QUE NOS ESTAMOS COMPLICANDO, UNA ESTRUCTURA PODRIA SER UN SIMPLE NOMVARIABLE, OSEA EL LLAMADOSUBRUTINA Y LLAMADOSUBRUTINA3 PODRIAN SER UNOO SOLO Y PARA EL FOREACH SERIA NOMVARIABLE Y NO ESTRUCTURA
def p_llamadosubrutina(p):
    'LLAMADOSUBRUTINA : NOMVARIABLE NOMVARIABLE'

def p_llamadosubrutina2(p):
    'LLAMADOSUBRUTINA : NOMVARIABLE NUMERO'

def p_llamadosubrutina3(p):
    'LLAMADOSUBRUTINA : NOMVARIABLE ESTRUCTURA'

def p_llamadosubrutina4(p):
    'LLAMADOSUBRUTINA : NOMVARIABLE EMPTY'

def p_write(p):
    'WRITELN : NOMVARIABLE PUNTOCOMA'

def p_write2(p):
    'WRITELN : NUMERO PUNTOCOMA'

def p_write3(p):
    'WRITELN : LLAMADOSUBRUTINA PUNTOCOMA'

def p_write4(p):
    'WRITELN : EMPTY'

def p_masnumero(p):
    'MASNUMERO : COMA NUMERO'

def p_masnumero2(p):
    'MASNUMERO : EMPTY'

def p_condicion(p):
    'CONDICION : NOMVARIABLE OPERADORRELACIONAL NOMVARIABLE'

def p_condicion2(p):
    'CONDICION : NOMVARIABLE OPERADORRELACIONAL LLAMADOSUBRUTINA'

def p_condicion3(p):
    'CONDICION : LLAMADOSUBRUTINA OPERADORRELACIONAL LLAMADOSUBRUTINA'

def p_condicion4(p):
    'CONDICION : NOMVARIABLE OPERADORMATEMATICO NOMVARIABLE OPERADORLOGICO NOMVARIABLE'

def p_condicion5(p):
    'CONDICION : NOMVARIABLE OPERADORMATEMATICO NOMVARIABLE OPERADORLOGICO LLAMADOSUBRUTINA'

def p_condicion6(p):
    'CONDICION : LLAMADOSUBRUTINA OPERADORMATEMATICO LLAMADOSUBRUTINA OPERADORLOGICO NOMVARIABLE'

def p_condicion7(p):
    'CONDICION : LLAMADOSUBRUTINA OPERADORMATEMATICO LLAMADOSUBRUTINA OPERADORLOGICO LLAMADOSUBRUTINA'


def p_operadorlogico(p):
    'OPERADORLOGICO : AND'

def p_operadorlogico2(p):
    'OPERADORLOGICO : OR'

def p_operadorlogico3(p):
    'OPERADORLOGICO : NOT'

def p_tipodato(p):
    'TIPODATO : INT'

def p_tipodato2(p):
    'TIPODATO : CHAR'

def p_tipodato3(p):
    'TIPODATO : DOUBLE'

def p_tipodato4(p):
    'TIPODATO : BOOLEAN'

def p_operadormatematico(p):
    'OPERADORMATEMATICO : SUMA '

def p_operadormatematico2(p):
    'OPERADORMATEMATICO : RESTA'

def p_operadormatematico3(p):
    'OPERADORMATEMATICO : MULTIPLICACION'

def p_operadormatematico4(p):
    'OPERADORMATEMATICO : DIVISION'

def p_operadormatematico5(p):
    'OPERADORMATEMATICO : ELEVADO'

def p_modoparametro(p):
    'MODOPARAMETRO : E'

def p_modoparametro2(p):
    'MODOPARAMETRO : S'

def p_modoparametro3(p):
    'MODOPARAMETRO : ES'

def p_operadorrelacionl(p):
    'OPERADORRELACIONAL : IGUAL'

def p_operadorrelacionl2(p):
    'OPERADORRELACIONAL : MENOR'

def p_operadorrelacionl3(p):
    'OPERADORRELACIONAL : MAYOR'

def p_operadorrelacionl4(p):
    'OPERADORRELACIONAL : MENORIGUAL'

def p_operadorrelacionl5(p):
    'OPERADORRELACIONAL : MAYORIGUAL'

def p_operadorrelacionl6(p):
    'OPERADORRELACIONAL : DIFERENTE'

def p_empty(p):
    'EMPTY : '
    pass

def p_error(p):
    if(p != None):
        print("Errror de Sintaxis en la linea " +  str(p.lineno) + " en el token " + str(p.value))
    else:
        print("Errror de Sintaxis")



parser = yacc.yacc()


while True:
   try:
       s = input('')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)