import pandas as pd
import matplotlib.pyplot as plt

# histogram över blodtryck
def blodtryck_hist(df):
    """
    Histogram of blood pressure
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df['systolic_bp'], bins=10)

    ax.set_xlabel("Blood pressure indicators (mmHg)")
    ax.set_ylabel("Number of people")
    ax.set_title("Histogram of blood pressure")
        
    plt.grid(axis = 'y')
    plt.show()
        

# boxplot över vikt per kön
def weight_by_gender(df):
    """
    Boxplot of weight by gender
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    df.boxplot(by='sex', column=['weight'], ax=ax)

    ax.set_xlabel("Gender (M/F)")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Boxplot of weight by gender")
    fig.suptitle("")

    plt.show()

# stapeldiagram över andelen rökare
def smokers_diagram(df):
    """
    Bar chart of smokers and non-smokers in percentage
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    smoking_percent = df['smoker'].value_counts(normalize=True).round(2)*100 
   
    smoking_percent.plot.bar(ax=ax)

    ax.set_xlabel("Smoking (Yes/No)")
    ax.set_ylabel("Percentage %")
    ax.set_title("Bar chart of smokers and non-smokers")

    plt.grid(axis = 'y')
    plt.show()


# del2 relationen mellan blodtryck och ålder
def relation_age_bp (df):
    """
    Scatterplot of relation between age and blood pressure
    """
    fig, ax = plt.subplots(figsize=(8,5))
    ax.scatter(x = df['age'], y = df['systolic_bp'])
    
    ax.set_xlabel("Age")
    ax.set_ylabel("Systolic blood pressure (mmHg)")
    ax.set_title("Scatterplot of relation between age and blood pressure")

    plt.grid(True)
    plt.show()
