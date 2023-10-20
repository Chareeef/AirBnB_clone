# HTML and CSS Basics

## What is HTML?

HTML, which stands for HyperText Markup Language, is the standard language used to create and structure web pages. It is a markup language that allows you to define the structure and content of a web page using a set of tags and elements. HTML provides the foundation for building web pages by defining the structure of the document, such as headings, paragraphs, links, images, and more.

## How to create an HTML page

To create an HTML page, you need a text editor (e.g., Visual Studio Code, Notepad, Sublime Text). Follow these steps:

1. Open a text editor.
2. Start with an HTML document structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Your Page Title</title>
  </head>
  <body>
    <!-- Your content goes here -->
  </body>
</html>
```

3. Add content within the `<body>` section, using HTML tags to structure your page.

4. Save the file with the ".html" extension (e.g., "index.html").

5. Open the file in a web browser to view your HTML page.

## What is a markup language?

A markup language is a system for annotating a document to identify elements, such as headings, paragraphs, and links, and to define their structure and presentation. HTML is a prime example of a markup language used for creating web pages.

## What is the DOM?

The Document Object Model (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, content, and style. In other words, it's a tree-like structure that represents the elements of an HTML page, allowing you to interact with and manipulate them using JavaScript.

## What is an element/tag?

In HTML, an element, also known as a tag, is a fundamental building block of a web page. It defines the structure and content of a page. Elements are enclosed within angle brackets ("<" and ">"). For example, `<p>` is an element used for paragraphs, and `<a>` is an element used for links.

## What is an attribute?

An attribute provides additional information about an HTML element and is always specified in the opening tag. Attributes are typically name-value pairs, and they modify the element in some way. For example, the `<a>` element can have an "href" attribute to specify the URL of the link.

## How does the browser load a webpage?

When a web page is requested in a browser, the following steps occur:

1. The browser sends a request to the web server for the webpage's content.

2. The server processes the request and sends back an HTML file.

3. The browser starts parsing the HTML file, building the Document Object Model (DOM) tree.

4. The browser downloads associated resources like stylesheets, scripts, and images.

5. The browser renders the webpage, combining the HTML, CSS, and JavaScript to display it on the screen.

## What is CSS?

CSS, or Cascading Style Sheets, is a stylesheet language used to control the presentation and layout of web pages. It allows you to define how elements on a page should be styled, including aspects like colors, fonts, spacing, and more.

## How to add style to an element

To add style to an HTML element, you can use CSS. You can apply styles directly to an element using the "style" attribute or by defining styles in a separate CSS file and linking it to your HTML document. For example:

Inline style:
```html
<p style="color: blue; font-size: 16px;">This is a blue text.</p>
```

External CSS:
```html
<link rel="stylesheet" type="text/css" href="styles.css">
```

## What is a class?

A class in CSS is a way to group multiple HTML elements so that you can apply the same style to all of them. Classes are defined in your CSS and then added to HTML elements using the `class` attribute. This allows you to maintain a consistent style for elements that share the same characteristics.

## What is a selector?

A selector in CSS is a pattern that matches one or more HTML elements for styling. For example, you can select all paragraphs with the selector `p`, or you can select elements with a specific class using `.classname`.

## How to compute CSS Specificity Value

CSS specificity is a system used to determine which CSS rule should be applied when multiple rules conflict. Specificity is calculated based on selectors and their components. To compute specificity, follow these rules:

1. Count the number of ID selectors in the selector.
2. Count the number of class selectors, attribute selectors, and pseudo-classes.
3. Count the number of element selectors and pseudo-elements.
4. Create a specificity value by combining these counts.

The higher the specificity value, the more specific the selector is.

## What are Box properties in CSS

Box properties in CSS are used to control the layout and dimensions of elements on a web page. Key box properties include:

- `width` and `height`: Sets the dimensions of an element.
- `margin`: Controls the space outside an element.
- `padding`: Manages the space inside an element.
- `border`: Defines the border around an element.
- `display`: Determines how the element is displayed (e.g., block, inline, flex).

These properties allow you to precisely control the positioning and appearance of elements on your webpage.
