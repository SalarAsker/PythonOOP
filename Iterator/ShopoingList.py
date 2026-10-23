
class ShoppingList:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)


shopping = ShoppingList()

shopping.add("bananas")
shopping.add("apples")
shopping.add("pineapple")

for product in shopping.products:
    print(product)

# for product in shopping:
#     print(product)



class Counter:
    def __init__(self):
        self.numbers = [1, 2, 3]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            item = self.numbers[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

counter = Counter()

for number in counter:
    print(number)