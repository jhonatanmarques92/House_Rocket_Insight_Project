import pandas as pd
import streamlit as st
import plotly.express as px


# settings
st.set_page_config( layout='wide' )


# Funções
@st.cache( allow_output_mutation=True )
def data(path):
    df = pd.read_csv(path)
    

    return df


def date(df):
    # Convertendo a coluna date para o tipo datetime
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    st.header('Dashboard da House Rocket')

    return df


def duplicated(df):
    # Ordenando da data mais atual para a mais antiga
    df = df.sort_values('date', ascending=False)

    # Excluindo as linhas cujo o ID são duplicados, mantendo apenas as datas mais atuais delas
    df.drop_duplicates('id', keep='first', inplace=True) 

    return df

def select_filter(df):
    # Criar um slider para filtrar por preço
    min = float(df['price'].min())
    max = float(df['price'].max())
    slider_price = st.slider('Selecione os preços',  min, max, (min, max), step=5000.00)
    df = df[df['price'].between(slider_price[0], slider_price[1])]

    # Botão de rádio para a seleção de com vista para a água
    c1, c2 = st.columns(2)
    radio_water = c1.radio('Vista para a água', ( 'Ambos', 'Com vista', 'Sem vista'))
    if radio_water == 'Com vista':
        df = df[df['waterfront'] == 1]
    elif radio_water == 'Sem vista':
        df = df[df['waterfront'] == 0]
    else:
        pass

    # Checkbox para habilitar ou desabilitar visualização de mapa e tabela
    mapa = c2.checkbox('Visualização dos imóveis no mapa', value=True)
    tabela = c2.checkbox('Visualização da tabela dos dados', value=True)
    # Filtro da tabela para visualização
    if tabela:
        df = df.sort_index()
        multi_colunas = st.multiselect('Selecione as colunas para visualizar', df.columns, list(df.columns))
        lista = []
        for e in multi_colunas:
            lista.append(e)
        st.dataframe(df[lista])
    # Filtro do mapa para vizualização
    if mapa:
        fig = px.scatter_mapbox(df, lat='lat', lon='long', hover_name='id' , color_continuous_scale=px.colors.cyclical.IceFire,size='price')
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)


    return None



if __name__ == '__main__':
    # Carregar os dados
    path = 'kc_house_data.csv'
    df = data(path)
    
    # Transformação dos dados
    df = date(df)

    df = duplicated(df)
    
    df = select_filter(df)