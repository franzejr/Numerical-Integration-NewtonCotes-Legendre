#Integracao Numerica - Newton Cotes e Gauss-Legendre
#Universidade Federal do Ceara
#Metodos Numericos 2 - Prof. Creto Vidal
# Trabalho 4 
#@franzejr - 0322836

from GaussLegendre import *
from NewtonCotes import * 
import sys,math

def main():
	#Tratamento da Entrada
	if len(sys.argv) == 6:
		estrategiaH = sys.argv[1]
		metodo = sys.argv[2]
		a = float(sys.argv[3])
		b = float(sys.argv[4])
		precisao_NumParticoes = float(sys.argv[5])

	else:
		print "Voce deve inserir:<particoes,tolerancia> <metodo> a b <numeroParticoes,precisao>\n"
		print  "<metodo> = trapezio, simpson, simpson38, boole, legendre\n"
		print "Se for NewtonCotes Aberto ou Fechado o programa ira perguntar depois\n"
		return

	#Condicoes iniciais para o loop
	condicao = 0.1
	n=1
	valor_anterior=0

	if (metodo != "legendre"):
		
		aberto = raw_input("aberto[a]/fechado[f]? [a/f]:\n")
		
		#Saber se o Newton Cotes eh aberto ou fechado
		if (aberto == "a"):
			#Escolhendo qual metodo utilizar de acordo com o usuario
			if (metodo.lower() == "trapezio"):
				metodoIntegracao = TrapezioAberto()
			elif(metodo.lower() == "simpson"):
				metodoIntegracao = SimpsonAberto()
			elif(metodo.lower() == "simpson38"):
				metodoIntegracao = Simpson38Aberto()
			elif(metodo.lower() == "boole"):
				metodoIntegracao = BooleAberto()
		else:
			#Escolhendo os metodos de NewtonCotes Fechados
			if (metodo.lower() == "trapezio"):
				metodoIntegracao = Trapezio()
			elif(metodo.lower() == "simpson"):
				metodoIntegracao = Simpson()
			elif(metodo.lower() == "simpson38"):
				metodoIntegracao = Simpson38()
			elif(metodo.lower() == "boole"):
				metodoIntegracao = Boole()

		#Sabendo quais estrategias H iremos usar
		if(estrategiaH == "tolerancia"):
			while(1):
				if( math.fabs(condicao) < precisao_NumParticoes): break
			
				valor_atual = metodoIntegracao.resolver(a,b,n)
				condicao = valor_atual - valor_anterior
		   
				print  n,valor_atual
				valor_anterior = valor_atual
				n+=1

		elif(estrategiaH == "particoes"):

			for i in range(1,int(precisao_NumParticoes)):
				
				#O Tamanho do Subintervalo vai variar de acordo com o numero de particoes
				tamanhoSubIntevalo = (b - a)/i
				valor_atual = metodoIntegracao.resolver(a,b,i)
		   
				print  i,valor_atual
	else:
		#Instanciando um GaussLegendre
		metodoIntegracao = GaussLegendre(a,b)
		ai = metodoIntegracao.a
		bi = metodoIntegracao.b

		numPontos = int(raw_input("GaussLegendre com quantos pontos?? [2,3,4]:\n"))

		#Escolhendo quais estrategias utilizar
		if(estrategiaH == "tolerancia"):

		   	while(1):
				if( math.fabs(condicao) < precisao_NumParticoes): break
				
				#O Tamanho do Subintervalo vai variar de acordo com o numero de particoes
				tamanhoSubIntevalo = (metodoIntegracao.b - metodoIntegracao.a)/n

				valor_atual = metodoIntegracao.calcular(n,numPontos,tamanhoSubIntevalo,ai,bi)

				condicao = valor_atual - valor_anterior
		   
				print  n,valor_atual
				valor_anterior = valor_atual
				n+=1
		elif (estrategiaH == "particoes"):

			for i in range(1,int(precisao_NumParticoes)):
				#O Tamanho do Subintervalo vai variar de acordo com o numero de particoes
				tamanhoSubIntevalo = (metodoIntegracao.b - metodoIntegracao.a)/i
				valor_atual = metodoIntegracao.calcular(i,numPontos,tamanhoSubIntevalo,ai,bi)
		   
				print  i,valor_atual



main()