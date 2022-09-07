
from core import Bot

if __name__ == "__main__":
    app = Bot(plugins=["default","nondefault"])
    app.run()
