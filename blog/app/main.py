from app import app, db  # import our Flask app & db obj
import models
import views

if __name__ == '__main__':
    app.run()