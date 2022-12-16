import streamlit as st
from presentation_card import presentation_card
from portfolio_carousel import portfolio_carousel
from PIL import Image

img_cabeçalho = Image.open(r"images\head.png")
  
title = "Work"     
subtitle =  '''Check my commercioal and non commercial projects.
            If you have any questions feel free to ask me for more information'''
cards = [["images/zenk.jpg", "ZENK project", "Web Scraping | RPA | Data Anlysis", "A formação da memória requer a expressão gênica A formação da memória requer a expressão gênica A formação da memória requer a expressão gênica induzida pela atividade neuronal. Esta resposta inclui uma série de genes dependentes de atividade tidos como mediadores das mudanças necessárias para a consolidação e manutenção da memória."],
        ["images/B2B.jpg", "Prospecção de Clientes B2B", "Google API | Python | Streamlit", "Aplicação para prospectar potenciais clientes B2B no Rio Grande do Norte utilizando uma API da Google chamada Places."],
        ["images/tracking.jpg", "Bird Tracking", "Data Processing | Data Visualization", "Aplicação para processar dados de coordenadas e gerar visualizações em mapa de calor."]]
        
def main():
   
    st.image(img_cabeçalho, use_column_width=True)

    value = presentation_card(image_path="images/profile.png",
                              name="Abraão Andrade",
                              post="Cientista de Dados Júnior",
                              description="Atua como Pesquisador no Instituto do Cérebro UFRN e Estagiário em Análise de Dados e Automação de Processos no Supermercado Nordestão")
    
    value = portfolio_carousel(title=title,
                               subtitle=subtitle,
                               cards=cards)

if __name__ == '__main__':
    main()