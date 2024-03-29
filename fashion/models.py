from django.db import models

# Create your models here.


# Each product has its own:

#                         <div class="col-lg-4 col-12 mb-3">      
#                             <div class="product-thumb">
#                                 <a href="product-detail.html">
#                                     <img src="{% static 'images/product/evan-mcdougall-qnh1odlqOmk-unsplash.jpeg' %}" class="img-fluid product-image" alt="">
#                                 </a>

#                                 <div class="product-top d-flex">
#                                     <span class="product-alert me-auto">New Arrival</span>

#                                     <a href="#" class="bi-heart-fill product-icon"></a>
#                                 </div>

#                                 <div class="product-info d-flex">
#                                     <div>
#                                         <h5 class="product-title mb-0">
#                                             <a href="product-detail.html" class="product-title-link">Tree pot</a>
#                                         </h5>

#                                         <p class="product-p">Original package design from house</p>
#                                     </div>

#                                     <small class="product-price text-muted ms-auto mt-auto mb-5">$25</small>
#                                 </div>
#                             </div>
#                         </div>

class FeaturedProduct:
    '''featured products in index.html'''
    id: int
    img: str= ""
    product_alert: str= ""
    product_title: str= ""
    product_details_html: str= ""
    product_desc: str= ""
    product_price: float= 0.0
    special_offer:bool= False
