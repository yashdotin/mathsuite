from django.shortcuts import render
from utils.safe_eval import safe_eval

def index(request):
    result = None
    error = None
    expr = ""
    if request.method == "POST":
        expr = request.POST.get("expr","")
        try:
            result = safe_eval(expr)
        except Exception as e:
            error = str(e)
    return render(request, "calculator/index.html", {"result": result, "error": error, "expr": expr})
