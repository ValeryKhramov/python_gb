name = "Alex"
ZERO = 0  # Константаge
age = None

a = 42
print(id(a))

a = "Hello world!"
print(id(a))

a = 3.14 / 3
print(id(a))

print(name, age, a, 456, "text", sep=' (=^.^=) ', end="#")
print("any text")

result = input("Input your text: ")
print("Your text = ", result)

# Антипаттерн "Магические числа"

ADULT = 18
age = int(input("Сколько тебе лет?: "))
how_old = ADULT - age
print(f'{how_old} лет осталось до совершеннолетия!')




