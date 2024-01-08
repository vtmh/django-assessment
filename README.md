# Django Assessment
Make a login app using Django's Auth that consists of a custom user model named "CustomUser".

Focus on the design of the login interface as well as simplicity in backend -- Style and Design are important!

Tech:
- Django
- use SQLite for the DB
- use any CSS framework you want, we use Bootstrap 4 in production though.
- jQuery or plain JS fine
- Use Axios if utlizing ajax.

Requirements:
* do not use Django Admin, this needs to be built out customly.
- User Registration
    - No duplicate users
- Login Interface
    - Once User Accesses System Allow them to Edit thier Account as a secure page
- 2FA based on Email.
    - console out the email if needed, it doesn't have to run through SMTP if you can't find a free option, but it should be production ready if wanted.
- Forgot password functionality (you can use password hints or email based reset).
- Logout 
 
Optional:
- Docker Containerization
- SMS 2FA
- Celery (or Django view) for Async Email Check.
- Enable elevated user permissions for a user-type to view and edit all registered users. This would be essentailly a super user with more priveldges than everyone else.
