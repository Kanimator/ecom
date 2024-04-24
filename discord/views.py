from django.shortcuts import render

def discord_info(request):
    context = { "title": "Discord" }
    return render(request, "discord/discord.html", context=context)
