# JavaScript - Web jQuery

This is a preparatory project to learn how to manipulate the DOM with jQuery before implementing it into the HolbertonBnB project.

## Tests :heavy_check_mark:

* [tests](./tests): Folder containing HTML files for testing DOM manipulation scripts.

## Tasks :page_with_curl:

### 0. No jQuery
- **File:** [0-script.js](./0-script.js)
- **Description:** A JavaScript script that uses `document.querySelector` to update the text color of the HTML tag `HEADER` to red (`#ff0`).

### 1. With jQuery
- **File:** [1-script.js](./1-script.js)
- **Description:** A JavaScript script that uses jQuery to update the text color of the HTML tag `HEADER` to red (`#ff0`).

### 2. Click and Turn Red
- **File:** [2-script.js](./2-script.js)
- **Description:** A JavaScript script that uses jQuery to update the text color of the HTML tag `HEADER` to red (`#ff0`) when the user clicks on the tag `DIV#red_header`.

### 3. Add `.red` Class
- **File:** [3-script.js](./3-script.js)
- **Description:** A JavaScript script that uses jQuery to add the class `.red` to the HTML tag `HEADER` when the user clicks on the tag `DIV#red_header`.

### 4. Toggle Classes
- **File:** [4-script.js](./4-script.js)
- **Description:** A JavaScript script that uses jQuery to toggle the class of the HTML tag `HEADER` between `.red` and `.green` when the user clicks on the tag `DIV#red_header`.

### 5. List of Elements
- **File:** [5-script.js](./5-script.js)
- **Description:** A JavaScript script that uses jQuery to add an `LI` element to a list when the user clicks on the tag `DIV#add_item`.
  - Adds the element `<li>Item</li>` to `UL.my_list`.

### 6. Change the Text
- **File:** [6-script.js](./6-script.js)
- **Description:** A JavaScript script that uses jQuery to update the text of the HTML tag `HEADER` to "New Header!!!" when the user clicks on the tag `DIV#update_header`.

### 7. Star Wars Character
- **File:** [7-script.js](./7-script.js)
- **Description:** A JavaScript script that uses jQuery to fetch the Star Wars API `https://swapi.co/api/people/5/?format=json` and display the name in the HTML tag `DIV#character`.

### 8. Star Wars Movies
- **File:** [8-script.js](./8-script.js)
- **Description:** A JavaScript script that uses jQuery to fetch and list all movie titles from the Star Wars API `https://swapi.co/api/films/?format=json`.
  - Titles are listed in the HTML tag `UL#list_movies`.

### 9. Say Hello!
- **File:** [9-script.js](./9-script.js)
- **Description:** A JavaScript script that uses jQuery to fetch and display how to say "Hello" in French using the API `https://fourtonfish.com/hellosalut/?lang=fr`.
  - Displays the translation in the HTML tag `DIV#hello`.
  - Works when imported in the `HEAD` tag.

### 10. No jQuery - Document Loaded
- **File:** [100-script.js](./100-script.js)
- **Description:** A JavaScript script that uses `document.querySelector` to update the text color of the HTML tag `HEADER` to red (`#ff0`).
  - Works when imported in the `HEAD` tag.

### 11. List, Add, Remove
- **File:** [101-script.js](./101-script.js)
- **Description:** A JavaScript script that uses jQuery to add, remove, and clear `LI` elements from a list based on user click input.
  - Adds a new element when the user clicks `DIV#add_item`.
    - Adds `<li>Item</li>` to the HTML tag `UL.my_list`.
  - Removes the last element when the user clicks `DIV#remove_item`.
  - Clears all elements when the user clicks `DIV#clear_list`.
  - Works when imported in the `HEAD` tag.

### 12. Say Hello to Everybody!
- **File:** [102-script.js](./102-script.js)
- **Description:** A JavaScript script that uses jQuery to fetch and display how to say "Hello" in a given language using the API `https://www.fourtonfish.com/hellosalut/hello/`.
  - Fetches the translation for the language entered in the HTML tag `INPUT#language_code`.
  - Fetches the translation when the user clicks on the HTML tag `INPUT#btn_translate`.
  - Displays the translation in the HTML tag `DIV#hello`.
  - Works when imported in the `HEAD` tag.

### 13. And Press ENTER
- **File:** [103-script.js](./103-script.js)
- **Description:** A JavaScript script that uses jQuery to fetch and display how to say "Hello" in a given language using the API `https://www.fourtonfish.com/hellosalut/hello/`.
  - Identical to [102-script.js](./102-script.js) except that the translation is fetched when either the user clicks on the HTML tag `INPUT#btn_translate` or presses `ENTER` when hovering over the tag `INPUT#language_code`.

## Author

- [Ahmed Azagaz](https://www.linkedin.com/in/ahmed-azagaz-0678b7281/)
