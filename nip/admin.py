from django.contrib import admin
from .models import (WorkSection, PersonnelTypes, Personnel, ShiftTypes, Shifts, ShiftAssignmentPivoted_by_id)


# from .models import ShiftAssignmentPivoted_by_id

class WorkSectionAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Title')
    list_filter = ('Code', 'Title')


class PersonnelTypesAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Title')
    list_filter = ('Code', 'Title')


class ShiftTypesAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Title')
    list_filter = ('Code', 'Title')


class ShiftAssignmentPivoted_by_id_Admin(admin.ModelAdmin):
    list_display = ('FullName', 'PersonnelTypes_id', 'D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10'
                                        , 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20'
                                        , 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30')
    list_filter = ("WorkSection", "YearWorkingPeriod", "Cost", "Rank",)


# exclude = ['owner']  # to hide owner field

# def save_model(self, request, obj, form, change):
#     if getattr(obj, 'owner', None) is None:
#         obj.owner = request.user
#     obj.save()
# get_queryset function to villa list display by user
# def get_queryset(self, request):
#     qs = super(PicturesAdmin, self).get_queryset(request)
#     if request.user.is_superuser:
#         return qs
#     return qs.filter(owner=request.user)

admin.site.register(WorkSection, WorkSectionAdmin)
admin.site.register(PersonnelTypes, PersonnelTypesAdmin)
admin.site.register(ShiftTypes, ShiftTypesAdmin)
admin.site.register(ShiftAssignmentPivoted_by_id, ShiftAssignmentPivoted_by_id_Admin)
