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

## 📕 Day_01 : PROJECT settings

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



11. Docker 실행

    ```
    > docker bulid .
    # docker desktop -> images에 none이 생성되면 성공
    ```


12. docker-compose.yml 생성

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
    
13. docker-compose 실행
    > docker-compose build 
    

14. app 폴더 안에 Django 생성

    > docker-compose run -rm app sh -c 'django-admin startproject app .'