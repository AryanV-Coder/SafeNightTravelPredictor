# 🌙🛡️ Safe Night Travel Predictor

Ever wondered if it's safe to travel at night based on your circumstances? This machine learning project helps predict night travel safety using various factors like transportation mode, location familiarity, and personal characteristics.

## 🎯 What Does This Project Do?

This project uses **logistic regression** to predict whether night travel is safe based on real-world factors. Instead of relying on gut feelings, it analyzes patterns from data to make informed predictions about travel safety.

## 🔍 The Story Behind This Project

Night travel safety is a genuine concern for many people. Rather than making decisions based on fear or assumptions, I wanted to create a data-driven approach to understand what factors actually contribute to safer night travel experiences. 

The model considers factors like:
- **Time of travel** (how late is it?)
- **Gender** and personal demographics
- **Transportation mode** (walking, 2-wheeler, 4-wheeler, auto)
- **Companion presence** (traveling alone vs. with others)
- **Location familiarity** (known vs. unknown areas)
- **Phone battery level** (emergency preparedness)
- **Previous incident history** in the area

## 📊 Dataset Overview

The project uses a dataset of **200 night travel experiences** with the following features:

| Feature | Description | Values |
|---------|-------------|---------|
| `Time` | Hour of travel (0-24) | Numerical |
| `Gender` | Traveler's gender | F, M, Other |
| `LocationFamiliarity` | Familiar with the area? | yes, no |
| `ModeOfTransport` | How are you traveling? | walk, 2-wheeler, 4-wheeler, auto |
| `PresenceOfCompanions` | Traveling with others? | yes, no |
| `PhoneBatteryLevel` | Battery percentage (0-100) | Numerical |
| `PreviousIncidentArea` | Any incidents reported in this area? | yes, no |
| `SafeToTravel` | **Target**: Is it safe to travel? | yes, no |

## 🧠 Model Performance & Insights

### Performance Metrics
- **Accuracy**: 65% (not perfect, but better than random guessing!)
- **Precision for Safe Travel**: 73%
- **Recall for Safe Travel**: 73%

### Key Discoveries 🔍

The model revealed some interesting patterns:

1. **Having Companions is Key** 🤝  
   The strongest predictor of safety! Traveling with others significantly increases perceived safety.

2. **Transportation Mode Matters** 🚗  
   - 4-wheelers feel safest
   - Walking feels less safe (especially alone)
   - 2-wheelers and autos fall in between

3. **Gender Differences** 👥  
   - Females report feeling safer than males in this dataset
   - This might reflect different travel patterns or risk assessment approaches

4. **Location Familiarity** 📍  
   Knowing the area does help, but it's not as crucial as having companions

5. **Phone Battery & Time** 🔋⏰  
   Surprisingly, these have minimal impact on safety perception

### Important Note ⚠️
This model predicts **perceived safety** based on the training data patterns, not actual crime statistics. Results should be used as one factor among many when making travel decisions.

## 🛠️ Technical Details

### Tech Stack
- **Language**: Python 3.13
- **ML Library**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Web Interface**: Streamlit (planned)

### Model Architecture
- **Algorithm**: Logistic Regression with L2 regularization
- **Feature Encoding**: 
  - Binary features → 0/1 mapping
  - Categorical features → One-hot encoding
- **Train/Test Split**: 80/20 with stratification
- **Cross-validation**: Planned for future versions

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AryanV-Coder/SafeNightTravelPredictor.git
   cd SafeNightTravelPredictor
   ```

2. **Set up virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Explore the model training**
   ```bash
   jupyter notebook model_training/model.ipynb
   ```

5. **Run the web app** (coming soon!)
   ```bash
   streamlit run main.py
   ```

## 📁 Project Structure

```
SafeNightTravelPredictor/
├── README.md                          # You're here! 👋
├── main.py                            # Streamlit web app (in development)
├── requirements.txt                   # Python dependencies
├── model_training/
│   ├── model.ipynb                    # Complete model development notebook
│   ├── safe_night_travel_dummy_data.csv  # Training dataset
│   └── models/                        # Saved models (coming soon)
└── venv/                              # Virtual environment
```

## 🎨 Features in Development

- [ ] **Interactive Web Interface**: Upload your travel details and get safety predictions
- [ ] **Model Persistence**: Save and load trained models
- [ ] **Better Visualizations**: Interactive charts and insights
- [ ] **Real-time Predictions**: API endpoint for mobile apps
- [ ] **Enhanced Dataset**: More diverse and larger training data

## 🤔 Limitations & Future Work

### Current Limitations
- Small dataset (200 records) - more data needed for better accuracy
- Based on subjective safety perception, not objective crime data
- May not generalize across different geographical regions
- Doesn't account for real-time factors (weather, events, etc.)

### Future Improvements
- Integrate real crime statistics and demographic data
- Add weather and seasonal factors
- Implement ensemble methods (Random Forest, XGBoost)
- Develop mobile-friendly interface
- Add confidence intervals for predictions

## 🤝 Contributing

This project is a learning exercise, but contributions are welcome! Here's how you can help:

1. **Data Collection**: Help gather more diverse, real-world data
2. **Feature Engineering**: Suggest new relevant features
3. **Model Improvement**: Try different algorithms or hyperparameters
4. **UI/UX**: Improve the web interface
5. **Documentation**: Help make the code more accessible

## 📈 What I Learned

Building this project taught me:
- Real-world data is messy and requires careful preprocessing
- Feature encoding significantly impacts model performance
- Domain knowledge is crucial for interpreting ML results
- The importance of understanding model limitations
- How to balance technical complexity with practical usability

## 📜 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## 🙏 Acknowledgments

- Inspired by the need for data-driven personal safety decisions
- Thanks to the open-source ML community for excellent tools
- Grateful for feedback from friends and family who tested early versions

---

**Remember**: This tool is meant to supplement, not replace, common sense and local knowledge about travel safety. Stay safe out there! 🌙✨

---

*Built with ❤️ by [Aryan Varshney](https://github.com/AryanV-Coder)*
