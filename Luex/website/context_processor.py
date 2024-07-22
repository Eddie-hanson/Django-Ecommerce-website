from .models import Cart, Cart_Item
from .views import _CartID


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(Cart_Id=_CartID(request))
            cart_Items = Cart_Item.objects.all().filter(cart=cart[:1])
            for item in cart_Items:
                cart_count += item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
