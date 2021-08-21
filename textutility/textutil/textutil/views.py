# i have created this file-
from django.http import HttpResponse
from django.shortcuts import render

def error(request):
    return render(request,'error.html')

def index(request):
    # x={'name':'Sanju Roy','place':'Mars'}
    return render(request,'index.html')
    # return HttpResponse('''<h1>HOME</h1> <a href="/removepunc">removepunc</a> \t<a href="/capfirst">capfirst</a>\t <a href="/newlineremove">newlineremove</a> \t<a href="/spaceremove">spaceremove</a>\t <a href="/charcount">charcount</a>''')

def about(request):
    return render(request,'about.html')

def analyze(request):
    # print(request.GET.get('text','default'))
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('analyze', 'off')
    uppercase = request.POST.get('uppercase','off')
    RemoveextraSpace= request.POST.get('remove_space', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount= request.POST.get('charcount','off')

    if removepunc=="on":
        punctuations=''',./;~!@#$%^&*()_'"-<>?:'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove punctuation','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if (uppercase=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Capital All Text', 'analyzed_text': analyzed}
        djtext=analyzed

    if (RemoveextraSpace=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed

    if charcount=='on':
        count=len(djtext)
        params = {'purpose': 'The Number Of Character', 'analyzed_text': count}
    if(removepunc!="on" and uppercase!="on" and RemoveextraSpace!="on" and newlineremover!="on" and charcount!="on"):
        return render(request,'error.html')

    return render(request, 'analyze.html', params)
