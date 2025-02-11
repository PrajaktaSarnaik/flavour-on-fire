# Testing

This is the TESTING file for the [Flavour On Fire](https://flavour-on-fire-1bb1fc2c2e8e.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [Lighthouse Scores](#lighthouse-scores)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)
    
## Validation

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

I have had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if I were to use my website's URL so I have had to follow the below approach for every page:

- Via the deployed Heroku app link, I have navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing you to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.

All HTML pages were validated and returned a 'No errors or warnings to show' result, except for the recipe detail page. This page pulls content from the database using Summernote, which results in a error related to the <p> tags. However, this issue stems from how Django processes and renders the content, making it unfixable within the current setup.

![Chef's Special HTML validator Screenshot](static/readme_images/validation_and_testing/chef_special_html_validator.PNG)

![Index HTML validator Screenshot](static/readme_images/validation_and_testing/index_html_validator.PNG)

![Our Chefs HTML validator Screenshot](static/readme_images/validation_and_testing/our_chef_html_validator.PNG)

![Recipe Detail HTML validator Screenshot](static/readme_images/validation_and_testing/recipe_detail_html_validator.PNG)
*This issue stems from how Django processes and renders the content, making it unfixable within the current setup.*


![Share Recipe HTML validator Screenshot](static/readme_images/validation_and_testing/share_recipe_html_validator.PNG)

![Sign In HTML validator Screenshot](static/readme_images/validation_and_testing/sign_in_html_validator.PNG)

![Sign Out HTML validator Screenshot](static/readme_images/validation_and_testing/sign_out_html_validator.PNG)

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- | 
| Home | 0 | 0 |
| Sign In | 0 | 0 |
| Sign Out | 0 | 0 |
| Recipe Detail | 1 | 0 |
| Chef's Special | 0 | 0 |
| Our Chefs | 0 | 0 |
| Share your recipe | 0 | 0 |

<hr>

### CSS Validation

I've used the W3C CSS Validator to ensure that my stylesheets are error-free and compliant with web standards, helping improve the overall quality and consistency of my code.

![CSS validator Screenshot](static/readme_images/validation_and_testing/css_validator.PNG)

<hr>

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the small amount of JavaScript code added to the project. External JS, for Bootstrap purposes, obtained via [CDN](https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js) was not validated through JSHint

![print JS](static/readme_images/validation_and_testing/script_js_validator.PNG)
*Used for print button logic*

![comment JS](static/readme_images/validation_and_testing/comments_js_validator.PNG) 
*Used to edit and update comments*


| Page |  sed For |  Errors | Warnings |
| ---- | ----------- |------ | -------- |
| recipe_detail.html | Used for print button logic | none | none |
| recipe_detail.html | Used to edit and update comments | none | none |


### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files that were created or edited by myself. No issues presented and line lengths were double checked. I have included some screenshots of validation of python files used within apps.

Please click on **"no errors"** to view respective screenshot.

| Feature | admin.py | forms.py | models.py | urls.py | views.py |
|---------|----------|----------|-----------|---------|----------|
| Recipe | [no errors](static/readme_images/python_validation/recipe_admin_py.PNG) | [no errors](static/readme_images/python_validation/recipe_forms_py.PNG) | [no errors](static/readme_images/python_validation/recipe_models_py.PNG) | [no errors](static/readme_images/python_validation/recipe_urls_py.PNG) | [no errors](static/readme_images/python_validation/recipe_views_py.PNG) |
| Author  | [no errors](static/readme_images/python_validation/author_admin_py.PNG) | N/A | [no errors](static/readme_images/python_validation/author_models_py.PNG) | [no errors](static/readme_images/python_validation/author_urls_py.PNG) | [no errors](static/readme_images/python_validation/author_views_py.PNG) |

Here are some screenshots of validation of python files used within **Flavour** project.

![settings py file](static/readme_images/python_validation/flavour_settings_py.PNG)
*Validation of Settings.py*

![urls py file](static/readme_images/python_validation/flavour_urls_py.PNG)
*Validation of project's urls.py*