from logging import getLogger

from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from django.db.models.expressions import Window
from django.db.models.functions import RowNumber
from django.db.models import F

from .models import Customer, Address, City, Country


logger = getLogger(__name__)


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'sakila'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(MultiDBModelAdmin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request, using=self.using, **kwargs)



# Register your models here.
# @admin.register(Customer, MultiDBModelAdmin)
class CustomerAdmin(MultiDBModelAdmin):
    # line_numbering = 0
    # ordering = ['-last_update']
    list_display = ('row_number', 'first_name', 'last_name', 'address', 'last_update')
    list_select_related = (
        'address',
    )
    search_fields = ('first_name', 'last_name', 'address__address')
    date_hierarchy = 'last_update'
    list_display_links = ('first_name', 'last_name')
    list_filter = ('last_update', 'store')
    list_per_page = 20
    # autocomplete_fields = ['address']
    # radio_fields = {"active": admin.ACTION_CHECKBOX_NAME}
    # fields = ('store', 'first_name', 'last_name','email',)
    # fields = '__all__'
    raw_id_fields = ("address",)
    readonly_fields = ('customer_id', )
    list_editable = ('address',)
    # list_select_related = ('customer', 'address')
    radio_fields = {"active": admin.VERTICAL}
    # filter_vertical = ('address',)
    # filter_horizontal = ('address',)
    # raw_id_fields = ('address',)
    # list_display = ('name', 'last_update', )
    # exclude = ('id', )
    # readonly_fields = ('address_report',)
    #
    # def address_report(self, instance):
    #     # assuming get_full_address() returns a list of strings
    #     # for each line of the address and you want to separate each
    #     # line by a linebreak
    #     return format_html_join(
    #         mark_safe('<br>'),
    #         '{}',
    #         ((line,) for line in instance.get_full_address()),
    #     ) or mark_safe("<span class='errors'>I can't determine this address.</span>")
    #
    # # short_description functions like a model field's verbose_name
    # address_report.short_description = "Address"

    def row_number(self, obj):
        logger.debug("@@@@ row_number : %s" % obj.row_number)
        return obj.row_number
    row_number.short_description = '#'



    # admin_select_related = (
    #     'address',
    # )

    # def get_queryset(self, request):
    #     return Customer.objects.annotate(row_number=Window(expression=RowNumber(), partition_by=[F('customer_id')], order_by=[F('last_update')])).order_by('row_number', 'customer_id')
    #
    # def line_number(self, obj):
    #     self.line_numbering += 1
    #     return self.line_numbering

    # def line_number(self, obj):
    #     self.line_numbering += 1
    #     return self.line_numbering
    #
    # line_number.short_description = '#'


class AddressAdmin(MultiDBModelAdmin):
    list_display = ['address', 'address2', 'district', 'city', 'postal_code', 'phone', 'last_update'] # [field.name for field in Address._meta.get_fields()]
    list_per_page = 20
    readonly_fields = ('address_id',)
    search_fields = ('address', 'city__city',)
    # exclude = ('address', 'address2', 'district', 'city_id', 'postal_code', 'phone', 'last_update', )


class CityAdmin(MultiDBModelAdmin):
    list_display = ['city', 'country', 'last_update'] # [field.name for field in Address._meta.get_fields()]
    readonly_fields = ('city_id',)
    search_fields = ('city', 'country__country',)
    list_per_page = 20


class CountryAdmin(MultiDBModelAdmin):
    list_display = ['country', 'last_update'] # [field.name for field in Address._meta.get_fields()]
    list_per_page = 20
    exclude = ('country_id',)

#
#
# admin.site.register(Customer, CustomerAdmin, MultiDBModelAdmin)


admin.site.register(Country, CountryAdmin)


admin.site.register(Address, AddressAdmin)


admin.site.register(City, CityAdmin)


admin.site.register(Customer, CustomerAdmin)

# othersite = admin.AdminSite('othersite')
# othersite.register(Customer, MultiDBModelAdmin)

# # urls.py
# from django.conf.urls import url
# from django.contrib import admin
# from myapp.admin import othersite
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^otheradmin/', othersite.urls),
# ]