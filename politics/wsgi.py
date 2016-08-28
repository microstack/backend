from settings import set_project_paths, BACKEND_POLITICS_PORT
set_project_paths()


from api import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=BACKEND_POLITICS_PORT)
