from django.contrib import admin
from csvapp.models import CsvUser, CsvUserProfile

class CsvUserAdminPanel(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'contact',)

    # adding search functionality or filters
    list_filter = ('first_name', 'email')

# Register your models here.
admin.site.register(CsvUser, CsvUserAdminPanel)
admin.site.register(CsvUserProfile)

# customizing admin site titles and headers
admin.site.site_header = 'CSV' # brand name or site name
admin.site.site_title = 'CSV | Admin Panel' # title (browser tab)
admin.site.index_title = 'CSV | Admin Panel' # Body title
