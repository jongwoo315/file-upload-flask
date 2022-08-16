from flask import Flask
from src.file_upload.basic.views import basic
from src.file_upload.form_data.views import form_data
from src.file_upload.pre_signed_url.views import pre_signed_url

def create_app():
    app = Flask(__name__)
    app.register_blueprint(basic)
    app.register_blueprint(form_data)
    app.register_blueprint(pre_signed_url)

    @app.before_request
    def before_request():
        return

    @app.after_request
    def after_request(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = ['POST']
        return response

    return app

if __name__ == '__main__':
    create_app()
