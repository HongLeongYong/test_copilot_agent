import os

def list_desktop_files():
    desktop_path = os.path.expanduser("~/Desktop")
    try:
        files = os.listdir(desktop_path)
        print("Files and folders on your Desktop:")
        for file in files:
            print(file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_desktop_files()