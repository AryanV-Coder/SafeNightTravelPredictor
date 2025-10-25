# 🇮🇳 Safe Travels for a Stronger India: The Night Travel Safety Predictor

[Live demo › https://safenighttravelpredictor.streamlit.app/]

In a nation that never sleeps, ensuring the safety of every citizen is a matter of pride. This project is a tribute to the spirit of a fearless, progressive India, where technology empowers us to make smarter, safer decisions. 

The **Safe Night Travel Predictor** is a machine learning tool that provides a data-driven assessment of travel safety at night, helping our fellow Indians navigate their journeys with greater confidence.

## 🎯 Project Goal

To use logistic regression to predict whether night travel is safe based on key real-world factors. This model analyzes patterns from data to provide a calculated safety assessment, moving beyond gut feelings to informed predictions.

## ✨ Key Features Analyzed

Our model considers factors that matter most on the ground:
- **Time of Travel**: How late is it?
- **Transportation Mode**: Are you walking, or in a 2-wheeler, 4-wheeler, or auto?
- **Companions**: Are you traveling alone or with others?
- **Location Familiarity**: Do you know the area?
- **Personal Demographics**: Factors like gender.
- **Preparedness**: Phone battery level and incident history in the area.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- A virtual environment (recommended for a clean setup)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AryanV-Coder/SafeNightTravelPredictor.git
   cd SafeNightTravelPredictor
   ```

2. **Set up your virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Explore the model and its training:**
   ```bash
   jupyter notebook model_training/model.ipynb
   ```

5. **Run the Web App** (Coming Soon!):
   ```bash
   streamlit run main.py
   ```

## 🛠️  Technical Snapshot

- **Language**: Python
- **Core Libraries**: `scikit-learn`, `pandas`, `numpy`
- **Algorithm**: Logistic Regression with L2 Regularization
- **Feature Encoding**: One-Hot and Ordinal Encoding for categorical data.

## 💡 The Vision Ahead

- **Interactive Web Interface**: An easy-to-use Streamlit app where anyone can input their travel details and get an instant safety prediction.
- **Model Persistence**: Saving and loading trained models for efficiency.
- **API Endpoint**: A future goal to allow integration with other applications.

## 🤝 Contribute to a Safer India

This is more than just a project; it's a step towards a safer nation. Contributions are welcome!
- **Data**: Help us gather more diverse data.
- **Modeling**: Experiment with different algorithms.
- **Development**: Help build the web interface.

## 📜 License

This project is proudly open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

*Built with ❤️ and a vision for a safer India by [Aryan Varshney](https://github.com/AryanV-Coder)*
