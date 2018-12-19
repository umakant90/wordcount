from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    # print("welcome")
    # return HttpResponse("<h1><b>This is home pgae!!!!</h1><b>")
    return render(request,"home.html",{'name':'He there is Umakant Mekhale'})

def contact(request):
    return HttpResponse("<h1>Contact Page !!!</h1><br>We are in contact page now")

def formdata(request):
    return render(request,"form.html")

def count(request):
    data=request.GET['fulltextarea']
    # print(data)
    word_list=data.split()
    print('List data is : ',word_list)
    len_word=len(word_list)
    print('lenght = ',len_word)
    return render(request,'count.html',{'fulltext':data,'word_cnt':len_word})

def about(request):
    return render(request,'about.html')