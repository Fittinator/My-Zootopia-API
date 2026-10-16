
from html import escape
from pathlib import Path

import data_fetcher


BASE_DIR = Path(__file__).resolve().parent


def serialize_animal(animal_obj):
    """Convert a single animal into an HTML card."""
    output = ""

    # Start the HTML card
    output += '<li class="cards__item">\n'

    # Add the animal's name
    if "name" in animal_obj:
        output += (
            f'  <div class="card__title">'
            f'{animal_obj["name"]}</div>\n'
        )

    # Start the card's text section
    output += '  <p class="card__text">\n'

    # Add diet and type if available
    if "characteristics" in animal_obj:
        characteristics = animal_obj["characteristics"]

        if "diet" in characteristics:
            output += (
                f'    <strong>Diet:</strong> '
                f'{characteristics["diet"]}<br/>\n'
            )

    # Add the first location if available
    if "locations" in animal_obj:
        locations = animal_obj["locations"]

        if locations:
            output += (
                f'    <strong>Location:</strong> '
                f'{locations[0]}<br/>\n'
            )

    if "characteristics" in animal_obj:
        characteristics = animal_obj["characteristics"]

        if "type" in characteristics:
            output += (
                f'    <strong>Type:</strong> '
                f'{characteristics["type"]}<br/>\n'
            )

    # Close the HTML card
    output += "  </p>\n"
    output += "</li>\n"

    return output


def main():
    """Generate an HTML page containing all animals."""

    animal_name = input("Enter a name of an animal: ").strip()
    if not animal_name:
        print("Bitte einen Tiernamen eingeben.")
        return

    try:
        animals_data = data_fetcher.fetch_data(animal_name)
    except ValueError:
        print("Abruf fehlgeschlagen. Bitte API_KEY in .env und Verbindung prüfen.")
        return

    # Read the HTML template
    with open(BASE_DIR / "animals_template.html", "r", encoding="utf-8") as file:
        html_template = file.read()

    # Generate HTML for all animals
    output = ""

    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    if not animals_data:
        output = (
            '<li class="cards__item">'
            f'<h2>The animal "{escape(animal_name)}" doesn\'t exist.</h2>'
            '<p>Please try another animal name.</p></li>'
        )

    # Insert animal cards into the template
    new_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__", output
    )

    # Save the generated HTML page
    with open(BASE_DIR / "animals.html", "w", encoding="utf-8") as file:
        file.write(new_html)

    print("animals.html wurde erfolgreich erstellt!")


if __name__ == "__main__":
    main()
