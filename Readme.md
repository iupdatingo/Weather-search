# Weather Search Application

This project is a simple Flask-based web application that retrieves weather information for a given city using the OpenWeather API.

## Features
- Search weather information by city.
- Displays temperature, humidity, weather conditions, and more.

## Project Structure
├── api_key.txt # File containing your OpenWeather API key 
├── app.py # Flask application script 
├── jscript.java # Frontend JavaScript logic for handling user input 
└── templates 
  └── index.html # HTML template for the web interface

---

## Prerequisites
- Python (version 3.7 or higher)
- pip (Python package installer)

## Steps to Run on Windows

### 1. Clone or Download the Project
Download this project to your local machine.

### 2. Install Python
Ensure Python 3.7 or higher is installed. You can download it from [Python.org](https://www.python.org/downloads/).

### 3. Install Virtual Environment (Optional but Recommended)
Create and activate a virtual environment for this project:
```
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies
Navigate to the project directory and install dependencies using requirements.txt:
```
pip install -r requirements.txt
```

### 5. Add Your API Key
Create a file named api_key.txt in the project directory and add your OpenWeather API key inside it.

### 6. Run the Application
Run the Flask application using:
```
python app.py
```
The server will start at http://127.0.0.1:5000. Open this URL in your web browser.

### 7. Access the Application
You can search for the weather by entering a city name in the search box on the application homepage.

---

## Troubleshooting

### Issue: NoModuleNamedFlask
If you encounter the error ModuleNotFoundError: No module named 'Flask':
  1. Ensure that the dependencies were installed successfully using `pip install -r requirements.txt`.
  2. Run the app.py script from a terminal with administrative privileges (optional but sometimes required).

### Issue: Port Already in Use
If the application fails to start because the port is in use, change the port number in app.py:
```
app.run(host='0.0.0.0', port=5001)
```

### Additional Notes
The application is developed to run on Linux and Windows, but ensure all dependencies are installed and configured correctly.
Virtual environments help avoid conflicts between project dependencies.