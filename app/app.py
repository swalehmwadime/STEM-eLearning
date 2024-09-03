from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Use your database URI here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    repo_link = db.Column(db.String(256), nullable=False)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    link = db.Column(db.String(256), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    course = db.relationship('Course', backref=db.backref('resources', lazy=True))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    all_courses = Course.query.all()
    return render_template('courses.html', courses=all_courses)

@app.route('/resources')
def resources():
    all_resources = Resource.query.all()
    return render_template('resources.html', resources=all_resources)

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/courses/python')
def python_course():
    return render_template('python_course.html')


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        repo_link = request.form['repo_link']
        
        new_course = Course(title=title, description=description, repo_link=repo_link)
        db.session.add(new_course)
        db.session.commit()
        
        flash('Course added successfully!', 'success')
        return redirect(url_for('courses'))
    
    return render_template('add_course.html')
# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables based on the models
    app.run(debug=True)





