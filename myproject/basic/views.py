from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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