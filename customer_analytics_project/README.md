
# Customer Credit Risk Analysis

This project analyzes the German Credit dataset to understand customer behavior and credit risk. It involves comprehensive data preprocessing, exploratory data analysis (EDA), and visualization to reveal insights into creditworthiness and related patterns.

---

## 📁 Project Structure

```text
.
├── data/                       # Raw and cleaned datasets, data-related scripts
│   ├── german.data
│   ├── german.csv
│   ├── german_cleaned.csv
│   └── data.py
├── notebooks/                 # Jupyter notebooks for data cleaning and feature mappings
│   ├── data_cleaning.ipynb
│   ├── mappings.ipynb
│   ├── data_cleaning.py
│   └── mappings.py
├── reports/
│   ├── graphs/                # Scripts and notebooks for graph generation
│   │   ├── graphs.ipynb
│   │   └── graphs.py
│   └── images/                # Visualizations generated during EDA
│       ├── correlation_heatmap.png
│       ├── credit_amount_distribution.png
│       └── ...
├── generate_all_graphs.py     # Script to generate all graphs in batch
├── requirements.txt           # Project dependencies
├── README.md                  # Project overview and documentation
└── customer_analytics_project.iml  # IDE project config
```

---

## 📊 Project Objectives

- Clean and preprocess the German Credit dataset
- Perform exploratory data analysis (EDA)
- Visualize relationships between features and target variable
- Identify patterns in credit approval decisions
- Gain insight into customer profiles and credit risk factors

---

## 📈 Key Visualizations

Some of the generated plots include:

- **Target Variable Distribution**
- **Credit Amount Distribution**
- **Correlation Heatmap**
- **Duration vs Credit Amount**
- **Purpose vs Target**
- **Employment Status Analysis**
- **Violinplots of Numeric Features**

All visuals are stored under `reports/images/`.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <project-directory>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

To run the entire analysis pipeline and generate all visuals:
```bash
python generate_all_graphs.py
```

To explore the analysis in detail, open the Jupyter notebooks in the `notebooks/` and `reports/graphs/` directories.

---

## 📚 Dataset Information

The dataset used is the [German Credit Data](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) from the UCI Machine Learning Repository, containing information on 1000 customers with 20 features each.

---

## 📌 Author

Developed by **Yağız Efe Özdemir**  
Email: [ozdemir.yefe1@gmail.com](mailto:ozdemir.yefe1@gmail.com)  
GitHub: [https://github.com/YagizEfeOzdemir](https://github.com/YagizEfeOzdemir)
