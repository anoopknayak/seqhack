from app import app
from app.api import api


# Automatically tear down SQLAlchemy.

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


# Login required decorator.
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))

    return wrap


# ----------------------------------------------------------------------------#
# Blueprints
# ----------------------------------------------------------------------------#

app.register_blueprint(api, url_prefix='/api/v1')

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
