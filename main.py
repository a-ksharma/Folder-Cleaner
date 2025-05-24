import os
# Creating Folders
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
createIfNotExists('Images')
createIfNotExists('Docs')
createIfNotExists('Media')
createIfNotExists('Others')
# Folders Created

# Moving Files
def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")
# Files Moved

if __name__ == "__main__":
    files = os.listdir()
    files.remove("Cleaner.py")
    print(files)

    # Initialising Values
    imgExts = [".png", ".jpg", ".jpeg", ".gif"]
    docExts = [".txt", ".doc", ".docx", ".xls", ".pdf", ".html", ".htm"]
    mediaExts = [".mp3", ".mp4", ".m4v", ".mkv", ".flv"]
    others = []
    # Initialized

    # For Images
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    print(f"Images are {images}")

    # For Documents
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    print(f"Documents are {docs}")

    # For Medias
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    print(f"Medias are {medias}")

    # For Others
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile(file):
            others.append(file)
    print(f"Others are {others}")

    # Calling move Function
    move("Images", images)
    move("Media", medias)
    move("Docs", docs)
    move("Others", others)
