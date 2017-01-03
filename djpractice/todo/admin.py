from django.contrib import admin
from .models import Task


def register(mdl):

    class MdlAdmin(admin.ModelAdmin):
        list_display = ['__str__'] + \
                       getattr(mdl, 'admin_method', []) + \
                       [i.name for i in mdl._meta.fields]
        filter_horizontal = [i.name for i in mdl._meta.many_to_many]

    if hasattr(mdl, 'Admin'):
        if hasattr(mdl.Admin, 'inlines'):
            mdl.Admin.inlines = [get_tabular(globals()[i])
                                 for i in mdl.Admin.inlines]

        class NewMdlAdmin(mdl.Admin, MdlAdmin):
            pass

        admin.site.register(mdl, NewMdlAdmin)

    else:
        admin.site.register(mdl, MdlAdmin)


def get_tabular(mdl):
    class MdlInline(admin.TabularInline):
        model = mdl
    return MdlInline


for i in [
        Task,
]:
    register(i)
