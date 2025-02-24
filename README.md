# **Weather App (Django)**  

This is a **Django-based weather comparison app** that allows users to enter two cities and compare their weather conditions. The app fetches real-time weather data using the **OpenWeatherMap API** and displays current temperature, weather conditions, and a **5-day forecast** for both cities.  

---

## **Features**  
✅ Search and compare weather between two cities  
✅ Display **current temperature, weather description, and icons**  
✅ Show **5-day weather forecast** with **min/max temperatures**  
✅ User-friendly interface with a simple input form  
✅ Uses Django **template inheritance** for better code organization  

---

## **Tech Stack**  
🔹 **Backend:** Django (Python)  
🔹 **Frontend:** HTML, CSS (Bootstrap for styling)  
🔹 **API:** OpenWeatherMap API (for real-time weather data)  
🔹 **Database:** SQLite (default Django database)  

---

## **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/prakhar051/weather_app_django.git
cd weather_app_django

2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Get OpenWeatherMap API Key
1. Sign up on OpenWeatherMap
2. Copy your API key
3. Save it inside a file in the project folder:
echo "your_api_key_here" > API_key

5️⃣ Run Migrations (For Database Setup)
python manage.py migrate

6️⃣ Start the Django Server
python manage.py runserver
