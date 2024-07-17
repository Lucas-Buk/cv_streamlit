import streamlit as st
from PIL import Image
########## header

st.set_page_config(# Alternate names: setup_page, page, layout
	layout='wide',  # Can be "centered" or "wide". In the future also "dashboard", etc.
	page_title='CV Lucas Buk Cardoso',  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
    initial_sidebar_state='expanded', # Can be "auto", "expanded", "collapsed"
)

with st.sidebar:
    image = Image.open('perfil.png')
    st.image(image, width=250)
    st.write('# Lucas Buk Cardoso')

    st.write('#### ')
    st.write('#### :house: São Paulo, SP - Brasil')
    st.write('#### :e-mail: lucas.cardoso@maua.br')
    st.write('#### :page_facing_up: https://lattes.cnpq.br/5417608945198427')
    col1, col2 = st.columns([1,20], vertical_alignment='center')
    col1.image(Image.open('github-logo.png'), width=20) 
    col2.write('#### https://github.com/Lucas-Buk') 

st.markdown('## Resumo', unsafe_allow_html = True)
st.info("""
"Resumo Resumo Resumo"
""")

# with open("Abraham Olajide Yusuf.pdf", "rb") as f:
#     PDFbyte=f.read()
# st.download_button(label="Download CV", data=PDFbyte, file_name="Abraham Olajide Yusuf.pdf", mime="application/octet-stream")    



###################
# custom function for text printing

def txt(a,b):
    col1,col2 = st.columns([4,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a,b):
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)
    
def txt3(a,b):
    col1, col2 = st.columns([4,4])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


#########

st.write("## Formação Acadêmica")

txt('** **, ', 'Mês, Ano - Mês, Ano')
st.info("""

""")


st.write("## Experiência")
txt2('** **, ', 'Mês, Ano - Mês, Ano')
st.info("""

""")

st.write("## Publicações")
txt2('** **, ', 'Mês, Ano - Mês, Ano')
st.info("""

""")

st.write("## Premiações")
txt2('** **, ', 'Mês, Ano - Mês, Ano')
st.info("""

""")

st.write("## Palestras e Vídeos")
txt2('** **, ', 'Mês, Ano - Mês, Ano')
st.info("""

""")

st.write("## Sobre a Área de Ciência de Dados e IA em Saúde Pública do NSEE")
st.info("""

""")
