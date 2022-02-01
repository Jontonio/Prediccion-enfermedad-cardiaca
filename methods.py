import joblib as jb



def prediction(tipo, data):
    
    if tipo == 'kmeans':
        rm = jb.load('models/kmeans_enfermedadCardiaca.pkl')
        result = rm.predict(data)
        return "Algoritmo kmeans predice que " + resultToString(result[0])
    elif tipo == 'knn':
        knn = jb.load('models/knn_enfermedadCardiaca.pkl')
        result = knn.predict(data)
        return "Algoritmo knn predice que " + resultToString(result[0])
    elif tipo == 'rl':
        rl = jb.load('models/rl_enfermedadCardiaca.pkl')
        result = rl.predict(data)
        return "Algoritmo regresión lineal predice que " + resultToString(result[0])
    elif tipo == 'rm':
        rm = jb.load('models/rm_enfermedadCardiaca.pkl')
        result = rm.predict(data)
        return "Algoritmo Random Forest predice que " + resultToString(result[0])
    elif tipo == 'svc':
        svc = jb.load('models/svc_enfermedadCardiaca.pkl')
        result = svc.predict(data)
        return "Algoritmo Maquina de vectores predice que " + resultToString(result[0]) 
        

def resultToString(res):
    if res == 0:
        return "No tiene enfermedad cardíaca"
    else: 
        return "Tiene enfermedad cardíaca"