from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from store.models import Product


def cart_summary(request):
    #get the cart
    cart=Cart(request)
    cart_products=cart.get_prods

    return render(request,'cart/cart_summary.html',{'cart_products':cart_products})
    


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from store.models import Product
from .cart import Cart

def cart_add(request):
    # Get the cart
    cart = Cart(request)

    # Check if the request is a POST request
    if request.method == 'POST' and request.POST.get('action') == 'post':
        # Get the product ID from the POST data
        product_id = int(request.POST.get('product_id'))

        # Look up the product in the database
        product = get_object_or_404(Product, id=product_id)

        # Add the product to the cart
        cart.add(product=product)

        # Get the updated cart quantity
        cart_quantity = len(cart)

        # Return a JSON response with the updated cart quantity
        response = JsonResponse({'quantity': cart_quantity})
        return response

    # If the request is not valid, return an error response
    return JsonResponse({'error': 'Invalid request'}, status=400)


def cart_delete(request):
    pass

def cart_update(request):
    pass