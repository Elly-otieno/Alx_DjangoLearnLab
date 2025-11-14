from django.db import models

# Create your models here.

# Foreign key relationships

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

# Optimizing queries with prefetching
products = Product.objects.prefetch_related('category')


# OneToOneField

class User(models.Model):
    username = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField


# ManyToManyField

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')


'''
Handling Related Object Deletion
When working with related objects, it’s important to manage their deletion behavior. 
Django provides several options for handling related object deletion, such as CASCADE (deleting related objects automatically), 
PROTECT (preventing deletion if related objects exist), 
SET_NULL (setting the related field to NULL), 
and SET_DEFAULT (setting the related field to a default value).
'''


# Tests
# 1. Create a model representing a company with departments and employees, using ForeignKey relationships

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

# 2. Create a model for a product and its detailed description using a OneToOneField

class Product(models.Model):
    name = models.CharField(max_length=100)

class Description(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    bio = models.TextField()

# 3. Implement a ManyToManyField to model the relationship between students and courses

class Student(models.Model):
    name = models.CharField(max_length=100)
    adm_no = models.IntegerField(unique=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')



'''
 CASCADE (default for tightly linked models)
department = models.ForeignKey(Department, on_delete=models.CASCADE)


- If a department is deleted, all its employees are deleted too.
- Use when dependent data shouldn’t exist without the parent.


🔹 PROTECT (prevent deletion)
department = models.ForeignKey(Department, on_delete=models.PROTECT)


- Raises an error if you try to delete a department with employees.
- Use when you want to preserve data integrity.


🔹 SET_NULL (make field empty)
department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

- Employees remain, but their department field becomes NULL.
- Use when the relationship is optional.

🔹 SET_DEFAULT (fallback value)
department = models.ForeignKey(Department, on_delete=models.SET_DEFAULT, default=1)

- Employees are reassigned to a default department.
- Use when you want a safe fallback.



⚡ Optimizing Queries with select_related and prefetch_related
Let’s say you want to display a list of students and their courses, or employees and their departments.
🔹 select_related (for ForeignKey or OneToOne)

Employee.objects.select_related('department')

- Fetches employee and department in one SQL query.
- Best for single-object relationships.

🔹 prefetch_related (for ManyToMany or reverse FK)
- Runs two queries and merges them in Python.
- Best for multi-object relationships.



- 

'''

class Book(models.Model):
    pass