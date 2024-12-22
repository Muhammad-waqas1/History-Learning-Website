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
    <style>
        .section-title {
            color: #343a40;
            font-weight: 700;
            margin-bottom: 30px;
            text-align: center;
        }

        img {
            float: right;
            width: 350px;
            height: 350px;
            object-fit: cover;
            padding: 30px;
        }

    </style>
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

    <main class="container my-5">
        <section class="mt-5">               
    """

    footer = """

                Parahere

            <img src="..\Images\bible-3.jpg" class="img-fluid" alt="Bible Image">
            <div class="d-grid gap-2 col-6 mx-auto">
                <a href="https://www.britannica.com/topic/Bible" target="_blank" type="button"
                    class="btn btn-success">Read Detailed History</a>
            </div>
        </section>


        <!-- Video -->
        <section class="mt-5 text-center">
            <h2 class="section-title">Video Reference</h2>
            <video width="90%" height="auto" class="object-fit-contain" controls>
                <source src="https://www.w3schools.com/html/mov_bbb.mp4">
                Your browser does not support the video tag.

            </video>
        </section>

        <!-- Glossary of Terms -->
        <section class="mt-5 ">
            <h2 class="section-title">Glossary of Terms</h2>
            
            <!-- Glossary Here !  -->

        </section>

        <!-- Top Questions -->
        <section class="mt-5 text-center">
            <h2 class="section-title">Top Questions</h2>
            <div class="accordion" id="accordionExample">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse"
                            data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                            Accordion_1
                        </button>
                    </h2>
                    <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
                        <div class="accordion-body">

                            Accordion_1_innerData

                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                            data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                            Accordion_2
                        </button>
                    </h2>
                    <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
                        <div class="accordion-body">

                            Accordion_1_innerData

                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                            data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                            Accordion_3
                        </button>
                    </h2>
                    <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
                        <div class="accordion-body">

                            Accordion_1_innerData

                        </div>
                    </div>
                </div>
            </div>
        </section>


        <!-- Questions -->
        <section class="mt-5">
            <h2 class="section-title">Have any Questions?</h2>
            <p class="lead">Our experts are here to help. Feel free to ask anything related to our Article or services.
            </p>
            <form id="contactForm">
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Email Address</label>
                    <input type="email" class="form-control" id="exampleFormControlInput1"
                        placeholder="name@example.com" required>
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlTextarea1" class="form-label">Your Question</label>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"
                        placeholder="Ask anything you want" required></textarea>
                </div>
                <button class="btn btn-primary">Submit Question</button>
            </form>
        </section>

    </main>


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
                <p class="text-center">&copy; 2024 History Vault Website. All Rights Reserved</p>
            </footer>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        window.onload = function () {
            const form = document.getElementById('contactForm');
            const emailInput = document.getElementById('exampleFormControlInput1');
            const questionInput = document.getElementById('exampleFormControlTextarea1');

            form.addEventListener('submit', function (event) {
                event.preventDefault();

                alert("Your question has been submitted successfully!");

                setTimeout(function () {
                    form.submit();
                    emailInput.value = '';
                    questionInput.value = '';
                }, 500);
            });
        };
    </script>
</body>

</html>"""

    # Create the HTML files inside the Articles folder
    for file_name in file_names:
        file_path = os.path.join(articles_dir, file_name)

        # Writing header, content (optional), and footer to the file
        with open(file_path, 'w') as file:
            file.write(header)
            file.write(f"<h1 class=\"section-title\">{file_name[:-5].replace('_', ' ').title()}</h1>\n")  # You can add content here
            file.write(footer)
        print(f"Created: {file_path}")

if __name__ == "__main__":
    # List of your file names
    file_names = [
        "Quran_history.html",
        "Bible_history.html",
        "History_of_Business.html",
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
