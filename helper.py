from __future__ import print_function
import math

def radiansToDegrees(angle):
    return (180*angle/math.pi)

# while 1: print(radiansToDegrees(float(eval(input("Numero em radianos: ")))))

###########################################################################

numeros = [1, 5, 4, 7, 3, 6, 8, 4, 12, 45, 327, 45, 342, 6,54, 123]

def sortList(lista, mode):

    listaMod = lista

    if mode == "asc":

        listaMod.sort()
        return listaMod

    elif mode == "desc":

        listaMod.sort(reverse = True)
        return listaMod

    else:
        return lista


#print(sortList(numeros, "desc"))

###########################################################################

def toBinary(decimal):
    current = decimal

    binaryArray = []

    binaryString = ""

    while current > 0:
        binaryArray.append(current%2)
        current = math.floor(current/2)

    binaryArray.reverse()

    for i in binaryArray:
        binaryString += (str(i))

    return binaryString

#print(toBinary(123345))

###########################################################################

def countVowels(word):
    
    vowels = ("a", "i", "u", "e", "o")

    count = 0

    for letter in word:
        if letter in vowels:
            count+=1

    return count

print(countVowels("test"))