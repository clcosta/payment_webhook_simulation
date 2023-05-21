# Payment Webhook

## Prerequisites

- Python >= 3.10

## Install and Run

Clone the repository
```
https://github.com/clcosta/payment_webhook_simulation.git
```

### Start Script

```shell

# Windows
./scripts/start.ps1
# OR
./scripts/start.bat
# Linux
./scripts/start.sh
```

### Python

```
pip install -r requirements.txt

python main.py
```


## Required TODO's

- [x] Access simulator webhook and get the object of payment.
- [x] Handle with Payment object status:
    - [x] If payment is approved:
        - Aprove user access to course plataform.
        - Send a message to the user.
    - [x] If payment is refused:
        - Send a message to the user.
    - [x] If payment is refunded:
        - Revoke user access to course plataform.
        - Send a message to the user.
- [x] Log all the webhooks received from the simulator and all actions taken.
  - [x] Log in bank.
  - [x] Associate to simulator callback url.
- [x] The register account of the course plataform need to field *token*, the user will be sending in the register plataform in a field of Form and the token needs to be equals to "uhdfaAADF123".
- [x] The login logic.
- [x] The user need a page to show all payments status.

### Optional TODO's

- [ ] Send email instead of printing a message.
- [ ] Enhance security measures.
- [x] Separate DataBase class.
- [ ] Refactor code.


## Code Tree
```
payment_webhook_simulation
├── README.md
├── app.py
├── db.db
├── payment_webhook
│   ├── __init__.py
│   ├── application
│   │   ├── __init__.py
│   │   ├── controllers
│   │   │   ├── __init__.py
│   │   │   ├── base_controller.py
│   │   │   ├── home_controller.py
│   │   │   ├── user_controller.py
│   │   │   └── wb_callback_controller.py
│   │   ├── payment_handle.py
│   │   └── webhook_schemas.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── contracts
│   │   │   ├── __init__.py
│   │   │   ├── action_taken.py
│   │   │   ├── payment_status.py
│   │   │   └── payment_type_schema.py
│   │   └── database
│   │       ├── __init__.py
│   │       ├── context.py
│   │       ├── default_data
│   │       │   ├── __init__.py
│   │       │   └── payment_status.py
│   │       ├── engine.py
│   │       ├── main.py
│   │       ├── models
│   │       │   ├── __init__.py
│   │       │   ├── auth.py
│   │       │   ├── base.py
│   │       │   ├── payment_history.py
│   │       │   ├── payment_type.py
│   │       │   └── user.py
│   │       └── utils.py
│   ├── infra
│   │   ├── __init__.py
│   │   └── settings.py
│   └── main
│       ├── __init__.py
│       └── server
│           ├── __init__.py
│           ├── routes
│           │   ├── __init__.py
│           │   ├── pages.py
│           │   └── webhook.py
│           └── templates
│               ├── base.html
│               ├── home.html
│               ├── login.html
│               ├── message.html
│               ├── nav.html
│               └── register.html
└── requirements.txt
```
