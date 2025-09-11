def mqf (x,y,model):
    liste = []

    for i in range(0, len(x)):
        y_i = y[i]
        f_x_i = model(x[i])
        liste.append((f_x_i - y_i)**2)

    mqf = sum(l for l in liste)/ len(x)
    return mqf