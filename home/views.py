from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact, Order, Party
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json
import math

AREAS = ['Chakiya','Civil Lines','Himmatganj','Kareli','Rajapur']

# Create your views here.
def home(request):
    return render(request, 'index.html')

def adminportal(request):
    print('User authenticated :',request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'adminportal.html')
    else:
        return redirect('login')

def ordersheet(request):
    print('User authenticated :',request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'ordersheet.html')
    else:
        return redirect('login')

def party(request):
    print('User authenticated :',request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if(request.method=='POST'):
            id = request.POST.get('id','NA')
            name = request.POST.get('name','NA')
            area = request.POST.get('area','NA')
            contact = request.POST.get('contact','NA')
            address = request.POST.get('address','NA')
            img = request.POST.get('img','NA')
            lat = request.POST.get('lat',0)
            lng = request.POST.get('lng',0)
            if (not name=='NA') and area in AREAS:
                party = Party(id=id, name=name, area=area, contact=contact, address=address, img=img, lat=lat, lng=lng)
                party.save()
                print('Party posted successfully')

        area = request.GET.get('area',None)
        if area not in AREAS: area = None

        if area is None: parties = Party.objects.all()
        else: parties = Party.objects.filter(area=area)
        totalparties = len(parties)
        totalpages = math.ceil(totalparties/10)
        
        page = request.GET.get('page')
        if page is None: page = 1
        else: page = int(page)
        if page>1: prv = page-1
        else: prv = None
        if page<totalpages: nxt = page+1
        else: nxt = None

        if area is None: area = 'all'
        parties = parties[(page-1)*10:page*10]
        context = {'parties': parties,'pages': range(1,totalpages+1),'page':page,'nxt':nxt,'prv':prv, 'area':area, 'select':getSelectList(area)}
        return render(request,'party.html', context)

def contact(request):
    if(request.method=="POST"):
        # name = request.POST['name']
        # email = request.POST['email']
        # message = request.POST['message']
        name = request.POST.get('name','NA')
        email = request.POST.get('email','NA')
        phone = request.POST.get('phone','NA')        
        message = request.POST.get('message','NA')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        print('Contact posted successfully')

    #return render(request, 'index.html')
    return redirect('home')

def order(request):
    if(request.method=='POST'):
        shopname = request.POST.get('shopname','NA')
        address = request.POST.get('address','NA')
        contact = request.POST.get('contact','NA')
        i1 = request.POST.get('i1',0)
        i2 = request.POST.get('i2',0)
        i3 = request.POST.get('i3',0)
        i4 = request.POST.get('i4',0)
        i5 = request.POST.get('i5',0)
        if not i1.isnumeric():
            i1 = 0
        if not i2.isnumeric():
            i2 = 0
        if not i3.isnumeric():
            i3 = 0
        if not i4.isnumeric():
            i4 = 0
        if not i5.isnumeric():
            i5 = 0
        message = request.POST.get('message','NA')
        order = Order(shopname=shopname, address=address, contact=contact, i1=i1, i2=i2, i3=i3, i4=i4, i5=i5, message=message)
        order.save()
        print("Order posted successfully")

    #return render(request, 'index.html')
    return redirect('home')

def store(request):
    return render(request, 'store.html')

def product(request, slug):
    if slug == 'item1':
        print('item1')
        itemname = 'Table Butter 22 gm'
        itemimage = 'img/item1-small.jpg'
        itemrprice = 8.46
        itemcprice = 10.00
    elif slug == 'item2':
        print('item2')
        itemname = 'Table Butter 50 gm'
        itemimage = 'img/item2-small.jpg'
        itemrprice = 18.00
        itemcprice = 20.00
    elif slug == 'item3':
        print('item3')
        itemname = 'Table Butter 100 gm (TUB)'
        itemimage = 'img/item3-small.jpg'
        itemrprice = 45.25
        itemcprice = 50.00
    elif slug == 'item4':
        print('item4')
        itemname = 'Table Butter 100 gm (CAKE)'
        itemimage = 'img/item4-small.jpg'
        itemrprice = 43.50
        itemcprice = 48.00
    elif slug == 'item5':
        print('item5')
        itemname = 'Table Butter 500 gm'
        itemimage = 'img/item5-small.jpg'
        itemrprice = 213.00
        itemcprice = 235.00
    else:
        print('404')
        return render(request, 'custom404.html')
    
    itemimage = "/static/" + itemimage
    context = {'itemname': itemname, 'itemimage': itemimage, 'itemrprice': itemrprice, 'itemcprice': itemcprice}
    return render(request, 'product.html', context)

def login(request):
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/adminportal')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def getSelectList(area):
    flag = False
    select = ['','','','','','']
    for i in range(5):
        if area==AREAS[i] :
            select[i+1] = 'selected'
            flag = True

    if not flag: select[0] = 'selected'
    return select

# def ujjwal(request):
#     fname = 'D:\Projects\Django\jmd\home\shops-export.json'
#     str_data = open(fname).read()
#     json_data = json.loads(str_data)
#     for entry in json_data:
#         id = entry['id']
#         name = entry['name']
#         area = entry['area']
#         contact = entry['contact']
#         address = entry['address']
#         img = entry['img']
#         lat = entry['lat']
#         lng = entry['lng']
#         party = Party(id=id, name=name, area=area, contact=contact, address=address, img=img, lat=lat, lng=lng)
#         party.save()
#         print(name)
#     return HttpResponse('Done')