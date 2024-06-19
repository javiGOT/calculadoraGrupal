try :
    while True:
        num1 = int(input(""));
        simbolo = input("");
        num2 = int(input(""));
        if simbolo == "+":
            resultado = num1 + num2;
            print(num1,simbolo,num2,"=",resultado);

except :
    print("Error");