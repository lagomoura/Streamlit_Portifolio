# sourcery skip: use-named-expression
from pathlib import Path
import streamlit as st
from PIL import Image

# Page settings #
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"style"/"main.css"
resume_file = current_dir/"assets"/"cv_Gustavo_Lago.pdf"
profile_pic = current_dir/"assets" / "pic_prof_circle.png"

# variables generales #
NAME = "Gustavo Lago"
DESCRIPTION = "Python & JavaScript Developer | Data Analyst | Business Inteligence"
EMAIL = "mouralago@live.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/gustavo-moura-/",
    "GitHub": "https://github.com/lagomoura",
}

PROJECTS = {
    "one": "empty",
    "two": "empty",
    "three": "empty"
}


# . Las configuraciones de pagina no son compartidas con otras paginas.
st.set_page_config(
    page_title="Hola y bienvenido",
    page_icon="👋"
)

st.title("Bienvenidx a mi portfolio")
st.sidebar.success("Seleccione una opción abajo: ")


#! LOADING CSS
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# = HERO SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📝Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="aplication/octet-stream",
    )
    st.write("📧", EMAIL)

# = Social links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (plataforma, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{plataforma}]({link})")

# = Qualification
st.write("#")
st.subheader("Experience & Qualifications")
st.write("""
  - 3 Years of Experience extracting and actionable insights from data
  - Strong experience and knowladge in Python and Excel
  - Good Understand of statistical and respectives applications
  - Excelent team-player and displaying strong sense os initiative on tasks
""")

# = Skills
st.write("#")
st.subheader("Hard Skills")
st.write("""
  - Programming: Python, JavaScript, SQL
  - Data Visualization: PowerBI, MS Excel, Plotly, Streamlit
  - Modeling: Logistic regression, linear regression, decision trees
  - Databases: MySQL, MongoDB
""")

# = Work History
st.write("#")
st.subheader("Work History")
st.write("---")

# ? JOB1
st.write("💻 Desarrolador Web Freelance")
st.write("02/2021 - 03/2021")
st.write("""
         - Creacion de landing page para empresa logistica Buybox Argentina
         - Mas experiencias
         - Otras experiencias
         - Una mas
""")

# ? JOB2
st.write("🐍 Desarrolador Pyhton Freelance")
st.write("02/2021 - 03/2021")
st.write("""
         - Creacion de landing page para empresa logistica Buybox Argentina
         - Mas experiencias
         - Otras experiencias
         - Una mas
""")

# ? JOB3
st.write("📊 Analista de atomacion Freelance")
st.write("02/2021 - 03/2021")
st.write("""
         - Creacion de landing page para empresa logistica Buybox Argentina
         - Mas experiencias
         - Otras experiencias
         - Una mas
""")

#= Projects 
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
  st.write(f"[{project}]({link})")

# . Streamlit trabaja con un sistema de estados. Permite acceder al estado de  otras paginas

# Se la variable no esta en el estado de la pagina, tendra como contenido uns string vacia
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

# Creamos una caja de input de texto
my_input = st.text_input("Busque por palabra llave",
                         st.session_state["my_input"])

# Boton de submit
submit = st.button("Buscar")

# En el caso que submit sea clickeado, guardamos en el estado la variable my_input y guardamos en ese estado, el contenido de la caja de texto.
if submit:
    st.session_state["my_input"] = my_input
    st.write(f"Palabra llave buscada: {my_input}")

# Usamos ese estado para vincular paginas.
