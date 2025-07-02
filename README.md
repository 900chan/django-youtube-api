# *PROJECT* Django-Youtube-RestAPI

---
## 🖥️ 프로젝트 소개

---
Docker를 기반으로 Django와 DB:Postgre SQL를 활용하여 유튜브 REST API와 소켓 연결을 통한 실시간 채팅 기능을 구현하고 마지막으로 AWS EC2에 배포하는 Project입니다.

---
## 📑 프로젝트에 들어가기 전 개념 정리

---

### Docker란?

    > Docker란 Go언어로 작성된 리눅스 컨테이너 기반으로하는 애플리케이션을 독립적이고 격리된 환경에서 실행할 수 있게 지원하는 플랫폼입니다. 
    기존의 개발 및 운영 환경에서는 서로 다른 환경 설정으로 인해 오류가 발생하기 쉬웠지만, Docker는 컨테이너라는 일관된 환경을 제공해 이러한 문제를 해결합니다.
    Docker 컨테이너를 사용하면, 개발자는 애플리케이션과 필요한 라이브러리를 하나의 이미지로 패키징하여 어디서든 동일하게 실행할 수 있습니다.

---
![Image](https://github.com/user-attachments/assets/97721e27-d1c8-407d-9ce1-c93b5c4fbed9)
도커의 흐름 : [이미지 출처](https://velog.io/@ssunykim/Docker-%EC%A0%95%EC%9D%98%EC%9E%A5%EC%A0%90%EA%B5%AC%EC%84%B1%EC%9A%94%EC%86%8C)
### Docker의 구성요소
* Docker Client
> 도커를 사용하기 위한 커맨드 라인 도구. 사용자는 도커 클라이언트를 통해 도커 호스트와 상호 작용하고, 도커 이미지를 관리하며, 도커 컨테이너를 실행, 중지, 삭제 등을 할 수 있다.

* Docker Host
> 도커 이미지를 저장하고, 도커 컨테이너를 실행하며, 도커 클라이언트와 통신한다.

* Docker Registry
> 도커 이미지를 저장하는 중앙 저장소. 도커 클라이언트는 도커 레지스트리에서 이미지를 검색하고, 푸시, 풀 할 수 있다.

* Docker Deamon 
> 도커 호스트에서 실행되며, 도커 클라이언트와 상호 작용하고, 도커 이미지와 컨테이너를 관리한다.

* Docker Image
> 도커 컨테이너를 실행하는데 필요한 파일과 설정을 포함하는 가볍고 독립적인 실행 가능한 패키지. 도커 레지스트리에서 가져올 수 있고, 도커 파일을 사용하여 빌드할 수도 있다.

* Docker Container 
> 도커 이미지의 인스턴스입니다. 격리된 환경에서 실행되며, 운영 체제 수준의 가상화 기술을 사용하여 프로세스를 격리한다.

* Docker Hub
> 도커 커뮤니티에서 제공하는 공개적인 도커 레지스트리. 도커 허브에서는 다양한 도커 이미지를 검색하고, 공유하고, 다운로드할 수 있다.

* Docker File
> 도커 이미지를 빌드하기 위한 텍스트 파일. 도커 이미지를 구성하는 명령어와 설정이 포함되어 있다. 도커 파일을 사용하면 반복적인 이미지 빌드를 자동화할 수 있다.

---

### Docker Image 와 Container
> 도커 이미지는 파일로 어플리케이션 실행에 필요한 독립적인 환경을 포함하며, 런타임 환경을 위한 일종의 템플릿이다.
> 또한 소스코드, 라이브러리, 종속성, 도구 및 응용 프로그램을 실행하는데 필요한 기타 파일을 포함하는 불변 파일이다.

> 도커 컨테이너는 이미지를 실행한 인스턴스이다. 이미지가 설계도라면, 컨테이너는 그것을 바탕으로 만들어진 집이라 할 수 있다.
> 컨테이너는 격리된 공간에서 실행되며, 독립적인 특성을 띈다.

>> Docker Image와 Docker Container는 서로 존재하지 않으면 작동을 할 수가 없어 제일 중요한 개념이다. 도커 이미지는 프로그램을 실행하는데 필요한 파일을 포함한 파일이라 혼자 실행 할 수 없고, 컨테이너는 이미지가 갖고 있는 파일을 바탕으로 실행해야하는데 하나라도 없으면 둘 다 쓸 수 없기 때문이다. 이렇게 도커 이미지와 도커 컨테이너는 서로의 의존성이 강한 특성을 보인다. 

## 📕 Day_01 : PROJECT settings - 01

---

1. __Git Repository 생성__

    > [900chan/django-youtube-api](https://github.com/900chan/django-youtube-api) # 현재 Repository 주소 입니다.

2. __Docker 회원가입 및  설치__

    > [Docker](https://hub.docker.com/) # 회원가입 및 프로그램 설치
   
3.  __Docker 토큰 발급 및 Github 등록__

    > My account settings -> Personal acceess tokens -> Generate new token -> 입력 후 Copy Access Token


4. __django-youtube-api 파일 안에 .env 파일 생성__

    ```
    # .env
    DOCKER_ACCESS_TOKEN="생성한 토큰 입력"
    ```

5. __GitHub에 Token & USER 등록__

    >    GitHub Project Repository의 settings -> Secrets and vairables -> Actions -> New repository secret 
    ```
    # 총 두 개의 secret 생성
    1. Name : DOCKERHUB_USERS, Secret: 900chan(Docker 유저 이름)
    2. Name : DOCKERHUB_TOKEN, Secret: "생성한 토큰 입력"   
    ```
   
6. __django-youtube-api 파일 안에 requirments.txt와 requirments.dev.txt 파일 생성__

    ##### requirments.txt
   
    ```
    django>=5.0.1,<6.0.0 #Django Framework
    djangorestframework>=3.14.0,<4.0.0 # DRF 
    ```
    ##### requirments.dev.txt
    ```
    flake8>=7.0.0,<8.0.0 # flake8 = python codestyle을 체크해주는 프로그램
    ```
   
7. __Dockerfile 생성__
    ```
    #  Python 3.11이 설치된 Alpine Linux 3.19
    # Alpine Linux는 경량화된 리눅스 배포판으로, 컨테이너 환경에 적합
    FROM python:3.11-alpine3.19
    
    # LABEL 명령어는 이미지에 메타데이터를 추가합니다. 여기서는 이미지의 유지 관리자를 "seopftware"로 지정하고 있습니다.
    LABEL maintainer="seopftware"
    
    # 환경 변수 PYTHONUNBUFFERED를 1로 설정합니다. 
    # 이는 Python이 표준 입출력 버퍼링을 비활성화하게 하여, 로그가 즉시 콘솔에 출력되게 합니다. 
    # 이는 Docker 컨테이너에서 로그를 더 쉽게 볼 수 있게 합니다.
    ENV PYTHONUNBUFFERED 1
    
    # 로컬 파일 시스템의 requirements.txt 파일을 컨테이너의 /tmp/requirements.txt로 복사합니다. 
    # 이 파일은 필요한 Python 패키지들을 명시합니다.
    COPY ./requirements.txt /tmp/requirements.txt
    COPY ./requirements.dev.txt /tmp/requirements.dev.txt
    COPY ./app /app
    
    WORKDIR /app
    EXPOSE 8000
    
    ARG DEV=false
    ```
    ```
   RUN python -m venv /py && \ 
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

    ENV PATH="/py/bin:$PATH"

    USER django-user
    ```
   
8. __app 폴더 생성__



9. __.dockerignore 파일 생성__

    ```
    # Git
    .git
    .gitignore
    
    # Docker
    .docker
    
    # Python
    app/__pycache__/
    app/*/__pycache__/
    app/*/*/__pycache__/
    app/*/*/*/__pycache__/
    .env/
    .venv/
    venv/
    ```
   


10. __.gitignore 생성__
    
    * gitignore 코드 복사 후 기입 
    [Gitignore for a Django project | Djangowaves](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/)



11. __Docker 실행__

    ```
    > docker bulid .
    # docker desktop -> images에 none이 생성되면 성공
    ```


12. __docker-compose.yml 생성__

    ```
    version: "3.11" # Docker ComposeAPI
    services:
      app: # Django
        build:
          context: .
          args:
            - DEV=true
        ports:
          - "8000:8000"
        volumes:
          - ./app:/app
        command: sh -c "python manage.py runserver 0.0.0.0:8000"
    ```
    
13. __docker-compose 실행__
    > docker-compose build 
    

14. __app 폴더 안에 Django 생성__

    > docker-compose run -rm app sh -c 'django-admin startproject app .'
    
---

# 📖 Day_02: PROJECT settings - 02

---
### 🧐 Day_02 :  간단한 개념 정리

---

![Image](https://github.com/user-attachments/assets/4698636f-77eb-4efb-9a90-72fb1ac8825e)
[참조 - CI/CD 파이프라인](https://www.redhat.com/ko/topics/devops/what-is-ci-cd)

#### CI / CD 란?
> CI는 Cotinuous Integration,  지속적인 통합이라는 의미이자 
> 어플리케이션의 새로운 코드 변경 사항이 정기적으로 빌드 및 테스트되어 공유 레포지토리에 통합하는 것을 의미한다.

> CD는 Continuius Delivery & Continuous Deployment, 지속적인 서비스 제공 혹은 지속적인 배포를 의미한다.
 
>  * CI는 새로운 소스코드의 빌드, 테스트, 병합까지라면 CD는 개발자의 변경 사항이 레포지토리를 넘어, 고객의 프로덕션 환경까지 릴리즈 되는 것이다.
>  * 이와 같이 작업한 소스 코드를 빌드하고, 저장소에 전달 후 배포까지의 과정을 CI/CD라 한다.

#### Github Actions 란?

> * Github Actions는 빌드, 테스트 및 배포 파이프라인을 자동화할 수 있는 지속적 통합 및 지속적 배포(CI/CD) 플랫폼이다.
> * 레포지토리에 대한 모든 풀 요청을 빌드 및 테스트하는 workflow를 생성하거나 merge된 풀 요청을 프로덕션에 배포할 수 있다.

#### Github Actions 구성요소

> * Workflow
> > * workflow는 Github actions의 기본 구성 단위로 ".github/workflows/<workflow_name>.yml"이라는 YAML 파일에 정의된다.
> >* workflow는 하나 이상의 작업을 포함할 수 있으며 레포지토리에서 푸시 또는 풀 요청과 같은 이벤트에 의해 트리거 된다. 

> * Events
> > * events는 workflow를 시작하는 트리거이다. 
> > * 일반적인 event에는 push, pull_request및 일정이 포함된다.
> 특정 요구 사항에 따라 workflow를 트리거하는 사용자 지정 event를 만들 수 있다.

> * Jobs
> > * jobs는 workflow 내에서 실행되는 개별 작업이다.
> > * 러너라는 가상 머신에서 실행되며 하나 이상의 단계를 포함할 수 있다.
> > jobs는 종속성에 따라 병렬 또는 순차적으로 실행될 수 있다.

> * Steps
> > * steps는 작업 내 작업의 가장 작은 단위이다. 
> > * 각 steps는 셀 명령을 실행하거나 작업을 실행할 수 있다.
> > workflow 파일에 지정된 순서대로 실행되며 각 steps는 동일한 실행기 인스턴스 내에서 실행된다.

> * Actions
> > * action은 작업 흐름에서 공유 및 결합할 수 있는 재사용 가능한 코드 단위이다.
> > * Github 커뮤니티에서 개발 및 배포하거나 자체적으로 사용할 수 있도록 만들 수 있다.

> * Runners
> > * runner는 작업이 실행되는 가상 머신 또는 자체 호스팅 환경이다.
> > * Github는 다양한 운영 체제 및 하드웨어 구성을 호스팅 runner에 제공하거나 보다 전문적인 요구 사항을 위해 자체 호스팅 runner를 설정할 수 있다.


> * Environment Variables and Secrets
> > * 환경 변수는 workflow 내의 작업 및 스크립트에서 액세스할 수 있는 데이터를 저장하는데 사용한다.
> > * secret은 액세스 토큰 또는 API 키와 같은 민감한 데이터를 저장하는 데 사용되는 암호화된 환경 변수이다.

> * Artifacts and Caching
> > * artifact는 빌드 출력 또는 테스트 결과와 같이 나중에 저장하고 사용할 수 있는 workflow에서 생성된 파일이다.
> > * caching은 workflow 실행 간에 데이터를 저장하고 검색하는데 사용되므로 이전에 다운로드한 종속성 또는 빌드 출력을 재사용하여 프로세스 속도를 높일 수 있다.
---

### 💾 여러가지 DataBase 중에 왜 *PostgreSQL*인가?

* PostgreSQL?
> PostgreSQL은 사용자 정의 객체와 테이블 접근 방식을 결합하여 보다 복잡한 데이터 구조를 구축하는 엔터프라이즈급 오픈소스 객체 관계형 데이터베이스 관리 시스템이다.

* PostgreSQL의 장점

1) 뛰어난 확장성
> PostgreSQL의 특징인 수직적 확장성은 확실한 비즈니스 성장과 개발을 지원한다.

2) 사용자 정의 데이터 유형 지원
> PostgreSQL은 기본적으로 JSON, XML, H-STORE 등 다양한 데이터 유형을 지원한다. 또한 사용자가 직접 데이터 유형을 정의할 수 있어 유연성을 높일 수 있다.

3) 쉽게 통합 가능한 서드파티 도구
> PostgreSQL DBMS는 무료 및 상용 도구에 강력한 추가 지원을 제공한다. 

4) 오픈 소스 및 커뮤니티 중심 지원 
> PostgreSQL은 완전한 오픈소스이며 다양한 커뮤니티의 지원을 받아 완전한 에코시스템으로 자리를 잡았다. 소스코드가 오픈소스 라이선스를 따르기 떄문에 비즈니스 요구에 따라 자유롭게 사용, 수정, 구현할 수 있다.
---
1. __flake8 설정__

```
# app/.flake8
# pep8 코딩컨벤션을 준수하는지 체크해줌.

[flake8]
exclude =
    migrations, # 데이터베이스 스키마 변경을 자동으로 관리하기 위한 스크립트를 포함, 동적으로 생성되며 일반적으로 개발자가 직접 작성하지 않음
    __pycache__, # 컴파일된 바이트코드 저장소, 소스 코드가 아님
    manage.py, # 기본 스타일이 이미 준수
    settings.py # 코드 스타일보단 설정 값에 초점을 맞춤
```

2. __Github Actions 설정__

```
# .github/workflows/check.yml

# Github Actions CI/CD
---
name: Checks # Workflow 이름

on: [push] # git push 이벤트 활성화

jobs:
  test-lint:
    name: Test and Lint
    
    # ubuntu-20.04가 더 이상 지원하지 않아 최신 버전으로 변경
    runs-on: ubuntu-latest # 작업 환경
    
    steps: #작업 단계
      - name: Login in to Docker Hub
        uses: docker/login-action@v3 # v1은 더 이상 지원하지 않기에 최신 버전인 v3으로 변경
        with:
          username: ${{ secrets.DOCKERHUB_USER }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Check Out - pull repository code # Github에 있는 코드를 작업 환경으로 가져옴
        uses: actions/checkout@v2

      - name: Run Test-Code
      
        # docker-compose 명령어가 구버전이라 '-'제거 후 실행
        run: docker compose run --rm app sh -c 'python manage.py test'

      - name: Run Flake8 for Lint Check # pep8 style guide를 잘 준수하고 있는지 체크
        run: docker compose run --rm app sh -c 'flake8'

```

3. __Github Actions 실행__

```
> git add . 
> git commit -m "Project Settings"
> git push -u origin main
```
> 본인의 Github > actions에 들어가서 아래 사진처럼 잘 실행됐는지 체크.

<img width="698" alt="Image" src="https://github.com/user-attachments/assets/a887beda-abfe-475f-a5da-771ba823ed05" />

4. __PostgreSQL 컨테이너 설정__

```
#docker-compose.yml

# version: '3.11' # 버전을 지정하니 더 이상 지원하지 않는 커맨드라는 오류가 떠 주석처리
services:
  app:
    build:
      context: .
      args:
        - DEV=true
    ports:
      - "8000:8000"
    volumes:
      - ./app:/app
    command: >
      sh -c "python manage.py runserver 0.0.0.0:8000"
    environment:
      - DB_HOST=db
      - DB_NAME=youtube
      - DB_USER=900chan
      - DB_PASS=1234
    depends_on:
      - db

  db: # PostgreSQL Database
    image: postgres:16-alpine
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=youtube
      - POSTGRES_USER=900chan
      - POSTGRES_PASSWORD=1234

```
> ##### docker-compose 파일 기반으로 서비스를 빌드하고 실행
> > docker-compose up --build

5. __Dockerfile 업데이트__

```
# Dockerfile
...

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    > apk add --update --no-cache postgresql-client jpeg-dev && \  
    > apk add --update --no-cache --virtual .tmp-build-deps \
        > build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    > apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user
... 
```

6. __requirements.txt 업데이트__

```
django>=5.0.1,<6.0.0 # Django Framework
djangorestframework>=3.14.0,<4.0.0 # DRF (Django Rest Framework)
> psycopg2-binary>=2.9.9,<3.0.0 # Psycopg2: PostgreSQL connector
```
> 새로 추가한 내용을 기반으로 다시 한번 빌드해주기
> > docker-compose build
---
# 📄   Day_3: PROJECT settings - 03

---
1. __Django 변수 setting__

```
import os 

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

```
2. __Django custom 명령어 생성__

(1) Creating app core
> docker-compose run --rm app sh -c "python manage.py startapp core"

(2) settings에 core 추가
```
# app/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core' <- core 알려주기
]
```

(3) 사용자 정의 Django 명령어 추가

```
# core/management/commands/wait_for_db.py

# wait_for_db
# -> Django가 DB가 준비될 때까지 연결을 재시도하게 해주기 위해 필요
# -> 하나의 도커 이미지에 각 컨테이너(app,db)가 존재하기 때문
import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError

class Command(BaseCommand):
    def handle(self, *args, **options):
         self.stdout.write("Wating for DB connection ...")

         is_db_connected = None

         while not is_db_connected:
            try:
                is_db_connected  = connections['default']

            except(OperationalError, Psycopg2OperationalError):
               self.stdout.write("Retry DB connection ...")
               time.sleep(1)

         self.stdout.write(self.style.SUCCESS('Success to PostgreSQL connection!'))
```
(4) docker-compose.yml에 postgres 추가
```
 # docker-compose.yml
 
 db:
    image: postgres:16
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=youtube
      - POSTGRES_USER=seopftware
      - POSTGRES_PASSWORD=password123
```
(5) docker 설정 후 build & up
> * docker-compose run --rm app sh -c 'python manage.py makemigrations'
> * docker-compose up --build

3. __DB Test Code 작성 및 실행__

* Test Code 작성
```
# core/test.py

from django.test import SimpleTestCase
from unittest.mock import patch
from django.core.management import call_command
from psycopg2 import OperationalError as Psycopg2OPsycopgError
from django.db.utils import OperationalError

@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandsTests(SimpleTestCase):
    #wait_for_db 명령어가 DB가 준비되었을 떄 잘 동작하는지 체크하는 함수
    def test_wait_for_db_ready(self, patched_getitem):
        patched_getitem.return_value = True
        call_command('wait_for_db')
        self.assertEqual(patched_getitem.call_count, 1)



    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        patched_getitem.side_effect = [Psycopg2OPsycopgError] + \
            [OperationalError] * 5 + [True]
        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)
```
> Test Code 실행
> > docker-compose run --rm app sh -c 'python manage.py test core'

4. __Github Actions 업데이트__
```
    name : Test
    run: docker compose run --rm app sh -c 'python manage.py wait_for_db && python manage.py test'
```

5. __Youtube Models 폴더 생성__

```
# users, videos, reactions, comments, subscriptions, common
- docker-compose run --rm app sh -c 'python manage.py startapp users'
- docker-compose run --rm app sh -c 'python manage.py startapp videos'
- docker-compose run --rm app sh -c 'python manage.py startapp reactions'
- docker-compose run --rm app sh -c 'python manage.py startapp comments'
- docker-compose run --rm app sh -c 'python manage.py startapp subscriptions'
- docker-compose run --rm app sh -c 'python manage.py startapp common'
```
---
# 📑  Day_4: PROJECT settings - Models

---

1. __Custom UserModel 생성__

(1) users앱 생성
>  docker-compose run --rm app sh -c "django-admin startapp users"

(2) settings 업데이트
```
# app/settings.py

AUTH_USER_MODEL = 'users.User' # 기본 모델을 users앱의 user로 지정

DJANGO_SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
 
CUSTOM_USER_APPS = [
    'users.apps.UsersConfig'
]

INSTALLED_APPS = CUSTOM_USER_APPS + DJANGO_SYSTEM_APPS
```

(3) User Model 정의
```
# users/models.py

from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser,
        PermissionsMixin
    )
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=30)
    is_business = models.BooleanField(default=False)

    # PermissionsMixin : 유저의 권한 관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager() # 유저를 생성 및 관리
 
    def __str__(self):
        return f'email : {self.email}, nickname : {self.nickname}'
```

(4) Test Code 작성
```
# users/test.py

from django.test import TestCase
from django.contrib.auth import get_user_model

# TDD : Test Driven Development (테스트 주도 개발)

class UserTestCase(TestCase):

    # 일반 유저 생성 테스트 함수
    def test_create_user(self):
        email = 'absbrb@naver.com'
        password = 'password123'

        user = get_user_model().objects.create_user(email=email, password=password)
        # 유저가 정상적으로 만들어졌는지 체크
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)


    # 슈퍼 유저 생성 테스트 함수
    def test_create_superuser(self):
        email = 'absbrb_super@naver.com'
        password = 'password123'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        # 슈퍼유저
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
```

(5) User Model에 일반 유저, 슈퍼 유저 추가
```
# users/models.py

from django.db import models
from django.contrib.auth.models import (
        BaseUserManager
    )

class UserManager(BaseUserManager):
    # 일반 유저 생성 함수
    def create_user(self, email, password):
        if not email:
            raise ValueError('Please enter an email address')

        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    # 슈퍼 유저 생성 함수
    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
```
(6) DB migration 진행
> docker-compose run --rm app sh -c 'python manage.py makemigrations'

(7) 관리자 계정 생성
> docker-compose run -—rm app sh -c 'python manage.py createsuperuser'
> > #email, password 입력 후 생성


2. __ Models 정의__

(1) common/models.py
```
from django.db import models

# - created_at: 데이터 생성시간
# - updated_at: 데이터 업데이트 시간
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

(2) videos/models.py
```
from django.db import models
from common.models import CommonModel
from users.models import User


class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField(blank=True) # S3 Bucket -> Save File -> URL -> Save URL
    video_file = models.FileField(upload_to='storage/') # upload_to='저장경로'

    # User : Video -> 1:N
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

(3) reactions/models.py
```
from django.db import models
from common.models import CommonModel

class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction'),
    )

    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION,
)
```

(4) comments/models.py
```
from django.db import models
from common.models import CommonModel

class Comment(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
```

(5) subscriptions/models.py
```
from django.db import models
from common.models import CommonModel




class Subscription(CommonModel):
    subscriber = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribers')
    # subscriber_set -> subscriptions (내가 구독한 사람들)
    # subscribed_to_set -> subscribers (나를 구독한 사람들)
```

(6) Models 정의 후 등록 및 DB migration
```
CUSTOM_USER_APPS = [
    'users.apps.UsersConfig',
    'videos.apps.VideosConfig',
    'comments.apps.CommentsConfig',
    'subscriptions.apps.SubscriptionsConfig',
    'reactions.apps.ReactionsConfig',
    'rest_framework',
    'drf_spectacular'
]

> docker-compose run --rm app sh -c 'python manage.py makemigrations'
> docker-compose run --rm app sh -c 'python manage.py migrate'>
```

3. __DRF setting__

(1) requirements.txt에 DRF 추가
> drf-spectacular>=0.27.2,<0.28.0

(2) settings에 DRF 추가
```
# app/settings.py 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'rest_framework',
    'drf_spectacular'
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

(3) path 추가
```
# app/urls.py

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
		...,
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

(4) docker 실행해서 잘 연결되는지 확인
> docker-compose up 