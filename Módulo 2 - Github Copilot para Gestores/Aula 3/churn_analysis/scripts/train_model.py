import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def load_data(filepath):
    """Carrega os dados do arquivo."""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Pré-processa os dados."""
    df = df.dropna()
    X = df.drop("Churn", axis=1).drop("CustomerID", axis=1)
    y = df["Churn"]
    return X, y

def train_model(X_train, y_train):
    """Treina o modelo RandomForest."""
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, filepath):
    """Salva o modelo treinado."""
    joblib.dump(model, filepath)

if __name__ == "__main__":
    # Carrega os dados
    data = load_data("data/churn_data.csv")
    
    # Pré-processa os dados
    X, y = preprocess_data(data)
    
    # Divide os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Treina o modelo
    model = train_model(X_train, y_train)
    
    # Avalia o modelo
    predictions = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")
    
    # Salva o modelo
    save_model(model, "models/model.pkl")

