from django.contrib import admin
from school.models import Student, Course, Registration

"""
Administração personalizada para a entidade Estudante.

Atributos:
    list_display (tuple): Uma tupla que define quais campos da entidade Estudante são exibidos na lista de visualização do admin.
    list_display_links (tuple): Uma tupla que define quais campos da entidade Estudante são clicáveis na lista de visualização do admin para acessar os detalhes do registro.
    search_fields (tuple): Uma tupla que define os campos pelos quais é possível realizar pesquisas na lista de visualização do admin.
    list_per_page (int): O número de registros da entidade Estudante exibidos por página na lista de visualização do admin.
"""
class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'date_of_birth',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Student, Students)

"""
Administração personalizada para a entidade Curso.

Atributos:
    list_display (tuple): Uma tupla que define quais campos da entidade Curso são exibidos na lista de visualização do admin.
    list_display_links (tuple): Uma tupla que define quais campos da entidade Curso são clicáveis na lista de visualização do admin para acessar os detalhes do registro.
    search_fields (tuple): Uma tupla que define os campos pelos quais é possível realizar pesquisas na lista de visualização do admin.
    list_per_page (int): O número de registros da entidade Curso exibidos por página na lista de visualização do admin.
"""
class Courses(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'category', 'level',)
    list_display_links = ('id', 'code', 'name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Course, Courses)


class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period',)
    list_display_links = ('id', 'student', 'course',)
    search_fields = ('student', 'course',)
    list_per_page = 10

admin.site.register(Registration, Registrations)
