from flask import Blueprint, render_template, request

pages_router = Blueprint('pages', __name__)


@pages_router.route('/', methods=['GET'])
def home():
    # TODO: Auth Middleware
    return render_template('home.html')

@pages_router.route('/cadaster',methods=['GET','POST'])
def cadaster():
    # TODO: Auth Middleware
    # TODO: Cadaster Handle
    print()
    return render_template('cadaster.html')

@pages_router.route('/login',methods=['GET','POST'])
def login():
    # TODO: Auth Middleware
    # TODO: Login Handle
    print(request)
    return render_template('login.html')

@pages_router.route('/logout',methods=['GET'])
def logout():
    # TODO: Auth Middleware
    # TODO: Logout Handle
    print()
    return render_template('logout.html')