# 4 Year ReCoding: An Alzheimer's Journey In Data

### Introduction
In 2020, our mom was enrolled in the ReCODE Protocol™, a program targeting cognitive decline reversal. Despite its ineffectiveness for her, we wanted to share our comprehensive daily dataset of supplements, meals, medications, and biomarkers in the hopes that it will benefit others embarking on a similar journey.

Extending the ‘ReCoding’ site with new skills learned from CS33 is my final project.  For this project, I wanted to develop a website that would eventually provide a large data table for browsing and analysis.  For this iteration of this project, the website links to a 14-day sample of the data, located in the project data sheet.  The website also includes some supporting resources related to the program.  All of these components will continue to evolve even after the course ends. 

### YouTube Intro Video:


### Components:
This project has 4 main components:

1. **A single-page website**: https://afw13.github.io/4yearsrecoding/

2. **A website wireframe** designed in Figma.  I wanted to use this project as an opportunity to imporve my Figma skills.  Having a wireframe designed in advance, helped to pace my coding and keep it focused on distinct elements. 

3. **A sample datasheet**.  Presently, this sheet contains a 14-day set of data, linked on the website.  Once the datasheet is more fully populated, it will be embedded on the website.

4. **A codebase**.  The website relies on HTML, CSS, Python and Javascript, all available in Github.  

# Code 
I began this project with a wireframe that I designed in Figma.  Designing the wireframe helped me to understand each “container” or section of the website.  With this wireframe complete, I set out to build each container and its elements, one by one. The code for this project is composed of HTML, CSS, Python and Javascript files and was designed with responsiveness in mind.

### HTML/CSS:

The HTML for this project is straightforward.  To start, I built each section of the website in HTML: headings, supporting text, buttons, images, containers and a footer.

I wanted to use some interesting fonts so the <head> contains a few links to various Google fonts that are used on the site.  



### CSS:
The css code starts by setting a background color for the body and then style elements for the overall website frame.  I used Flexbox (flex) here (and in a few other instances) to ensure some responsiveness on the site.  

Buttons were used for navigation links.  In .frame a.button I just made sure that the background color matched the body color of the site so that they didn’t look like ‘buttons’.  

Styling heading and supporting text was relatively simple.  Here, I encountered the need to set max-width property so that the text wouldn’t spillover to both ends of the screen. 

Across the entire CSS code, getting the hang of the relationship between max-width, width, margin and padding properties was difficult. It took countless iterations to understand the change that would result by adjusting each property.  For example, I wanted the .site-footer to display on the left of the page but also aligned with the left end of the .grey-line.  With a bit of research I discovered that this would involve matching max-width of grey-line and site-footer to 80%; 

### Javascript:

This project uses JavaScript to enhance interactivity and user experience by implementing collapsible sections on the Resources page. When the page loads, the script listens for the DOMContentLoaded event to ensure that the HTML is fully loaded before any JavaScript executes. The script then selects all elements with the class .collapsible-header and attaches a click event listener to each. Upon clicking any of these headers, the associated images, which is the next sibling in the HTML structure, has its visibility toggled. This is achieved by adding or removing the show class, which controls the display property of these content sections, making them collapsible. This feature allows for a clean and efficient way to manage the display of extensive content (that will likely grow in the future), improving usability and page navigation.

## Responsivenss 
This website is designed with responsiveness in mind to provide an optimal viewing experience across a variety of devices, from desktops to smartphones. Key measures taken to ensure this include:

**Viewport Meta Tag**: Each HTML file includes a <meta name="viewport" content="width=device-width, initial-scale=1.0"> tag, which controls the page's dimensions and scaling to match the device's width. 

**Flexible Layouts Using Flexbox**: Some CSS employs Flexbox in the .frame container to create layouts that adapt dynamically to the available space. This technique aligns items centrally and maintains a consistent gap, ensuring content is neatly organized and accessible on any screen size.

**Responsive Typography and Element Sizing**: Some CSS uses relative units (vw, %, em) for font sizes and spacing. For instance, in the .heading class, font size is set in viewport widths (vw), which adjust according to screen size. This ensures that the typography is scalable and readable on different devices.

**Media Queries**: Some custom media queries are implemented for devices with a maximum width of 767px. These queries adjust padding, font sizes, and other properties to improve readability and usability on smaller screens. 

## Django Implementation

This project utilizes Django for backend development. Django's key features, such as URL routing, models, and views, were leveraged to create a scalable web application.

**Templating** 
The HTML files in this project utilize Django's template inheritance feature to maintain a consistent structure and style across different pages. Each page extends from the landing_page.html base template using {% extends 'landing_page.html' %}. This setup allows specific sections like the title, heading, and content to be customized for each page (About, Resources, etc.) by overriding blocks defined in the base template ({% block title %}, {% block heading %}, and {% block content %}). 

**URL Patterns**
In this project, URL patterns were configured in the `urls.py` files to handle different routes and direct requests to the appropriate views. For example, the `/about/`, `/resources/`, and `/dataset/` URLs were mapped to their respective views to render the corresponding pages.

**Models**
The `models.py` file in the `dataset` app defines the data models used in the project. The `DatasetEntry` model was created to represent the structure of the dataset, with fields corresponding to the columns in the CSV file. This model allows for efficient storage, retrieval, and manipulation of the dataset data using Django's Object-Relational Mapping (ORM).

**Views**
In this project, views were implemented to render the appropriate templates and pass the necessary data to them. For instance, the `dataset_view` in `views.py` retrieves all the `DatasetEntry` objects from the database and passes them to the `dataset.html` template for rendering.

**Database Integration**
Django's built-in ORM was used to interact with the database. The `import_dataset` management command was created to import the dataset from a CSV file into the database. This command reads the CSV file, creates `DatasetEntry` instances for each row, and saves them to the database using Django's ORM.

## DataTables
To display the comprehensive dataset in a user-friendly tabular format on the website, the DataTables library was used. This involved integrating the necessary JavaScript and CSS files, creating an HTML table structure with headers corresponding to the dataset fields, and dynamically populating the table body with data from the Django model using a template loop. The DataTables plugin was then initialized on this table, enabling features like responsive behavior across different screen sizes. This implementation ensures that, as this dataset becomes larger, it can be easily explored and analyzed by visitors to the site.  It was also a great opportunity to try a library I had never used before (Thanks, Chris!)

## Known Issues:

>> The website currently exists as a single page.  In future iterations, I’d like to build out separate pages for the About, Research and Resources sections and add page content to each. 

>> The Learn More button does not click out to anything 


- responseivenss 


