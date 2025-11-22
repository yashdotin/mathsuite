from django.shortcuts import render
import io, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def index(request):
    return render(request, "geometry/index.html")

def draw_shape(request):   
    shape = request.GET.get('shape')
    img_b64 = None
    info = None

    
    # CIRCLE
   
    if shape == "circle":
        try:
            r = float(request.GET.get("r"))
            area = 3.14159 * r * r
            perimeter = 2 * 3.14159 * r
            info = f"Circle — Radius: {r}, Area: {area:.4f}, Perimeter: {perimeter:.4f}"

            fig, ax = plt.subplots(figsize=(4,4))
            circle = plt.Circle((0.5, 0.5), 0.4, fill=False, linewidth=2)
            ax.add_patch(circle)
            ax.set_aspect('equal'); ax.axis('off')

            buf = io.BytesIO()
            plt.savefig(buf, format="png", dpi=120, bbox_inches="tight")
            buf.seek(0)
            img_b64 = base64.b64encode(buf.read()).decode()
            plt.close()

        except:
            info = "Invalid radius"

    # RECTANGLE

    elif shape == "rectangle":
        try:
            length = float(request.GET.get("length"))
            breadth = float(request.GET.get("breadth"))

            area = length * breadth
            perimeter = 2 * (length + breadth)
            info = f"Rectangle — Length: {length}, Breadth: {breadth}, Area: {area:.4f}, Perimeter: {perimeter:.4f}"

            fig, ax = plt.subplots(figsize=(4,4))
            rect = plt.Rectangle((0.1,0.1), 0.8, 0.8 * (breadth / length), fill=False, linewidth=2)
            ax.add_patch(rect)
            ax.set_aspect('equal'); ax.axis('off')

            buf = io.BytesIO()
            plt.savefig(buf, format="png", dpi=120, bbox_inches="tight")
            buf.seek(0)
            img_b64 = base64.b64encode(buf.read()).decode()
            plt.close()

        except:
            info = "Invalid length or breadth"
            
    # TRIANGLE

    elif shape == "triangle":
        try:
            base = float(request.GET.get("base"))
            height = float(request.GET.get("height"))

            area = 0.5 * base * height
            info = f"Triangle — Base: {base}, Height: {height}, Area: {area:.4f}"

            fig, ax = plt.subplots(figsize=(4,4))
            ax.plot([0.1, 0.9, 0.1], [0.1, 0.1, 0.1 + 0.8], linewidth=2)
            ax.set_xlim(0,1); ax.set_ylim(0,1)
            ax.set_aspect('equal'); ax.axis('off')

            buf = io.BytesIO()
            plt.savefig(buf, format="png", dpi=120, bbox_inches="tight")
            buf.seek(0)
            img_b64 = base64.b64encode(buf.read()).decode()
            plt.close()

        except:
            info = "Invalid base or height"

    else:
        info = "Unknown shape."

    return render(request, "geometry/draw.html", {"img": img_b64, "info": info})
