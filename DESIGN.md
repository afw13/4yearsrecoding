# Introduction
I began this project with a wireframe that I designed in Figma.  Designing the wireframe helped me to understand each “container” or section of the website.  With this wireframe complete, I set out to build each container and its elements, one by one. The code for this project is composed of HTML, CSS and Javascript files.  

### HTML:

The HTML for this project is straightforward.  To start, I built each section of the website in HTML: headings, supporting text, buttons, images, containers and a footer.

I wanted to use some interesting fonts so the <head> contains a few links to various Google fonts that are used on the site.  

The <body> tag starts with buttons used in the top navigation.  These were easy to code in HTML but harder to style in CSS.  

Some images are also linked in the HTML code.  It took a while for me to understand the correct src path to incorporate here but once I figured it out for one image, it was easy for the rest. 

I divided some of the content by inserting horizontal lines and added a simple footer to the bottom of the page.  

### CSS:

Styling this website in CSS introduced many challenges.  

The css code starts by setting a background color for the body and then style elements for the overall website frame.  I used Flexbox (```css
flex
```) here (and in a few other instances) to ensure some responsiveness on the site.  

Buttons were used for navigation links.  In ```css
.frame a.button
``` I just made sure that the background color matched the body color of the site so that they didn’t look like ‘buttons’.  

Styling heading and supporting text was relatively simple.  Here, I encountered the need to set ```css
max-width
``` property so that the text wouldn’t spillover to both ends of the screen. 

Across the entire CSS code, getting the hang of the relationship between max-width, width, margin and padding properties was difficult. It took countless iterations to understand the change that would result by adjusting each property.  For example, I wanted the ```css
.site-footer
``` to display on the left of the page but also aligned with the left end of the .grey-line.  With a bit of research I discovered that this would involve matching max-width of grey-line and site-footer to 80%; 

### Javascript:

There is just one small section of Javascript on this site:  the ```javascript
scrollFunction
```.  I implemented this as an easy way to try Javascript coding. 