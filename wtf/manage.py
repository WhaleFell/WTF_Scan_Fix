from app import create_app, db, models

app = create_app()


def make_shell_context():
    return dict(app=app, db=db)


def run():
    """run the app"""
    app.run(port=5000, host="0.0.0.0")


if __name__ == "__main__":
    run()
