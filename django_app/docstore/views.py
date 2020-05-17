from django.shortcuts import render,redirect
from .models import app_name
# Create your views here.
from django.core.files.storage import FileSystemStorage
from .forms import BookForm

def home(request):
    appl=' ,'
    url={}
    context={'app': appl.join(list(app_name.objects.values_list('app',flat='True')))}
    if request.method == 'POST':
        uploaded_file=request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs=FileSystemStorage()
        con=fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(con)
        print(url)
    return render(request,'upload.html',context)


def book_list(request):
    books = app_name.objects.all()
    return render(request,'book_list.html',{
        'books':books
    })


def upload_book(request):
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request,'upload_book.html',{
        'form':form
    })
