#parse_ula.py
import ply.yacc as yacc;
import sys
import lex_ula as lex_ula;
import base as base
import os

clear = lambda: os.system('cls')
tokens = lex_ula.tokens;

def strToList(line):
	return line.split(',')

inputFile = str(sys.argv);
outputFile = "";
fileContents = "";
actualPath = [];
actualPath = strToList(inputFile);
importPathList = actualPath[1]
importPath = importPathList[2:(len(importPathList))-2]
exportPath = importPath[0:len(importPath)-4] + ".ast"
aTree = "";

def importFile(input):
	with open(input) as f:
		lines = f.readlines();
		fileContents = ''.join(lines);
		return fileContents;

importData = importFile(importPath);

def deleteContent(fName):
    with open(fName, "w"):
        pass

def exportFile(outputFile, content):
	f = open(outputFile, 'a');
	f.write(content);
	f.close();

def p_start(p):
	'''start : program'''
	p[0] = ('Start', p[1])

def p_program(p):
	'''program : multStatements '''
	p[0] = ('Program', p[1])

def p_multStatements(p):
	'''multStatements : statement multStatements'''
	p[0] = (p[1],p[2])

def p_multStatememts_empty(p):
	'''multStatements : Empty'''

def p_statement(p):
	'''statement : ID EQUALS expression'''
	p[0] = ('AssignStatement','ID,'+p[1], p[3])

def p_expression_plus(p):
	'''expression : expression ADDITION term'''
	p[0] = ('AddExpression',p[1],p[3])

def p_expression_minus(p):
	'expression : expression SUBTRACTION term'
	p[0] = ('SubExpression',p[1],p[3])

def p_expression_term(p):
	'''expression : term'''
	p[0] = p[1]

def p_term_div(p):
	'''term : term DIVISION factor'''
	p[0] = ('DivExpression',p[1],p[3])

def p_term_mult(p):
	'''term : term MULTIPLICATION factor'''
	p[0] = ('MulExpression',p[1],p[3])

def p_term_factor(p):
	'''term : factor'''
	p[0] = p[1]

def p_factor_expr(p):
	'''factor : LPAREN expression RPAREN'''
	p[0] = p[2]

def p_factor_float(p):
	'''factor : FLOAT_LITERAL'''
	p[0] = ('FloatExpression','FLOAT_LITERAL,'+ p[1])

def p_factor_ID(p):
	'''factor : ID'''
	p[0] = ('IdentifierExpression','ID,'+p[1])

def p_error(p):
    yacc.yacc().errok();
    #print "Syntax error in input!"

def p_empty(p):
    '''Empty :'''
    # p[0] = (())
    pass

# def p_error_whitespace(p):
#     '''statement : statement WHITESPACE statement'''
#     print("Whitespace encountered")
#
# def p_error_comment(p):
#     '''statement : COMMENT'''
#     print("Comment found")

parser = yacc.yacc()

def ast(tup, i):
    for item in tup:
        if type(item) == type(()):#)item is tuple:
            ast(item,i)
        else:
            if item == None:
                a = 0;
            else :
                #print('\t'*i + item)
                global aTree
                aTree = aTree + '\t'*i + item + "\n"
                if item[0:2]!='ID':
                    i+=1
                elif item[0:2 == 'ID'] :
                    i-=1;
                else:
                    a = 3;

def main():
	treeTuple = parser.parse(importData)
	ast(treeTuple,0)
	deleteContent(exportPath);
	exportFile(exportPath,aTree)
	print(aTree);




main()
definer();


