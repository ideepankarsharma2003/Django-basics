from django.shortcuts import render

# Create your views here.
def add_home(request):
    return render(request, 'add.html')

def add(request):
    # num1= request.GET['num1']
    # num2= request.GET['num2']
    num1= request.POST['num1']
    num2= request.POST['num2']

    return render(request, 'result.html', {
        "num1": num1,
        "num2": num2,
        "result": f"{int(num1)+int(num2)}"
    })

    