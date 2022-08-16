# file-upload-flask
Flask를 활용한 AWS S3 file upload 프로젝트

## Table of Contents
- [Introduction](#Introduction)
- [Technologies Used](#Technologies-Used)
- [Setup](#Setup)
- [Usage](#Usage)
- [Acknowledgements](#Acknowledgements)

## Introduction
- Flask blueprint를 활용하여 함수분리
- pre_signed_url()함수는 boto3 s3 generate_presigned_post()사용
    - AWS api gateway를 통해서는 10mb가 넘는 file upload가 불가능한 상황에서 활용했던 방법

## Technologies Used
- Python: 3.9

## Setup
- 기본 환경 설정
    ```shell
    $ pipenv shell --python 3.9
    $ python -V
    $ pipenv install
    ```
- `config.py.default`
    - config값들 수정 후, config.py로 파일명 수정

## Usage
```shell
$ flask run --port 5001  # 5000포트는 mac os monterey에서 선점
```

## Acknowledgements
- https://gist.github.com/alexdebrie/3e8b96217f5aff01227050b17a24e380
- https://tedboy.github.io/flask/interface_api.incoming_request_data.html
