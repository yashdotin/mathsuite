from django.shortcuts import render

UNIT_MAP_LENGTH = {  
    'm': 1.0,
    'km': 1000.0,
    'cm': 0.01,
    'mm': 0.001,
    'mi': 1609.344,
    'ft': 0.3048,
}

def index(request):
    value = None
    out = None
    from_u = 'm'
    to_u = 'cm'
    if request.method == "POST":
        try:
            value = float(request.POST.get("value"))
            from_u = request.POST.get("from_u")
            to_u = request.POST.get("to_u")
            base = value * UNIT_MAP_LENGTH[from_u]
            out = base / UNIT_MAP_LENGTH[to_u]
        except Exception as e:
            out = f"Error: {e}"
    return render(request, "converter/index.html", {"out": out, "value": value, "from_u": from_u, "to_u": to_u, "unit_map": UNIT_MAP_LENGTH})
