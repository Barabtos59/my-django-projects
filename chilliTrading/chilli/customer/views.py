from django.shortcuts import render

from customer.models import login

from customer.models import farmer_details

from customer.models import owner_detils

from customer.models import rate_chart


# Create your views here.

def showindex(request):
    userdict = login.objects.all()
    return render(request,"index.html",{"userdict":userdict})
def insertlogin(request):
    if request.method == "POST":
        s1 = request.POST.get('username')
        s2 = request.POST.get('password')
        login.objects.create(username=s1, password=s2)
    return render(request, "login.html")
    return render(request, "login.html")

def showlogin(request):
    userdict = login.objects.all()
    return render(request,"viewlogin.html",{"userdict":userdict})

def insertfarmer_details(request):
    if request.method == "POST":
        s1 = request.POST.get('farmer_id')
        s2 = request.POST.get('farmer_name')
        s3 = request.POST.get('village')
        s4 = request.POST.get('City')
        s5 = request.POST.get('contact_number')
        farmer_details.objects.create(farmer_id=s1, farmer_name=s2, village=s3, City=s4, contact_number=s5)
    return render(request, "farmer_details.html")
    return render(request, "farmer_details.html")

def showfarmerdetails(request):
    userdict=farmer_details.objects.all()
    return render(request,"viewfarmerdetails.html",{"userdict":userdict})



def insertownerdetails(request):
    if request.method == "POST":
        s1 = request.POST.get('owner_id')
        s2 = request.POST.get('name')
        s3 = request.POST.get('address')
        s4 = request.POST.get('city')
        s5 = request.POST.get('email_id')
        s6 = request.POST.get('contact_number')

        owner_detils.objects.create(owner_id=s1, name=s2, address=s3, city=s4, email_id=s5, contact_number=s6)
        return render(request, "owner_details.html")
    return render(request, "owner_details.html")


def showownerdetails(request):
    userdict=owner_detils.objects.all()
    return render(request,"viewownerdetails.html",{"userdict":userdict})

def insertrate_chart(request):
    if request.method == "POST":
        s1 = request.POST.get('warehouse_id')
        s2 = request.POST.get('rate_per_month')
        s3 = request.POST.get('per_square_meter')
        s4 = request.POST.get('min_space')
        s5 = request.POST.get('max_space')
        rate_chart.objects.create(warehouse_id=s1, rate_per_month=s2, per_square_meter=s3, min_space=s4, max_space=s5)
        return render(request, "rate_chart.html")
    return render(request, "rate_chart.html")

def showrate_chart(request):
    userdict=rate_chart.objects.all()
    return render(request,"viewrate_chart.html",{"userdict":userdict})

def insertrequest_for_storage(request):
    if request.method == "POST":
        s1 = request.POST.get('request_id')
        s2 = request.POST.get('farmer_id')
        s3 = request.POST.get('warehouse_id')
        s4 = request.POST.get('quantity')
        s5 = request.POST.get('from_date')
        s5 = request.POST.get('to_date')
        s5 = request.POST.get('status')
        rate_chart.objects.create(request_id=s1, farmer_id=s2, warehouse_id=s3, quantity=s4, from_date=s5, to_date=s6, status=s7)
        return render(request, "request_for_storage.html")
    return render(request, "request_for_storage.html")

def showrequest_for_storage(request):
    userdict=rate_chart.objects.all()
    return render(request,"viewrequest_for_storage.html",{"userdict":userdict})

def insertwarehouse_details(request):
    if request.method == "POST":
        s1 = request.POST.get('warehouse_id')
        s2 = request.POST.get('warehouse_name')
        s3 = request.POST.get('capacity')
        s4 = request.POST.get('warehouse_type')
        s5 = request.POST.get('address')
        s5 = request.POST.get('owner_id')
        s5 = request.POST.get('contact_number')
        rate_chart.objects.create(warehouse_id=s1, warehouse_name=s2, capacity=s3, warehouse_type=s4, address=s5, owner_id=s6, contact_number=s7)
        return render(request, "warehouse_details.html")
    return render(request, "warehouse_details.html")

def showwarehouse_details(request):
    userdict=rate_chart.objects.all()
    return render(request,"viewwarehouse_details.html",{"userdict":userdict})


def showfarmerhome(request):
    userdict = login.objects.all()
    return render(request,"farmer_home.html",{"userdict":userdict})

def showownerhome(request):
    userdict = login.objects.all()
    return render(request,"owner_home.html",{"userdict":userdict})


def forgot_password(request):
    if request.method == "POST":
        s1 = request.POST.get('username')
        forgotpassword.objects.create(username=s1)
        return render(request, "forgotpassword.html")
    return render(request, "forgotpassword.html")

def change_password(request):
    if request.method == "POST":
        s1 = request.POST.get('old_password')
        s3 = request.POST.get('new_password')
        s3 = request.POST.get('cunfirm_password')
        changepassword.objects.create(old_password=s1,new_password=s2,cunfirm_password=s3)
        return render(request, "changepassword.html")
    return render(request, "changepassword.html")

def logcheck(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        count=login.objects.filter(username=username).count()
        if count>=1:
            udata=login.objects.get(username=username)
            upass=udata.password
            utype=udata.utype
            if upass==password:
                if utype=='owner':
                    return render(request,'owner_home.html')
                if utype=='farmer':
                    return render(request,'farmer_home.html')

            else:
                return render(request,'login.html',{'msg':'invalid password'})
        else:
            return render(request, 'login.html', {'msg': 'invalid username'})

    return render(request,'login.html')