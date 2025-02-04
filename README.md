# Django User Registration Demo 📝

This repository demonstrates the process of user registration using Django's default authentication system and how you can later customize the user interface (UI) of the registration fields. 🔐

## Features 🌟

- **Default Django Registration**: The `main` branch includes a basic user registration system using Django’s built-in `UserCreationForm`. It handles user input and registration, with no UI customizations. ✍️
  
- **UI Customization**: The `customizing_registration` branch showcases how to customize the UI of the user registration form by leveraging HTML, CSS, and Bootstrap to provide a better and more visually appealing experience. 🎨✨

## Setup Instructions ⚙️

1. Clone the repository:

    ```bash
    git clone https://github.com/dcccalvin/user_authentication.git
    cd user_authentication
    ```

2. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

3. Navigate to `http://127.0.0.1:8000/register/` to see the default registration form. 🚀

4. Switch to the `customizing_registration` branch for the custom UI version:

    ```bash
    git checkout customizing_registration
    ```

5. Visit the same URL to see the customized registration form. 🎨

## What’s Inside 📦

- **Main Branch (default_registration)**:  
   - The form uses Django’s `UserCreationForm`, with no special customizations applied to the front-end. 💻

- **Customizing Registration Branch**:  
   - This branch customizes the registration form using HTML and Bootstrap, and adds necessary CSS to improve the user experience. 💡

## Contributing 🤝

Feel free to fork the repository, create a branch, and submit pull requests. Contributions are welcome! 💬

