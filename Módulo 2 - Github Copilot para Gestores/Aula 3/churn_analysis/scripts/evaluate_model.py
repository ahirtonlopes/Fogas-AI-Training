import pandas as pd
import joblib
from sklearn.metrics import classification_report

def load_data(filepath):
    """Carrega os dados do arquivo."""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Pré-processa os dados."""
    df = df.dropna()
    X = df.drop("Churn", axis=1).drop("CustomerID", axis=1)
    y = df["Churn"]
    return X, y

def evaluate_model(model, X_test, y_test):
    """Avalia o modelo com base nos dados de teste."""
    predictions = model.predict(X_test)
    print("Relatório de Classificação:")
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    # Carrega os dados e o modelo treinado
    data = load_data("data/churn_data.csv")
    model = joblib.load("models/model.pkl")
    
    # Pré-processa os dados
    X, y = preprocess_data(data)
    
    # Divide os dados em treino e teste
    from sklearn.model_selection import train_test_split
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Avalia o modelo
    evaluate_model(model, X_test, y_test)
