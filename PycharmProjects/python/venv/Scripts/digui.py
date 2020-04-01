import random
list1=[1,13,6,34,3,23]
list2 = [3,5,7,9]
list3=list1+list2
def one(list3):
    if len(list3)<2:
        return list3
    else:
        res = random.choice(list3)
        small=[i for i in list3 if i<res]
        big = [i for i in list3 if i>res]

        return one(small) + [res] + one(big)
    print(one(small) + [res] + one(big))
one(list3)

