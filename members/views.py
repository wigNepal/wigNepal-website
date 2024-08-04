from django.shortcuts import render, redirect
from .forms import submissionForm
from django.http import HttpResponse
import os

def homepage(request):
    return render(request, 'index.html')

# Create your views here.
def regform(request):
    if request.method == 'POST':
        form = submissionForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = submissionForm()
        return render(request, 'regform.html',{'form':form})
    
def about(request):
    return render(request, 'about.html')

# def success(request):
    # # Load your separate success HTML file
    # html_file_path = os.path.join('html', 'success.html')
    # with open(os.path.join(BASE_DIR, 'members', 'static', html_file_path), 'r') as file:
    html_content = "success"

    return HttpResponse(html_content)