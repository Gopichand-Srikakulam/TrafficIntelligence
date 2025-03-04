# Traffic Volume Estimation Using Machine Learning

## Project Overview
This project is a **Traffic Volume Estimation System** built using **Machine Learning (RandomForestRegressor)** and deployed with **Flask**. The system predicts traffic volume based on various input features such as weather conditions, time, and date.

## Features
- **User Input Interface**: Web interface to input parameters.
- **Machine Learning Model**: Predicts traffic volume using a trained **RandomForestRegressor**.
- **Flask Backend**: Handles input, processes data, and serves predictions.
- **Web-based Visualization**: Displays estimated traffic volume on an interactive webpage.
- **Static Assets Handling**: Includes background images and UI styling.

## Project Structure
```
/ml-project/
├── static/                # Contains static files like images
│   ├── ferrari.png        # Background image for UI
├── templates/             # HTML templates for Flask
│   ├── index.html         # Main input page
│   ├── output.html        # Result display page
├── model.pkl              # Pre-trained machine learning model
├── encoder.pkl            # Data scaler/encoder
├── app.py                 # Flask application
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
```

## Installation & Setup
### Prerequisites
- Python 3.x
- Flask
- Scikit-learn
- Pandas, NumPy

### Steps to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/traffic-volume-estimation.git
   cd traffic-volume-estimation
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```sh
   python app.py
   ```
4. Open in the browser:
   ```
   http://127.0.0.1:5000
   ```

## Model Download Link
The trained **RandomForestRegressor** model is stored on Google Drive. You can download it from the link below:
[Download Model from Google Drive](https://drive.google.com/file/d/13m8YpMX0pXRMB9BpEjKoP0Kap6AB2LZa/view)

After downloading, place `model.pkl` and `encoder.pkl` in the project directory.

## Usage
1. Enter required input values on the web interface.
2. Click the **Predict** button.
3. View estimated traffic volume on the results page.

## Troubleshooting
- If the background image is not loading, ensure `ferrari.png` is inside the `static/` folder and referenced correctly in `output.html`.
- If Flask cannot find templates, ensure `index.html` and `output.html` are inside the `templates/` directory.
- If model-related errors occur, ensure `model.pkl` and `encoder.pkl` are properly downloaded and placed in the project root.

## Future Improvements
- Improve UI with more interactive charts.
- Deploy on cloud services (AWS, Heroku, etc.).
- Enhance model accuracy with more feature engineering.
