from django.shortcuts import render,HttpResponse

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]

# Create your views here.
def home (request):
    text = "<h1>Welcome</h1>!"
    return HttpResponse(text)

def about (request):
    text= "Автор - Аркадий"
    return HttpResponse(text)

def items_list(request):
    item= items[0]
    html_result ="""
    Список товаров:
    <ul>
    <li>Кроссовки адидас</li>
    <li>Куртка</li>
    </ul>
    """