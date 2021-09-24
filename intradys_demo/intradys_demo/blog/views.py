from django.http.response import JsonResponse
from django.shortcuts import render
from .models import CustomSettings, Color

# Create your views here.

def index(request):
    context = {}
    context["link"] = "index"
    context["all_colors"] = Color.objects.all()
    # used to generate all buttons
    # this should only exist within a form system to prevent any csrf and not be used in a production env 
    return render(request, "blog/index.html", context=context)

def get_color_setting(request):
    cust_set = CustomSettings.objects.get(name="color")
    color_obj = Color.objects.get(name = cust_set.value)
    data = {
        "chosen_color" : color_obj.hex_value,
    }
    return JsonResponse(data)

def set_color_setting(request):
    # request and database queries are not sanitized
    # this ajax call is for demonstration only and should not be used in a production env 
    try:
        chosen_color = request.GET.get('chosen_color', None)
        if chosen_color:
            color_obj = Color.objects.get(name=chosen_color)
            print(color_obj)
            CustomSettings.objects.update_or_create(name="color", defaults={"value": color_obj})
            response = "OK"
        else:
            response = "color not registered or provided in query"
    except Exception as e:
        response = f"oups: {e}"
    finally:
        data = {
            "state": response
        }
        return JsonResponse(data)
    