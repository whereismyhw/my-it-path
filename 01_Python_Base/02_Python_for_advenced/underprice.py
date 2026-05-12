def get_products(file):
    with open(file + ".txt") as f:
        return {k: int(v) for line in f for k, v in [line.strip().split(": ")]}
    
shops = ('desyatochka', 'kubit', 'polosa')
translate = {'desyatochka': 'Десяточка', 'kubit': 'Кубит', 'polosa': 'Полоса'}
shops_d = {shop: get_products(shop) for shop in shops}

buying = [input() for _ in range(int(input()))]
answer = {}

for product in buying:
    price = None
    for k, v in shops_d.items():
        if price is None or v.get(product, float('inf')) <= price:
            price = v.get(product)
            name = k
    answer.setdefault(name, []).append(product)

for shop in shops:
    value = ', '.join(answer.get(shop, ['–']))
    print(f'{translate[shop]}:\n{value}')