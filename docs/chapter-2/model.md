## 모델 생성

***아무리 바빠도 중간중간 github repository에 commit하는 것을 잊지 마세요!***

-----

### django model
django model에 대한 설명은 역시 [장고걸스 튜토리얼](https://tutorial.djangogirls.org/ko/django_models/)에 
잘 나와 있으니 여기에서는 생략하도록 할게요!
model을 정의하는 방법은 `model.py`에 직접 정의 후 자동으로 DB 테이블을 생성해주는 방식과
DB 테이블을 먼저 만든 후 거꾸로 `model.py` 파일을 생성하는 방식이 있어요.

`model.py`를 만든 후 DB로 migration 해 주는 튜토리얼은 많이 있으니
우리는 두 번쨰 방식을 연습해보기로 해요!


### 어플리케이션 생성하기
django 모델을 만들기 전에 어플리케이션 하나를 생성할거에요.
아래 명령어를 실행해서 `portfolio`라는 이름의 어플리케이션을 생성하세요.
```bash
(django) ~/django$ python manage.py startapp portfolio
```

그리고 `mysite/settings.py`에서도 `INSTALLED_APPS` 맨 끝에
'portfolio'라는 이름을 추가해주세요.
```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
)
```


### 어떻게 model을 정의해야 할까요?
이제 모델을 정의해볼 차례에요. 우리에게 필요한 클래스들은 무엇이 있을까요?
아래와 같은 경우 데이터베이스에 저장해 두고 자동 렌더링 되도록 하는 게 편해요!
- HTML 페이지 소스 내에서 반복이 발생하는 부분들
- 자주 변경되는 내용들

힌트를 얻으려면 우리가 베이스로 사용할 포트폴리오 템플릿을 보면 된답니다.
예를 들면 템플릿의 첫 페이지는 아래와 같이 'John Doe'라는 사람에 대한 묘사로서 
'3D ARTIST', 'PHOTOGRAPHER', 'WEB DESIGNER'가 반복해서 움직이고 있어요.

![HOME](img/4.gif)


또는 아래 그림처럼 자신에 대한 소개말도 코드에 직접 박아 넣는 것보다는 DB에서 관리하는 게 수정이 편하겠죠!
![ABOUT](img/2.PNG)


그리고 아래와 같이 3개의 항목이 동일한 형태로 반복되는 경우도 모델로 정의해줄 수 있어요!

![SERVICE](img/5.PNG)



### 우리가 만들 페이지의 메뉴 구성
우리가 만들 페이지는 대략 아래와 같이 구성될 거에요.
1~5 숫자 표시는 개별 모델 클래스로 정의될 내용을 뜻한답니다.
이 외에도 각자에게 필요한 항목이 있으면 추가하시면 돼요!

![메뉴 탭 구성](img/6.png)

![학력, 경력 메뉴](img/7.png)

![출판물 메뉴](img/8.png)


### model 테이블 생성하기

DB 테이블로 관리할 컨텐츠의 항목들을 MySQL에서 먼저 정의하고 이후에 `model.py`를 생성해 줄거에요.
테이블을 생성할 때는 MySQL 워크벤치에서 GUI를 이용해 편하게 하셔도 되고
아래에 올려드리는 SQL 스크립트를 실행하셔도 돼요.
각 항목들은 제가 임의로 결정한 것이니 자신의 필요에 맞게 바꾸셔도 된답니다!

```sql
CREATE TABLE `about` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `about_me` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `home_img` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `domain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title_kor` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `title_eng` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `desc_kor` text COLLATE utf8_unicode_ci,
  `desc_eng` text COLLATE utf8_unicode_ci,
  `icon` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `experience_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `experience` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start` date NOT NULL,
  `end` date DEFAULT NULL,
  `title_kor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `title_enh` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_kor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `location_eng` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `desc_kor` longtext COLLATE utf8_unicode_ci NOT NULL,
  `desc_eng` longtext COLLATE utf8_unicode_ci,
  `ex_type` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `experience_c5c777d7` (`ex_type`),
  CONSTRAINT `experience_ex_type_6bb48d317f62021a_fk_experience_type_id` FOREIGN KEY (`ex_type`) REFERENCES `experience_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title_kor` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `title_eng` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `title_img` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date_start` date NOT NULL,
  `date_end` date DEFAULT NULL,
  `desc_kor` text COLLATE utf8_unicode_ci NOT NULL,
  `desc_eng` text COLLATE utf8_unicode_ci,
  `proj_url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `publication_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_type` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `p_type` (`p_type`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `publication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_date` date NOT NULL,
  `citation_kor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `citation_eng` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc_kor` varchar(300) COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc_eng` varchar(300) COLLATE utf8_unicode_ci DEFAULT NULL,
  `p_type` int(11) NOT NULL,
  `p_url` varchar(300) COLLATE utf8_unicode_ci,
  PRIMARY KEY (`id`),
  KEY `publication_ee532d29` (`p_type`),
  CONSTRAINT `publication_p_type_4497eeb232344f3f_fk_publication_type_id` FOREIGN KEY (`p_type`) REFERENCES `publication_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
```

넘어가기 전에 각 테이블의 설명을 간단히 적어드릴게요.
아래 컨텐츠 테이블 구성은 R&D 인력을 기본으로 하여 작성된 것이므로
자신의 직종에 따라 조금 변경될 수 있어요!

| 테이블 이름 | 설명 |
| ------ | ------ |
| about | 메인 사진, about 아래에 있는 설명 문단을 관리합니다 |
| domain | 메인 페이지의 이름 아래 움직이는 텍스트, 나의 관심 분야(Job domain) 설명 등을 관리합니다 |
| experience_type | 학업, 직장, 수상 등 경력의 종류를 관리합니다 |
| experience | 학업, 직장, 수상 등 경력 사항을 관리합니다 |
| project | 프로젝트 기본 정보를 관리합니다 |
| publication_type | 학술논문, 단행본 등 출판물의 종류를 관리합니다 |
| publication | 학술논문, 단행본 등 출판물의 정보를 관리합니다 |



### MySQL 테이블을 model로 가져오기

