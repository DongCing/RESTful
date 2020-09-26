from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Api.models import Book


# 获取书的列表；创建一本书
@csrf_exempt
def books(request):

    if request.method == "GET":
        book_list = Book.objects.all()
        print(type(book_list))

        book_list_json = []

        for book in book_list:
            book_list_json.append(book.to_dict())

        data = {
            # 通常给前端看这个状态码
            'status': 200,
            'msg': 'ok',
            'data': book_list_json,
        }
        # 对传输时的状态码进行改变
        return JsonResponse(data=data, status=201)

    elif request.method == "POST":
        b_name = request.POST.get('b_name')
        b_price = request.POST.get('b_price')

        book = Book()
        book.b_name = b_name
        book.b_price = b_price
        book.save()

        print("ok")

        data = {
            'status': 201,
            'msg': 'add success',
            'data': book.to_dict()
        }

        return JsonResponse(data=data)


# 获取书，删除指定书
def book(request, bookid):

    if request.method == "GET":

        book_obj = Book.objects.get(pk=bookid)

        data = {
            'status': 200,
            'msg': 'ok',
            'data': book_obj.to_dict(),
        }

        return JsonResponse(data=data)

    elif request.method == "DELETE":

        book_obj = Book.objects.get(pk=bookid)

        book_obj.delete()

        data = {
            'status': 204,
            'msg': 'delete success',
            # 数据删除后，没有数据了，不要字段就不写'data': {},
            # 还有数据，正常返回对象，'data': {},
            # 没有数据了，保留字段，根据字段默认值填写data
            # 对象{}，数组[]，数字0
            'data': {},
        }

        return JsonResponse(data=data)
