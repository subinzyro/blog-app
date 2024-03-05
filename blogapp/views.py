from django.shortcuts import render,redirect
from blogapp.models import Blog
from blogapp.forms import BlogForm

# Create your views here.

def add(request):
    if request.method == "POST":
        form = BlogForm(request.POST) 
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = BlogForm()
    return render(request,'index.html',{'form':form})
def show(request):
    blogs = Blog.objects.all()
    return render(request,"show.html",{'blogs':blogs})
def home(request):
    blogs = Blog.objects.all()
    return render(request,"show.html",{'blogs':blogs})
def destroy(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("/show")
def edit(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,'edit.html', {'blog':blog})

def update(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST, instance = blog)
    if form.is_valid():
        form.save()

        
        return redirect("/show")
    return render(request, 'edit.html', {'blog': blog})