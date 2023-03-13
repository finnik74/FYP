from random import random
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
# import cv2
import numpy
from userInfo.auth import auth_user, auth_register
from django.http import JsonResponse
import json
from BayLime import baylime_implement
from BayLime import lime_demo
from BayLime import lime_professor

def auth(request):
    if request.method != 'POST':
        return JsonResponse({
            'message': 'Invalid Request Type!',
            'status': 'fail'})
    print(request.body.decode('utf-8'))
    user_info = json.loads(request.body.decode('utf-8'))

    # name/password 的有效性验证在前端完成
    auth_results = auth_user(user_info)
    print(f'user_info: {user_info} auth_results: {auth_results}')
    return JsonResponse(auth_results)

def user_register(request):
    if request.method != 'POST':
        return JsonResponse({
            'message':'Invalid Request Type!',
            'status': 'fail'})
    print(request.body.decode('utf-8'))
    user_info = json.loads(request.body.decode('utf-8'))
    auth_results = auth_register(user_info)
    print(f'user_info: {user_info} auth_results: {auth_results}')
    return JsonResponse(auth_results)

def bay(request):
    if request.method != 'POST':
        return JsonResponse({
            'message':'Invalid Request Type!',
            'status': 'fail'})
    num = {'small':5,'normal':10,'big':15}
    positive_only = {'True':True,'False':False}
    hide_rest = {'True':False,'False':True}
    choice = json.loads(request.body.decode('utf-8'))
    fig = baylime_implement.bay_main(po=positive_only[choice['po']],num=num[choice['num']],hd=hide_rest[choice['hr']],pattern=choice['pattern'])
    print('User choice',choice)
    return JsonResponse({'fig':fig,'pattern':choice['pattern']})

def limeDemo(request):
    if request.method != 'POST':
        return JsonResponse({
            'message':'Invalid Request Type!',
            'status': 'fail'})
    return JsonResponse({'pic':lime_demo.randomchange()})

def load_sp(request):
    if request.method != 'POST':
        return JsonResponse({
            'message':'Invalid Request Type!',
            'status': 'fail'})
    choice = json.loads(request.body.decode('utf-8'))
    print(choice)
    return JsonResponse({'pic':lime_professor.load_image(choice['n'])})

def verify_sp(request):
    if request.method != 'POST':
        return JsonResponse({
            'message':'Invalid Request Type!',
            'status': 'fail'})
    choice = json.loads(request.body.decode('utf-8'))
    print(choice,'verify')
    return JsonResponse({'pic':lime_professor.verify(choice['n'],choice['prior'])})


def baylime_predict(request):
    if request.method != 'POST':
        return JsonResponse({
            'message':'Invalid Request Type!',
            'status': 'fail'})
    choice = json.loads(request.body.decode('utf-8'))
    fig = baylime_implement.customized_baylime(lam=choice['trust_level'],n_level=choice['n'],pr_c=choice['prior'])

    return JsonResponse({'pic':fig})


# def upload(request):
#     if request.method == 'POST':
#         # 获取上传的文件
#         uploaded_file = request.FILES['file']
#         # 读取文件内容
#         content = uploaded_file.read()
#
#         # 获取文件名
#         filename = uploaded_file.name
#         print(filename)
#         # Convert string to an image
#         im = cv2.imdecode(numpy.fromstring(content, numpy.uint8), cv2.IMREAD_COLOR)
#         # Display image
#         add = 'userPicture/'+str(random())[:10]+'name:'+filename
#         # cv2.imwrite(add, im)
#         # cv2.waitKey(0)
#         # cv2.destroyAllWindows()
#
#         # fig = baylime_implement.bay_main(po=True,hd=False,num=15,pattern='non_bay')
#         return JsonResponse({'success':'asdad'})

