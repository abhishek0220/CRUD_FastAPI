from dotenv import load_dotenv
load_dotenv()


def load_application():
    from User_Item_CRUD import app
    return app


app = load_application()
