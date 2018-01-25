## 모델 생성과 migrate

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
| about | **메인 사진**, about 아래에 있는 **설명 문단**을 관리합니다 |
| domain | 메인 페이지의 이름 아래 움직이는 텍스트, 나의 **관심 분야(Job domain) 설명** 등을 관리합니다 |
| experience_type | 학업, 직장, 수상 등 **경력의 종류**를 관리합니다 |
| experience | 학업, 직장, 수상 등 **경력 사항**을 관리합니다 |
| project | **프로젝트 기본 정보**를 관리합니다 |
| publication_type | 학술논문, 단행본 등 출판물의 **종류**를 관리합니다 |
| publication | 학술논문, 단행본 등 출판물의 **정보**를 관리합니다 |



### MySQL 테이블을 model로 가져오기
이제 생성한 MySQL 테이블 정보를 거꾸로 django `model.py`로 가져올 차례에요.
아래 명령어를 실행해주세요.
```bash
(django) ~/django$ python manage.py inspectdb > portfolio/models.py
(django) ~/django$ ls -al
```

`ls -al`의 결과로 해당 위치의 파일 목록이 보일 텐데 그 중 `models.py`라는 파일이 생성된 것을 확인할 수 있을 거에요!
remote 서버와 local을 동기화시켜 진행하고 계신 분들은 이 파일을 꼭 local 환경으로 내려받기 해 주세요.
파일을 한번 열어 보면 대략 아래와 같은 모습일거에요. 'about' 테이블을 예로 하나 확인해볼까요?
```python
class About(models.Model):
    about_me = models.CharField(max_length=255)
    home_img = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'about'
```

우리가 MySQL에서 먼저 정의했던 테이블 구조대로 django model 클래스가 자동 생성되었어요!
혹시 여기서 약간 손보고 싶은 부분이 있다면 수정해주세요.


### model migration
`model.py`가 변경되었으니 migration을 해 주어야 해요.
아래 명령어를 실행해서 migration 파일을 생성해주세요.
```bash
(django) ~/django$ python manage.py makemigrations
Migrations for 'portfolio':
  0001_initial.py:
    - Create model AuthGroup
    - Create model AuthGroupPermissions
    - Create model AuthPermission
    - Create model AuthUser
    - Create model AuthUserGroups
    - Create model AuthUserUserPermissions
    - Create model DjangoAdminLog
    - Create model DjangoContentType
    - Create model DjangoMigrations
    - Create model DjangoSession
    - Create model About
    - Create model Domain
    - Create model Experience
    - Create model ExperienceType
    - Create model Project
    - Create model Publication
    - Create model PublicationType
    - Add field p_type to publication
    - Add field ex_type to experience
```

형식적으로 아래 명령어도 실행해주세요.
`model.py` 파일을 이용해서 데이터베이스에 테이블을 생성하거나 변경해주는 건데
우리는 DB 테이블을 먼저 생성해 두었기 때문에 `No migrations to apply.`라는 문구가 뜰 거에요!
```bash
(django) ~/django$ python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, auth, contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  No migrations to apply.
```


### Reference
- [Integrating Django with a legacy database](https://docs.djangoproject.com/en/2.0/howto/legacy-databases/)
