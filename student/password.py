from django.http import JsonResponse
from django.db import connection
from django.contrib.auth.models import User
from database.models import S
import json
def verify(request):
    request.params = json.loads(request.body)
    oldpassword = request.params['oldpassword']
    student = S.objects.get(xh=request.session['member_id'])
    user = User.objects.get(username=student.xh)
    if user.check_password(oldpassword):
        return JsonResponse({'ret': 0, 'msg': '身份验证成功'})
    else:
        return JsonResponse({'ret': 1, 'msg': '身份验证失败'})

def alterpassword(request):
    request.params = json.loads(request.body)
    newpassword = request.params['newpassword']
    newpwdagain = request.params['newpwdagain']
    student = S.objects.get(xh=request.session['member_id'])
    user = User.objects.get(username=student.xh)
    if  newpassword==newpwdagain:
        user.set_password(newpassword)
        user.save()
        return JsonResponse({'ret': 0, 'msg': '密码修改成功'})
    else:
        return JsonResponse({'ret':1,'msg':'两次密码不一致'})
