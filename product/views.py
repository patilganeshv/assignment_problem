from django.shortcuts import render, HttpResponse
from product.models import Product


def product(request):
	context = {'success': False }
	if request.method == "POST":
		name = request.POST['name']
		desc = request.POST['desc']
		cpi = request.POST['cost_per_item']
		sq = request.POST['stock_quantity']		
		#Volume = cost per item * stock quantity
		volume = (int(cpi) * int(sq))
		ins = Product(Name=name, Description=desc, CostPerItem=cpi, StockQuantity=sq, Volume=volume)
		ins.save()
		context = {'success': True }
	return render(request, 'product.html', context)


def products_list(request):
	allProducts = Product.objects.all()
	context = {'products_list': allProducts}
	return render(request, 'products_list.html', context)	
