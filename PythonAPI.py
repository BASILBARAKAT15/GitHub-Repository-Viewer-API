import requests
import csv

def get_repositories(username):
    """
    Fetches all repositories of a given GitHub username.

    :param username: GitHub username
    :return: List of repository dictionaries with details
    """
    repositories = []
    page = 1

    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error: Unable to fetch repositories. Details: {e}")
            return []

        data = response.json()
        if not data:
            break  # No more repositories available
        repositories.extend(data)
        page += 1

    return repositories


def display_repositories(repositories):
    """
    Displays a list of repositories with details.

    :param repositories: List of repository objects
    """
    if not repositories:
        print("No repositories found.")
        return

    print(f"\nFound {len(repositories)} repositories:\n")
    for repo in repositories:
        print(f"Name: {repo.get('name')}")
        print(f"Description: {repo.get('description')}")
        print(f"Stars: {repo.get('stargazers_count')}")
        print(f"Forks: {repo.get('forks_count')}")
        print(f"Language: {repo.get('language')}")
        print(f"URL: {repo.get('html_url')}")
        print("-" * 60)


def save_repositories_to_csv(repositories, filename="repos.csv"):
    """
    Saves repository details to a CSV file.

    :param repositories: List of repository objects
    :param filename: CSV filename (default: repos.csv)
    """
    if not repositories:
        print("No repositories to save.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
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

    print(f"\n✅ Repositories saved to '{filename}' successfully.")


def main():
    """Main function to run the GitHub Repository Viewer."""
    print("GitHub Repository Viewer")
    username = input("Enter GitHub username: ").strip()
    repositories = get_repositories(username)

    display_repositories(repositories)

    if repositories:
        save_choice = input("\nDo you want to save these repositories to a CSV file? (y/n): ").lower()
        if save_choice == "y":
            save_repositories_to_csv(repositories)


if __name__ == "__main__":
    main()
