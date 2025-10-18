import streamlit as st
from views import View

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")

        if "usuario_id" not in st.session_state:
            st.error("Nenhum profissional logado.")
            return

        id_profissional = st.session_state["usuario_id"]

        horarios = View.horario_filtrar_profissional(id_profissional)

        if len(horarios) == 0:
            st.info("Você não possui serviços agendados.")
            return

        opcoes = []
        for h in horarios:
            cliente = View.cliente_listar_id(h.get_id_cliente())
            nome_cliente = cliente.get_nome() if cliente else "Cliente não encontrado"
            descricao = f"{h.get_id()} - {h.get_data()} - {nome_cliente} - Confirmado: {h.get_confirmado()}"
            opcoes.append((descricao, h))

        selecionado = st.selectbox(
            "Informe o horário para confirmar",
            options=opcoes,
            format_func=lambda x: x[0] 
        )

        if selecionado:
            horario = selecionado[1]
            cliente = View.cliente_listar_id(horario.get_id_cliente())
            servico = View.servico_listar_id(horario.get_id_servico())

            if cliente and servico:
                st.write(f"**Cliente:** {cliente.get_nome()} — {cliente.get_email()}")
                st.write(f"**Serviço:** {servico.get_descricao()}")
            
            if st.button("Confirmar"):
                horario.set_confirmado(True)
                View.horario_atualizar(horario)
                st.success("Serviço confirmado com sucesso! ✅")
                st.balloons()
