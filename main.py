#1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, 
#non-scalar verilerden de oluşabilir. 
#Örnek olarak:

#input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

#output: [1,'a','cat',2,3,'dog',4,5]



inputList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(inputList):
    flattenList=[]
    for item in inputList:
        if type(item) == list:
            flattenList += flatten(item)
        else:
            flattenList.append(item)
    
    return flattenList
    

print(flatten(inputList))

#2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
# Örnek olarak:

#input: [[1, 2], [3, 4], [5, 6, 7]]

#output: [[[7, 6, 5], [4, 3], [2, 1]]

inputList2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(inputList):
    reverseList=[]
    for item in inputList:
        reverseList.append(item[::-1])
    
    return reverseList[::-1]

print(reverse(inputList2))