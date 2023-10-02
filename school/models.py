from django.db import models

"""
Representa um estudante com informações básicas.

Atributos:
    name (str): O nome do estudante.
    rg (str): O RG (Registro Geral) do estudante.
    cpf (str): O CPF (Cadastro de Pessoas Físicas) do estudante.
    date_of_birth (date): A data de nascimento do estudante.

Métodos:
    __str__(): Retorna uma representação em string do estudante, que é o seu nome.
"""
class Student(models.Model):
    name = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=14)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
    
"""
Representa um curso com informações detalhadas.

Atributos:
    code (str): O código identificador do curso.
    name (str): O nome do curso.
    category (str): A categoria ou área do curso.
    description (str): Uma descrição breve do curso.
    level (str): O nível do curso, que pode ser 'Basic' (Básico), 'Intermediate' (Intermediário) ou 'Advanced' (Avançado).

Métodos:
    __str__(): Retorna uma representação em string do curso, que é o seu nome.
"""
class Course(models.Model):
    LEVEL = (
        ("BC", "Basic"),
        ("IN", "Intermediary"),
        ("AV", "Advanced"),
    )
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    level = models.CharField(max_length=2, choices=LEVEL, blank=False, null=False, default='BC')

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    PERIOD = (
        ("MN", "Morning"),
        ("AN", "Afternoon"),
        ("NG", "Night"),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=2, choices=PERIOD, blank=False, null=False, default='NG')