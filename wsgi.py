from app import create_app
import app

app = create_app(celery=app.celery)

app.run()