from django.shortcuts import render

def create_build(request):
    context = { "title": "Create Custom Build" }
    return render(request, "custombuild/build.html", context=context)

def get_build(request, custom_build_id):
    context = { "title": f"Build #{custom_build_id}" }
    return render(request, "custombuild/build.html", context=context)

def submit_build(request, custom_build_id):
    context = { "title": f"Submit Build #{custom_build_id}" }
    return render(request, "custombuild/build.html", context=context)

def gallery(request):
    context = { "title": "Custom Build Gallery" }
    return render(request, "custombuild/gallery.html", context=context)
