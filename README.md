# Weather API – Python

A simple Python application that fetches current weather information from [WeatherAPI](https://www.weatherapi.com/), processes the JSON response, and displays a formatted weather summary.

## Features

- Fetches real-time weather data using a REST API.
- Parses JSON responses.
- Uses Object-Oriented Programming (OOP) to organize weather data.
- Loads API credentials securely from a `.env` file.
- Handles HTTP and connection errors.
- Uses a Python virtual environment to manage dependencies.

## Technologies Used

- **Python 3.14**
- **Requests** – For making HTTP requests.
- **python-dotenv** – For loading environment variables.
- **WeatherAPI** – As the weather data provider.

## Project Structure

```text
weather-api-python/
│
├── main.py
├── weather.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

> Note: The `.env` file is excluded from version control and should never be uploaded to GitHub.

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/hamzawyNerd/weather-api-python.git
cd weather-api-python
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your API key

Get an API key from [WeatherAPI](https://www.weatherapi.com/).

Create a `.env` file in the project root directory and add:

```env
WEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

### 6. Run the application

```bash
python main.py
```

## Example Output

```text
Weather Summary
City: Kafr El Sheikh
Temperature: 20.8
Condition: Clear
Humidity: 53
```

*Weather values may vary depending on current conditions.*

## What I Learned

This project helped me practice fundamental Python development concepts:

- Working with REST APIs and HTTP requests.
- Understanding and parsing JSON data.
- Applying OOP principles using Python classes.
- Managing dependencies with virtual environments.
- Handling environment variables and protecting sensitive credentials.
- Implementing basic error handling.

---

**Author:** Mahmoud Hamza Abdella

**GitHub:** [hamzawyNerd](https://github.com/hamzawyNerd)
