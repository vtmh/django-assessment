# Django Custom User With allauth
 Made a login app using Django's Auth that consists of a custom user model named "CustomUser".

### Tech Stack: 
Python, Django, SQLite, CSS, Bootstrap 5, and Docker. 

### Implementation:
- Docker Containerization of app. Built my own Dockerfile and used docker-compose to `up` the system.
- User Registration
   - No duplicate users
- Login Interface
   - Once Users Access the System Allow them to Edit their Account as a secure page.
- Create a custom template tag that shows the last time a user logged in, using the local timezone when rendered. 
- 2FA based on Email for both signup and login. 
- Forgot password functionality (you can use password hints or email-based reset).
- Logout  
- Give the user an option to change the color scheme of the site permanently by choice.
- Allow the user to change the timezone by selecting for the custom template tag

## Usage

First clone this repo
```bash
git clone https://github.com/ns2772/Django-Assessment.git 
```

Create a `.env` file
```bash
touch mysite/.env
```

Place your credentials in `.env` file
```bash
DEBUG=True
SECRET_KEY=your-secret-key
```

Create A virtualenv
```bash
virtualenv env
```

Build the Docker Container
```bash
docker-compose build
```

Run the Docker Container:
```bash
docker-compose up
```

Admin login credentials:
```bash
admin@example.com
```
```bash
User@123
```

