from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
    # return HttpResponse("HLEL")
def remove(request):
    text=request.GET.get('text','defualt')
    punc=request.GET.get('sub','off')
    answer=""
    allpunc='''!()-[]{};:'",<>./?@#$%^&*_~'''
    for i in text:
        if i not in allpunc:
            answer+=i
    parameter={'initial':text, 'puncbutton':punc, 'aftertext':answer}
    return render(request,'answer.html',parameter)
    

