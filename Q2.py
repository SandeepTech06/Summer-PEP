
def count_Dupli_Prod(name, price, weight):
    duplicate = 0
    product = []

    for i in range(len(name)):
        if (name[i], price[i], weight[i]) in product:
            duplicate += 1
        else:
            product.append((name[i], price[i], weight[i]))

    return duplicate


name = ["Apple", "Banana", "Orange", "Apple", "Banana"]
price = [100, 50, 80, 100, 50]
weight = [3, 2, 1, 3, 2]

print(count_Dupli_Prod(name, price, weight))