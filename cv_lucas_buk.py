import streamlit as st
from PIL import Image
from io import BytesIO
import base64

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
    st.write('#### ')

    # Carregar a imagem do GitHub
    github_logo = Image.open('github-logo.png')
    buffered = BytesIO()
    github_logo.save(buffered, format="PNG")
    github_logo_base64 = base64.b64encode(buffered.getvalue()).decode()
    # Criar as colunas
    col1, col2 = st.columns(2)

    # Adicionar o link do CV Lattes na primeira coluna
    col1.markdown(
        """
        <a href="https://lattes.cnpq.br/5417608945198427" target="_blank" style="text-decoration: none; font-size: 16px;">
            📄CV Lattes
        </a>
        """, unsafe_allow_html=True)

    # Adicionar o link do GitHub na segunda coluna
    col2.markdown(
        f"""
        <a href="https://github.com/Lucas-Buk" target="_blank" style="text-decoration: none; font-size: 16px;">
            <img src="data:image/png;base64,{github_logo_base64}" width="18"/> GitHub
        </a>
        """, unsafe_allow_html=True)
 

st.markdown('## Resumo', unsafe_allow_html = True)
st.markdown("""
Possui Especialização em Ciência de Dados e Inteligência Artificial e graduação em Engenharia de Controle e Automação, ambos pelo Instituto Mauá de Tecnologia. Atualmente é Doutorando em Engenharia Elétrica na Escola Politécnica da USP e engenheiro pesquisador no Núcleo de Sistemas Eletrônicos Embarcados (NSEE) do Instituto Mauá de Tecnologia, visando aplicações de Ciência de Dados e Inteligência Artificial na área da saúde pública. Lidera a participação do NSEE no projeto ConeCta-SP da FAPESP.
""")

###################

def txt(a, b):
    col1,col2 = st.columns([4, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


###################

# Formação Acadêmica
st.write("## Formação Acadêmica")

txt('**Doutorado Direto - Engenharia Elétrica na Escola Politécnica da USP**', 'Março, 2022 - Presente')

txt('**Especialização em Ciência de Dados e Inteligência Artificial - Instituto Mauá de Tecnologia**', 'Agosto, 2020 - Dezembro, 2021')

txt('**Bacharel em Engenharia de Controle e Automação - Instituto Mauá de Tecnologia**', 'Fevereiro, 2015 - Dezembro, 2019')

txt('**Curso Técnico em Automação Industrial - ETEC Jorge Street**', 'Fevereiro, 2013 - Dezembro, 2014')

# Experiência
st.write("## Experiência")

txt2('**Engenheiro Pesquisador**', 'Abril, 2021 - Presente')
st.info("""
Atuação como engenheiro pesquisador e líder da área de Ciência de Dados e Inteligência Artificial no Núcleo de Sistemas Eletrônicos Embarcados (NSEE) do Instituto Mauá de Tecnologia, com aplicações em saúde pública e análise de acidentes.
""")

txt2('**Coordenador do módulo Ciência de Dados, Técnicas e Aplicações na Pós-Graduação**', 'Março, 2024 - Presente')
st.info("""
Atuação como coordenador do módulo de Ciência de Dados na Pós-Graduação do Instituto Mauá de Tecnologia.
""")

txt2('**Professor da Pós-Graduação**', 'Março, 2022 - Presente')
st.info("""
Atuação como professor da Pós-Graduação do Instituto Mauá de Tecnologia, nas disciplinas de Aprendizado de Máquina, Projetos em Ciência de Dados e Introdução à Ciência de Dados.
""")

txt2('**Estágio operacional no Centro de Pesquisas do Instituto Mauá de Tecnologia**', 'Agosto, 2019 - Janiro, 2020')
st.info("""
Estagiário no Núcleo de Sistemas Produtivos Inteligentes (NSPI) do Instituto Mauá de Tecnologia, atuando na operação de uma planta de indústria 4.0.
""")

# Publicações
st.write("## Publicações")

txt2('**Machine learning for predicting survival of colorectal cancer patients**', 'Junho, 2023')
st.info(f"""
Artigo publicado na **Scientific Reports** da **Nature**, com o estudo realizado para a predição da sobrevida de pacientes com câncer colorretal.

Disponível em: https://www.nature.com/articles/s41598-023-35649-9.
""")

txt2('**Desafio ético no compartilhamento de dados em Saúde**', 'Julho, 2023')
st.info("""
Artigo publicado na **Revista CREMESP**, comentando sobre como compartilhar dados de saúde, proteger a privacidade dos pacientes e, ainda assim, não limitar o aprendizado dos modelos de IA.  

Disponível em: https://www.cremesp.org.br/library/modulos/flipbook/revista/102/36/index.html
""")

# Projetos de Pesquisa
st.write("## Projetos de Pesquisa")

txt2('**Criação de modelos de IA para predizer a sobrevida de pacientes com câncer de pulmão**', '2024 - Etapas iniciais')
my_bar = st.progress(20, text='Iniciando as análises')
st.info("""
A partir dos dados de câncer de pulmão do Registro Hospitalar de Câncer do Estado de São Paulo (RHC-SP), serão criados modelos de machine learning de classificação e de sobrevida, além do modelo de Cox, de modo a comparar os resultados para a predição de sobrevida e vantagens e desvantagens dos diferentes tipos de modelos. Espera-se também realizar análises dos anos pandêmicos e seus impactos no tratamento de câncer de pulmão.
        
Projeto vinculado ao ConeCta-SP, colaboração com Faculdade de Saúde Pública da USP, AC Camargo Cancer Center e Fundação Oncocentro de São Paulo.
""")

txt2('**Predição de recorrência em pacientes com câncer de pulmão**', '2024 - Etapas iniciais')
my_bar = st.progress(20, text='Iniciando as análises')
st.info("""
Utilização de algoritmos de IA para predição a volta do câncer (recorrência) em pacientes com câncer de pulmão, dados provenientes do Registro Hospitalar de Câncer de São Paulo (RHC-SP).
        
Colaboração com o Thoracic Oncology Research Group (THORG).
""")

txt2('**Análise dos anos de vida perdidos de pacientes com câncer de pulmão**', '2024 - Abstract aceito na WCLC da IASLC')
my_bar = st.progress(100, text='Completo')
st.info("""
Realização de análises dos anos perdidos por pacientes de câncer de pulmão. O Abstract com as análises foi aceito na World Conference on Lung Cancer da International Association for the Study of Lung Cancer (IASLC).
        
Colaboração com o Thoracic Oncology Research Group (THORG).
""")

txt2('**Predição de sobrevida cruzada em tipos de câncer**', '2024 - Submissão do artigo')
my_bar = st.progress(100, text='Completo')
st.info("""
Criação de modelos de machine learning para predizer a sobrevida entre tipos diferentes de câncer, de modo a buscar características em comum para os vários tipos testados. Dois grupos foram selecionados para realização da predição cruzada: cânceres mais frequentes e relacionados ao sistema digestório.
        
Projeto vinculado ao ConeCta-SP, colaboração com Faculdade de Saúde Pública da USP, AC Camargo Cancer Center e Fundação Oncocentro de São Paulo.
""")

txt2('**Análise de sobrevida de pacientes com câncer colorretal**', '2023 - Publicado na Scientific Reports')
my_bar = st.progress(100, text='Completo')
st.info("""
Aplicação das ferramentas de Ciência de Dados e Inteligência Artificial para determinar o melhor modelo de machine learning para predizer a sobrevida de pacientes com câncer colorretal presentes no Registro Hospitalar de Câncer (RHC-SP).

Projeto vinculado ao ConeCta-SP, colaboração com Faculdade de Saúde Pública da USP, AC Camargo Cancer Center e Fundação Oncocentro de São Paulo.

> Artigo completo: https://www.nature.com/articles/s41598-023-35649-9
> Documentação disponível em: https://colorectal-site.readthedocs.io/en/latest/
""")

txt2('**Análise de sobrevida em pacientes com qualquer tipo de câncer**', '2022 - Finalizado')
my_bar = st.progress(100, text='Completo')
st.info("""
Testes iniciais relizados no Registro Hospitalar de Câncer de São Paulo, de modo a tratar os dados e treinar algoritmos de IA para predizer a sobrevida dos pacientes presentes no banco de dados. A realização deste estudo piloto levou a Mauá a participar do projeto FAPESP ConeCta-SP, colaborando no subprojeto do Eixo 2 chamado "Inteligência Artificial na predição de sobrevida de pacientes com câncer no período da epidemia da COVID-19 (2020/21) e anos não-epidêmicos"
        
Projeto vinculado ao ConeCta-SP, colaboração com Faculdade de Saúde Pública da USP, AC Camargo Cancer Center e Fundação Oncocentro de São Paulo.
        
> Documentação disponível em: https://cancer-project.readthedocs.io/en/latest/
""")

txt2('**Análise de acidentes em rodovias federais**', '2022 - Submissão do artigo')
my_bar = st.progress(100, text='Completo')
st.info("""
Realização de análises de fluxo e acidentes em estradas federais do Brasil, visando encontrar explicações e correlações entre os horários e locais de ocorrência.
        
Colaboração com a Faculdade de Saúde Pública da USP.
""")

# Premiações e Reconhecimentos
st.write("## Premiações e Reconhecimentos")
txt2('**Melhor aluno de Engenharia de Controle e Automação**', 'Janeiro, 2020')
st.info("""
Prêmio de melhor aluno do curso de Engenharia de Controle e Automação do Instituto Mauá de Tecnologia, entre os formandos em 2019.
""")

txt2('**Melhor TCC do Eureka 2019 pela votação popular**', 'Janeiro, 2020')
st.info("""
Prêmio de melhor trabalho de graduação do Eureka 2019, com Robô de Companhia para Idosos, eleito pela votação dos visitantes do evento.
""")

txt2('**Participação no Desafio UFABC de Empreendedorismo**', 'Junho, 2015')
st.info("""
Participação e 5° lugar do projeto do Assento Preferencial Automatizado, realizado como TCC do curso técnico em Automação Industrial, na fase final do desafio.
""")

# Palestras e Vídeos
st.write("## Palestras e Vídeos")

txt2('**Utilização de Inteligência Artificial no estudo de sobrevida de pacientes com câncer**', 'Setembro, 2023')
st.info("""
Palestra na Conferência Científica com o AC Camargo Cancer Center, mostrando as etapas realizadas no estudo com pacientes de câncer colorretal publicado na Scientific Reports.
        
Disponível em: https://www.youtube.com/live/UYwVvTFmMM4?si=0T7FpngXyvGNttQi
""")

txt2('**WorkShop: Ciência de Dados e Inteligência Artificial**', 'Fevereiro, 2023')
st.info("""
Terceira parte do WorkShop: Ciência de Dados e Inteligência Artificial, promovido pelos professores da Pós-graduação de Ciência de Dados e Inteligência Artificial do Instituto Mauá de Tecnologia. 
        
Disponível em: https://youtu.be/ArP-ygF3LEc?si=rMbcHXHzEO-wXZJO

WorkShop completo em: https://youtube.com/playlist?list=PLnWpv5C1ai2fDtEXxTSWnQyrNUoIJPHxD&si=bt3Wx2IZrDDAi5ba
""")


