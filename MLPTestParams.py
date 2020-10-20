from ExpParams import ExpParams

activation_func = ['identity' , 'logistic' , 'tanh' , 'relu']
solver_func = ['adam' , 'sgd']
network_architecture = [(30,50,) , (10,10,10)]

MLPExperimentVars = { "activation": activation_func,  "hidden_layer_sizes": network_architecture , "solver": solver_func}