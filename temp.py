import os

def create_files(file_names, directory='.'):
    for file_name in file_names:
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            pass  # Create an empty file
        print(f"Created: {file_path}")

if __name__ == "__main__":
    # Replace with your list of file names
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
        "History_of_health_care .html",
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
