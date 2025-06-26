# 🏠 Indian House Price Predictor

Welcome to the **Indian House Price Predictor**!  
This interactive app uses machine learning to estimate house prices across Indian cities based on your custom inputs. Whether you're a home-buyer, seller, or just curious, this tool provides quick and insightful price predictions.

---

## 🚀 Try It Yourself!

You can run the app locally with a simple command (see below) and interact with a beautiful Gradio web interface:

- 🌆 **Choose your City and Locality**  
- 📐 **Enter Area, Bedrooms, Age, and Location Score**  
- 📊 **Get instant price estimates and compare with local historical averages!**

![App Screenshot](demo_screenshot.png)

---

## 🛠️ How It Works

- **Input Features:** Area (sqft), Bedrooms, Age of Property (years), and Location Score (1-10)
- **Model:** Uses a trained Linear Regression model from scikit-learn
- **Data:** Based on real Indian house data (`indian_house_data.csv`)
- **Interface:** Built with [Gradio](https://gradio.app/) for instant interactivity

---

## ✨ Features

- **Dynamic Dropdowns:** Localities update based on your city selection
- **Live Predictions:** Get results with a single click
- **Comparison:** See both model estimate and historical average for the locality
- **User-friendly UI:** Clean and colorful interface

---

## 📦 Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/hardik0501/House_predit.git
    cd House_predit
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    <details>
    <summary>Click for dependencies</summary>

    - pandas  
    - scikit-learn  
    - gradio  
    </details>

3. **Run the App**
    ```bash
    python House_predictor.py
    ```

4. **Open in Browser**  
    The app will automatically open a link like `http://localhost:7860/`

---

## 🏗️ File Structure

- `House_predictor.py` – Main application code
- `indian_house_data.csv` – Dataset used for predictions
- `requirements.txt` – Python dependencies
- `README.md` – You're here!

---

## 💡 Example Usage

1. Select your **City** (e.g., Delhi)
2. Pick a **Locality**
3. Enter **Area** (e.g., 1200 sqft), **Bedrooms** (e.g., 3), **Age** (e.g., 10 years)
4. Adjust the **Location Score**
5. Click "**Predict Price**" and view the results instantly!

---

## 📈 Screenshot

![Demo Screenshot](demo_screenshot.png)

---

## 🤝 Contribute

- Pull requests are welcome!  
- For issues or feature requests, please open a GitHub issue.

---

## ⚡ Credits

- Developed by [@hardik0501](https://github.com/hardik0501)
- Powered by [Gradio](https://gradio.app/) and [scikit-learn](https://scikit-learn.org/)

---

> **Disclaimer:** This tool is for educational/demo purposes. Predictions are based on sample data and may not represent actual market prices.

---
