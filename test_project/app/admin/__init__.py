from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app import db
from app.models.user import User

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

class UserAdmin(SecureModelView):
    column_list = ['username', 'email', 'is_admin', 'is_active']
    column_searchable_list = ['username', 'email']
    column_filters = ['is_admin', 'is_active']
    form_excluded_columns = ['password_hash']

def init_admin(app, admin):
    admin.add_view(UserAdmin(User, db.session))