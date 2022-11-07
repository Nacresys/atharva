from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import contact_us,partners,partner_categories,clients
# Create your views here.


def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name",'')
        subject = request.POST.get("subject",'')
        email = request.POST.get("email",'')
        phone = request.POST.get("phone",'')
        message = request.POST.get("message",'')
        abc = contact_us(name=name,subject=subject,email=email,phone=phone,message=message)
        abc.save()
    return render(request,"contact.html")

def partners_func(request):
    categories = partner_categories.objects.all()
    partner_list = partners.objects.all()
    return render(request,"partners.html",{"categories":categories,"list":partner_list})

def clients_page(request):
    client_list = clients.objects.all()
    return render(request,"clients.html",{"client_list":client_list})

def upload_partners(request):
    category_list = partner_categories.objects.all()
    if request.method == 'POST' and request.FILES['myfile']:
        try:
            name = request.POST.get("name")
            cat_no = request.POST.get("cat_num")
            descr = request.POST.get("description")
            cat = partner_categories.objects.get(cat_id=cat_no)
            category = str(cat.name)
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            sv = partners(name=name,category=category,category_id=cat_no,image=uploaded_file_url,description=descr)
            sv.save()
        except:
            pass
    return render(request,"administrator.html",{"category_list":category_list})

def upload_clients(request):
    if request.method == 'POST':
        try:
            client_name = request.POST.get("client_name")
            type_connect = request.POST.get("type_connect")
            client_img = request.FILES['client_img']
            fc = FileSystemStorage()
            fname = fc.save(client_img.name, client_img)
            img_url = fc.url(fname)
            print(client_name,type_connect,img_url)
            sc = clients(name=client_name,image=img_url,type_connect=type_connect)
            sc.save()
            return redirect('/administrator')
        except:
            pass
    return render(request,"administrator.html")

def solutions(request):
    return render(request,"solutions.html")

def faq(request):
    return render(request,"faq.html")


def jd(request):
    if request.method == 'POST':
        try:
            title = request.POST.get("title")
            qfication = request.POST.get("qualification")
            capabilities = request.POST.get("capabilities")
            jdfile = request.FILES['jdfile']
            fc = FileSystemStorage()
            fname = fc.save(jdfile.name, jdfile)
            jd_url = fc.url(fname)
            sc = job_description(title=title,jdfile=jd_url,qualification=qfication,capabilities=capabilities)
            sc.save()
            return redirect('/administrator')
        except:
            pass
    return render(request, "administrator.html")

def careers(request):
    jdlist = job_description.objects.all()
    return render(request,"careers.html",{"jd":jdlist})
