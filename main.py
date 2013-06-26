import os
import jinja2
import webapp2
import ufuncts

# error strings constants
C_USERNAME_ERROR = "That's not a valid username."
C_PASSWORD_ERROR = "That wasn't a valid password."
C_VERIFY_ERROR = "Your passwords didn't match."
C_EMAIL_ERROR = "That's not a valid email."

jinja_environment  = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


class MainPage(webapp2.RequestHandler):
       
    def write_form(self, rot_str = ""):
            template_values = {
                'rot_str': rot_str
            }
            template = jinja_environment.get_template('birthday.html')
            self.response.out.write(template.render(template_values))

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get('text')
        text = ufuncts.rot13(user_text)
        self.write_form(text)

class SignupPage(webapp2.RequestHandler):
    def write_form(self,
                   username = '',
                   password = '',
                   verify = '',
                   email = '',
                   username_error = '',
                   password_error = '',
                   verify_error = '',
                   email_error = ''):
        template_values = {'username': username,
                           'password': password,
                           'verify': verify,
                           'email': email,
                           'username_error': username_error,
                           'password_error': password_error,
                           'verify_error': verify_error,
                           'email_error': email_error}
        template = jinja_environment.get_template('signup.html')
        self.response.out.write(template.render(template_values))


    def get(self):
        self.write_form()
            
    def post(self):
        # set errors to ''
        username_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''
        
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        if not ufuncts.valid_username(username):
            username_error = C_USERNAME_ERROR
        if not ufuncts.valid_password(password):
            password_error = C_PASSWORD_ERROR
        if (not password_error and not password == verify):
            verify_error = C_VERIFY_ERROR
        if email and not ufuncts.valid_email(email):
            email_error = C_EMAIL_ERROR

        if (username_error or password_error or verify_error or email_error):            
            self.write_form(username,
                            '',
                            '',
                            email,
                            username_error,
                            password_error,
                            verify_error,
                            email_error)
        else:
            self.redirect('/welcome?username=' + username)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        template_values = {'username': username}
        template = jinja_environment.get_template('welcome.html')
        self.response.out.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', SignupPage),
    ('/welcome', WelcomePage),
    ], debug=True)
