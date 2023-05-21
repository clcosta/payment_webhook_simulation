import os

from payment_webhook import app

if __name__ == '__main__':
    app.run(
        host=os.getenv('HOST', default='0.0.0.0'),
        port=int(os.getenv('PORT', default=8000)),
        debug=bool(os.getenv('DEBUG', default=False)),
    )
