import os

def create_files(file_names, directory='.', folder_name='Articles'):
    # Create Articles folder if it doesn't exist
    articles_dir = os.path.join(directory, folder_name)
    os.makedirs(articles_dir, exist_ok=True)

    # HTML Header and Footer templates
    header = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>History Vault Website - Article</title> 
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
</head>

<body>

    <!-- Header -->
    <nav class="navbar navbar-expand-lg">
        <div class="container">
            <a class="navbar-brand" href="/">History Vault</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="../contact.html">Contact</a></li>
                    <li class="nav-item"><a class="nav-link" href="../contribute.html">Contribute</a></li>
                </ul>
            </div>
        </div>
    </nav>
    """

    footer = """
    <!-- Footer -->
    <footer>
        <div class="container">
            <footer class="py-3 my-4">
                <ul class="nav justify-content-center border-bottom pb-3 mb-3">
                    <li class="nav-item"><a href="/" class="nav-link px-2">Home</a></li>
                    <li class="nav-item"><a href="../about.html" class="nav-link px-2">About</a></li>
                    <li class="nav-item"><a href="../contact.html" class="nav-link px-2">Contact</a></li>
                    <li class="nav-item"><a href="../contribute.html" class="nav-link px-2">Contribute</a></li>
                </ul>
                <p class="text-center">© 2024 History Vault Website. All Rights Reserved</p>
            </footer>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>

</html>"""

    # Create the HTML files inside the Articles folder
    for file_name in file_names:
        file_path = os.path.join(articles_dir, file_name)

        # Writing header, content (optional), and footer to the file
        with open(file_path, 'w') as file:
            file.write(header)
            file.write(f"<h1>{file_name.replace('_', ' ').title()}</h1>\n")  # You can add content here
            file.write(footer)
        print(f"Created: {file_path}")

if __name__ == "__main__":
    # List of your file names
    file_names = [
        "quran_history.html",
        "bible_history.html",
        "history_of_business.html",
        "History_of_Wars.html",
        "History_of_Palestine.html",
        "World_history.html",
        "History_of_communication.html",
        "History_of_technology.html",
        "Economic_history.html",
        "Environmental_history.html",
        "History_of_flags.html",
        "History_of_health_care.html",
        "History_of_industries.html",
        "Legal_history.html",
        "History_of_media.html",
        "Military_history.html",
        "History_of_philosophy.html",
        "Political_history.html",
        "Social_history.html",
        "History_of_sports.html",
        "History_of_youth.html",
        "History_of_accounting.html",
        "History_of_agriculture.html",
        "History_of_books.html",
        "History_of_clothing.html",
        "History_of_engineering.html",
        "History_of_finance.html",
        "History_of_law.html",
        "History_of_literature.html",
        "History_of_medicine.html",
        "History_of_metaphysics.html",
        "History_of_mining.html",
        "History_of_money.html",
        "History_of_music.html",
        "History_of_painting.html",
        "History_of_paper.html",
        "History_of_scholarship.html",
        "History_of_the_alphabet.html",
        "History_of_the_automobile.html",
        "History_of_theatre.html",
        "History_of_trade.html",
        "History_of_transport.html",
        "History_of_writing.html"
    ]
    create_files(file_names)
