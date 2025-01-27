from scripts.train_model import load_data, preprocess_data, train_model, save_model

def main():
    # Caminho para os dados
    data_path = "data/churn_data.csv"
    
    # Carrega os dados
    data = load_data(data_path)
    
    # Pré-processa os dados
    X, y = preprocess_data(data)
    
    # Treina o modelo
    model = train_model(X, y)
    
    # Salva o modelo
    save_model(model, "models/final_model.pkl")
    print("Modelo treinado e salvo com sucesso!")

if __name__ == "__main__":
    main()
