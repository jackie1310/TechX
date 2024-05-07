# biến
title = "hello"

# hàm
def getTitle():
    print(title)

# hash table
object = {
    "id": 123,
    "name": "abc"
}
# class
# thuộc tính: biến
# phương thức: hàm

# đối tượng => lớp đối tượng 

# lớp đối tượng Product
# thuộc tính: id, name, price
# phương thức: in ra thông tin Product, tính chiết khấu (price * 5)

class Product:
    def __init__(self, id, name, price):
        self.id = id # 1
        self.name = name # An
        self.price = price # 10 

    def infoProduct(self):
        print(f"id: {self.id} - name: {self.name} - price: {self.price} ")

    def tinhChietKhau(self, phanTram):
        return self.price * phanTram

    def tinhKhuyenMai(self):
        chietKhau = self.tinhChietKhau(10)
        return self.price + chietKhau

# đối tượng
product = Product(1, "An", 10)

product.infoProduct()

print(product.tinhChietKhau(5))
print(product.tinhKhuyenMai())

print(product.name)