# 🛡️ Checkpass - Password Security Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

**Checkpass** is a modern, user-friendly desktop application built with Python that helps you manage your password security. It features a robust password strength analyzer and a cryptographically secure password generator.

![App Screenshot](https://via.placeholder.com/800x400?text=Insert+Your+App+Screenshot+Here)

## ✨ Features

* **Real-time Strength Analysis**: Evaluates your password based on length, complexity, and character variety (uppercase, lowercase, numbers, symbols).
* **Visual Feedback**: Provides immediate color-coded feedback (Red/Orange/Green) based on the security score.
* **Secure Generation**: Uses Python's `secrets` module (instead of the standard `random`) to generate cryptographically strong passwords suitable for production use.
* **Modern UI**: Built with `CustomTkinter` for a sleek, modern look that adapts to your system theme.
* **Clipboard Ready**: (Future implementation) Easily copy your generated passwords.

## 🚀 Installation

To run this application locally, you need Python installed on your machine.

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yuriromano02/checkpass.git](https://github.com/yuriromano02/checkpass.git)
    cd checkpass
    ```

2.  **Install dependencies**
    This project uses `customtkinter` for the GUI.
    ```bash
    pip install customtkinter
    ```

3.  **Run the application**
    ```bash
    python pass.py
    ```

## 🛠️ Technologies Used

* **[Python](https://www.python.org/)**: Core logic.
* **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)**: For the modern user interface.
* **Secrets & Re**: Standard Python libraries for cryptography and regex pattern matching.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements (e.g., adding a "Copy to Clipboard" button or saving history securely), feel free to open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
