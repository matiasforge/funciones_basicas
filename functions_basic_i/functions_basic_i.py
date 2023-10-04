#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())  # Imprimirá "5"

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Generará un error ya que 'number_of_days...' no está definido.

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())  # Imprimirá "5" y el segundo 'return' nunca se alcanza.

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())  # Imprimirá "5", el 'print(10)' nunca se alcanza.

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)  # Imprimirá "5" (debido al 'print(5)') y luego "None" (ya que 'x' será None).

#6
def add(b, c):
    print(b+c)
print(add(1,2) + add(2,3))
# Imprimirá la suma de 1+2 (3) y la suma de 2+3 (5), pero da error al intentar sumar 'None' ya que 'add()' no tiene 'return'.

#7
def concatenate(b, c):
    return str(b)+str(c)
print(concatenate(2,5))  # Imprimirá "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())  # Imprimirá "100" y luego "10" (debido al 'return 10').

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))  # Imprimirá "7".
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))  # Imprimirá "14".
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))  # Imprimirá "21" (7 + 14).

#10
def addition(b, c):
    return b+c
    return 10
print(addition(3,5))  # Imprimirá "8", el segundo 'return' nunca se alcanza.

#11
b = 500
print(b)  # Imprimirá "500"
def foobar():
    b = 300
    print(b)
print(b)  # Imprimirá "500" nuevamente
foobar()  # Imprimirá "300"
print(b)  # Imprimirá "500" nuevamente

#12
b = 500
print(b)  # Imprimirá "500"
def foobar():
    b = 300
    print(b)
    return b
print(b)  # Imprimirá "500" nuevamente
foobar()  # Imprimirá "300"
print(b)  # Imprimirá "500" nuevamente

#13
b = 500
print(b)  # Imprimirá "500"
def foobar():
    b = 300
    print(b)
    return b
print(b)  # Imprimirá "500" nuevamente
b = foobar()  # Imprimirá "300" y asignará 300 a 'b'
print(b)  # Imprimirá "300"

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Imprimirá "1", "3", "2" en ese orden.

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)  # Imprimirá "1", "3", "5", "10"
