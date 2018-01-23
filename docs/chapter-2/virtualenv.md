## python 가상환경 생성하기

***introduction에도 적어두었지만 [장고걸스 튜토리얼](https://tutorial.djangogirls.org/ko/)을 접하지 못한 분들은
이걸 먼저 따라해보시길 바랍니다.***

-----

### python 가상환경
본 튜토리얼은 리눅스 환경에서 진행한다는 가정 하에 제작되었어요.
한 머신 안에도 `python` 인터프리터가 여러 버전 동시에 존재할 수 있기 때문에
우리는 충돌을 방지하기 위해 python virtualenv(가상 환경)를 먼저 하나 만들고 그 안에 장고를 설치할거에요.

`python` 가상 환경은 장고걸스 튜토리얼의 [이 페이지](https://tutorial.djangogirls.org/ko/django_installation/)에도
설명되어 있어요. 우선 `python` 인터프리터를 이용해서 `virtualenv`라는 `python` 패키지를 설치하고,
그 패키지를 이용해서 내가 제어할 수 있는 위치에 가상 환경을 생성해요. 
이렇게 생성된 가상 환경 내에서 `django`를 설치하면 됩니다.
그리고 앞으로 django 프로젝트 관련하여 `python` 스크립트를 실행할 때는 가상 환경으로 들어가서 실행해야 해요.

리눅스 머신을 기준으로 가상 환경들은 `~/.virtualenvs` 위치의 디렉토리에 넣어주는 경우가 많아요.
(우리는 장고걸스 튜토리얼과 다른 이 위치에 가상환경을 생성합니다!)
가상 환경 디렉토리는 장고 프로젝트의 소스와 위치가 달라도 무관해요.

### `python virtualenvwrapper`
그냥 `virtualenv`를 이용해서 가상환경을 생성하면, 
해당 가상환경으로 들어가기 위해서는 매번 그 디렉토리에 가서 `activate` 명령어를 실행해 주어야 해요.
하지만 `virtualenvwrapper`를 이용해 생성하면 머신 내의 어느 위치에서든 가상환경으로 들어갈 수가 있어서 편리해요.

우선 `pip`로 `virtualenvwrapper` 패키지를 설치합니다. 
이 때 앞으로 가상환경 내에서 사용하고 싶은 버전의 `pip`를 이용해 설치해주어야 합니다.
예를 들어 `python3`를 사용하고 싶다면 해당 머신에 `python3.6`이 설치되어 있어야 하고, 
`pip`도 `python3` 버전으로 설치되어 있어야 해요.

저는 `python3.5.2`를 이용했습니다.
```bash
sudo pip install virtualenvwrapper
sudo pip install --upgrade virtualenvwrapper
mkdir ~/.virtualenvs
``` 

그리고 `virtualenvwrapper`를 사용하기 위해 `~/.bashrc` 파일에 몇 가지를 추가해주어야 해요.
아래 세 줄을 커맨드 라인에서 실행합니다.
아래 명령어 중 `{PYTHON 인터프리터 절대경로}`라고 되어 있는 부분은 각자 머신에서 실제 절대경로로 바꿔주세요.
(예를 들면 저는 `export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3`으로 사용한답니다.)
```bash
echo export WORKON_HOME=~/.virtualenvs >> ~/.bashrc
echo export VIRTUALENVWRAPPER_PYTHON={PYTHON 인터프리터 절대경로} >> ~/.bashrc
echo source /usr/local/bin/virtualenvwrapper.sh >> ~/.bashrc

source ~/.bashrc
```

여기까지 되었으면 실제 가상환경을 생성할 차례입니다. 아래 커맨드를 실행하세요.
아래 커맨드는 `django`라는 이름의 `python` 가상 환경을 `~/.virtualenvs`라는 디렉토리 안에 만들어줄거에요.
잘 생성되었는지 확인하고 싶다면 `lsvirtualenv` 명령어로 생성된 가상 환경의 목록을 확인해볼 수 있어요.
```bash
mkvirtualenv django
```

가상 환경으로 진입하기 위해서는 머신 내 어느 위치에서든 `workon`이라는 명령어를 실행하면 된답니다.
만약 `workon` 명령어가 존재하지 않는다고 나오면
위의 `~/.bashrc`에 추가해 준 경로나 `virtualenvwrapper.sh` 파일에 문제가 발생한 거에요.
반드시 `virtualenvwrapper.sh`가 실제 그 위치에 있는지, `source ~/.bashrc`는 실행되었는지 확인해주세요.

아래 명령어를 실행했을 때 가상환경으로 진입되면(좌측 괄호 안에 가상환경의 이름이 뜨면) 성공입니다!
```bash
~$ workon django
(django) ~$ 
```
`deactivate`을 실행하면 빠져나올 수 있어요.


### reference
- [Python: Install Virtualenv and Virtualenvwrapper](http://www.indjango.com/python-install-virtualenv-and-virtualenvwrapper/)
