from django.shortcuts import render, redirect
from main.models import Portfolio, Personalskill, Profisionalskill, Experience, Education, Post,    Categoriya,Blog


def index(request):
    ctx = {
        'port': Portfolio.objects.all().order_by('-id'),
        'personalskill': Personalskill.objects.all(),
        'profisionalskill': Profisionalskill.objects.all(),
        'experience': Experience.objects.all().order_by('-id'),
        'education': Education.objects.all().order_by('-id'),
        'categoriya': Categoriya.objects.all(),
        'post': Post.objects.all().order_by('-id'),
        'portfolio': Portfolio.objects.all().order_by('-id'),
        'blog': Blog.objects.all().order_by('-id')[0:2]

    }
    return render(request, 'main/index.html', ctx)
def portfolio(request, id):
    context = {
        'portfolio': Portfolio.objects.filter(categoriya_id=id).order_by("-id")
    }
    return render(request, 'main/index.html', context)


def post(request):
    if request.method == 'POST':
        a = Post(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'], text=request.POST['text'], title=request.POST['title'], number=request.POST['number'])
        print(a, "okkk")
        a.save()
        return redirect("index")
    return render(request, 'main/index.html')


