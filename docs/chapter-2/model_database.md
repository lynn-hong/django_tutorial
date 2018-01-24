## model 생성과 데이터베이스 연결

### MySQL 데이터베이스와 연결하기
우리는 MySQL을 사용할 거랍니다.
django에서 복수의 데이터베이스를 사용하려면 복잡한 설정을 해 주어야 해요.
개인 포트폴리오 사이트는 DB에 저장할 내용이 많지 않아 SQLite를 써도 무방하지만,
나중에 다른 용도의 사이트에서 많은 데이터를 화면에 뿌려줄 때를 생각한다면
본인이 사용하기 편한 다른 DBMS를 쓰는 게 좋을 수 있어요.
 
MySQL 외에도 다른 많은 DBMS가 있으니 튜토리얼을 참고하여 각자에게 편한 것을 사용하시면 돼요. 
혹시 설치가 되어있지 않은 분들은 [이런 포스트](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-14-04)들을
참고해서 설치를 해 주세요. 위의 예시는 리눅스 ubuntu 기준이랍니다.

>만약 MySQL 사용법을 잘 몰라서 설치가 필요 없는 SQLite를 사용하고 싶은 분들은
[장고걸스 튜토리얼](https://tutorial.djangogirls.org/ko/django_start_project/)대로 따라해주세요.


