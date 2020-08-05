
# Más sobre parámetros en Python

```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```

```{admonition} Objetivo de la sección
El objetivo de esta sección es estudiar algunas características adicionales para el paso de parámetros que ofrece el lenguaje Python.
```

Estudiaremos algunas características adicionales que ofrece Python para manejar los parámetros de una función con mayor flexibilidad. 
Estas características usualmente no están disponibles en otros lenguajes.

## Parámetros variables

*args (ojo... no tenemos listas ni ciclos!)

def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  

print ...

## Parámetros variables nombrados

**kwargs

def myFun(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 

myFun("Hi", first ='Geeks', mid ='for', last='Geeks')   


## Ejercicios

...


## Más allá de Python


Ambigüedad ...

The syntax for implementing varargs is as follows:

 public int sumNumber(int ... args){
        System.out.println("argument length: " + args.length);
        int sum = 0;
        for(int x: args){
            sum += x;
        }
        return sum;

In order to define vararg, ... (three dots) is used in the formal parameter of a method.

A method that takes variable number of arguments is called a variable-arity method, or simply a varargs method.


Kwargs no existe, pero se pueden usar estructuras en cambio