## django 프로젝트 시작하기

### 가상환경에서 django 설치하기
가상환경으로 제대로 진입했으면 `pip`를 우선 업데이트 해 주고 `django`를 설치할거에요.
아래 명령어를 실행합니다.
```bash
(django) ~$ pip install --upgrade pip
(django) ~$ pip install django==1.8.0
```

`pip`로 설치를 해줄 때 `==` 뒤에 버전을 붙이면 특정 버전으로 설치돼요.
`1.8.0`은 최신 버전이 아니지만 `1.9.0` 이후 버전에서 url을 쓰는 방식이 달라져 약간 버그가 있어서
본 튜토리얼에서는 `1.8.0`을 기준으로 합니다.
더 최신 버전으로 하시면 일부 문법이 달라지게 됩니다.

제대로 설치되었는지 확인하고 싶다면 '가상환경 내에서' `python`을 실행해 인터프리터 쉘로 들어가서
`import django`를 쳐보세요. django가 정상적으로 import 된다면 성공입니다!

### django 프로젝트 생성하기
이제 나의 django 프로젝트를 생성할거에요. 이후의 모든 과정은 가상환경 내에서 이루어집니다.
우선 본 튜토리얼 외에도 여러 django 프로젝트를 생성할 루트 디렉토리를 하나 만들어주세요.
여기서는 `django`라는 이름의 디렉토리를 만들고 그 안으로 이동했어요.
```bash
(django) ~$ mkdir django
(django) ~$ cd django
```

아래 명령어를 실행해주세요. `mysite`라는 이름의 프로젝트가 생성됩니다.

```bash
(django) ~/django$ django-admin startproject mysite .
```

### 기본 세팅 바꿔주기
웹서버를 구동시키기 전에 몇 가지 설정을 바꿔주려고 해요. 
우리가 모두 장고걸스 튜토리얼을 기본적으로 수료했다는 가정 하에,
여기서는 디렉토리의 구조나 각 컴포넌트들의 설명은 하지 않을게요.
상세한 설명을 보고 싶은 분들은 [여기](https://tutorial.djangogirls.org/ko/django_start_project/)를
참고해주세요!

바꿔주어야 할 스크립트는 `mysite/settings.py`에요

### MySQL 데이터베이스와 연결하기

