from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from . models import Contact
from . models import Registration,Product,Category,Cart,Order

# Create your views here.
def index (request):
    cat=Category.objects.all().values()
    context={
        "categories":cat
    }

    template=loader.get_template("index.html")
    return HttpResponse(template.render(context,request))

def about (request):
    template=loader.get_template("about.html")
    return HttpResponse(template.render({},request))

def services (request):
    template=loader.get_template("services.html")
    return HttpResponse(template.render({},request))

def contact (request):
    if request.method=='POST':

        contact_name=request.POST['contact_name']
        contact_email=request.POST['contact_email']
        contact_msg=request.POST['contact_msg']

        contact=Contact(
            contact_name=contact_name,
            contact_email=contact_email,
            contact_msg=contact_msg
        )

        contact.save()

    template=loader.get_template("contact.html")
    return HttpResponse(template.render({},request))

def registration (request):
    if "user" in request.session:
        return HttpResponseRedirect ("myaccount")
    
    msg=""
    if request.method=='POST':

        reg_name=request.POST['reg_name']
        reg_email=request.POST['reg_email']
        reg_mob=request.POST['reg_mob']
        reg_username=request.POST['reg_username']
        reg_pwd=request.POST['reg_pwd']

        reg1=Registration.objects.filter(reg_email=reg_email)
        reg2=Registration.objects.filter(reg_username=reg_username)
        reg3=Registration.objects.filter(reg_mob=reg_mob)

        if reg1:
            msg="Email already exist"
        elif reg2:
            msg="Username already exist"
        elif reg3:
            msg="Mobile Number already exist"
        else:
            reg=Registration(
                reg_name=reg_name,
                reg_email=reg_email,
                reg_mob=reg_mob,
                reg_username=reg_username,
                reg_pwd=reg_pwd
        )

            reg.save()

    context={
        "msg":msg
    }
        
    template=loader.get_template("login.html")
    return HttpResponse(template.render(context,request))

def login (request):
    if "user" in request.session:
        return HttpResponseRedirect ("myaccount")
    if request.method=='POST':
        log_username=request.POST['log_username']
        log_pwd=request.POST['log_pwd']

        login=Registration.objects.filter(reg_username=log_username,reg_pwd=log_pwd)
        if login:
            request.session["user"] =log_username
            return HttpResponseRedirect("products")
        
        
    template=loader.get_template("login.html")
    return HttpResponse(template.render({},request))


def myaccount (request):
    if "user" not in request.session:
        return HttpResponseRedirect("login")
    template=loader.get_template("myaccount.html")
    return HttpResponse(template.render({},request))

def logout(request):
    del request.session["user"]
    return HttpResponseRedirect("login")

def addproduct(request):
    msg=''
    if request.method=='POST':

        pro_name=request.POST['pro_name']
        pro_catid=request.POST['pro_catid']
        pro_price=request.POST['pro_price']
        pro_image=request.FILES['pro_image']

        product=Product(
            pro_name=pro_name,
            pro_catid=pro_catid,
            pro_price=pro_price,
            pro_image=pro_image
        )

        product.save()
        msg='Product uploaded successfully'

        

    cats=Category.objects.all().values()
    context={
        'cats':cats,
        'msg' :msg
    }

    template=loader.get_template("addproduct.html")
    return HttpResponse(template.render(context,request))

def products(request):
    if "cid" in request.GET:
        cid=request.GET["cid"]
        pro=Product.objects.filter(pro_catid=cid).values()
    else:
        pro=Product.objects.all().values()
    cat=Category.objects.all().values()
    context ={
        "category":cat,
        "products":pro
    }
    template=loader.get_template("products.html")
    return HttpResponse(template.render(context,request))

def addcategory(request):
    msg=''
    if request.method=='POST':
        cat_name=request.POST['cat_name']
        cat_image=request.FILES['cat_image']

        category=Category(
            cat_name=cat_name,
            cat_image=cat_image
        )

        category.save()
        msg='Product uploaded successfully'
    context={
        'msg':msg,
    }

    template=loader.get_template("addcategory.html")
    return HttpResponse(template.render(context,request))

def addtocart(request,id):
    if "user" not in request.session:
        return HttpResponseRedirect("/login")
    
    prod=Product.objects.filter(id=id)[0]
    user=request.session["user"]

    cart0=Cart.objects.filter(cart_user=user,cart_pid=id)

    if cart0:
        cart=Cart.objects.filter(cart_user=user,cart_pid=id)[0]
        cart.cart_qty=cart.cart_qty+1
        cart.cart_amount=cart.cart_qty*cart.cart_price

        cart.save()
    
    else:
        cart2=Cart(cart_user=user,cart_pid=prod.id,cart_name=prod.pro_name,cart_price=prod.pro_price,cart_image=prod.pro_image,cart_qty=1,cart_amount=prod.pro_price)

        cart2.save()

    return HttpResponseRedirect("/cart") 

def cart(request):  
    if "user" not in request.session:
        return HttpResponseRedirect("/login")
    user=request.session["user"]    
    carts=Cart.objects.filter(cart_user=user)
    context ={
        "carts":carts
    }   
    template=loader.get_template("cart.html")
    return HttpResponse(template.render(context,request))
def cartp(request,id):
    prod=Product.objects.filter(id=id)[0]
    user=request.session["user"]
    cart0=Cart.objects.filter(cart_user=user,cart_pid=id)
    if cart0:
        cart=Cart.objects.filter(cart_user=user,cart_pid=id)[0]
        cart.cart_qty=cart.cart_qty+1
        cart.cart_amount=cart.cart_qty*cart.cart_price
        cart.save()
    return HttpResponseRedirect("/cart")

def cartm(request,id):
    prod=Product.objects.filter(id=id)[0]
    user=request.session["user"]
    cart0=Cart.objects.filter(cart_user=user,cart_pid=id)
    if cart0:
        cart=Cart.objects.filter(cart_user=user,cart_pid=id)[0]
        if cart.cart_qty == 1:
           return HttpResponseRedirect("/cart")
        else:
            cart.cart_qty=cart.cart_qty-1
            cart.cart_amount=cart.cart_qty*cart.cart_price
            cart.save()
    return HttpResponseRedirect("/cart")

def delcart(request,id):
    cart=Cart.objects.filter(id=id)[0]
    cart.delete()
    return HttpResponseRedirect("/cart")


def checkout(request):  
    if "user" not in request.session:
        return HttpResponseRedirect("/login")
           
    user=request.session["user"]  
    check=Cart.objects.filter(cart_user=user)
    checklen=Cart.objects.filter(cart_user=user).count()
    
    total=0
    for x in check:
        total += x.cart_amount
    shpchrg = 99
    gtotal = shpchrg + total

    context ={
        "check":check,
        "checklen":checklen,
        "total":total,
        "shpchrg":shpchrg,
        "gtotal":gtotal
        
    }
    template=loader.get_template("checkout.html")
    return HttpResponse(template.render(context,request))

def checkp(request,id):
    prod=Product.objects.filter(id=id)[0]
    user=request.session["user"]
    cart0=Cart.objects.filter(cart_user=user,cart_pid=id)
    if cart0:
        cart=Cart.objects.filter(cart_user=user,cart_pid=id)[0]
        cart.cart_qty=cart.cart_qty+1
        cart.cart_amount=cart.cart_qty*cart.cart_price
        cart.save()
    return HttpResponseRedirect("/checkout")

def checkm(request,id):
    prod=Product.objects.filter(id=id)[0]
    user=request.session["user"]
    cart0=Cart.objects.filter(cart_user=user,cart_pid=id)
    if cart0:
        cart=Cart.objects.filter(cart_user=user,cart_pid=id)[0]
        if cart.cart_qty == 1:
           return HttpResponseRedirect("/checkout")
        else:
            cart.cart_qty=cart.cart_qty-1
            cart.cart_amount=cart.cart_qty*cart.cart_price
            cart.save()
    return HttpResponseRedirect("/checkout")

def delitem(request,id):
    cart=Cart.objects.filter(id=id)[0]
    cart.delete()
    return HttpResponseRedirect("/checkout")

def profile(request):
    if "user" not in request.session:
        return HttpResponseRedirect ("login")
    user=request.session["user"]
    profile=Registration.objects.filter(reg_username=user)[0]

    msg=""
    if request.method=="POST":
        reg_name=request.POST ["reg_name"]
        reg_email=request.POST ["reg_email"]
        reg_mob=request.POST ["reg_mob"]

        profile.reg_name=reg_name
        profile.reg_email=reg_email
        profile.reg_mob=reg_mob

        profile.save()
        return HttpResponseRedirect("/profile")
    
    context={
        "profile":profile,

    }
    
    template=loader.get_template("profile.html")
    return HttpResponse(template.render(context,request))

def confirm (request):
    if "user" not in request.session:
        return HttpResponseRedirect("/login")
    
    template=loader.get_template("confirm.html")
    return HttpResponse(template.render({},request))


def order (request):
    user=request.session["user"]
    ord=Cart.objects.filter(cart_user=user)
    for x in ord:
            order_user=x.cart_user
            order_pid=x.cart_pid
            order_proname=x.cart_name
            order_price=x.cart_price
            order_image=x.cart_image
            order_qty=x.cart_qty
            order_amount=x.cart_amount
            if request.method=='POST':
                order_name=request.POST['order_name']
                order_number=request.POST['order_number']
                order_address=request.POST['order_address']
                order_payment=request.POST['COD']
                user=request.session["user"]
                order=Order(
                    order_name=order_name,
                    order_number=order_number,
                    order_address=order_address,
                    order_payment=order_payment,
                    order_user=order_user,
                    order_pid=order_pid,
                    order_proname=order_proname,
                    order_price=order_price,
                    order_image=order_image,
                    order_qty=order_qty,
                    order_amount=order_amount,

            )
            order.save()

    return HttpResponseRedirect("/confirm") 


