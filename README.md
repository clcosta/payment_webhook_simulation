# Payment Webhook

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
- [ ] Log all the webhooks received from the simulator and all actions taken.
  - [x] Log in bank.
  - [ ] Associate to simulator callback url.
- [x] The register account of the course plataform need to field *token*, the user will be sending in the register plataform in a field of Form and the token needs to be equals to "uhdfaAADF123".
- [ ] The login logic.
- [ ] The user need a page to show all payments status.

### Optional TODO's

- [ ] Send email instead of printing a message.
- [ ] Enhance security measures.
- [ ] Separate DataBase class.
- [ ] Refactor code.


## Code Tree
```
payment_webhook_simulation
├── README.md
├── app.py  # WSGI FILE
├── db.db # Created automatically
└── payment_webhook
    ├── __init__.py
    ├── application
    │   ├── __init__.py
    │   ├── payment_handle.py
    │   └── webhook_schemas.py
    ├── data
    │   ├── __init__.py
    │   ├── contracts
    │   │   ├── __init__.py
    │   │   ├── models
    │   │   │   ├── __init__.py
    │   │   │   ├── auth_contract.py
    │   │   │   ├── payment_history_contract.py
    │   │   │   ├── payment_type_contract.py
    │   │   │   └── user_contract.py
    │   │   └── payment_status.py
    │   └── database
    │       ├── __init__.py
    │       ├── default_data
    │       │   ├── __init__.py
    │       │   └── payment_status.py
    │       ├── engine.py
    │       ├── main.py
    │       └── models
    │           ├── __init__.py
    │           ├── auth.py
    │           ├── payment_history.py
    │           ├── payment_type.py
    │           └── user.py
    ├── main
    │   ├── __init__.py
    │   └── server
    │       ├── __init__.py
    │       ├── main.py
    │       ├── routes
    │       │   ├── __init__.py
    │       │   ├── pages.py
    │       │   └── webhook.py
    │       └── templates
    │           ├── base.html
    │           ├── cadaster.html
    │           ├── home.html
    │           ├── login.html
    │           └── nav.html
    └── settings.py
```
