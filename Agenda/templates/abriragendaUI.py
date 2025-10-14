import streamlit as st
from views import View
import time
from datetime import datetime

class AbrirAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        data_inicio = st.text_input("Informe a data em formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        horario_inicio = st.text_input("Informe o horário inicial no formato HH:MM", datetime.now().strftime("%H:%M"))
        horario_final = st.text_input("Informe o horário final no formato HH:MM", datetime.now().strftime("%H:%M"))
        intervalo = st.text_input("Informe o intervalo entre os horários (min)", 60)
        if st.button("Abrir Agenda"):
            id_cliente = None 
    
    
    #id_servico = None
    #id_profissional = None
    #if cliente != None: id_cliente = cliente.get_id()
    #if servico != None: id_servico = servico.get_id()
    #if profissional != None: id_profissional = profissional.get_id()
    #View.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
    #st.success("Horário inserido com sucesso")