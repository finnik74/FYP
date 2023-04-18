from random import random

import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
# import cv2
import base64
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
    res = lime_professor.load_image(choice['n'],choice['id'])

    return JsonResponse({'pic':res[0],'segments':str(res[1]),'predict':res[2]})

def verify_sp(request):
    if request.method != 'POST':
        return JsonResponse({
            'message':'Invalid Request Type!',
            'status': 'fail'})
    choice = json.loads(request.body.decode('utf-8'))
    print(choice,'verify')
    return JsonResponse({'pic':lime_professor.verify(choice['n'],choice['prior'],choice['id'])})

True_false = {'True':True,'False':False}

def baylime_predict(request):
    if request.method != 'POST':
        return JsonResponse({
            'message':'Invalid Request Type!',
            'status': 'fail'})
    choice = json.loads(request.body.decode('utf-8'))
    print(choice)

    res = baylime_implement.customized_baylime(lam=choice['trust_level'],
                                               n_level=choice['n'],pr_c=choice['prior'],
                                               userid=choice['userid'],pattern=choice['pattern'],
                                               po = True_false[choice['po']], hd = True_false[choice['hd']],
                                               sp_sn = choice['sp_sn'], sample = int(choice['sample']),explain_num = int(choice['expain_num'])-1
                                               )
    # print(choice)
    return JsonResponse({'pic':res[0],'alpha':res[1],'lambda':res[2]})

# views.py
from django.conf import settings
import os

def download_csv(request):
    if request.method == 'POST':
        userid = json.loads(request.body.decode('utf-8'))['userid']
    file_path = os.path.join(settings.BASE_DIR, 'BayLime/data',userid, 'prior.csv')

    if os.path.exists(file_path):
        with open(file_path, 'rb') as csv_file:
            response = HttpResponse(csv_file.read(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="filename.csv"'
            return response
    else:
        return HttpResponse("Error: CSV file not found.")



import shutil


def delete_folder(request):
    if request.method == 'POST':
        userid = json.loads(request.body.decode('utf-8'))['userid']

        try:
            if os.path.exists(os.path.join('BayLime/data',userid)):
                shutil.rmtree(os.path.join('BayLime/data',userid))
            return JsonResponse({'message': 'Folder deleted successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

import cv2

def upload(request):
    if request.method == 'POST':
        # 获取上传的文件
        userid = request.POST.get('id')

        ploaded_file = request.FILES['file']


        # 从 data 中读取上传的文件数据
        content = ploaded_file.read()

        # 获取文件名
        filename = ploaded_file.name

        im = cv2.imdecode(numpy.fromstring(content, numpy.uint8), cv2.IMREAD_COLOR)


        # Display image
        if not os.path.exists(os.path.join('BayLime/data',userid)):
            os.mkdir(os.path.join('BayLime/data',userid))

        file_names = os.listdir(os.path.join('BayLime/data',userid))

        newname = 'image.'+ filename.split(".")[1]

        if os.path.exists(os.path.join('BayLime/data',userid,'img')):
            shutil.rmtree(os.path.join('BayLime/data',userid,'img'))
        os.mkdir(os.path.join('BayLime/data',userid,'img'))


        cv2.imwrite(os.path.join('BayLime/data',userid,'img',filename),im)


        with open(os.path.join('BayLime/data',userid,'img',filename), 'rb') as f:
            img_data = f.read()
            img_base64 = base64.b64encode(img_data).decode('utf-8')


        return JsonResponse({
            'code': 0,
            'msg': '上传成功',
            'img':img_base64
        })

