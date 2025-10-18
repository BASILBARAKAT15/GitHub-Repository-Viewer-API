# 🪟 GitHub Repository Viewer (GUI)

A simple Python GUI tool to view and export public GitHub repositories for any user.
Built using **Tkinter** and **Requests**, it lets you fetch repositories, display them in a clean table, and export the data to a CSV file.

---

## 🚀 Features

* 🔍 Fetches all **public repositories** for any GitHub username
* 📋 Displays key details:

  * Repository **Name**
  * ⭐ **Stars**
  * 🍴 **Forks**
  * 🧠 **Language**
* 💾 Exports data to **CSV file** (`username_repos.csv`)
* ⚠️ Handles network errors, invalid usernames, and empty results gracefully
* 🖥️ Simple, user-friendly **Tkinter GUI**

---

## 🧰 Requirements

* **Python 3.8+**
* Required modules:

  ```bash
  pip install requests
  ```

> ⚠️ Tkinter is included by default with most Python installations.

---

## 📦 Installation

1. Clone or download this repository:

   ```bash
   git clone https://github.com/yourusername/github-repo-viewer.git
   cd github-repo-viewer
   ```

2. Install dependencies:

   ```bash
   pip install requests
   ```

3. Run the program:

   ```bash
   python github_viewer_gui.py
   ```

---

## 🖱️ Usage

1. Enter a **GitHub username** in the input box.
2. Click **Fetch Repos** to retrieve all repositories.
3. Browse the results in the on-screen table.
4. Click **Save to CSV** to export results to a file of your choice.

---

## 🗂️ Example Output (CSV)

| Name        | Stars | Forks | Language   | URL                                                                              |
| ----------- | ----- | ----- | ---------- | -------------------------------------------------------------------------------- |
| hello-world | 150   | 20    | Python     | [https://github.com/octocat/hello-world](https://github.com/octocat/hello-world) |
| sample-app  | 45    | 10    | JavaScript | [https://github.com/octocat/sample-app](https://github.com/octocat/sample-app)   |

---

## 🧑‍💻 Author

**Your Name**
📧 [your.email@example.com](mailto:your.email@example.com)
💼 [LinkedIn](https://linkedin.com/in/yourprofile) • 🌐 [GitHub](https://github.com/yourusername)

---

## 📄 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it.
