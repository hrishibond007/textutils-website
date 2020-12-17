from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def analyze(request):
    # Get the text
    txt = request.POST.get("text","default")
    removepunc = request.POST.get("removepunc","off")
    fullcaps = request.POST.get("fullcaps","off")
    newline = request.POST.get("newline","off")
    spaceremove = request.POST.get("spaceremove","off")
    charactercount = request.POST.get("charactercount","off")
    if removepunc == "on":
        punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed += char
        params = {"purpose" : "Remove Punctuations","analyzed_text" : analyzed}
        txt = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in txt:
            analyzed = analyzed + char.upper()
            
        params = {"purpose" : "changed to upper case","analyzed_text" : analyzed}
        txt = analyzed

    if newline == "on":
        analyzed = ""
        for char in txt:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

            else:
                add_space = " "
                analyzed = analyzed + add_space

        params = {"purpose" : "remove newlines","analyzed_text" : analyzed}
        txt = analyzed

    if spaceremove == "on":
        analyzed = ""
        cs =""
        for char in txt:    
            if char == " ":
                if char == " " and cs == " ":
                    continue
                analyzed = analyzed + char

            else:
                analyzed = analyzed + char

            cs = char

        # for index,char in enumerate(txt):
        #     if not(txt[index] == " " and txt[index+1] == " "):
        #         space_rm =space_rm + char



        params = {"purpose" : "remove spaces","analyzed_text" : analyzed}
        txt = analyzed

    if charactercount == "on":
        analyzed = ""
        counter = 0
        for char in txt:
            analyzed = analyzed + char
            counter = counter + 1

        params = {"purpose" : "Character counter","analyzed_text" : counter}
        
    if(removepunc != "on" and fullcaps != "on" and newline != "on" and spaceremove != "on" and charactercount != "on"):
        return render(request,"error.html")
    return render(request,"analyze.html",params)
    