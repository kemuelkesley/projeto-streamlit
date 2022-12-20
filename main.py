import streamlit as st;
import Pages.Cliente.create as PageCreateCliente
import Pages.Cliente.List as PageListCliente
import Pages.Cliente.tela_inicio as PageSelecionaCliente


# Criando um Menu:
st.sidebar.title('Menu')

# Criando menus para fazer alguma alteração no cliente.
page_cliente = st.sidebar.selectbox('Cliente',['Inicio', 'Incluir', 'Consultar'])

if page_cliente == 'Inicio':
    # st.title("Bem vindo")
    PageSelecionaCliente.bem_vindo()

if page_cliente == 'Consultar':
    PageListCliente.List()

if page_cliente == 'Incluir': 
    PageCreateCliente.create() 

   