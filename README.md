# Ultimate Note-Taking App

## Overview

The Ultimate Note-Taking App is a powerful and user-friendly application designed to help users efficiently manage their notes. Built with Streamlit and SQLite, this app provides a robust backend for creating, reading, updating, and deleting notes. It also includes user authentication using hashed passwords for secure access.

## Features

- **User Registration**: Users can register with a username and password.
- **User Authentication**: Secure user authentication using hashed passwords.
- **CRUD Operations for Notes**: Users can create, read, update, and delete their notes.
- **User-Specific Notes**: Each user can only access their own notes.
- **Streamlit Interface**: A clean and interactive interface for managing notes.

## Installation

To get started with the Ultimate Note-Taking App, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Imanolasolo/ultimate-note-taking-app.git
   cd ultimate-note-taking-
   ```
   
2. **Create a virtual environment**:
    ```
    python -m venv venv
    ```

3. **Activate the virtual environment**
    - On windows
    ```
    venv\Scripts\activate
    ```
    - On macOS/Linux
    ```
    source venv/bin/activate
    ```

4. **Install the required dependencies**:
    ```
    pip install -r requirements.txt
    ```

5. **Initialize the database**
    ```
    python notes_project_streamlit/db.py
    ```


## Usage

To run the application, follow these steps:

1. **Start the Streamlit application**:
   ```sh
   streamlit run notes_project_streamlit/app.py
   ```

2. **Access the application**:
   Open your web browser and navigate to `http://localhost:8501/`.

## Project Structure

```
ultimate-note-taking-app/
├── notes_project_streamlit/
│   ├── db.py
│   ├── app.py
│   ├── dashboard.py
│   ├── requirements.txt
├── README.md
```

## File Descriptions

- **db.py**: Contains functions for initializing the database and performing CRUD operations on users and notes.
- **app.py**: The main entry point for the Streamlit application, handling user authentication and navigation to the dashboard.
- **dashboard.py**: Contains the dashboard functionality for displaying, creating, editing, and deleting notes.

## Deployment

To deploy the Ultimate Note-Taking App using Streamlit, follow these steps:

1. **Ensure all dependencies are listed in `requirements.txt`**:
   ```sh
   pip freeze > requirements.txt
   ```

2. **Deploy to Streamlit Sharing**:
   - Go to [Streamlit Sharing](https://streamlit.io/sharing).
   - Sign in with your GitHub account.
   - Click on "New app".
   - Select the repository and branch where your app is located.
   - Enter the path to `app.py` (e.g., app.py).
   - Click "Deploy".

3. **Access your deployed application**:
   Once deployed, you will receive a URL where your application is hosted. Share this URL with others to allow them to use your app.

## Contributing

We welcome contributions to the Ultimate Note-Taking App! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

If you have any questions or need further assistance, please feel free to contact us at [jjusturi@gmail.com].

---

Thank you for using the Ultimate Note-Taking App! We hope it helps you stay organized and productive.
