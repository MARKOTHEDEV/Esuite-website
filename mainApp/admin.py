from django.contrib import admin
from . import models
admin.site.site_header ="Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Your Admin Dashboard"





class SolutionDetailParagraphConten(admin.TabularInline):
    model = models.SolutionDetailParagraph
    extra=1

class SolutionDetailAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['heading',]})]
    inlines=[SolutionDetailParagraphConten]





admin.site.register(models.SolutionDetail,SolutionDetailAdmin)