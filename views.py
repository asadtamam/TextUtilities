# I have created this file - Asad
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

    #return HttpResponse("Home")

def analyze(request):
    djtext = (request.GET.get('text','default'))
    removepunc =(request.GET.get('removepunc', 'default'))
    fullcaps = (request.GET.get('fullcaps', 'default'))
    newlineremover = (request.GET.get('newlineremover', 'default'))
    extraspaceremover = (request.GET.get('extraspaceremover', 'default'))

    if removepunc == "on":

 #   analyzed = djtext
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == "" and djtext[index+1] == ""):
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("Error")

#def capfirst(request):
    #return HttpResponse("capitalize first")