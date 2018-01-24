## model 생성과 데이터베이스 연결

### MySQL 데이터베이스
우리는 MySQL을 사용할 거에요.
django에서 복수의 데이터베이스를 사용하려면 복잡한 설정을 해 주어야 해요.
개인 포트폴리오 사이트는 DB에 저장할 내용이 많지 않아 SQLite를 써도 무방하지만,
나중에 다른 용도의 사이트에서 많은 데이터를 화면에 뿌려줄 때를 생각한다면
본인이 사용하기 편한 다른 DBMS를 쓰는 게 좋을 수 있어요.
 
MySQL 외에도 다른 많은 DBMS가 있으니 튜토리얼을 참고하여 각자에게 편한 것을 사용하시면 돼요. 
혹시 MySQL이 설치되어있지 않은 분들은 [이런 포스트](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-14-04)들을
참고해서 설치를 해 주세요. 이 예시는 리눅스 ubuntu 기준이랍니다.

>만약 MySQL 사용법을 잘 몰라서 설치가 필요 없는 SQLite를 사용하고 싶은 분들은 이 페이지를 스킵하고
[장고걸스 튜토리얼](https://tutorial.djangogirls.org/ko/django_start_project/)대로 따라해주세요.


### DB 생성, `pymysql` 설치
우선 MySQL 워크벤치를 이용하거나 커맨드라인에서 SQL shell에 접속해서
DB를 하나 생성해주세요. 아래 명령어는 shell에서 'MYSITE'라는 이름의 DB를 직접 생성하는 경우입니다.
생성 후 다시 shell에서 빠져나오세요.
```sql
SQL> CREATE DATABASE MYSITE;
```

다음은 python 스크립트에서 이 데이터베이스에 접속할 수 있도록 해주는 패키지를 설치할 차례에요.
우리는 `pymysql` 패키지를 사용할 예정이에요. 다음과 같은 명령어를 실행해주세요.
```bash
(django) ~/django$ pip install pymysql
```


### DB 접속정보 파일 생성
스크립트에서 자동으로 데이터베이스에 접속할 수 있도록 접속정보를 기록한 `mysql.cnf` 파일을 제작할거에요.
`mysite/mysql.cnf` 파일을 하나 만드시고 아래 내용을 넣어주세요.
{ } 부분은 실제 접속정보로 채워주셔야 해요.
```ini
[client]
database = {내 DB 이름}
host = {DB 호스트 IP. local인 경우 'localhost'라고 적음}
user = {DB 유저네임}
password = {DB 비밀번호}
default-character-set = {적절하게 utf8 등 설정}
```
>본 튜토리얼 소스코드에는 실제 `mysite/mysql.cnf` 파일은 넣어두지 않고
`mysite/mysql_sample.cnf` 파일을 넣어두었어요. 그 파일을 수정해서 사용하셔도 됩니다!


### `settings.py` 수정하기
앞서 한 번 수정했던 `mysite/settings.py`에 DB 부분을 수정해 줄 차례에요.
우선 상단 `import` 부분에 `pymysql` 패키지를 추가해주어야 해요.
`import os` 바로 밑에 아래 다섯 줄을 추가해주세요.
```python
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except:
    pass
```

그리고 쭉 내려가서 `DATABASES`라는 항목을 아래와 같이 변경해주세요.
`{mysql.cnf 파일의 절대경로}` 부분을 실제 경로로 바꾸어주세요!
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '{mysql.cnf 파일의 절대경로}',
            'sql_mode': 'traditional',
            'init_command': 'SET foreign_key_checks = 0;',
        },
    }
}
```
