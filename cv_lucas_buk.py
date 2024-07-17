import streamlit as st
from PIL import Image
########## header

st.set_page_config(  # Alternate names: setup_page, page, layout
	layout='wide',  # Can be "centered" or "wide". In the future also "dashboard", etc.
	page_title='CV Lucas Buk Cardoso',  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)

col1, col2 = st.columns([2,3])

col1.write("""# Lucas Buk Cardoso""")
image = Image.open('perfil.png')
col1.image(image, width=250)

col2.write("### ")
col2.write("#### :house: São Paulo, SP - Brasil")
col2.write("#### :e-mail: lucas.cardoso@maua.br")
col2.image(Image.open('github-logo.png'), width=30) 
col2.write(f"#### https://github.com/Lucas-Buk")

st.markdown('## Summary', unsafe_allow_html = True)
st.info("""
"I'm a results-driven data scientist passionate about leveraging data science for real-world impact. With a proven track record in diverse industries, I excel in presenting insights, developing KPI dashboards, automating reporting, and conducting data analysis to drive actionable results. A quick learner, collaborative team player, and effective communicator, I'm eager to contribute my expertise to progressive organizations, making a meaningful difference in the industry."

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

###################
st.write("""
## Work and Experiences
""")

txt2('**Loreon Investment**, Data Analyst', 'February, 2021 - Present')
st.info("""
- Accomplished a remarkable 70% surge in report adoption by thoroughly revamping and enhancing existing reports. Skillfully harnessed MT5 API and Python-driven data analysis methods, showcasing an exceptional aptitude for data visualization and reporting.
- Conducted extensive data analysis utilizing Python and cutting-edge BI tools, generating insightful dashboards that uncovered valuable trading patterns, market trends, and portfolio performance. Demonstrated my proficiency in data analysis and visualization for data-driven decision-making.
- Utilized Python to create essential trading features, such as Bollinger Bands, support & resistance, and SMA, optimizing tactics and substantially boosting profitability. Proved my ability to develop advanced analytical solutions to enhance trading strategies.
- Spearheaded automation initiatives, streamlining critical processes, reducing manual efforts, and achieving remarkable efficiency gains for the organization. Highlighted my proactive approach in leveraging automation to optimize workflows and boost productivity.
- Collaborated with a team to provide data engineering expertise, leveraging Airflow, IDE, and ETL techniques to optimize data pipelines for trading and financial analysis at Loreon Investment. Demonstrated my versatility and ability to collaborate in a team environment.
- Pioneered the development of impactful Business Intelligence dashboards using PowerBI, Qlik, Metabase, and Streamlit, leading to streamlined processes, increased operational efficiency, and exceptional business outcomes. Showcased my skills in data visualization and BI tools, positioning me as a competent data scientist in the financial industry.
- 

""")


txt2('**BCG, Forage**, Data Science and Advance analytics virtual experience program', 'July, 2022 - September, 2022' )
st.info("""
- Completed prestigious Data Science and Analytics Virtual Experience Program with Boston Consulting Group (BCG), showcasing proficiency in Python, Pandas, NumPy, scikit-learn, and TensorFlow for data manipulation, analysis, and machine learning.
- Developed and implemented advanced machine learning models to predict business outcomes, optimizing strategies for enhanced productivity and profit.
- Utilized data visualization tools like Matplotlib and Seaborn to create insightful charts and graphs, effectively communicating findings to stakeholders and driving data-informed decisions for business growth. 

""")

txt2('**British Airways**, Data Science and Advance analytics virtual experience program', 'October 2022 - November, 2022')
st.info("""
-  Completed Data Science and Advanced Analytics Virtual Experience Program with British Airways, gaining hands-on experience in data analysis, machine learning, and predictive modeling.
-  Utilized Python, Pandas, NumPy, and scikit-learn to manipulate and analyze large datasets, extracting valuable insights to drive business decisions.
-  Developed machine learning models to predict customer behavior, optimize flight scheduling, and improve operational efficiency.
-  Leveraged data visualization tools like Matplotlib and PowerBI to create impactful visualizations, facilitating clear communication of complex findings to stakeholders.

""")
st.info(""" Projects with API :
- also use the Zoopla API to fetch the list of available properties for rent and sales in Oxoford, including the running cost of each property
""")
st.write("""## Education and Certifications""")
txt('**B.Tech**, (Pure and Applied Mathematics), Federal University of Technology, Minna, Niger State,Nigeria.','2015-2022')
txt('**Kaggle** Data science Certifications', ' June, 2022') 
txt('**SkillUP** Data science with Python', 'September, 2022')
txt('**SkillUP** Power BI for Beginners', 'October, 2022')
txt('**SkillUP** Introduction to SQL', 'November 2022')

st.write("""
## Skills and Tool
""") 
txt('**Programming**', "Python" )
txt('**Data processing/wrangling**', '"Sql", "Pandas", NoSql')
txt('**Machine Learning**', "Scikit-learn")
txt('**Power BI**', "Visualization")
st.write("""## Social-Media""")
txt3('**LinkedIn**', "https://www.linkedin.com/in/yusuf-olajide-a59aba238/")
txt3('**GitHub**', "https://github.com/Olajydo")
txt3('**Twitter**', '@loerareup')
txt3('**Phone Number**:', '07045511994')