from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_login import login_required, current_user

from webapp.auth import has_role

class CustomView(BaseView):
    @expose('/')
    @login_required
    @has_role('admin')
    def index(self):
        return self.render('admin/custom.html')
    
    @expose('/second_page')
    @login_required
    @has_role('admin')
    def second_page(self):
        return self.render('admin/second_page.html')
    
class CustomModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('admin')

