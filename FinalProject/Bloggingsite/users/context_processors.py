from .models import user_avatar
def avatar(request):
    if request.user.is_authenticated:
        user = request.user
        if  user_avatar.objects.filter(user = user).first()!=None:
            model_object_concerned = user_avatar.objects.get(user = user)
            avatar_svg_pass = model_object_concerned.avatar_svg
            return {'avatar_svg':avatar_svg_pass}
    return {}