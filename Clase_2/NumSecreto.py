print("Adivina el numero secreto\nIngrese la siguente informacion:")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
num = int(input("Digite un numero al azar: "))
numsecreto = 3 
if num==numsecreto: 
    print("Felicidades!", nombre, apellido, ", has elegido el número  correcto. Este era el número:", numsecreto)
else: print("Lo sentimos, has fallado al adivinar, pero muchas gracias por intentarlo. Suerte en la proxima!!!")