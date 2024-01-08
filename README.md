# Getting Started with Django


![image](https://github.com/ideepankarsharma2003/Django-basics/assets/74599435/d884aa79-a77d-49ea-8ad0-cbe39404bc75)

- Install django
```bash
pip install django
```

- Create django project
```bash
django-admin startproject hello
```

- Run Server
```bash
python .\manage.py runserver
```

- Create your first app
```bash
python .\manage.py startapp firstapp
```

Now our first app is available. We can create a urls.py in `firstapp` which will store the mappings as a list in   `urlpatterns`.
```python 
(function) def path(
    route: str,
    view: (...) -> _ResponseType,
    kwargs: dict[str, Any] = ...,
    name: str = ...
)

# For example ours look like this:
urlpatterns= [
    path('', views.home, name='home')
]
```
Now we also need to have the `home()->_ResponseType` method in our `views.py`


- Django Template Language (DTL)
create the [`templates`](templates) directory for storing the templates.
and then make changes to [hello/settings.py](hello/settings.py) so that the system can understand that the templates are stored in the same directory.
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        # templates are stored in the same directory
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

We use the jinja templates for web pages like [index.html](templates/index.html) extends [base.html](templates/base.html):
```html
{% extends 'base.html' %}

{% block content%}
<h1>Hello {{name}} !!!!</h1>
<h5>This is index.html</h5>
{% endblock %}
``` 


- Middlewares in Django

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # csrf middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```


- Static files

```bash
python .\manage.py collectstatic

156 static files copied to 'C:\Deepankar\Projects\Django\hello\assets'.
```


- Dynamic Content Loading
To load dynamic content in different formats, use your own model object and the populate it:
so our fashion product model in [fashion/models.py](fashion/models.py)  looks like this:
```python
class FeaturedProduct:
    '''featured products in index.html'''
    id: int
    img: str= ""
    product_alert: str= ""
    product_title: str= ""
    product_details_html: str= ""
    product_desc: str= ""
    product_price: float= 0.0
```
Also our [views.py](fashion/views.py) looks like this:
```python 

# Create your views here.
def index(request):
    fp1= FeaturedProduct()
    fp1.product_alert= "coming soon"
    fp1.product_title= "sasti chaddi"
    fp1.product_desc= "very comfortable and pretty sasti chaddi"
    fp1.product_price= "100.23"
    
    return render(request, 'index_fashion.html', {'fp1':fp1})

```

And finally you load that on [index_fashion.html](templates/index_fashion.html) as:
```html

<div class="col-lg-4 col-12 mb-3">
    <div class="product-thumb">
        <a href="product-detail.html">
            <img src="{% static 'images/product/jordan-nix-CkCUvwMXAac-unsplash.jpeg' %}" class="img-fluid product-image" alt="">
        </a>
        <div class="product-top d-flex">
            <span class="product-alert">{{fp1.product_alert}}</span>
            <a href="#" class="bi-heart-fill product-icon ms-auto"></a>
        </div>
        <div class="product-info d-flex">
            <div>
                <h5 class="product-title mb-0">
                    <a href="product-detail.html" class="product-title-link">{{fp1.product_title}}</a>
                </h5>
                <p class="product-p">{{fp1.product_desc}}</p>
            </div>
            <small class="product-price text-muted ms-auto mt-auto mb-5">${{fp1.product_price}}</small>
        </div>
    </div>
</div>
```

Also instead of doing this all manually, you can have a jinja loop for automatically populating every product:

```python

# Create your views here.
def index(request):
    
    fp1= FeaturedProduct()
    fp1.img= "sasti hoodie.png"
    fp1.product_alert= "coming soon"
    fp1.product_title= "sasti hoodie"
    fp1.product_desc= "very comfortable and pretty sasti hoodie"
    fp1.product_price= "100.23"
    
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

```

and then jinja loop would look like:
```html

{% static "images" as base_img_url %}
<!-- specifying that base image url is the path to find images -->
    <!-- Featured Products Loop -->
    {%for fp in fashion_products%}
    <div class="col-lg-4 col-12 mb-3">
        <div class="product-thumb">
            <a href="product-detail.html">
                <!-- <img src="{% static 'images/product/jordan-nix-CkCUvwMXAac-unsplash.jpeg' %}" class="img-fluid product-image" alt=""> -->
                <img src="{{base_img_url}}/{{fp.img}}" class="img-fluid product-image" alt="">
            </a>
            <div class="product-top d-flex">
                <span class="product-alert">{{fp.product_alert}}</span>
                <a href="#" class="bi-heart-fill product-icon ms-auto"></a>
            </div>
            <div class="product-info d-flex">
                <div>
                    <h5 class="product-title mb-0">
                        <a href="product-detail.html" class="product-title-link">{{fp.product_title}}</a>
                    </h5>
                    <p class="product-p">{{fp.product_desc}}</p>
                </div>
                <small class="product-price text-muted ms-auto mt-auto mb-5">${{fp.product_price}}</small>
            </div>
        </div>
    </div>
    {% endfor %}
```
Voila ! now it should appear like : <br>
![image](https://github.com/ideepankarsharma2003/Django-basics/assets/74599435/f8bc04b2-3980-478a-b1c3-d452bbb3ce7c)

