import streamlit as st

about_page = st.Page(
    page="views/home.py",
    title="Accueil",
    icon="📈",
    default=True,
)
interest_1_page = st.Page(
    page="views/first_scen.py",
    title="1.1.1",
    icon="📘",
)

interest_2_page = st.Page(
    page="views/second_scen.py",
    title="1.1.2",
    icon="📘",
)

interest_3_page = st.Page(
    page="views/third_scen.py",
    title="1.2.1",
    icon="📘",
)




pg = st.navigation(
    {
        "Polaris": [about_page],
        # "Projets": [project_1_page],
        "Scénarios": [interest_1_page, interest_2_page, interest_3_page],
    }
)

pg.run()