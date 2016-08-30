from settings import set_project_paths, BACKEND_WEATHER_PORT
set_project_paths()


from api import app
from tasks import periodic_update_publish_weather


periodic_update_publish_weather.delay()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=BACKEND_WEATHER_PORT)
