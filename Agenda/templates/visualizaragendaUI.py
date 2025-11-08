import streamlit as st
from views import View
import pandas as pd

class VisualizarAgendaUI:
    @staticmethod
    def colorir_urgencia(grau):
        if grau == 3: return 'background-color: #662222; color: white'
        if grau == 2: return 'background-color: #665522; color: black'
        if grau == 1: return 'background-color: #226622; color: white'
        return ''

    def main():
        st.header("Meus Serviços")

        if "usuario_id" not in st.session_state:
            st.error("Nenhum profissional logado.")
            return

        id_profissional = st.session_state["usuario_id"]
        horarios = View.horario_filtrar_profissional(id_profissional)

        if not horarios:
            st.info("Nenhum serviço agendado ainda.")
            return

        dados = []
        for h in horarios:
            cliente = View.cliente_listar_id(h.get_id_cliente())
            servico = View.servico_listar_id(h.get_id_servico())
            dados.append({
                "ID": h.get_id(),
                "Data": h.get_data().strftime("%d/%m/%Y %H:%M") if h.get_data() else "",
                "Urgência": h.get_urgencia(),
                "Confirmado": bool(h.get_confirmado()),
                "Cliente": cliente.get_nome() if cliente else None,
                "Serviço": servico.get_descricao() if servico else None
            })

        df = pd.DataFrame(dados)
        df["Urgência"] = df["Urgência"].astype("Int64")
        df = df.sort_values(by="Urgência", ascending=False, na_position="last")
        st.dataframe(df.style.applymap(VisualizarAgendaUI.colorir_urgencia, subset=["Urgência"]), use_container_width=True)
