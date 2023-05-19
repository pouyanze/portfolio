# Portfolio

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Description

The Portfolio project is a template designed to help individuals create their own professional portfolios along with their own blog. It provides a starting point and structure for showcasing personal information, skills, work experiences, projects, and more. This template aims to simplify the process of creating an impressive portfolio by providing a clean and customizable design.

## Table of Contents

- [Installation and Usage](#installation-and-usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation and Usage

To use the Portfolio template, follow these steps:
1. **Clone the Repository:** Clone the project repository to your local machine:
   ```
   git clone https://github.com/pouyanze/portfolio.git
   ```
   and then go to its directory:
   ```
   cd portfolio
   ```
2. **Install Pipenv:** If you don't have Pipenv installed, you can install it using pip:
   ```
   pip install pipenv
   ```

3. **Activate the Virtual Environment:** Activate the virtual environment created by Pipenv:
   ```
   pipenv shell
   ```
4. **Install Dependencies:** Install the project dependencies specified in the `Pipfile`:
   ```
   pipenv install
   ```

5. **Apply Database Migrations:** Apply the database migrations to set up the database:
   ```
   python manage.py migrate
   ```

6. **Create Superuser Account:** Create a superuser account to access the admin interface:
   ```
   python manage.py createsuperuser
   ```

7. **Start the Development Server:** Launch the development server:
   ```
   python manage.py runserver
   ```

8. **Access the Application:** Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the application.

Feel free to adapt and modify the template to suit your unique requirements and design preferences. Experiment with different styles, layouts, and content to make your portfolio stand out.

9. **Use blog posts API** at this address:
```
http://localhost:8000/api/posts
```
## Contributing

Contributions to the Portfolio project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the project's GitHub repository. 

If you are interested in making direct contributions to the codebase, follow these steps:

1. Fork the project repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main project repository.

Please follow the project's code style and guidelines when contributing. Ensure that your changes are well-documented and thoroughly tested.

## License

This project is licensed under the [MIT License](LICENSE). Make sure to include the license file in your project repository.

## Contact

If you have any questions, feedback, or want to contact me regarding the project, you can reach me through the following channels:

- Email: [pouyan.ze@gmail.com](mailto:pouyan.ze@gmail.com)
- GitHub: [pouyanze](https://github.com/pouyanze)

Feel free to reach out with any inquiries or suggestions. I appreciate your interest in the Portfolio template!
