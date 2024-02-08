# Calculadora em Python

print("\n******************* Calculadora em Python *******************")

oper = input("\nDigite a operação desejada (+, -, * ou /): ")
 
num1 = int(input('Digite o primeiro número:')) 
num2 = int(input('Digite o segundo número:'))

if oper == '+':
		soma = (num1 + num2)
		print('O resultado é: %s' %(soma))
elif oper == '-':
		subt = (num1 - num2)
		print('O resultado é: %s' %(subt))
elif oper == '*':
		mult = (num1 * num2)
		print('O resultado é: %s' %(mult))
elif oper == '/':
		div = (num1 / num2)
		print('O resultado é: %s' %(div))    
elif oper != '+' or '-' or '*' or '/':
	print('Operação inválida')
