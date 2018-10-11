import Modelo.ply.lex as lex
import sys

keywords = {
    # METODOS PILA
    'STACKS': 'STACKS',
    'PUSHS': 'PUSHS',
    'POPS': 'POPS',
    'EMPTYS': 'EMPTYS',
    'CLEARS': 'CLEARS',

    # METODOS COLA
    'QUEUES': 'QUEUES',
    'ADDQ': 'ADDG',
    'POLLQ': 'POLLG',
    'REMOVEQ': 'REMOVEG',

    # METODOS LISTA
    'LISTS': 'LISTS',
    'ADDL': 'ADDL',
    'SIZEL': 'SIZEL',
    'REMOVEL': 'REMOVEL',

    # CONDICIONALES
    'ELSE': 'ELSE',
    'IF': 'IF',
    'ENDIF': 'ENDIF',
    'CASE': 'CASE',

    #ESTRUCTURAS
    'ARBOL': 'ARBOL',
    'GRAFO': 'GRAFO',

    # CICLOS
    'FOR': 'FOR',
    'TO': 'TO',
    'DO': 'DO',
    'DOWN': 'DOWN',
    'INC': 'INC',
    'ENDFOR': 'ENDFOR',
    'FOREACH': 'FOREACH',
    'ENDFOREACH': 'ENDFOREACH',
    'REPEAT': 'REPEAT',
    'UNTIL': 'UNTIL',
    'WHILE': 'WHILE',
    'ENDWHILE': 'ENDWHILE',

    # SUBRUTINAS
    'PROCEDURE': 'PROCEDURE',
    'FUNTION': 'FUNTION',
    'RETURN': 'RETURN',

    # OPERADORES LÓGICOS
    'AND': 'AND',
    'OR': 'OR',
    'NOT': 'NOT',

    # OPERADORES ARITMETICOS
    'DIV': 'DIV',
    'MOD': 'MOD',

    # TIPOS DE DATOS
    'INT': 'INT',
    'CHAR': 'CHAR',
    'FLOAT': 'FLOAT',
    'DOUBLE': 'DOUBLE',
    'BOOLEAN': 'BOOLEAN',

    'BREAK': 'BREAK',
    'FALSE': 'FALSE',
    'TRUE': 'TRUE',
    'VAR': 'VAR',
    'THEN': 'THEN',
    'WHEN': 'WHEN',
    'BEGIN': 'BEGIN',
    'RAIZ': 'RAIZ',
    'POWER': 'POWER',
    'LAMBDA': 'LAMBDA',
    'WRITE': 'WRITE',

}

tokens = [
    'NOMVARIABLE',
    'NUMERO',
    'COMILLASIMPLE',
    'COMA',
    'ABRIRCORCHETE',
    'CERRARCORCHETE',
    'ABRIRLLAVE',
    'CERRARLLAVE',
    'ABRIRPARENTESIS',
    'CERRARPARETENSIS',
    'GUIONBAJO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'ELEVADO',
    'ASIGNACION',
    'IGUAL',
    'MENOR',
    'MAYOR',
    'MENORIGUAL',
    'MAYORIGUAL',
    'DIFERENTE'
] + list(keywords.values())

def t_comentario(t):
    r'\#.*' # el caracter numerico junto a cualquier otra cosa exepto una nueva linea (.), 0 o muchas veces (*)
    pass
    # No retornamos nada, porque descartamos el token

def t_nomvariable(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'nomvariable') #Si no esta en las palabras reservadas retornamos el ID
    #Sino la palabra reservada
    return t

def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

t_COMILLASIMPLE = r'\ char(27) '
t_COMA = r'\ , '
t_ABRIRCORCHETE = r'\ [ '
t_CERRARCORCHETE = r'\ ] '
t_ABRIRLLAVE = r'\ { '
t_CERRARLLAVE = r'\ } '
t_ABRIRPARENTESIS = r'\ ( '
t_CERRARPARENTESIS = r' \ )'
t_GUIONBAJO = r'\ _ '
t_SUMA = r'\ + '
t_RESTA = r'\ - '
t_MULTIPLICACION = r'\ * '
t_DIVISION = r'\ / '
t_ELEVADO = r'\ ^ '
t_ASIGNACION = r'\ <- '
t_IGUAL = r'\ = '
t_MENOR = r'\ < '
t_MAYOR = r'\ > '
t_MENORIGUAL = r'\ <= '
t_MAYORIGUAL = r'\ >= '
t_DIFERENTE = r'\ <> '


def t_newline(t):
    r'\n+'  # Regex salto de linea una o mas veces
    t.lexer.lineno = len(t.value)


# Un string que contiene los caracteres que ingnoraremos en este caso los espacios y tabulaciones
t_ignore = ' \t'


# Regla que manejare los errores, cuando encontramos un caracter no valido
def t_error(t):
    print("Caracter invalido '%s'" % t.value[0], sys.stderr)  # imprimimos como error
    t.lexer.skip(1)


lexer = lex.lex()

