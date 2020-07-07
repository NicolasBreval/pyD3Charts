# pyD3Charts
Python library for chart creation based on D3 javascript library.

This library allows to create charts easily using data as Python iterable objects and show charts in a window using pywebview and D3 javascript library.

pywebview is a cool library to create web views using Python language and it's essential in this library, because all charts are generated using a basic HTML page and a script which includes D3 library to transform Python data in a chart and then show this data more easily.

## Technologies
This project is based in many technologies:

### pywebview
Is a library used to create a webview application using Python. It's used to render HTML code of chart and show it in a window.

## D3
Data Driven Documents is a library written in JavaScript that make easily create charts. In JavaScript defines many properties of chart and D3 render it as a SVG in HTML.

## Jinja2
Due to charts are made using HTML and JavaScript, for automating process of HTML creation, project uses Jinja2 library, which allows to render templates from Python code. Jinja2 is many recognized because is used in another popular Python libraries, like Flask or Django.

## How to test library
This library is currently in development and is not packed as a real library yet, but you can test it clonning this project and executing *test.py* file with this command:

```
$ python test.py
```

The test module creates a webview with a random scatter plot and outputs it at a single HTML file called *example.html* at root project path.

## Examples
Here are shown many examples of charts created with this library:

### Simple scatter plot
<img src="https://raw.githubusercontent.com/NicolasBreval/pyD3Charts/master/img/scatter_plot.png" alt="Example of simple scatter plot" title="Example of simple scatter plot" width="50%" height="50%"/>


### Multi-series scatter plot
<img src="https://raw.githubusercontent.com/NicolasBreval/pyD3Charts/master/img/multi_series_scatter_plot.png" alt="Example of multi-series scatter plot" title="Example of multi-series scatter plot" width="50%" height="50%"/>