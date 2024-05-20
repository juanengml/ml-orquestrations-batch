import random
from plombery import get_logger

# Função de ativação (linear)
def activation_function(x):
    return x

# Função de predição
def predict(inputs, weights, bias):
    summation = sum(weight * inp for weight, inp in zip(weights, inputs)) + bias
    return activation_function(summation)

# Função de treino
def train(training_data, weights, bias, learning_rate, epochs):
    for _ in range(epochs):
        for inputs, target in training_data:
            prediction = predict(inputs, weights, bias)
            error = target - prediction
            
            # Atualização dos pesos e bias
            for i in range(len(weights)):
                weights[i] += learning_rate * error * inputs[i]
            bias += learning_rate * error
    return weights, bias

# Gerar dados de treinamento sintéticos
def generate_training_data(num_samples, num_features):
    training_data = []
    for _ in range(num_samples):
        inputs = [random.uniform(0, 1) for _ in range(num_features)]
        target = 1 if sum(inputs) > (num_features / 2) else 0  # Simples regra para classificação
        training_data.append((inputs, target))
    return training_data

def runner():
    # Parâmetros
    num_samples = 1000  # Número de amostras
    num_features = 100  # Número de características (inputs)

    # Gerar dados de treinamento
    training_data = generate_training_data(num_samples, num_features)

    # Inicialização dos pesos e bias
    weights = [random.uniform(-1, 1) for _ in range(num_features)]
    bias = random.uniform(-1, 1)

    # Parâmetros de treinamento
    learning_rate = 0.001
    epochs = 100

    # Treinamento do modelo
    weights, bias = train(training_data, weights, bias, learning_rate, epochs)
    
    inference = list()
    # Testando o modelo treinado
    logger = get_logger()
    for i in range(100):  # Testar nas primeiras 10 amostras para ver os resultados
        inputs, target = training_data[i]
        prediction = predict(inputs, weights, bias)
        inference.append({"Entrada": inputs, "Previsão": f"{prediction:.2f}", "Esperado":target})
        logger.debug({"Entrada": inputs, "Previsão": f"{prediction:.2f}", "Esperado":target})
    return inference    
