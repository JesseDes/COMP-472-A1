from ExpParams import ExpParams

splitting_criterion = ["gini", "entropy"]
max_depth = [10,None]
min_sample_size = [0.1 , 0.5, 2,4,6,8,10]
min_impurity_dec = [0.0, 0.1, 0.25, 0.5]
weight_class = ["balanced", None]

treeParams = {'criterion': splitting_criterion, "max_depth" : max_depth, "min_samples_split": min_sample_size, "min_impurity_decrease":  min_impurity_dec, "class_weight" : weight_class}