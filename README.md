# Getting Started with Django

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

