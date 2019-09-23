from django.http import JsonResponse
from django.db.models import Count, Sum
from accounts.models import Role
from stocks.models import Product
from sales.models import Sales
from expenses.models import Expenses

def roles_graph(request):
    dataset = Role.objects.values('name').annotate(total=Count('id'))
    chart = {
        'chart': {
            'type': 'column',
            'borderWidth': 0.1
        },
        'title': {'text': 'Number of users per Role'},
        'yAxis': {
            'title': {'text': 'Number of Users'}},
        'xAxis': {
            'title': {'text': 'User Roles'},
            'categories': [data['name'] for data in dataset]
        },
        'series': [{
            'name': 'Roles',
            'data': list(map(lambda row: {'name': row['name'], 'y': row['total']}, dataset))
        }],
        'plotOptions': {
            'column': {
                'colorByPoint': 'true'
            }
        },
        # 'showLegend': 'true'
    }
    return JsonResponse(chart)

def stocks_graph(request):
    dataset = Product.objects.values('name','stock_level')
    chart = {
        'chart': {
            'type': 'column',
            'borderWidth': 0.1
        },
        'title': {'text': 'Stock Level By Product'},
        'yAxis': {
            'title': {'text': 'Level of Product'}},
        'xAxis': {
            'title': {'text': 'Products'},
            'categories': [data['name'] for data in dataset]
        },
        'series': [{
            'name': 'Products',
            'data': list(map(lambda row: {'name': row['name'], 'y': row['stock_level']}, dataset))
        }],
        'plotOptions': {
            'column': {
                'colorByPoint': 'true'
            }
        }
    }
    return JsonResponse(chart)

def sales_graph(request):
    dataset = Sales.objects.values('name','total_amount').annotate(total=Sum('total_amount'))
    chart = {
        'chart': {
            'type': 'pie',
            'borderWidth': 0.1
        },
        'title': {'text': 'Total Revenue By Product'},
        'yAxis': {
            'title': {'text': 'Total Amounts'}},
        'xAxis': {
            'title': {'text': 'Products Sold'},
            'categories': [data['name'] for data in dataset]
        },
        'series': [{
            'name': 'Products',
            'data': list(map(lambda row: {'name': row['name'], 'y': row['total']}, dataset))
        }]
    }
    return JsonResponse(chart)

def expenses_graph(request):
    dataset = Expenses.objects.values('category','amount').annotate(total=Sum('amount'))
    chart = {
        'chart': {
            'type': 'pie',
            'borderWidth': 0.1
        },
        'title': {'text': 'Total Expenses By Category'},
        'yAxis': {
            'title': {'text': 'Total Amounts'}},
        'xAxis': {
            'title': {'text': 'Expenses Incured'},
            'categories': [data['category'] for data in dataset]
        },
        'series': [{
            'name': 'Expenses',
            'data': list(map(lambda row: {'category': row['category'], 'y': row['total']}, dataset))
        }]
    }
    return JsonResponse(chart)
