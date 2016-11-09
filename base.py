#lex_ula.py
import ply.lex as lex
import sys

def strToList(line):
	return line.split(',')

inputFile = str(sys.argv);
outputFile = "";
fileContents = "";
actualPath = [];
actualPath = strToList(inputFile);
importPathList = actualPath[1]
importPath = importPathList[2:(len(importPathList)-2)]

def importFile(input):
	with open(input) as f:
		lines = f.readlines();
		fileContents = ''.join(lines);
		return fileContents;

importData = importFile(importPath);

def exportFile(outputFile, content):
	f = open(outputFile, 'a');
	f.write(content);
	f.close();

tokens = (
   'FLOAT_LITERAL', 'ID', 'COMMENT', 'WHITESPACE', 'MULTIPLICATION', 'DIVISION', 'ADDITION', 'SUBTRACTION',
   'LPAREN', 'RPAREN', 'EQUALS',
)

# Regular expression rules for simple tokens
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
#t_FLOAT_LITERAL = r"[+-]*?((\d+(\.\d*)?)|\.\d+)([eE][+-]?[0-9]+)?"
t_FLOAT_LITERAL = r'([-+])?\d+(\.\d*)?([eE]([-+])?\d+)?'
t_MULTIPLICATION = r'\#'
t_DIVISION = r'\&'
t_ADDITION = r'\@'
t_SUBTRACTION = r'\$'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'\='
t_ignore_WHITESPACE = r'\s'
#t_COMMENT = r'(?://[^\n]*|/\*(?:(?!\*/).)*\*/)'
t_ignore_COMMENT = r'(/{2}.*)|(/\*([^*]|[\s]|(\*+([^*/]|[\r\n])))*\*+/)'

#-$ - subtraction
#-# - multiplication
#-& - division
#-@ - addition
#
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
#t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
#lexer.input(importData)




