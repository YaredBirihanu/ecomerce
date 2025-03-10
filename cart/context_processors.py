from .cart import Cart

#creat context processor so our cart can work on all page

def cart(request):
    
    #return default data from our cart
    return {'cart':Cart(request)}