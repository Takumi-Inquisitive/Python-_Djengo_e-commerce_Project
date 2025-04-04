from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, Order, OrderItem, Review
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import random
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout as auth_logout
from .forms import ReviewForm
from .models import CartItem

def home(request):
   
    all_products = list(Product.objects.all())
    featured_products = random.sample(all_products, min(4, len(all_products))) if all_products else []
    
    
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    
    context = {
        'featured_products': featured_products,
        'cart_count': cart_count,
    }
    
    return render(request, 'store/home.html', context)

def product_list(request):
    category = request.GET.get('category')
    if category:
        products = Product.objects.filter(category__name__iexact=category)
    else:
        products = Product.objects.all()
    
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'current_category': category
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been submitted!')
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    
    return render(request, 'store/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })

@login_required
def cart_view(request):
    
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next={request.path}')
    
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        
        if not created:
            cart_item.quantity += 1  
        cart_item.save()
        
        messages.success(request, f"{product.name} has been added to your cart!")
        
        # Get the referer (previous page) or default to product list
        referer = request.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer)
        return redirect('product_list')
    
    return redirect('product_list')

def remove_from_cart(request, product_id):
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, user=request.user, product__id=product_id)
        cart_item.delete()

        return JsonResponse({'success': True, 'message': 'Item removed from cart'})
    return JsonResponse({'success': False, 'message': 'Invalid request'})

@login_required
def checkout(request):
    cart_items = CartItem.objects.all()  

   
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    return render(request, 'store/checkout.html', {'cart_items': cart_items})

@login_required
def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)

    for item in order_items:
        item.total_price = item.price * item.quantity  # Calculate total price per item

    total_price = sum(item.total_price for item in order_items)  # Calculate total order price

    return render(request, 'store/order_summary.html', {
        'order_items': order_items,
        'total_price': total_price,
    })

@login_required
def update_cart(request, product_id):
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, user=request.user, product__id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            return JsonResponse({
                'success': True, 
                'message': 'Cart updated successfully',
                'quantity': quantity,
                'total_price': cart_item.product.price * quantity
            })
        else:
            cart_item.delete()
            return JsonResponse({
                'success': True, 
                'message': 'Item removed from cart'
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to TechStore.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'store/register.html', {'form': form})

def search_products(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
    else:
        products = Product.objects.none()
    
    return render(request, 'store/search_results.html', {'products': products, 'query': query})

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')
