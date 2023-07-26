from django.http import HttpResponse
from .models import Project, Task, Product
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject, ProductForm, CreateNewProduct
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'fazt'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(title=tile)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })


def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {
        'products': products
    })

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'products/create_product.html', {
        'form': form
    })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/detail.html', {
        'product': product
    })


def products(request):
    search_query = request.GET.get('q')

    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
    else:
        products = Product.objects.all()

    return render(request, 'products/products.html', {'products': products})








def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = CreateNewProduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', id=id)
    else:
        form = CreateNewProduct(instance=product)

    return render(request, 'products/edit_product.html', {
        'form': form
    })



def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'products/delete_product.html', {'product': product})



def terms_and_conditions(request):
    return render(request, 'terms.html')



def redirect_to_login(request):
    return redirect('login')


def show_login_form(request):
    # Si el usuario ha iniciado sesión correctamente, redirige a la página de inicio
    if request.user.is_authenticated:
        return redirect('index')

    # Si el método de la solicitud es POST, es un intento de inicio de sesión
    if request.method == 'POST':
        # Realiza el inicio de sesión aquí
        # ...

        # Después de un inicio de sesión exitoso, redirige a la página de inicio
        return redirect('index')
    
    # Si no es un intento de inicio de sesión, muestra la página de inicio de sesión
    return render(request, 'login.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')  # Cambia 'index' por el nombre de tu vista principal
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después de un registro exitoso
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})