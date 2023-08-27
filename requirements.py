import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# modèles, évaluation des performances
# (En général, j'exécute simplement ces 2 modèles lorsque j'effectue une analyse d'apprentissage automatique avec des données structurées. La RF est particulièrement utile pour les tests.)
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from lightgbm.sklearn import LGBMClassifier
from lightgbm.sklearn import LGBMRegressor

# Analyse de corrélation, VIF : suppression de la multicolinéarité
from statsmodels.stats.outliers_influence import variance_inflation_factor

# KFold(CV), partial : optuna
from sklearn.model_selection import KFold
from functools import partial


# bibliothèque pour le réglage des hyper-paramètres
import optuna

