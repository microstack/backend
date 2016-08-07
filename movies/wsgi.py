from settings import set_project_paths
set_project_paths()


from api import app
if __name__ == '__main__':
    app.run()
