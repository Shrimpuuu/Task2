[def dodawanie(a,b):
	return a + b
def odejmowanie(a,b):
	return a - b
def mnozenie(a,b):
	return a * b
def dzielenie(a,b):
	if b!=0:
		return a / b
	else:
		return "nie mozna dzielic przez zero kasztanie"

print("witaj w kalulatorze, wybierz operacje:")
print("1. dodawanie")
print("2. odejmowanie")
print("3. mnozenie")
print("4. dzielenie")

wybor = input("wybierz operacje")
 
if wybor in ('1','2', '3', '4'):
	num1= float(input("podaj pierwsza liczbe: "))
	num2= float(input("podaj durga liczbe: "))
	if wybor == '1':
		print("wynik dodawania: ", dodawanie(num1, num2)
	elif wybor == '2':
		print("wynik odjemowania: ", odejmowanie(num1, num2)
	elif wybor == '3':
		print("wynik mnozenia: ", mnozenie(num1, num2)
	elif wybor == '4':
		print("wynik dzielenie: ", dzielenie(num1, num2)
	else:
		print("co")
