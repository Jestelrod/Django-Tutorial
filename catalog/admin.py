from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

#class BooksInline(admin.TabularInline):
#    model = BookAdmin
#    
#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
#    inlines = [BooksInline]
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)
#admin.site.register(BookInstance)
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book',"status" ,'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    
admin.site.register(Language)


