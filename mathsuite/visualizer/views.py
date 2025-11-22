from django.shortcuts import render
import io, base64
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from utils.safe_eval import safe_eval

def index(request):
    return render(request, "visualizer/index.html")

def plot_function(request):
    expr = request.GET.get('expr','x')
    img_b64 = None
    error = None
    try:
        xs = np.linspace(-10,10,400)
        ys = []
        for x in xs:
            
            val = safe_eval(expr.replace('x', f'({x})'))
            ys.append(val)
        fig, ax = plt.subplots(figsize=(6,4))
        ax.plot(xs, ys)
        ax.axhline(0, color='k', linewidth=0.5)
        ax.axvline(0, color='k', linewidth=0.5)
        ax.set_title(f"y = {expr}")
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=100)
        buf.seek(0)
        img_b64 = base64.b64encode(buf.read()).decode()
        plt.close(fig)
    except Exception as e:
        error = str(e)
    return render(request, "visualizer/plot.html", {"img": img_b64, "error": error, "expr": expr})
