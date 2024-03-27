from django.contrib import admin
from .models import Catagory,Product,Customer,Orderitem,ShippingAddress,Review,Order
# Register your models here.

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('id','catagory_name','created','update','published')
    list_display_links = ('catagory_name',)
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('catagory_name',)

admin.site.register(Catagory,CatagoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','created','update','published')
    list_display_links = ('product_name',)
    list_editable = ('published',)
    list_filter = ('product_name',)
    search_fields = ('product_name',)


admin.site.register(Product,ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','ful_name','countri','created','update','published')
    list_display_links = ('ful_name',)
    list_editable = ('published',)
    list_filter = ('countri',)
    search_fields = ('countri','ful_name')



admin.site.register(Customer,CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','order_name','created','update','published')
    list_display_links = ('order_name',)
    list_filter = ('published',)
    search_fields = ('order_name',)

admin.site.register(Order,OrderAdmin)


class OrderitemAdmin(admin.ModelAdmin):
    list_display = ('id','recipient_name','where_to_go','created','update','published')
    list_display_links = ('recipient_name',)
    list_filter = ('where_to_go',)
    search_fields = ('recipient_name','where_to_go')



admin.site.register(Orderitem,OrderitemAdmin)


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('id','contri','citi','created','update','published')
    list_display_links = ('contri',)
    list_filter = ('citi',)
    search_fields = ('contri','contri')

admin.site.register(ShippingAddress,ShippingAddressAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created','update','published')
    list_display_links = ('title',)
    list_filter = ('published',)
    search_fields = ('title','content')


admin.site.register(Review,ReviewAdmin)