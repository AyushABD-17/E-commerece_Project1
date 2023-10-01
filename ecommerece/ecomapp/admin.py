from django.contrib import admin
from ecomapp.models import contact ,product,Orders,OrderUpdate

# Register your models here.

admin.site.register(contact)

admin.site.register(product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
