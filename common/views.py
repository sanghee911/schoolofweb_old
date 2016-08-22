# -*- coding: utf-8 -*-
from django.shortcuts import render


def home(request):
    context = {
        'page': 'home',
        'meta_title': 'Home',
        'meta_description': '웹 개발, 서버 관리, 하드웨어 등의 무료 인터넷 강좌를 제공하는 블로그 사이트 입니다.',
        'meta_keywords': '무료 인터넷 강좌, 파이썬, 장고, 리눅스, Python, Django, Linux',
        'meta_author': '이상희, Sanghee Lee',
        'meta_url': request.build_absolute_uri,
    }
    return render(request, 'common/home.html', context)
