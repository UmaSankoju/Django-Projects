from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from basic.models import UserProfile, Employee, Product
# Create your views here.
def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contactus(request):
    return render(request, 'contactus.html')

def sample1(request):
    qp1 = request.GET.get("name")
    return HttpResponse(f"Hello {qp1}  welcome to the website")

def sample(request):
    info = {"data":[{"name": "uma", "city":"hyd", "gender":"female"},{"name": "rishi", "city":"chennai", "gender":"male"},{"name": "harsha", "city":"banglore", "gender":"male"}]}
    return JsonResponse(info)

## Dynamic response using query parameters ##

def productinfo(request):
    product_name = request.GET.get("product", "mobile")
    quantity = int(request.GET.get("quantity", 1))      #mobile, 1, 25000 are default  values
    price = int(request.GET.get("price", 25000))
    
    #  ==> this is for add two are three items in one go
    # product_names = request.GET.getlist("product")
    # quantities = request.GET.getlist("quantity")
    # prices = request.GET.getlist("price") 
    
    #example ==> /productinfo?product=mobile&quantity=1&price=25000&product=laptop&quantity=2&price=60000

     
    data = {"product":product_name,"quantity":quantity, "price":price}
    return JsonResponse(data)


## filtering using Qyuery parameters ##

def studentdata(request):
    
    data = {"data":[{"name": "uma", "city":"hyd", "gender":"female"},{"name": "rishi", "city":"hyd", "gender":"male"},{"name": "harsha", "city":"banglore", "gender":"male"}]}
    filtereddata = []
    qp = request.GET.get("name")
    qp1 =  request.GET.get("city")
    qp2 = request.GET.get("gender")
    for item in data["data"]:
            
        match_name = qp and item["name"].lower() == qp.lower()
        match_city = qp1 and item["city"].lower() == qp1.lower()
        match_gender = qp2 and item["gender"].lower() == qp2.lower()

        if match_name or match_city or match_gender:
            filtereddata.append(item)
            
    if not qp and not qp1 and not qp2:
        return JsonResponse(data)
    
    return JsonResponse({"data": filtereddata})
   
   ## Pagination ##
     
def pagination(request):

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

   
    page = int(request.GET.get("page", 1))
    limit = int(request.GET.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit
    items = data[start:end]


    res = {
        "page": page,
        "limit": limit,
        "total_items": len(data),
        "total_pages": (len(data) + limit - 1) // limit,
        "items": items,
    }

    return JsonResponse(res)

def pagination1(request):
    fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Strawberry", "Pineapple", "Kiwi", "Watermelon", "Peach"]
    page = int(request.GET.get("page", 1))
    limit = int(request.GET.get("limit", 3))
    
    start = (page-1)*limit
    end = page*limit
    total_pages = (len(fruits) + limit - 1) // limit
    result = fruits[start:end]
    res = {"status":"success","current_page":page, "total_pages":total_pages, "fruits":result}
    return JsonResponse (res)

@csrf_exempt
def createdata(request):
    try:
        if request.method =="POST":
            data = json.loads(request.body) #dictionary
            name = data.get("name") #making name proprty from dictionary
            age = data.get("age")
            city = data.get("city")
            UserProfile.objects.create(name=name, age=age, city=city)
            print(data)
        return JsonResponse({"status":"success", "data":data, "statuscode":201}, status = 201)
    except Exception as e:
        return JsonResponse({"statuscode":500, "message":"internal server error"})
# @csrf_exempt
# def createproduct(request):
#     if request.method =="POST":
#         data = json.loads(request.body)
#         print(data)
#     return JsonResponse({"status":"success", "data":data, "statuscode":201})

@csrf_exempt
def createEmployee(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            Employee.objects.create(emp_name = data.get("emp_name"), emp_sal = data.get("emp_sal"), emp_email = data.get("emp_email"))
            print(data)
        return JsonResponse({"status":"success", "data":data, "statuscode":201}, status = 201)
    except IntegrityError as e:
        return JsonResponse({"statuscode":500, "message":"duplicate values are not allowed / check the field names properly"}, status = 401)
    except Exception as e:
        return JsonResponse({"statuscode":500, "message":str(e)}, status = 500)
    finally:
        print("done")
        
@csrf_exempt
def createproduct(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            Product.objects.create(product_name = data.get("product_name"), product_price = data.get("product_price"), product_quantity = data.get("product_quantity"))
            print(data)
        return JsonResponse({"status":"success", "data":data, "total_price": int(data.get("product_price")) * int(data.get("product_quantity")), "statuscode":201}, status = 201)
    except IntegrityError as e:
        return JsonResponse({"statuscode":500, "message":"duplicate values are not allowed / check the field names properly"}, status = 401)
    except Exception as e:
        return JsonResponse({"statuscode":500, "message":str(e)}, status = 500)
    finally:
        print("done")        