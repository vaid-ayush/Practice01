def calculatetax(price,tax):
    return price*tax

def billing_doc():
    tax_rate=0.18
    products=[{"Name":"Ayush","Age":26,"Bill":5000},{"Name":"Sanchit","Age":28,"Bill":2000}]

    print(f"Name\tPrice\tTax")

    for product in products:
        tax=calculatetax(product["Bill"],tax_rate)
        print(f"{product['Name']}\t{product['Bill']}\t{'Tax'}")
        

print(__name__)        