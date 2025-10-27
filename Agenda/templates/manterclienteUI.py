import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            list_dic = [obj.to_json() for obj in clientes]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        st.subheader("Inserir novo cliente")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            try:
                View.cliente_inserir(nome, email, fone, senha)
                st.success("✅ Cliente inserido com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(f"❌ Erro: {e}")
            except Exception as e:
                st.error(f"⚠️ Erro inesperado: {e}")

    def atualizar():
        st.subheader("Atualizar cliente existente")
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Escolha um cliente", clientes, format_func=lambda x: x.get_nome())
            nome = st.text_input("Novo nome", op.get_nome())
            email = st.text_input("Novo e-mail", op.get_email())
            fone = st.text_input("Novo fone", op.get_fone())
            senha = st.text_input("Nova senha", op.get_senha(), type="password")

            if st.button("Atualizar"):
                try:
                    View.cliente_atualizar(op.get_id(), nome, email, fone, senha)
                    st.success("✅ Cliente atualizado com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(f"❌ Erro: {e}")
                except Exception as e:
                    st.error(f"⚠️ Erro inesperado: {e}")

    def excluir():
        st.subheader("Excluir cliente")
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Escolha o cliente", clientes, format_func=lambda x: x.get_nome())
            if st.button("Excluir"):
                try:
                    View.cliente_excluir(op.get_id())
                    st.success("✅ Cliente excluído com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(f"❌ Erro: {e}")
                except Exception as e:
                    st.error(f"⚠️ Erro inesperado: {e}")
