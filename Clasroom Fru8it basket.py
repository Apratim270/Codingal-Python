Basket1={"apple","banana","orange","grapes","kiwi","apple"}
Basket2={"banana","kiwi","mango","papaya","apple","banana"}
print("Basket1:",Basket1)
print("Basket2:",Basket2)


Basket1.add("papaya")
print("Basket1 after adding papaya:",Basket1)



common_fruits=Basket1.intersection(Basket2)
print("Common fruits:",common_fruits)

import array as arr
fruit_counts=arr.array("i",[3,5,2,4])
print("Fruit counts:",fruit_counts)



fruit_counts.insert(0,6)
fruit_counts.append(7)
print("Fruits counted after addind items:",fruit_counts)


count_of_4=fruit_counts.count(4)
print("Number of time 4 appears:",count_of_4)






fruit_counts.reverse()
print("Fruits counted after reversing:",fruit_counts)


print("") 
print("============CLASS FRUIT BASKET=====================")
print("Basket1:",Basket1)
print("Basket2:",Basket2)
print("Shared Fruits:",common_fruits)
print("Fruit counts:",fruit_counts)
print("=========================================================")





