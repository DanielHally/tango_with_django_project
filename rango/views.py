from django.shortcuts import render

from rango.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': category_list,
        'pages' : page_list,
    }
    return render(request, 'rango/index.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        # Try find a category with the slug given
        category = Category.objects.get(slug=category_name_slug)

        # Get associated pages
        pages = Page.objects.filter(category=category)

        # Update context
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        # Don't do anything, template will display no category message
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
