import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Polaris')


st.text('Bonjour <user>, vous avez <X> nouvelles alertes depuis le <DD-MM-YYYY>')

st.write('Statistiques du domaine métier :')

# Générer un DataFrame aléatoire avec des scénarios
np.random.seed(42)  # Fixer la graine pour la reproductibilité
scenarios = ['1.1.1', '1.1.2', '1.2.1']
n_dossiers = np.random.randint(50, 200, size=len(scenarios))  # Nombre aléatoire de dossiers par scénario

# Créer le DataFrame
df = pd.DataFrame({
    'Scénario': scenarios,
    'Nombre de dossiers': n_dossiers
})

plt.figure(figsize=(8, 6))
sns.barplot(x='Scénario', y='Nombre de dossiers', data=df, hue='Scénario', dodge=False, palette='Blues_d', legend=False)

# Ajouter des labels et un titre
plt.title("Nombre de Dossiers par Scénario", fontsize=15)
plt.xlabel("Scénarios", fontsize=12)
plt.ylabel("Nombre de Dossiers", fontsize=12)

# Afficher le plot dans Streamlit
st.pyplot(plt)