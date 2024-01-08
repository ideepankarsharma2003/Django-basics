from django.shortcuts import render
from .models import FeaturedProduct

# Create your views here.
def index(request):
    
    fp1= FeaturedProduct()
    fp1.img= "sasti hoodie.png"
    fp1.product_alert= "coming soon"
    fp1.product_title= "sasti hoodie"
    fp1.product_desc= "very comfortable and pretty sasti hoodie"
    fp1.product_price= "100.23"
    fp1.special_offer=True
    
    fp2= FeaturedProduct()
    fp2.img= "bhootbangla.jpg"
    fp2.product_alert= "haunted"
    fp2.product_title= "Bhoot Bangla"
    fp2.product_desc= "very haunted bhoot bangla"
    fp2.product_price= "2590"
    
    fp3= FeaturedProduct()
    fp3.img= "TootiGhadi.png"
    fp3.product_alert= "Tooti Footi"
    fp3.product_title= "Tooti Ghadi"
    fp3.product_desc= "tooti hui ghadi"
    fp3.product_price= "20"
    
    fashion_products= [fp1, fp2, fp3]
    
    return render(request, 'index_fashion.html', {'fashion_products':fashion_products})
