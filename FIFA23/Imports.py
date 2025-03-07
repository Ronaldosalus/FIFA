import streamlit as st
import pandas as pd
import time
import numpy as np
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os 

# Escreve palavra por palavra que nem o chatgpt.
def escrevendo(palavra: str):
    for carac in palavra.split(" "):
        yield carac + " "
        time.sleep(0.05)


# IA do Marco, ela ta com erro na parte da IA, precisa arrumar.
def Marco(pergunta, mensagens):
    api_key = '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'
    os.environ['GROQ_API_KEY'] = api_key

    chat = ChatGroq(model='llama-3.1-70b-versatile')

    def resposta_bot(mensagens):
        mensagens_modelo = [('system', 'Você é um assistente criativo chamado Marco, você pergunta quem é a pessoa com quem está falando, e chama a pessoa de quem ela falou que é. Criado pelo Ronaldo que é uma criança de 12 anos.')]
        mensagens_modelo += mensagens
        template = ChatPromptTemplate.from_messages(mensagens_modelo)
        chain = template | chat
        return chain.invoke({}).content

    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(('assistant', resposta))
    return resposta