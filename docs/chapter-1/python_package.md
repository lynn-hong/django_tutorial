## python 패키지 구조

### python 패키지의 디렉토리 구조
- python 패키지는 구조가 프로젝트마다 조금씩 다르지만 일반적으로 아래와 같은 구조로 제작한다(github 기준).

``` bash
.
|-- .github/
   |-- CONTRIBUTING.md
   |-- ISSUE_TEMPLATE.md
   |-- PULL_REQUEST_TEMPLATE.md
|-- docs/
|-- resources/
|-- pysrc/
|-- (src)/
|-- CHANGELOG.md
|-- README.md
|-- LICENSE
|-- .gitignore
```

|  구성요소  |  설명  |
| ------------- | ------------- |
| .github | github repository를 관리하기 위한 템플릿들을 추가하는 곳 |
| | - CONTRIBUTING.md: 컨트리뷰션 템플릿|
| | - ISSUE_TEMPLATE.md: 이슈 템플릿|
| | - PULL_REQUEST_TEMPLATE.md: 풀리퀘스트 템플릿|
| docs  | 패키지에 대한 설명을 넣는 곳. gitbook과 연동하지 않더라도 stand alone한 문서 파일이 있다면 여기에 넣음 |
| resources  | 패키지에서 사용하는 리소스들을 넣는 곳. 용량이 큰(수십~수백mb 이상) 데이터나 리소스 파일은 형상관리를 하지 않고 Amazon S3에서 내려받는 식으로 관리함  |
| (py)src  | python과 다른 언어(주로 java, C++)의 소스가 섞여 있는 경우 python 코드임을 구분해주기 위해 `pysrc`라는 명칭 사용. 만약 python만으로 이루어진 패키지라면 그냥 `src`라고만 해도 됨 |
| (src) | 위에서 설명한 대로 python과 다른 언어들이 섞여 있는 경우 주로 java, c++ 코드를 관리하는 곳 |
| CHANGELOG.md | 패키지의 변경 사항이나 업데이트 내용을 관리하기 위한 문서. release 버전을 기준으로 CHANGELOG를 작성함 |
| README.md | 패키지의 설치, 구동 방법이나 기본적인 설명을 작성하는 문서. 한 문서 안에 다 들어가지 않을 만한 자세한 설명은 `docs` 내의 튜토리얼로 빼거나 github wiki에 별도 관리 |
| .gitignore | 형상관리에서 제외할 것들을 추가하는 문서. 특정 확장자를 모두 제외하고 싶다면 `*.pyc` 같은 형식으로, 특정 디렉토리를 통째로 제외하고 싶다면 `data`와 같은 형식으로 기재해주면 됨 |

