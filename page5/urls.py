from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("contact",views.contact,name="contact"),
    path("registration",views.registration,name="registration"),
    path("login",views.login,name="login"),
    path("myaccount",views.myaccount,name="myaccount"),
    path("logout",views.logout,name="logout"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("products",views.products,name="products"),
    path("addcategory",views.addcategory,name="addcategory"),
    path("addtocart/<int:id>",views.addtocart,name="addtocart"),
    path("cart",views.cart,name="cart"),
    path("cartp/<int:id>",views.cartp,name="cartp"),
    path("cartm/<int:id>",views.cartm,name="cartm"),
    path("delcart/<int:id>",views.delcart,name="delcart"),
    path("checkout",views.checkout,name="checkout"),
    path("checkp/<int:id>",views.checkp,name="checkp"),
    path("checkm/<int:id>",views.checkm,name="checkm"),
    path("delitem/<int:id>",views.delitem,name="delitem"),
    path("profile",views.profile,name="profile"),
    path("confirm",views.confirm,name="confirm"),
    path("order",views.order,name="order")
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)