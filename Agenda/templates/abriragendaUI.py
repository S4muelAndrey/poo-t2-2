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
            a = 1
            
