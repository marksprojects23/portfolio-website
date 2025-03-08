# Overview

As a software engineer, I am committed to continuous learning and skill enhancement. By engaging in diverse projects that incorporate unfamiliar languages and technologies, I aim to strengthen my coding foundations and produce tangible outcomes that demonstrate my growth and adaptability.

This web application is a website, generated through the Django framework, that is designed to show off all the various projects I've worked on while also introducing myself from a developer standpoint. The projects page has a search bar for anyone wanting to take a deep dive into my work, and each project is kept in a SQLite database. To start a test server, enter the first `portfolio` folder and run `python manage.py runserver` with the latest version of Python. After that, visit the `http://127.0.0.1:8000` website to see the first page of the web application.

{Describe your purpose for writing this software.}
I've created this web application to upload to my domain at `markcuizon.com` while also expanding my repertoire by learning yet another web application framework in Django. This also serves as a project to show off my other projects, a way to tie up all that I've done so far.

[Software Demo Video](https://youtu.be/0UdHbnRJXP4)

# Web Pages

The Home/Index page is a simple introduction page to myself as a developer. There are two buttons on the page: One directs the user to my Projects page and the other directly links to my GitHub. With Django views, the HTML for these pages are loaded in.

My Projects page's header title is clickable to bring the user back to the Home/Index page. The projects I've worked on are listed below with the latest project submitted being at the top. Each alternating project has the image (and, soon, the titles and descriptions too) aligned on the right. The search bar can restrict the project list to only those containing the query in the title and description but also the `technologies`, which are hidden tags where I put the languages and technologies I've used to creathe the project. This page dynamically pulls and queries from a SQLite database built within Django.

# Development Environment

- **Visual Studio Code with extensions**: Main code editor, allowing for efficient coding, error-checking, and project management.
- **ChatGPT**: Generative AI that is vastly helpful as a coding assistant and advisor.
- **Internet**: Source for documentations and learning.

### Language and Libraries

- **Python 3.12.3**: The main language used to code this project. Very versatile and high-level.
- **Django**: Python web framework that encourages rapid development and clean, pragmatic design.
- **Hypertext Markup Language**: Used for the structure of the web pages themselves. Django Template Language was also integrated into the HTML.
- **Cascading Style Sheets**: Put in the `static` folder and keeps elements in both pages the same, such as the black background and white text.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [ChatGPT](https://chat.openai.com/) - Coding Assistant.
* [Django Documentation](https://docs.djangoproject.com/en/5.1/) - Main knowledge source for all Django concepts.
* [YouTube](https://www.youtube.com/) - Fantastic source of free visual information.
* [Stack Overflow](https://stackoverflow.com/) - For troubleshooting and finding solutions to coding problems.

# Future Work

* JavaScript for dynamic search.
* Tidying up the projects page for a more visually appealing look.
* Upload to `markcuizon.com`.
