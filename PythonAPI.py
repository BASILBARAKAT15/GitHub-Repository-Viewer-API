import requests
import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def get_repositories(username):
    """Fetches repositories from GitHub API."""
    repositories = []
    page = 1

    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Unable to fetch repositories:\n{e}")
            return []

        data = response.json()
        if not data:
            break
        repositories.extend(data)
        page += 1

    return repositories


def save_repositories_to_csv(repositories, username):
    """Saves repository data to a CSV file."""
    if not repositories:
        messagebox.showwarning("Warning", "No repositories to save.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        initialfile=f"{username}_repos.csv",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_path:
        return  # User canceled

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Description", "Stars", "Forks", "Language", "URL"])
        for repo in repositories:
            writer.writerow([
                repo.get("name"),
                repo.get("description"),
                repo.get("stargazers_count"),
                repo.get("forks_count"),
                repo.get("language"),
                repo.get("html_url")
            ])

    messagebox.showinfo("Success", f"Repositories saved to:\n{file_path}")


def fetch_and_display():
    """Handles the fetch button click."""
    username = entry_username.get().strip()
    if not username:
        messagebox.showwarning("Input Error", "Please enter a GitHub username.")
        return

    tree.delete(*tree.get_children())  # Clear previous data
    repos = get_repositories(username)
    if not repos:
        return

    for repo in repos:
        tree.insert("", "end", values=(
            repo.get("name"),
            repo.get("stargazers_count"),
            repo.get("forks_count"),
            repo.get("language") or "N/A"
        ))

    save_button.config(state="normal")
    global current_repos, current_username
    current_repos = repos
    current_username = username


# --- GUI Setup ---
root = tk.Tk()
root.title("GitHub Repository Viewer")
root.geometry("800x500")
root.resizable(False, False)

frame_top = tk.Frame(root, pady=10)
frame_top.pack()

tk.Label(frame_top, text="Enter GitHub username:", font=("Arial", 12)).pack(side="left")
entry_username = tk.Entry(frame_top, font=("Arial", 12), width=30)
entry_username.pack(side="left", padx=10)
fetch_button = tk.Button(frame_top, text="Fetch Repos", command=fetch_and_display)
fetch_button.pack(side="left")

# Table (Treeview)
columns = ("Name", "Stars", "Forks", "Language")
tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180 if col == "Name" else 100, anchor="center")
tree.pack(pady=10, fill="both", expand=True)

# Save button
save_button = tk.Button(root, text="Save to CSV", state="disabled",
                        command=lambda: save_repositories_to_csv(current_repos, current_username))
save_button.pack(pady=10)

root.mainloop()
