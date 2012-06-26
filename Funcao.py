#funcao que iremos utilizar
import math

########## Trigonometric functions
# math.acos(x)
# 	Return the arc cosine of x, in radians.
# math.asin(x)
# 	Return the arc sine of x, in radians.
# math.atan(x)
# 	Return the arc tangent of x, in radians.
# math.atan2(y, x)
# 	Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.
# math.cos(x)
# 	Return the cosine of x radians.
# math.hypot(x, y)
# 	Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).
# math.sin(x)
# 	Return the sine of x radians.
# math.tan(x)
# 	Return the tangent of x radians.

########## Hyperbolic functions
# math.acosh(x)
# 	Return the inverse hyperbolic cosine of x.
# math.asinh(x)
# 	Return the inverse hyperbolic sine of x.
# math.atanh(x)
# 	Return the inverse hyperbolic tangent of x.
# math.cosh(x)
# 	Return the hyperbolic cosine of x.
# math.sinh(x)
# 	Return the hyperbolic sine of x.
# math.tanh(x)
# 	Return the hyperbolic tangent of x.


def f(x):
	#return math.exp(-x)*math.sin(x)
	#return 1/(math.sqrt(4-x*x))
	#return 1/(x*x*x + 1)
	return 2*x + 90 /(x*x*x + 1)

#Funcao Generica para calculo do Xi
#intervaloA: inicio do intervalo A
#intervaloB: final da parte onde vamos integrar
#i: qual Xi queremos. Ex.: x0, x1...xN
#numIntervalos: Se o polinomio eh de grau n fechado, entao teremos 2 intervalos, por exemplo, n-1 intervalos, n+1 pontos
############### Se o polinomio eh de grau n aberto, n+2 intervalos, n+1 pontos
def calcularXi(intervaloA, intervaloB, i, numIntervalos):
	return intervaloA + i * (intervaloB - intervaloA) / numIntervalos
