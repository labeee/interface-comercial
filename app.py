import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import random

# CSS externo que inclui os ícones da barra lateral.
font_awesome = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css']

# App raiz.
app = dash.Dash(__name__, external_stylesheets=font_awesome)

# Gráfico com dados genéricos. Futuramente, será gerado com os dados de retorno das redes neurais.
fig = go.Figure(go.Bar(x=['Edificação real', 'Edificação de referência'], y=[0.62, 0.35]), go.Layout(yaxis=dict(tickformat="%")))

# Layout do app raiz. Aqui está implementada toda a parte gráfica da interface.
app.layout = html.Div(children = [
    
    # GAMBIARRA (que, por sinal, não funciona). No código HTML antigo, era um input de tipo checklist, mas o Dash não possui
    # um componente de comportamento correspondente. Esse é o mais próximo. 
    core.Checklist(id='check'),
    
    # Aqui ficam os elementos da parte esquerda do header, que consistem em um ícone de menu hamburguer e o nome
    # 'INTERFACE COMERCIAL'.
    html.Header(children = [
        html.Label(htmlFor='check', children=[
            html.I(className='fas fa-bars', id='sidebar-btn')
        ]),
        
        html.Div(className='left-area', children=[
            html.H3(children=[
                'Interface ', 
                html.Span('Comercial')
            ])
        ])
    ]),

    # Lado direito do header. Botões de função autoexplicativa.
    html.Div(className='right-area', children=[
        html.A('Sair', href='#', className='sair-btn'),
        html.A('Usuário', href='#', className='usuario-btn'),
        html.A('Classifique', href='#', className='classifique-btn')
    ]),

    # Barra lateral. No momento em que este comentário está sendo escrito, o funcionamento de expansão e colapso ainda não está
    # devidamente implementado, mas será.
    html.Div(className='sidebar', id='sidebar', children=[
        html.A(href='#', children=[
            html.I(className='fas fa-desktop'),
            html.Span('Modelo BIM')
        ]),
        html.A(href='#', children=[
            html.I(className='fas fa-store-alt'),
            html.Span('Dados da edificação')
        ]),
        html.A(href='#', children=[
            html.I(className='fas fa-sun'),
            html.Span('Envoltória')
        ]),
        html.A(href='#', children=[
            html.I(className='fas fa-solar-panel'),
            html.Span('Aquecimento solar')
        ]),
        html.A(href='#', children=[
            html.I(className='fas fa-cog'),
            html.Span('Equipamentos')
        ]),
        html.A(href='#', children=[
            html.I(className='fas fa-leaf'),
            html.Span('Energia renovável')
        ]),
        html.A(href='#', children=[
            html.I(className='fas fa-hand-holding-water'),
            html.Span('Uso racional da água')
        ]),
        html.A(href='#', children=[
            html.I(className='fas fa-smog'),
            html.Span('Emissão de dióxido de carbono')
        ])
    ]),

    # Componente correspondente à seção onde o usuário irá fornecer os dados de entrada da rede neural.
    html.Div(className='data-area', children=[
        html.Div(className='input-area', children=[
            # Botões que possibilitam a escolha do tipo de edificação.
            html.Nav(className='edific-buttons', children=[
                html.A('Edificação Real', href='#', className='real-button'),
                html.A('Edificação de Referência', href='#', className='reference-button')
            ]),

            # Seção onde o usuário poderá selecioar o app que deseja.
            html.Div(className='input-section', children=[
                html.Div(className='app-section', children=[
                html.A(className='app-arrow', children=[
                    html.I(className='fas fa-angle-double-left')
                ]),
                html.A(href='#', className='app-unit', children=[
                    html.Span('APP1')
                ]),
                html.A(href='#', className='app-unit', children=[
                    html.Span('APP2')
                ]),
                html.A(href='#', className='app-unit', children=[
                    html.Span('APP3')
                ]),
                html.A(href='#', className='app-unit', children=[
                    html.Span('APP4')
                ]),
                html.A(className='app-arrow', children=[
                    html.I(className='fas fa-angle-double-right')
                ])
            ]),

            # Div com botões de escolha entre 'Volumetria' e 'Materiais'.
            html.Div(className='vol-mat', children=[
                html.A(href='#', className='vol-mat-item', children=[
                    html.Strong('Volumetria')
                ]),
                html.A(href='#', className='vol-mat-item', children=[
                    html.Strong('Materiais')
                ])
            ]),

            # Links para a inserção de dados de entrada pelo usuário. Os componentes atuam em 'duplas': um botão, no qual usuário
            # clica/pressiona para selecionar o link, e, logo abaixo, um div que expande sempre que o botão é clicado/pressionado.
            html.Div(className='input-links', children=[
                html.Button(className='input-button', id='area-fachada', children=[
                    html.Strong('Área da fachada')
                ]),
                html.Div(className='input-button-content', style={'max-height': '0'}, id='area-fachada-content', children=[
                    html.Div(className='br-area', children=[
                        html.A('Norte', className='region', id='norte'),
                        html.A('Nordeste', className='region', id='nordeste')
                    ]),
                    html.Div(className='br-area', children=[
                        html.A('Sul', className='region', id='sul'),
                        html.A('Noroeste', className='region', id='noroeste')
                    ]),
                    html.Div(className='br-area', children=[
                        html.A('Leste', className='region', id='leste'),
                        html.A('Sudeste', className='region', id='sudeste')
                    ]),
                    html.Div(className='br-area', children=[
                        html.A('Oeste', className='region', id='oeste'),
                        html.A('Sudoeste', className='region', id='sudoeste')
                    ])
                ]),

                html.Button(className='input-button', id='pe-direito', children=[
                    html.Strong('Pé direito')
                ]),
                html.Div(className='input-button-content', style={'max-height': '0'}, id='pe-direito-content', children=[
                    html.P('haverá conteúdo aqui')
                ]),
                html.Button(className='input-button', id='altura-pavimento', children=[
                    html.Strong('Altura do pavimento')
                ]),
                html.Div(className='input-button-content', style={'max-height': '0'}, id='altura-pavimento-content', children=[
                    html.P('haverá conteúdo aqui')
                ]),
                html.Button(className='input-button', id='tamanho-projecao', children=[
                    html.Strong('Tamanho da projeção')
                ]),
                html.Div(className='input-button-content', style={'max-height': '0'}, id='tamanho-projecao-content', children=[
                    html.P('haverá conteúdo aqui')
                ]),
                html.Button(className='input-button', id='exposicao-cobertura', children=[
                    html.Strong('Exposição da cobertura')
                ]),
                html.Div(className='input-button-content', style={'max-height': '0'}, id='exposicao-cobertura-content', children=[
                    html.P('haverá conteúdo aqui')
                ]),
                html.Button(className='input-button', id='pilotis', children=[
                    html.Strong('Pilotis')
                ]),
                html.Div(className='input-button-content', style={'max-height': '0'}, id='pilotis-content', children=[
                    html.P('haverá conteúdo aqui')
                ]),
                html.Button(className='input-button', id='esquadrias', n_clicks=0, children=[
                    html.Strong('Esquadrias')
                ]),
                html.Div(className='input-button-content', style={'max-height': '0'}, id='esquadrias-content', children=[
                    html.A('Fator de abertura para ventilação', className='esquadrias-content-item'),
                    html.A('Largura', className='esquadrias-content-item'),
                    html.A('Altura', className='esquadrias-content-item'),
                    html.A('Fator de abertura para ventilação', className='esquadrias-content-item'),
                    html.A('Com e sem veneziana', className='esquadrias-content-item'),
                    html.A('Fator de vidro de cada fachada', className='esquadrias-content-item'),
                    html.A('Fator altura da abertura', className='esquadrias-content-item')
                ])
            ]),

            # Botão que submete os dados de entrada para a interface.
            html.Div(className='classification-button-area', id='classification-button-area', children=[
                html.Button(id='classification-button', className='classification-button', children=[
                    html.Strong('CLASSIFICAÇÃO FINAL')
                ])
            ])
        ])

        # O colchete e o parêntese abaixo parecem ser desnecessários, mas, por algum motivo, o código não roda sem eles.
        ]),

        # Região do gráfico onde serão mostrados os dados de saída.
        html.Div(className='output-area', id='output_area', children=[
            core.Graph(id='final_graph', figure=fig)
        ])
    ])
])

# Função de callback que colapsa a barra lateral. Está incompleta.
@app.callback(Output(component_id='sidebar', component_property='style'),
    [Input(component_id='sidebar-btn', component_property='n_clicks')])
def change_sidebar(clicks):
    if clicks % 2:
        return {'left' : '-170px'}
    return {'left' : '0'}

# Função de callback que expande o conteúdo do link 'area-fachada'.
@app.callback(Output(component_id='area-fachada-content', component_property='style'),
    [Input(component_id='area-fachada', component_property='n_clicks')])
def update_area_fachada(clicks):
    if clicks % 2:
        return {'max-height': '100%'}
    return {'max-height': '0'}

# Função de callback que expande o conteúdo do link 'pe-direito'.
@app.callback(Output(component_id='pe-direito-content', component_property='style'),
    [Input(component_id='pe-direito', component_property='n_clicks')])
def update_pe_direito(clicks):
    if clicks % 2:
        return {'max-height': '100%'}
    return {'max-height': '0'}

# Função de callback que expande o conteúdo do link 'altura-pavimento'.
@app.callback(Output(component_id='altura-pavimento-content', component_property='style'),
    [Input(component_id='altura-pavimento', component_property='n_clicks')])
def update_altura_pavimento(clicks):
    if clicks % 2:
        return {'max-height': '100%'}   
    return {'max-height': '0'}

# Função de callback que expande o conteúdo do link 'tamanho-projecao'.
@app.callback(Output(component_id='tamanho-projecao-content', component_property='style'),
    [Input(component_id='tamanho-projecao', component_property='n_clicks')])
def update_tamanho_projecao(clicks):
    if clicks % 2:
        return {'max-height': '100%'}
    return {'max-height': '0'}

# Função de callback que expande o conteúdo do link 'exposicao-cobertura'.
@app.callback(Output(component_id='exposicao-cobertura-content', component_property='style'),
    [Input(component_id='exposicao-cobertura', component_property='n_clicks')])
def update_exposicao_cobertura(clicks):
    if clicks % 2:
        return {'max-height': '100%'}
    return {'max-height': '0'}

# Função de callback que expande o conteúdo do link 'pilotis'.
@app.callback(Output(component_id='pilotis-content', component_property='style'),
    [Input(component_id='pilotis', component_property='n_clicks')])
def update_pilotis(clicks):
    if clicks % 2:
        return {'max-height': '100%'}
    return {'max-height': '0'}

# Função de callback que expande o conteúdo do link 'esquadrias'.
@app.callback(Output(component_id='esquadrias-content', component_property='style'),
    [Input(component_id='esquadrias', component_property='n_clicks')])
def update_esquadrias(clicks):
    if clicks % 2:
        return {'max-height': '100%'}
    return {'max-height': '0'}

# Função de callback que, futuramente, irá enviar os dados de entrada para as redes, aguardar os de saída e, então, criar um novo
# gráfico a partir deles.
@app.callback(Output(component_id='output_area', component_property='final_graph'),
    [Input(component_id='classification-button', component_property='n_clicks')])
def change_fig(clicks):
    real = random.random()
    reference = random.random()
    temp_fig = go.Figure(go.Bar(x=['Edificação real', 'Edificação de referência'], y=[real, reference]), go.Layout(yaxis=dict(tickformat="%")))
    return temp_fig

if __name__ == '__main__':
    app.run_server()