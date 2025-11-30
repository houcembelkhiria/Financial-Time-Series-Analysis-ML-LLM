# 📊 Advanced Financial Time Series Analysis with ML & LLM

[![R](https://img.shields.io/badge/R-4.x-blue.svg)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-3.x-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)]()

> **End-to-end financial forecasting system combining classical econometrics, deep learning, and generative AI**

A comprehensive time series analysis project comparing ARIMA, GARCH, LSTM, and VAR models for financial forecasting, with integrated LLM-powered analysis using Flan-T5-Large.

---

## 🎯 Project Highlights

- **7 Econometric & ML Models**: ARIMA, SARIMA, GARCH, EGARCH, LSTM, GRU, VAR
- **LLM Integration**: Flan-T5-Large (780M parameters) for automated financial analysis
- **Hybrid Architecture**: R + Python + Transformers seamless integration
- **Real Financial Data**: Apple (AAPL) & Bitcoin (BTC) analysis (2020-2022)
- **Production-Ready**: Robust error handling, fallback mechanisms, comprehensive testing

---

## 📈 Key Results

| Asset | Best Model | RMSE | Improvement vs Baseline |
|-------|-----------|------|------------------------|
| **AAPL** | LSTM | 0.0198 | **+7.9%** vs ARIMA |
| **BTC** | LSTM | 0.0461 | **+11.9%** vs ARIMA |

**Key Finding**: Deep learning models (LSTM) significantly outperform classical approaches, especially for high-volatility assets (+11.9% improvement for Bitcoin).

---

## 🛠️ Tech Stack

### Core Technologies
- **R**: Statistical modeling, time series analysis
- **Python**: Deep learning, NLP, LLM integration
- **Jupyter Notebook**: Interactive analysis and visualization

### Key Libraries

**R Ecosystem**:
```r
tidyverse, forecast, rugarch, vars, tseries, ggplot2, keras, reticulate, jsonlite
```

**Python Ecosystem**:
```python
transformers, torch, pandas, numpy, scikit-learn, matplotlib
```

### AI/ML Models
- **Classical**: ARIMA/SARIMA, GARCH/EGARCH
- **Deep Learning**: LSTM, GRU (Keras/TensorFlow)
- **Multivariate**: VAR (Vector Autoregression)
- **Generative AI**: Flan-T5-Large (Google, 780M parameters)

---

## 🚀 Features

### 1. Comprehensive Time Series Analysis
- ✅ Stationarity testing (ADF, KPSS)
- ✅ ACF/PACF analysis
- ✅ STL decomposition (Trend, Seasonality, Residuals)
- ✅ Volatility clustering detection (ARCH test)

### 2. Classical Econometric Models
- **ARIMA/SARIMA**: Optimal for trend and seasonality
- **GARCH/EGARCH**: Volatility modeling with asymmetric effects
- **ARIMAX**: Exogenous variables integration (macro indicators)

### 3. Advanced Machine Learning
- **LSTM Networks**: Non-linear pattern recognition
- **Architecture**: 2-layer LSTM with dropout regularization
- **Optimization**: Adam optimizer, early stopping, batch normalization

### 4. Multivariate Analysis
- **VAR Models**: Cross-asset interdependencies
- **Granger Causality Tests**: Directional influence detection
- **Impulse Response Functions**: Shock transmission analysis

### 5. Generative AI Integration 🤖
- **Model**: Flan-T5-Large (Google, 780M parameters)
- **Tasks**: 
  - Automated hypothesis generation
  - Technical result vulgarization
  - Investment recommendation synthesis
- **Architecture**: Hybrid LLM + Expert validation system
- **Prompts**: Fine-tuned for financial analysis

### 6. Extensions
- **FinBERT Embeddings**: Event sentiment analysis
- **DCC-GARCH**: Dynamic conditional correlation
- **Rolling Analysis**: Time-varying model performance

---

## 📊 Project Structure

```
Financial-Time-Series-Analysis-ML-LLM/
│
├── Mini_Projet_Complet.ipynb          # Main analysis notebook (124 cells)
├── llm_api.py                          # Flan-T5-Large integration script
│
├── AAPL.csv                            # Apple stock prices (2020-2022)
├── BTC-USD.csv                         # Bitcoin prices (2020-2022)
├── macro_indicators.csv                # Macroeconomic variables
├── news_events.csv                     # Financial news events
│
├── docs/
│   ├── Rapport_Analyse_Series_Temporelles.docx  # Full report (20+ pages)
│   └── GUIDE_UTILISATION.md            # User guide
│
├── README.md                           # This file
├── LICENSE                             # MIT License
└── .gitignore                          # Git ignore rules
```

---

## 🔬 Methodology

### 1. Data Pipeline
```
Raw Data → Cleaning → Stationarity Tests → Train/Test Split (80/20)
```

### 2. Modeling Workflow
```
EDA → Classical Models → Deep Learning → Multivariate → LLM Analysis → Comparison
```

### 3. Evaluation Metrics
- **RMSE**: Root Mean Squared Error
- **MAE**: Mean Absolute Error
- **MAPE**: Mean Absolute Percentage Error
- **Ljung-Box Test**: Residual autocorrelation
- **AIC/BIC**: Model selection criteria

---

## 💡 Key Insights

### 1. Model Selection by Asset Type

**For Stable Assets (AAPL)**:
- ✅ ARIMA/GARCH: Effective for trend and volatility
- ✅ LSTM: +7.9% improvement over ARIMA
- 📊 Best: Hybrid ARIMA-GARCH-LSTM approach

**For Volatile Assets (BTC)**:
- ⚠️ ARIMA: Limited effectiveness (high volatility)
- ✅ GARCH: Essential for volatility clustering
- ✅ LSTM: +11.9% improvement (captures non-linearity)
- 📊 Best: LSTM + GARCH for volatility

### 2. Cross-Asset Analysis (VAR)
- **Weak interdependence** between AAPL and BTC (p > 0.05)
- **Diversification benefit**: Low correlation confirms portfolio separation
- **Shock transmission**: Limited contagion effects detected

### 3. LLM for Financial Analysis
- **Strengths**: Fast hypothesis generation, accessible vulgarization
- **Limitations**: Requires expert validation, concise outputs
- **Solution**: Hybrid architecture (LLM + Expert) ensures quality

---

## 📚 Scientific Rigor

### Statistical Tests Performed
- ✅ Augmented Dickey-Fuller (ADF) test
- ✅ ARCH/GARCH effects test
- ✅ Ljung-Box autocorrelation test
- ✅ Jarque-Bera normality test
- ✅ Granger causality test

### Model Diagnostics
- ✅ Residual analysis (ACF/PACF)
- ✅ Heteroskedasticity tests
- ✅ Out-of-sample validation
- ✅ Walk-forward analysis
- ✅ Stability tests (VAR roots)

---

## 🎓 Skills Demonstrated

### Data Science & ML
- Time series forecasting
- Deep learning (LSTM, GRU)
- Model selection & hyperparameter tuning
- Cross-validation strategies
- Performance optimization

### Financial Analysis
- Econometric modeling (ARIMA, GARCH, VAR)
- Volatility modeling
- Risk assessment (VaR implications)
- Portfolio diversification analysis

### Software Engineering
- R-Python integration (reticulate)
- API design (LLM wrapper)
- Error handling & fallback mechanisms
- Reproducible research (notebooks)
- Documentation

### AI/NLP
- LLM integration (Transformers)
- Prompt engineering for finance
- Hybrid AI systems
- Text generation for business use

---

## 🚀 Getting Started

### Prerequisites

**R Packages**:
```r
install.packages(c(
  "tidyverse", "forecast", "rugarch", "vars", 
  "tseries", "ggplot2", "keras", "reticulate", 
  "jsonlite", "readr", "lubridate", "zoo", "moments"
))
```

**Python Packages**:
```bash
pip install transformers torch pandas numpy scikit-learn matplotlib
```

### Quick Start

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/Financial-Time-Series-Analysis-ML-LLM.git
cd Financial-Time-Series-Analysis-ML-LLM
```

2. **Open the notebook**:
```bash
jupyter notebook Mini_Projet_Complet.ipynb
```

3. **Run cells sequentially** (1-124)
   - Total execution time: ~15-20 minutes (without LSTM retraining)

### With LLM (Optional)

For Flan-T5-Large integration:
```bash
pip install transformers torch

# First run downloads ~3 GB model (5-10 min)
# Subsequent runs: instant
```

---

## 📊 Visualizations

The project includes comprehensive visualizations:
- 📈 Price evolution & returns distribution
- 📊 ACF/PACF correlograms
- 🔥 Volatility clustering heatmaps
- 🎯 Model predictions vs actuals
- 📉 Residual diagnostics
- 🌐 Impulse response functions (VAR)
- 🔗 Dynamic correlation matrices (DCC-GARCH)

---

## 🏆 Results & Performance

### Quantitative Performance

| Model | AAPL RMSE | BTC RMSE | Speed (ms) | Interpretability |
|-------|-----------|----------|------------|------------------|
| ARIMA | 0.0215 | 0.0523 | 45 | ⭐⭐⭐⭐⭐ |
| GARCH | 0.0208 | 0.0498 | 120 | ⭐⭐⭐⭐ |
| **LSTM** | **0.0198** | **0.0461** | 1250 | ⭐⭐ |
| VAR | 0.0205 | 0.0485 | 180 | ⭐⭐⭐⭐ |

### Trade-offs
- **LSTM**: Best accuracy, slower (acceptable for daily forecasts)
- **ARIMA/GARCH**: Fast, interpretable, good for stable assets
- **VAR**: Unique for multi-asset analysis

---

## 📝 Academic Report

A comprehensive 20+ page report is included covering:
- **Introduction**: Problem statement & objectives
- **Methodology**: Detailed model descriptions (ARIMA, GARCH, LSTM, VAR)
- **Results**: Statistical analysis & visualizations
- **LLM Integration**: Architecture & evaluation (Flan-T5-Large)
- **Critical Discussion**: Limitations, advantages/disadvantages
- **Conclusion**: Key findings & future work
- **Annexes**: Code references, bibliography

📄 Available in `docs/Rapport_Analyse_Series_Temporelles.docx`

---

## 🔮 Future Enhancements

- [ ] Real-time data streaming integration
- [ ] Ensemble methods (stacking multiple models)
- [ ] Transformer models (Attention mechanisms)
- [ ] High-frequency data analysis (intraday)
- [ ] More asset classes (commodities, FX, bonds)
- [ ] Automated trading strategy backtesting
- [ ] Web dashboard (Streamlit/Dash)
- [ ] Fine-tune Flan-T5 on financial corpus

---

## 🤝 Contributing

This project was developed as part of a Data Science Master's program at TEK-UP University. Suggestions and improvements are welcome!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Additional asset classes
- Alternative model architectures
- Performance optimizations
- Visualization enhancements
- Documentation improvements

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Data Science Student @ TEK-UP University**

Master's in Data Science | Financial AI Enthusiast

- 💼 LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- 📧 Email: your.email@example.com
- 🌐 Portfolio: [yourwebsite.com](https://yourwebsite.com)

---

## 🙏 Acknowledgments

- **Supervisor**: Prof. Ahmed Dhouibi (TEK-UP University)
- **Data Sources**: Yahoo Finance, compiled macro indicators
- **Models**: Google (Flan-T5-Large), Keras/TensorFlow
- **Inspiration**: State-of-the-art financial econometrics research

---

## 📖 References

1. Box, G. E. P., & Jenkins, G. M. (1970). *Time Series Analysis: Forecasting and Control*
2. Bollerslev, T. (1986). *Generalized autoregressive conditional heteroskedasticity*
3. Hochreiter, S., & Schmidhuber, J. (1997). *Long short-term memory*
4. Sims, C. A. (1980). *Macroeconomics and reality. Econometrica*
5. Chung, J., et al. (2023). *Scaling Instruction-Finetuned Language Models (Flan-T5)*

---

## 📊 Project Stats

![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-5000%2B-blue)
![Models](https://img.shields.io/badge/Models-7-green)
![Best RMSE](https://img.shields.io/badge/Best%20RMSE-0.0198-brightgreen)
![Duration](https://img.shields.io/badge/Project%20Duration-3%20months-orange)

---

<div align="center">

### ⭐ Star this repo if you find it useful!

**Made with ❤️ for Financial Data Science**

[Report Bug](https://github.com/yourusername/Financial-Time-Series-Analysis-ML-LLM/issues) · [Request Feature](https://github.com/yourusername/Financial-Time-Series-Analysis-ML-LLM/issues)

</div>

