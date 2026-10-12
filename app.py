
from flask import Flask, render_template

app = Flask(__name__)

# Personal Information
profile = {
    "name": "Muqaddas Saleem",
    "role": "Software Engineering Student",
    "email": "muqaddussaleem@gmail.com",
    "location": "Karachi, Pakistan",
    "university": "Indus University",
    "education": "Bachelor of Science in Software Engineering (BSSE)",
    "introduction": (
        "I am a Software Engineering student at Indus University. "
        "I have basic knowledge of HTML, CSS, and C++. "
        "I enjoy learning new technologies and developing my "
        "programming and web development skills."
    ),
    "skills": ["HTML", "CSS", "C++"],
    "interests": [
        "Web Development",
        "Front-End Development",
        "Software Development",
        "UI Design"
    ],
    "linkedin": "https://www.linkedin.com/in/muqaddus-saleem-42b342443?utm_source=share_via&utm_content=profile&utm_medium=member_ios",
    "github": "https://github.com/muqaddussaleem-debug",
    "instagram": "https://www.instagram.com/muqaddas_saleem_16?xtok=OWd2YnV4MWVwaHY1&utm_source=qr"
}


projects = [
    {
        "title": "Personal Portfolio Website",
        "description": (
            "A personal website that presents my profile, education, "
            "skills, interests, projects, and contact information. "
            "The website uses Python Flask, HTML, and CSS."
        ),
        "technology": "Python, Flask, HTML, CSS"
    },
    {
        "title": "Student Marks Analyzer",
        "description": (
            "A proposed C++ program that takes student names and marks, "
            "calculates average marks, and finds the highest and "
            "lowest marks. It helps practise loops, conditions, "
            "and basic programming."
        ),
        "technology": "C++"
    }
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=profile,
        projects=projects
    )


if __name__ == "__main__":
    app.run(debug=True)
