authorized_users = ['youssef@hotmail.com','muhammed@hotmail.com']
def login_required(func):
    def wrapper(email,*args):
        if email in authorized_users :
            print('your user is authorized')
            return func(email,*args)
        else :
            print(f'user: {email} doesn`t found , please crate an account')
    return wrapper        
@login_required
def adding_items_to_cart(email,product_name,price,quantity):
    subtotal= price*quantity
    print(f'product: {product_name} added to cart')

adding_items_to_cart('youssef@hotmail.com','laptop',15000,1)
adding_items_to_cart('muhammed@hotmail.com','fridge',30000,2)
adding_items_to_cart('ahmed@hotmail.com','mobile',10000,1)    