import os
import streamlit as st
import pandas as pd 

# import des données 
df = pd.read_csv('./data.csv',usecols=['type', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig'],nrows=10)
# Ajouter deux colonnes vides au DataFrame
df['Commentaire'] = ""
df['Commentaire2'] = ""

def get_df():
    return df.copy()

# Filtrage par colonne
filtre = st.sidebar.multiselect('Type', options=df['type'].unique(), default=df['type'].unique())
# Obtenir le DataFrame avec les commentaires
df = get_df()

st.sidebar.title("Informations générales")
client_id = st.sidebar.selectbox("Numéro sociétaire", df['nameOrig'])
client_info = df[df['nameOrig'] == client_id].iloc[0]
st.sidebar.write(f"Numéro de contrat: {client_info['oldbalanceOrg']}")
st.sidebar.write(f"Revenus du client: {client_info['newbalanceOrig']}")
st.sidebar.write(f"Risque du client:")

# Fonction pour mettre à jour le DataFrame
def update_dataframe(index, comment):
    df.at[index, 'Commentaire'] = comment

df_filtre = df[df['type'].isin(filtre)]
data_placeholder = st.empty()
data_placeholder.dataframe(df_filtre, height=600, width=None)

# Sélection de l'index
selected_index = st.selectbox("Sélectionnez un index pour ajouter un commentaire", df_filtre.index)

# Affichage du champ de commentaire si un index est sélectionné
if selected_index is not None:
    commentaire2 = st.text_input(f"Le modèle s'est-il trompé ? (Y/N)", value=df_filtre.at[selected_index, 'Commentaire2'])
    commentaire = st.text_area(f"Commentaire pour l'index {selected_index}", value=df_filtre.at[selected_index, 'Commentaire'])
    if st.button('Enregistrer les commentaires'):
        update_dataframe(selected_index, commentaire)
        st.success("Commentaire mis à jour avec succès!")
        # Rafraîchir df_filtre après mise à jour du commentaire
        df_filtre = df[(df['type'].isin(filtre))]
        data_placeholder.dataframe(df_filtre, height=600, width=None)