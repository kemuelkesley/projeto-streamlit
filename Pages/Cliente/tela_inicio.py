# Tela de Login
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# Criando tela de Login e Senha

def bem_vindo():
    # with open('assets/css/style.css') as f:
    #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.title("Seja Bem Vindo :sunglasses:")
 
    st.subheader("""
        Esse é meu primeiro projeto com STREAMLIT.
    """, anchor=None)

    st.write("Objetivo foi criar um CRUD.")
    st.write("Para ver o projeto, vá no **Menu a sua esquerda e clique em Incluir.**")
    
    # Imagem
    image = Image.open("assets/image/kemStreamlit.jpeg")
    # btn = st.button("Ver o Projeto", type="secondary")
    st.image(image, caption="Kemuel Kesley",width=400)
       

    st.subheader("Sobre Mim")
    st.write("""
        Olá, me chamo kemuel, sou Desenvolvedor FullStack, estudante de Sistema da Informação Faculdade Estácio de Sá Maceio-AL.
        Atualmente me encontro no 4 Pérido.
    """)

    st.subheader("Como entrei na Área de Tecnologia.")
    st.write("""
        Bom um resumo bem breve ,foi que eu entrei nesse mundo bem novo, quando ganhei meu primeiro computador aos 16 anos.
        Com a ideia do meu pai que eu tinha que aprender a consertar meu próprio computador quando quebrasse.
        Foi dai que ele me colocou no meu primeiro curso de Montagem e manutenção de computadores no Senai.
        Depois comecei a consertar os computadores dos amigos, vizinhos, até montei meu laboratorio, onde eu visitava sozinho empresas para dar manutenção e instalar equipamentos.

    """)
    
    st.subheader("Como Desenvolvedor onde trabalhei.")
    
    st.markdown("##### TRE-AL")
    st.write("- Atualmente eu passei em um concurso e estou esperando ser chamado para a área de desenvolvimento.")    
        
    st.markdown("##### Casa da Industria SESI/SENAI")
    st.write("- Atuei na área educacional do SESI e SENAI, onde tive meu primeiro contato com Banco de dados **SQL-SERVER, HTML, CSS, JAVASCRITP**, onde participei de alguns projetos no **Front-End** e a maior parte eu ficava analisando dados e criando consultas.")    
   
    st.markdown("##### Myia")
    st.write("- Onde atuei dando suporte aos úsuarios e tive meu **primeiro contato com Python e um pouco de ciência de dados**.")    
   


    st.subheader("Projetos que fiz e participei")
    st.write("- 1 - Criação de um sistema de Cadastro para o Senai-AL")
    st.write("- Link - https://portaldeservicos.fiea.com.br/senai/cadastroalunoqualifica/")
    st.write("- 2 - Manutenção e Suporte no site oficial do Senai")
    st.write("- Link - https://al.senai.br/")
    st.write("- GitHub: https://github.com/kemuelkesley")

    # Contatos
    st.subheader("Contato:")
    st.write("- Facebook: https://www.facebook.com/")
    st.write("- Instagram: https://www.instagram.com/kemuelkesley/")
    st.write("- E-mail: kemuelkesley@gmail.com")

    