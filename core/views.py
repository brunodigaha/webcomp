# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from ply import lex

class HomeClass(TemplateView):

	template_name = "core/home.html"


class SobreClass(TemplateView):

	template_name = "core/sobre.html"

class ContatoClass(TemplateView):

	template_name = "core/contato.html"



def analiselexica(request):

	template_name = "core/home.html"
	context={}


	codigo=request.POST.get('codigo','')		
	if codigo:
		context['codigo']=codigo

	print codigo


	reserved = {
	   'print' : 'PRINT',
	   
	    }

	#tupla contendo os tokes
	tokens =[
	    'ID','NUMBER',
	    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
	    'LPAREN','RPAREN',
	    'BEGIN','END','DELIMITER',
	    'AT',
	    ] + list(reserved.values())

	# Tokens
	t_AT      = r'\:'
	t_BEGIN   = r'\{'
	t_END     = r'\}'
	t_DELIMITER = r'\;'
	t_PLUS    = r'\+'
	t_MINUS   = r'-'
	t_TIMES   = r'\*'
	t_DIVIDE  = r'/'
	t_EQUALS  = r'='	
	t_LPAREN  = r'\('
	t_RPAREN  = r'\)'
	#t_ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'


	def t_ID(t):
	    r'[a-zA-Z_][a-zA-Z_0-9]*'
	    t.type = reserved.get(t.value,'ID')    # Check for reserved words
	    return t

	def t_NUMBER(t):
	    r'\d+'
	    try:
	        t.value = int(t.value)
	    except ValueError:
	        print("Integer value too large %d", t.value)
	        t.value = 0
	    return t

	# Ignored characters
	t_ignore = " \r"
	#t_ignore = " \t"
	

	def t_COMMENT(t):
	    r'\#.*'
	    pass
	    # No return value. Token discarded

	def t_newline(t):
	    r'\n+'
	    t.lexer.lineno += t.value.count("\n")
	    
	# Compute column. 
	#     input is the input text string
	#     token is a token instance
	def find_column(input,token):
	    last_cr = input.rfind('\n',0,token.lexpos)
	    if last_cr < 0:
		last_cr = 0
	    column = (token.lexpos - last_cr) + 1
	    return column
	lerror=[]
	def t_error(t):
	    #print("Illegal character '%s'" % t.value[0])
	    lr=(t.value[0],t.lineno,t.lexpos)
	    lerror.append(lr)
	    t.lexer.skip(1)
	    
	lexer = lex.lex()
	#lexer = lex.lex(optimize=1)


	
	#arq.write(data)
	lexer.input(str(codigo))
	

	'''for tok in lexer:
	    #(tipo,valor,linha,posicaodocaractere)
	    print tok'''
	
	llex=[]
	while 1:
	    tok = lex.token()
	    if not tok: break

	    lt=(tok.type,tok.value,tok.lineno,tok.lexpos)
	    llex.append(lt)

	context['llex']=tuple(llex)
	context['lerror']=tuple(lerror)
				
	return render (request,template_name,context)