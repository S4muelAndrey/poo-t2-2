import streamlit as st
import pandas as pd
from views import View
import time

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionis")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Nome")
        especialidade = st.text_input("Especialidade")
        conselho = st.text_input("Conselho")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        if st.button("Inserir"):
            View.profissional_inserir(nome, especialidade, conselho, email, senha)
            st.success("Profissional inserido com sucesso!")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            especialidade = st.text_input("Informe o novo e-mail", op.get_especialidade())
            conselho = st.text_input("Informe o novo fone", op.get_conselho())
            if st.button("Atualizar"):
                id = op.get_id()
                View.profissional_atualizar(id, nome, especialidade, conselho)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionals", profissionais)
            if st.button("Excluir"):
                id = op.get_id()
                View.profissional_excluir(id)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()
