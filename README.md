```
payment_webhook_simulation
├── app.py  # WSGI FILE
├── db.db # Created automatically
├── payment_webhook
│   ├── application
│   ├── data
│   │   ├── contracts
│   │   │   └── models
│   │   │       ├── payment_history_contract.py
│   │   │       ├── payment_type_contract.py
│   │   │       └── user_contract.py
│   │   ├── database
│   │   │   ├── default_data
│   │   │   │   └── payment_status.py
│   │   │   ├── engine.py
│   │   │   ├── main.py
│   │   │   └── models
│   │   │       ├── payment_history.py
│   │   │       ├── payment_type.py
│   │   │       └── user.py
│   │   └── service
│   │       ├── cryptography_service.py
│   │       └── payment_status_enum.py
│   ├── main
│   │   └── server
│   │       ├── main.py
│   │       ├── routes
│   │       │   ├── pages.py
│   │       │   └── webhook.py
│   │       └── templates
│   │           ├── base.html
│   │           ├── cadaster.html
│   │           ├── home.html
│   │           ├── login.html
│   │           └── nav.html
│   └── settings.py
```