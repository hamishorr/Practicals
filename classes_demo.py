
_author_ = 'Hamish Orr'


class Product:
    def __init__(self,name='', price=0.0, on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = on_sale

    def __str__(self):
        if self.is_on_sale:
            on_sale_str = "(on sale)"
        else:
            on_sale_str = ""

        return "{}, ${:.2f}, {}".format(self.name, self.price, on_sale_str)

    def put_on_sale(self):
        self.is_on_sale = True
        self.price *= 0.9


item = Product("iPhone",900,False)
item.put_on_sale()

print(item)
