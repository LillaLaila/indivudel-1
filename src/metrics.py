import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

class HealthAnalyser:
    """
    Class that calculating statistic of:
    average blood pressure, 
    average percentage of people with disease, 
    percentage of smokers and non-smokers
    """
    def __init__ (self, df):
        self.df = df

    def mean_bp (self):
        return self.df['systolic_bp'].mean()
    
    def disease_percent (self):
        return (self.df['disease'].mean() * 100)
    
    def smokers_percent (self):
        return (self.df['smoker'].value_counts(normalize=True) * 100)


def counting_analys (df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate average, median, max, min for:
    age, weight, height, blood pressure, cholesterol
    """
    column=["age", "weight", "height", "systolic_bp", "cholesterol"]
    return pd.DataFrame ({
        "Mean": df[column].mean(),
        "Median": df[column].median(),
        "Max": df[column].max(),
        "Min": df[column].min()
    }).round()



def smokers_nosmokers (df):
    """
    Calculate smokers and non-smokers in percentage
    """
    smoking_percent = df['smoker'].value_counts(normalize=True)*100 
    for yes_no, value in smoking_percent.items():
        print(f"{yes_no}: {value:.0f} %")
        print("---------")



def disease_prc (df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate people with and without disease in percentage
    """
    disease_percent = (df['disease'].value_counts(normalize = True)*100).round(2)
    return disease_percent.to_frame(name="Percentage of disease:")



def simulating_disease (df):
    """
    Calculate simulation of how many people might have the disease
    """
    np.random.seed(42)
    p = df['disease'].mean()
    simulate_disease = np.random.binomial(n = 1, p = p, size = 1000)
    # print(simulate_disease)
    result = simulate_disease.mean()*100
    print(f"Simulated disease mean: {result:.2f} %\n")
    return result



def ci_normal (df):
    """
    Calculate Confidence Interval (95%) for blood pressure
    """
    bp = df['systolic_bp']
    bp_mean = bp.mean()
    bp_standard_deviation = bp.std(ddof=1)
    bp_length = len(bp)
    z = 1.96 # 95%
    half_width = z*bp_standard_deviation / np.sqrt(bp_length)

    low = bp_mean - half_width
    high = bp_mean + half_width

    print(f"The mean blood pressure is: {bp_mean:.2f} mmHg.")
    print(f"The 95% confidence interval is: {low:.2f}, {high:.2f}.")
    return low, high


def regression_age_bp(df):
    """
    Calculate linear regression to predict blood pressure from age and weight
    """
    x = df[['age', 'weight']]
    y = df['systolic_bp']

    model = LinearRegression()
    model.fit(x, y)

    print(f"Slope for age: {model.coef_[0]:.2f}")
    print(f"Slope for weight: {model.coef_[1]:.2f}")

    print(f"Intercept: {model.intercept_:.2f}")

    return model