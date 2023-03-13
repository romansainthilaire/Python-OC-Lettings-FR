from django.shortcuts import render

from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def list(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "profiles/list.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis, pellentesque
# dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo
# tristique lacus, it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus
# et netus et males
def detail(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/detail.html", context)
