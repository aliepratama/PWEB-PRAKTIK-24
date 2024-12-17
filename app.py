from flask_migrate import Migrate
from myproject import create_app, db
from myproject.models import Books


app = create_app()
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
