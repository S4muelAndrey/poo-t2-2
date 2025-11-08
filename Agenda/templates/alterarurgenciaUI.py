import streamlit as st
from views import View

class AlterarUrgencia:
    def main():
        st.header("Alterar Urgência")
        id_profissional = st.session_state["usuario_id"]
        profissional = View.profissional_listar_id(id_profissional)
        horarios = View.horario_filtrar_profissional(id_profissional)
        if len(horarios) == 0:
            st.info("Nenhum serviço agendado ainda.")
        else:
            horario = st.selectbox("Agenda", horarios)
            id = horario.get_id()
            data = horario.get_data()
            confirmado = horario.get_confirmado()
            id_cliente = horario.get_id_cliente()
            id_servico = horario.get_id_servico()
            id_profissional = horario.get_id_profissional()
            urgencia = st.selectbox("Informe o grau de urgência", (1, 2, 3), index=None, key="key_atualizar")

            if st.button("Atualizar o grau de urgência"):
                View.horario_atualizar(id, data, urgencia, confirmado, id_cliente, id_servico, id_profissional)
                st.success(f"Urgência alterada para {urgencia} com sucesso")