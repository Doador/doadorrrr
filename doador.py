import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime

# Função para adicionar imagem de fundo na página Home
def add_bg_image(image_path):
    try:
        img = Image.open(image_path)
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"Imagem não encontrada em {image_path}. Verifique o caminho.")

# Função para salvar os dados em um CSV (Doador)
def salvar_doador(nome, idade, sexo, tipo_sanguineo):
    arquivo = "doadores.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Tipo Sanguíneo"])
    novo_doador = pd.DataFrame([[nome, idade, sexo, tipo_sanguineo]], columns=["Nome", "Idade", "Sexo", "Tipo Sanguíneo"])
    df = pd.concat([df, novo_doador], ignore_index=True)
    df.to_csv(arquivo, index=False)

# Função para salvar o agendamento em CSV
def salvar_agendamento(nome, idade, sexo, tipo_doacao, tipo_sanguineo, local, data_hora, hora, notas):
    df_agendamento = pd.DataFrame({
        "Nome": [nome],
        "Idade": [idade],
        "Sexo": [sexo],
        "Tipo Sanguíneo": [tipo_sanguineo],
        "Local": [local],
        "Data": [data_hora],
        "Hora": [hora],
        "Notas": [notas if notas else "Nenhuma"]
    })
    df_agendamento.to_csv('agendamentos.csv', index=False, mode='a', header=False)

# Função para salvar voluntários em CSV
def salvar_voluntario(nome, idade, sexo, contato, interesse):
    arquivo = "voluntarios.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    novo_voluntario = pd.DataFrame([[nome, idade, sexo, contato, interesse]], columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    df = pd.concat([df, novo_voluntario], ignore_index=True)
    df.to_csv(arquivo, index=False)

# Inicializa as opções de navegação no estado da sessão
if "Ops" not in st.session_state:
    st.session_state.ops = [
        "Home", "Importância", "Requisitos para Doação",
        "Etapas para Doação", "Elegibilidade de Doação", 
        'Agendamento', "Cadastro para Voluntários", 'Vídeo', 'Fim'
    ]

# Barra lateral para navegação
with st.sidebar:
    pagina = st.radio('Navegação', st.session_state.ops, key='Nav')

def MudarA():
    st.session_state.Nav = 'Home'
def MudarB():
    st.session_state.Nav = 'Importância'
def MudarC():
    st.session_state.Nav = 'Requisitos para Doação'
def MudarD():
    st.session_state.Nav = 'Etapas para Doação'
def MudarE():
    st.session_state.Nav = 'Elegibilidade de Doação'
def MudarF():
    st.session_state.Nav = 'Agendamento'  
def MudarG():
    st.session_state.Nav = 'Cadastro para Voluntários'
def MudarH():
    st.session_state.Nav = 'Vídeo'
def MudarI():
    st.session_state.Nav = 'Fim'


# Interface Streamlit
st.title("Sistema de Doação de Sangue, Medula óssea e Órgãos")

# Lógica para exibir a página selecionada
if pagina == "Home":
    st.subheader("Doação de Sangue")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi instituída pela 
    Organização Mundial da Saúde (OMS) para lembrar da importância da conscientização quanto à 
    necessidade da doação de sangue e como uma forma de agradecimento aos doadores.""")
    
    st.subheader("Doação de Órgãos")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi instituída pela 
    Organização Mundial da Saúde (OMS) para lembrar da importância da conscientização quanto à 
    necessidade da doação de sangue e como uma forma de agradecimento aos doadores.""")

    st.subheader("Doação de Medula Óssea")
    st.write("""O Dia Mundial da Doação de Medula Óssea é celebrado no terceiro sábado de setembro. Essa data, estabelecida pela World Marrow Donor Association (WMDA), tem como objetivo aumentar a conscientização sobre a doação de medula óssea e promover o registro de novos doadores. O dia também destaca a importância de contar com uma base diversificada de doadores cadastrados, já que a compatibilidade entre doadores e receptores é complexa e depende de fatores genéticos.""")
    add_bg_image("doe.png")
    st.button('Ir para Importância', type="primary", on_click=MudarB)

elif pagina == "Importância":
    st.title("A Importância da Doação de Sangue, Medula Óssea e Órgãos")

    # Explicação sobre a importância da doação de sangue
    st.subheader("A Importância da Doação de Sangue")
    st.write("""A doação de sangue é um ato de solidariedade e amor ao próximo que ajuda a salvar inúmeras vidas diariamente. O sangue doado é essencial para tratamentos médicos, como em cirurgias, acidentes e no suporte a pacientes com doenças graves, como câncer e anemias. Cada doação pode beneficiar até três pessoas, pois o sangue é separado em componentes (plasma, plaquetas e glóbulos vermelhos), utilizados para necessidades distintas.""")
    
    st.subheader("Qrcode com informações em tempo real")
    st.write("""Acessando este qrcode você tem acesso a informações em tempo real sobre o estoque de sangue""")
    st.image("qrr.png")

    # Explicação sobre a importância da doação de medula óssea
    st.subheader("A Importância da Doação de Medula Óssea")
    st.write("""A doação de medula óssea é vital para pacientes com doenças hematológicas graves, como leucemia, linfoma e anemia aplástica. A medula óssea, responsável pela produção de células sanguíneas, precisa ser substituída por uma saudável em casos de danos graves. O procedimento de doação é seguro e pode salvar vidas, especialmente em crianças e jovens. Registre-se em bancos de medula, como o REDOME e HEMOBRAZ, e faça a diferença.""")

    # Explicação sobre a importância da doação de órgãos
    st.subheader("A Importância da Doação de Órgãos")
    st.write("""A doação de órgãos é uma forma de garantir que pessoas com falência de órgãos tenham uma segunda chance de vida. Um único doador pode salvar várias vidas, doando órgãos como coração, rins, fígado e pulmões, além de tecidos como córnea e pele. A decisão de ser um doador deve ser informada à família, pois o consentimento é fundamental para que a doação seja realizada.""")

    st.button('Ir para Requisitos para Doação', type="primary", on_click=MudarC)

# Explicação sobre a importância da doação de órgãos
elif pagina == "Requisitos para Doação":
    st.title("Requisitos para Doação de Sangue")
    
    # Adicionando logs para verificar se as partes estão sendo executadas
    st.write("Verificando requisitos de doação de sangue...")
    st.write(""" 
    - Apresentar boa condição de saúde.
    - Ter entre 16 e 69 anos.
    - Pesar no mínimo 51 quilos.
    - Estar descansado (dormido pelo menos seis horas nas 24 horas anteriores).
    - Estar alimentado (evitar alimentação gordurosa nas 4 horas anteriores).
    - Apresentar documento original com foto recente.
    """)
    st.write(""" 
    Fatores que podem impedir a doação:
    - Doenças crônicas, HIV, Hepatite, Malária.
    - Uso de drogas ilícitas ou medicamentos.
    """)

    # Requisitos sobre a importância da doação de Medula Óssea
    st.subheader("Requisitos para Doação de Medula Óssea")
    st.write("Verificando requisitos de medula óssea...")
    st.write(""" 
    - Ter entre 18 e 55 anos.
    - Estar em boas condições de saúde.
    - Não ter doenças autoimunes, HIV, Hepatite ou outras doenças graves.
    - Não ter histórico de câncer.
    - Estar disposto a se cadastrar e realizar os exames necessários.
    """)

    # Requisitos sobre a importância da doação de Órgãos
    st.subheader("Requisitos para Doação de Órgãos")
    st.write("Verificando requisitos de doação de órgãos...")
    st.write(""" 
    - Ser maior de idade (no Brasil, é necessário ter 18 anos).
    - Não ter doenças que impeçam a doação (ex: câncer, doenças infecciosas).
    - Informar a família sobre a decisão de ser doador.
    - Assinar o documento de doação ou ser registrado em um sistema de doação de órgãos.
    """)

    st.button('Ir para Etapas para Doação', type="primary", on_click=MudarD)

elif pagina == "Etapas para Doação":
    st.title("Etapas para Doação de Sangue, Medula Óssea e Órgãos")

    st.subheader("Etapas para Doação de Sangue")
    st.write("""
    1. Registro: O doador deve se registrar na unidade de coleta de sangue.
    2. Triagem: Avaliação de saúde e verificação dos requisitos.
    3. Coleta: O sangue é coletado de forma segura.
    4. Pós-Coleta: O doador recebe orientações sobre cuidados após a doação e um lanche.
    """)

    st.subheader("Etapas para Doação de Medula Óssea")
    st.write("""
    1. Cadastro: O interessado deve se cadastrar em um banco de sangue de medula óssea.
    2. Coleta de Amostra: O doador fornece uma amostra de sangue para tipagem HLA.
    3. Triagem: Avaliação médica e exames de saúde.
    4. Procedimento de Coleta: A medula é coletada por aferese ou punção.
    5. Acompanhamento: Monitoramento da saúde do doador após a doação.
    """)

    st.subheader("Etapas para Doação de Órgãos")
    st.write("""
    1. Cadastro: O interessado deve se cadastrar e informar a família.
    2. Consentimento: Garantir que a família concorda com a doação.
    3. Avaliação Médica: Análise da possibilidade de doação em caso de morte cerebral.
    4. Coleta: Os órgãos são removidos em ambiente cirúrgico.
    5. Acompanhamento: Monitoramento dos receptores dos órgãos.
    """)
    st.button('Ir para Elegibilidade de doação', type="primary", on_click=MudarE)


# Página para Elegibilidade de Doação 
if pagina == "Elegibilidade de Doação":
    st.title("Verificação de Elegibilidade para Doação de Sangue, Medula Óssea e Órgãos")

    # Seleção do tipo de doação
    tipo_doacao2 = st.selectbox("Selecione o tipo de doação", ["Sangue", "Medula Óssea", "Órgãos"])

    # Verificação para doação de sangue
    if tipo_doacao2 == "Sangue":
        st.subheader("Verificação de Condições de Saúde para Doação de Sangue")
        with st.form(key="form_elegibilidade_de_sangue"):
            hiv = st.radio("Já teve HIV?", ("Sim", "Não"))
            hepatite = st.radio("Já teve Hepatite?", ("Sim", "Não"))
            malaria = st.radio("Já teve Malária?", ("Sim", "Não"))
            doencas_cronicas = st.radio("Possui alguma doença crônica?", ("Sim", "Não"))

            if doencas_cronicas == "Sim":
                dc = st.multiselect('Quais doenças crônicas?', options=['Diabetes', 'Hipertensão', 'Asma', 'AVC', 'Obesidade', 'Depressão'])
                if dc:
                    st.write(f"Você selecionou: {', '.join(dc)}")

            if hepatite == "Sim":
                hp = st.multiselect('Qual tipo de Hepatite?', options=['A', 'B', 'C'])
                if hp:
                    st.write(f"Você teve Hepatite do tipo: {', '.join(hp)}")

            dst = st.multiselect('Você já teve alguma das seguintes Doenças Sexualmente Transmissíveis (DSTs)?',
                                 options=['Sífilis', 'Gonorreia', 'Herpes', 'HPV', 'Outras'])
            if dst:
                st.write(f"Você teve: {', '.join(dst)}")

            tuberculose = st.radio("Já teve Tuberculose?", ("Sim", "Não"))
            drogas = st.radio("Faz ou já fez uso de Drogas?", ("Sim", "Não"))
            if drogas == "Sim":
                dg = st.multiselect('Quais drogas?', options=['Maconha', 'Cocaína', 'Crack'])
                if dg:
                    st.write(f"Você fez uso de: {', '.join(dg)}")

            fumar = st.radio("Fuma?", ("Sim", "Não"))
            bebidas = st.radio("Faz uso de bebidas alcoólicas?", ("Sim", "Não"))

            verificar_button = st.form_submit_button(label="Verificar Elegibilidade")

            if verificar_button:
                if hiv == "Sim" or hepatite == "Sim" or malaria == "Sim" or doencas_cronicas == "Sim":
                    st.error("Infelizmente, você não pode doar sangue devido a uma condição médica.")
                else:
                    st.success("Você está apto(a) para doar sangue!")

    # Verificação para doação de medula óssea
    if tipo_doacao2 == "Medula Óssea":
        st.subheader("Verificação de Condições de Saúde para Medula Óssea")
        with st.form(key="form_medula"):
            idade_medula = st.number_input("Idade:", min_value=18, max_value=55)

            condicoes = st.multiselect("Você tem alguma das seguintes condições de saúde?",
                                       options=["Doenças autoimunes (ex: lupus, artrite reumatoide)",
                                                "Câncer", "Infecções crônicas (ex: HIV, hepatite)",
                                                "Doenças do sangue (ex: anemia, leucemia)",
                                                "Doenças cardíacas", "Diabetes", "Outras (especifique)"])

            tratamento = st.radio("Você está atualmente sob tratamento médico?", ("Sim", "Não"))
            transfusao = st.radio("Você já realizou uma transfusão de sangue?", ("Sim", "Não"))
            alergia = st.radio("Você é alérgico a algum medicamento ou substância?", ("Sim", "Não"))
            fumo = st.radio("Você fuma?", ("Sim", "Não"))
            alcool = st.radio("Você consome bebidas alcoólicas?", ("Sim", "Não"))
            drogas_recreativas = st.radio("Você faz uso de drogas recreativas?", ("Sim", "Não"))
            consentimento = st.radio("Você está disposto a realizar exames de compatibilidade?", ("Sim", "Não"))
            ciente = st.radio("Você está ciente de que poderá ser chamado para realizar a doação a qualquer momento, se compatível?", ("Sim", "Não"))
            
            submit_medula = st.form_submit_button("Verificar Elegibilidade para Doação de Medula Óssea")

            if submit_medula:
                apto = True

                # Verificação de condições médicas
                if "Doenças autoimunes (ex: lupus, artrite reumatoide)" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a doenças autoimunes.")
                    apto = False
                elif "Câncer" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a histórico de câncer.")
                    apto = False
                elif "Infecções crônicas (ex: HIV, hepatite)" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a infecções crônicas.")
                    apto = False
                elif "Doenças do sangue (ex: anemia, leucemia)" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a doenças do sangue.")
                    apto = False
                elif "Doenças cardíacas" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a doenças cardíacas.")
                    apto = False
                elif "Diabetes" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido ao histórico de diabetes.")
                    apto = False

                # Outras condições
                if tratamento == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea enquanto estiver em tratamento médico.")
                    apto = False
                if transfusao == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido a transfusão recente.")
                    apto = False
                if alergia == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido a alergias.")
                    apto = False
                if fumo == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido ao uso de tabaco.")
                    apto = False
                if alcool == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido ao consumo de álcool.")
                    apto = False
                if drogas_recreativas == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido ao uso de drogas recreativas.")
                    apto = False

                if apto:
                    st.success("Você está apto(a) para doar medula óssea!")

    # Verificação para doação de órgãos
    if tipo_doacao2 == "Órgãos":
        st.subheader("Verificação de Condições de Saúde para Doação de Órgãos")
        with st.form(key="form_orgaos"):
            idade_orgaos = st.number_input("Idade:", min_value=18)

            doencas_orgaos = st.multiselect("Você possui alguma das seguintes condições?",
                                            options=["Câncer", "Doença Cardíaca", "Diabetes",
                                                     "Doenças infecciosas (ex: HIV, Hepatite)", "Outras"])

            historico_cirurgico = st.radio("Você já passou por alguma cirurgia importante?", ("Sim", "Não"))
            habito_fumo = st.radio("Você fuma?", ("Sim", "Não"))
            uso_alcool = st.radio("Você consome álcool regularmente?", ("Sim", "Não"))
            consentimento_orgaos = st.radio("Você expressou sua vontade de ser doador para seus familiares?", ("Sim", "Não"))
            
            submit_orgaos = st.form_submit_button("Verificar Elegibilidade para Doação de Órgãos")

            if submit_orgaos:
                apto_orgaos = True

                # Verificação de condições médicas
                if "Câncer" in doencas_orgaos:
                    st.error("Você não está apto(a) para doar órgãos devido a histórico de câncer.")
                    apto_orgaos = False
                elif "Doenças infecciosas (ex: HIV, Hepatite)" in doencas_orgaos:
                    st.error("Você não está apto(a) para doar órgãos devido a doenças infecciosas.")
                    apto_orgaos = False

                # Outras condições
                if historico_cirurgico == "Sim":
                    st.error("Você não está apto(a) para doar órgãos devido ao histórico cirúrgico.")
                    apto_orgaos = False
                if habito_fumo == "Sim":
                    st.error("Você não está apto(a) para doar órgãos devido ao hábito de fumar.")
                    apto_orgaos = False
                if uso_alcool == "Sim":
                    st.error("Você não está apto(a) para doar órgãos devido ao uso regular de álcool.")
                    apto_orgaos = False

                if apto_orgaos:
                    st.success("Você está apto(a) para doar órgãos!")

    st.button('Ir para Agendamento', type="primary", on_click=MudarF)


elif pagina == "Agendamento":
    st.title("Agendamento de Doação de Sangue, Medula Óssea e Órgãos")

    # Formulário de Agendamento
    st.subheader("Agende Sua Doação")

    # Formulário de Agendamento
    with st.form("form_agendamento"):
        nome = st.text_input("Nome Completo")
        idade = st.number_input("Idade", min_value=16, max_value=120)
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        tipo_doacao = st.selectbox("Tipo de Doação", ["Sangue", "Medula Óssea", "Órgãos"])
        tipo_sanguineo = st.selectbox("Tipo Sanguíneo", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        local = st.text_input("Local da Doação")
        data_hora = st.date_input("Data da Doação", min_value=datetime.now().date())
        hora = st.time_input("Hora da Doação")
        notas = st.text_area("Notas (opcional)")

        submit_agendamento = st.form_submit_button("Agendar")

        if submit_agendamento:
            if not (nome and local):
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                salvar_agendamento(nome, idade, sexo, tipo_doacao, tipo_sanguineo, local, data_hora, hora, notas)
                st.success("Agendamento realizado com sucesso!")

                # Adicionar link para download do arquivo CSV
                st.markdown("### Baixe seus dados de agendamento")
                with open("agendamentos.csv", "rb") as file:
                    st.download_button(
                        label="Baixar agendamentos",
                        data=file,
                        file_name="agendamentos.csv",
                        mime="text/csv"
                    )

    st.button('Ir para Cadastro para Voluntários', type="primary", on_click=MudarG)

elif pagina == "Cadastro para Voluntários":
    st.title("Cadastro para Voluntários")

    with st.form("form_voluntarios"):
        nome_voluntario = st.text_input("Nome Completo")
        idade_voluntario = st.number_input("Idade", min_value=16, max_value=120)
        sexo_voluntario = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        contato = st.text_input("Contato (e-mail ou telefone)")
        interesse = st.multiselect("Áreas de Interesse", 
                                   ["Doação de Sangue", "Doação de Medula Óssea", "Doação de Órgãos", "Eventos", "Campanhas Educativas"])
        submit_voluntario = st.form_submit_button("Cadastrar")

        if submit_voluntario:
            if not (nome_voluntario and contato and interesse):
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                salvar_voluntario(nome_voluntario, idade_voluntario, sexo_voluntario, contato, ", ".join(interesse))
                st.success("Cadastro realizado com sucesso!")

                # Adicionar link para download do arquivo CSV
                st.markdown("### Baixe seus dados de voluntários")
                with open("voluntarios.csv", "rb") as file:
                    st.download_button(
                        label="Baixar cadastro de voluntários",
                        data=file,
                        file_name="voluntarios.csv",
                        mime="text/csv"
                    )

    st.button('Ir para Vídeo', type="primary", on_click=MudarH)



elif pagina == "Vídeo":
    st.title("Vídeo Explicativo sobre a Doação de Sangue")
    st.write("Aqui pode ser exibido um vídeo sobre o processo de doação.")
    st.video("Vídeo.mp4")
    st.button('Ir para Fim', type="primary", on_click=MudarI)

elif pagina == "Fim":
    add_bg_image("imagemfim.png")
    st.button('Voltar para Home', type="primary", on_click=MudarA)import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime

# Função para adicionar imagem de fundo na página Home
def add_bg_image(image_path):
    try:
        img = Image.open(image_path)
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"Imagem não encontrada em {image_path}. Verifique o caminho.")

# Função para salvar os dados em um CSV (Doador)
def salvar_doador(nome, idade, sexo, tipo_sanguineo):
    arquivo = "doadores.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Tipo Sanguíneo"])
    novo_doador = pd.DataFrame([[nome, idade, sexo, tipo_sanguineo]], columns=["Nome", "Idade", "Sexo", "Tipo Sanguíneo"])
    df = pd.concat([df, novo_doador], ignore_index=True)
    df.to_csv(arquivo, index=False)

# Função para salvar o agendamento em CSV
def salvar_agendamento(nome, idade, sexo, tipo_doacao, tipo_sanguineo, local, data_hora, hora, notas):
    df_agendamento = pd.DataFrame({
        "Nome": [nome],
        "Idade": [idade],
        "Sexo": [sexo],
        "Tipo Sanguíneo": [tipo_sanguineo],
        "Local": [local],
        "Data": [data_hora],
        "Hora": [hora],
        "Notas": [notas if notas else "Nenhuma"]
    })
    df_agendamento.to_csv('agendamentos.csv', index=False, mode='a', header=False)

# Função para salvar voluntários em CSV
def salvar_voluntario(nome, idade, sexo, contato, interesse):
    arquivo = "voluntarios.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    novo_voluntario = pd.DataFrame([[nome, idade, sexo, contato, interesse]], columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    df = pd.concat([df, novo_voluntario], ignore_index=True)
    df.to_csv(arquivo, index=False)

# Inicializa as opções de navegação no estado da sessão
if "Ops" not in st.session_state:
    st.session_state.ops = [
        "Home", "Importância", "Requisitos para Doação",
        "Etapas para Doação", "Elegibilidade de Doação", 
        'Agendamento', "Cadastro para Voluntários", 'Vídeo', 'Fim'
    ]

# Barra lateral para navegação
with st.sidebar:
    pagina = st.radio('Navegação', st.session_state.ops, key='Nav')

def MudarA():
    st.session_state.Nav = 'Home'
def MudarB():
    st.session_state.Nav = 'Importância'
def MudarC():
    st.session_state.Nav = 'Requisitos para Doação'
def MudarD():
    st.session_state.Nav = 'Etapas para Doação'
def MudarE():
    st.session_state.Nav = 'Elegibilidade de Doação'
def MudarF():
    st.session_state.Nav = 'Agendamento'  
def MudarG():
    st.session_state.Nav = 'Cadastro para Voluntários'
def MudarH():
    st.session_state.Nav = 'Vídeo'
def MudarI():
    st.session_state.Nav = 'Fim'


# Interface Streamlit
st.title("Sistema de Doação de Sangue, Medula óssea e Órgãos")

# Lógica para exibir a página selecionada
if pagina == "Home":
    st.subheader("Doação de Sangue")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi instituída pela 
    Organização Mundial da Saúde (OMS) para lembrar da importância da conscientização quanto à 
    necessidade da doação de sangue e como uma forma de agradecimento aos doadores.""")
    
    st.subheader("Doação de Órgãos")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi instituída pela 
    Organização Mundial da Saúde (OMS) para lembrar da importância da conscientização quanto à 
    necessidade da doação de sangue e como uma forma de agradecimento aos doadores.""")

    st.subheader("Doação de Medula Óssea")
    st.write("""O Dia Mundial da Doação de Medula Óssea é celebrado no terceiro sábado de setembro. Essa data, estabelecida pela World Marrow Donor Association (WMDA), tem como objetivo aumentar a conscientização sobre a doação de medula óssea e promover o registro de novos doadores. O dia também destaca a importância de contar com uma base diversificada de doadores cadastrados, já que a compatibilidade entre doadores e receptores é complexa e depende de fatores genéticos.""")
    add_bg_image("doe.png")
    st.button('Ir para Importância', type="primary", on_click=MudarB)

elif pagina == "Importância":
    st.title("A Importância da Doação de Sangue, Medula Óssea e Órgãos")

    # Explicação sobre a importância da doação de sangue
    st.subheader("A Importância da Doação de Sangue")
    st.write("""A doação de sangue é um ato de solidariedade e amor ao próximo que ajuda a salvar inúmeras vidas diariamente. O sangue doado é essencial para tratamentos médicos, como em cirurgias, acidentes e no suporte a pacientes com doenças graves, como câncer e anemias. Cada doação pode beneficiar até três pessoas, pois o sangue é separado em componentes (plasma, plaquetas e glóbulos vermelhos), utilizados para necessidades distintas.""")
    
    st.subheader("Qrcode com informações em tempo real")
    st.write("""Acessando este qrcode você tem acesso a informações em tempo real sobre o estoque de sangue""")
    st.image("qrr.png")

    # Explicação sobre a importância da doação de medula óssea
    st.subheader("A Importância da Doação de Medula Óssea")
    st.write("""A doação de medula óssea é vital para pacientes com doenças hematológicas graves, como leucemia, linfoma e anemia aplástica. A medula óssea, responsável pela produção de células sanguíneas, precisa ser substituída por uma saudável em casos de danos graves. O procedimento de doação é seguro e pode salvar vidas, especialmente em crianças e jovens. Registre-se em bancos de medula, como o REDOME e HEMOBRAZ, e faça a diferença.""")

    # Explicação sobre a importância da doação de órgãos
    st.subheader("A Importância da Doação de Órgãos")
    st.write("""A doação de órgãos é uma forma de garantir que pessoas com falência de órgãos tenham uma segunda chance de vida. Um único doador pode salvar várias vidas, doando órgãos como coração, rins, fígado e pulmões, além de tecidos como córnea e pele. A decisão de ser um doador deve ser informada à família, pois o consentimento é fundamental para que a doação seja realizada.""")

    st.button('Ir para Requisitos para Doação', type="primary", on_click=MudarC)

# Explicação sobre a importância da doação de órgãos
elif pagina == "Requisitos para Doação":
    st.title("Requisitos para Doação de Sangue")
    
    # Adicionando logs para verificar se as partes estão sendo executadas
    st.write("Verificando requisitos de doação de sangue...")
    st.write(""" 
    - Apresentar boa condição de saúde.
    - Ter entre 16 e 69 anos.
    - Pesar no mínimo 51 quilos.
    - Estar descansado (dormido pelo menos seis horas nas 24 horas anteriores).
    - Estar alimentado (evitar alimentação gordurosa nas 4 horas anteriores).
    - Apresentar documento original com foto recente.
    """)
    st.write(""" 
    Fatores que podem impedir a doação:
    - Doenças crônicas, HIV, Hepatite, Malária.
    - Uso de drogas ilícitas ou medicamentos.
    """)

    # Requisitos sobre a importância da doação de Medula Óssea
    st.subheader("Requisitos para Doação de Medula Óssea")
    st.write("Verificando requisitos de medula óssea...")
    st.write(""" 
    - Ter entre 18 e 55 anos.
    - Estar em boas condições de saúde.
    - Não ter doenças autoimunes, HIV, Hepatite ou outras doenças graves.
    - Não ter histórico de câncer.
    - Estar disposto a se cadastrar e realizar os exames necessários.
    """)

    # Requisitos sobre a importância da doação de Órgãos
    st.subheader("Requisitos para Doação de Órgãos")
    st.write("Verificando requisitos de doação de órgãos...")
    st.write(""" 
    - Ser maior de idade (no Brasil, é necessário ter 18 anos).
    - Não ter doenças que impeçam a doação (ex: câncer, doenças infecciosas).
    - Informar a família sobre a decisão de ser doador.
    - Assinar o documento de doação ou ser registrado em um sistema de doação de órgãos.
    """)

    st.button('Ir para Etapas para Doação', type="primary", on_click=MudarD)

elif pagina == "Etapas para Doação":
    st.title("Etapas para Doação de Sangue, Medula Óssea e Órgãos")

    st.subheader("Etapas para Doação de Sangue")
    st.write("""
    1. Registro: O doador deve se registrar na unidade de coleta de sangue.
    2. Triagem: Avaliação de saúde e verificação dos requisitos.
    3. Coleta: O sangue é coletado de forma segura.
    4. Pós-Coleta: O doador recebe orientações sobre cuidados após a doação e um lanche.
    """)

    st.subheader("Etapas para Doação de Medula Óssea")
    st.write("""
    1. Cadastro: O interessado deve se cadastrar em um banco de sangue de medula óssea.
    2. Coleta de Amostra: O doador fornece uma amostra de sangue para tipagem HLA.
    3. Triagem: Avaliação médica e exames de saúde.
    4. Procedimento de Coleta: A medula é coletada por aferese ou punção.
    5. Acompanhamento: Monitoramento da saúde do doador após a doação.
    """)

    st.subheader("Etapas para Doação de Órgãos")
    st.write("""
    1. Cadastro: O interessado deve se cadastrar e informar a família.
    2. Consentimento: Garantir que a família concorda com a doação.
    3. Avaliação Médica: Análise da possibilidade de doação em caso de morte cerebral.
    4. Coleta: Os órgãos são removidos em ambiente cirúrgico.
    5. Acompanhamento: Monitoramento dos receptores dos órgãos.
    """)
    st.button('Ir para Elegibilidade de doação', type="primary", on_click=MudarE)


# Página para Elegibilidade de Doação 
if pagina == "Elegibilidade de Doação":
    st.title("Verificação de Elegibilidade para Doação de Sangue, Medula Óssea e Órgãos")

    # Seleção do tipo de doação
    tipo_doacao2 = st.selectbox("Selecione o tipo de doação", ["Sangue", "Medula Óssea", "Órgãos"])

    # Verificação para doação de sangue
    if tipo_doacao2 == "Sangue":
        st.subheader("Verificação de Condições de Saúde para Doação de Sangue")
        with st.form(key="form_elegibilidade_de_sangue"):
            hiv = st.radio("Já teve HIV?", ("Sim", "Não"))
            hepatite = st.radio("Já teve Hepatite?", ("Sim", "Não"))
            malaria = st.radio("Já teve Malária?", ("Sim", "Não"))
            doencas_cronicas = st.radio("Possui alguma doença crônica?", ("Sim", "Não"))

            if doencas_cronicas == "Sim":
                dc = st.multiselect('Quais doenças crônicas?', options=['Diabetes', 'Hipertensão', 'Asma', 'AVC', 'Obesidade', 'Depressão'])
                if dc:
                    st.write(f"Você selecionou: {', '.join(dc)}")

            if hepatite == "Sim":
                hp = st.multiselect('Qual tipo de Hepatite?', options=['A', 'B', 'C'])
                if hp:
                    st.write(f"Você teve Hepatite do tipo: {', '.join(hp)}")

            dst = st.multiselect('Você já teve alguma das seguintes Doenças Sexualmente Transmissíveis (DSTs)?',
                                 options=['Sífilis', 'Gonorreia', 'Herpes', 'HPV', 'Outras'])
            if dst:
                st.write(f"Você teve: {', '.join(dst)}")

            tuberculose = st.radio("Já teve Tuberculose?", ("Sim", "Não"))
            drogas = st.radio("Faz ou já fez uso de Drogas?", ("Sim", "Não"))
            if drogas == "Sim":
                dg = st.multiselect('Quais drogas?', options=['Maconha', 'Cocaína', 'Crack'])
                if dg:
                    st.write(f"Você fez uso de: {', '.join(dg)}")

            fumar = st.radio("Fuma?", ("Sim", "Não"))
            bebidas = st.radio("Faz uso de bebidas alcoólicas?", ("Sim", "Não"))

            verificar_button = st.form_submit_button(label="Verificar Elegibilidade")

            if verificar_button:
                if hiv == "Sim" or hepatite == "Sim" or malaria == "Sim" or doencas_cronicas == "Sim":
                    st.error("Infelizmente, você não pode doar sangue devido a uma condição médica.")
                else:
                    st.success("Você está apto(a) para doar sangue!")

    # Verificação para doação de medula óssea
    if tipo_doacao2 == "Medula Óssea":
        st.subheader("Verificação de Condições de Saúde para Medula Óssea")
        with st.form(key="form_medula"):
            idade_medula = st.number_input("Idade:", min_value=18, max_value=55)

            condicoes = st.multiselect("Você tem alguma das seguintes condições de saúde?",
                                       options=["Doenças autoimunes (ex: lupus, artrite reumatoide)",
                                                "Câncer", "Infecções crônicas (ex: HIV, hepatite)",
                                                "Doenças do sangue (ex: anemia, leucemia)",
                                                "Doenças cardíacas", "Diabetes", "Outras (especifique)"])

            tratamento = st.radio("Você está atualmente sob tratamento médico?", ("Sim", "Não"))
            transfusao = st.radio("Você já realizou uma transfusão de sangue?", ("Sim", "Não"))
            alergia = st.radio("Você é alérgico a algum medicamento ou substância?", ("Sim", "Não"))
            fumo = st.radio("Você fuma?", ("Sim", "Não"))
            alcool = st.radio("Você consome bebidas alcoólicas?", ("Sim", "Não"))
            drogas_recreativas = st.radio("Você faz uso de drogas recreativas?", ("Sim", "Não"))
            consentimento = st.radio("Você está disposto a realizar exames de compatibilidade?", ("Sim", "Não"))
            ciente = st.radio("Você está ciente de que poderá ser chamado para realizar a doação a qualquer momento, se compatível?", ("Sim", "Não"))
            
            submit_medula = st.form_submit_button("Verificar Elegibilidade para Doação de Medula Óssea")

            if submit_medula:
                apto = True

                # Verificação de condições médicas
                if "Doenças autoimunes (ex: lupus, artrite reumatoide)" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a doenças autoimunes.")
                    apto = False
                elif "Câncer" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a histórico de câncer.")
                    apto = False
                elif "Infecções crônicas (ex: HIV, hepatite)" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a infecções crônicas.")
                    apto = False
                elif "Doenças do sangue (ex: anemia, leucemia)" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a doenças do sangue.")
                    apto = False
                elif "Doenças cardíacas" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido a doenças cardíacas.")
                    apto = False
                elif "Diabetes" in condicoes:
                    st.error("Você não está apto(a) para doar medula óssea devido ao histórico de diabetes.")
                    apto = False

                # Outras condições
                if tratamento == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea enquanto estiver em tratamento médico.")
                    apto = False
                if transfusao == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido a transfusão recente.")
                    apto = False
                if alergia == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido a alergias.")
                    apto = False
                if fumo == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido ao uso de tabaco.")
                    apto = False
                if alcool == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido ao consumo de álcool.")
                    apto = False
                if drogas_recreativas == "Sim":
                    st.error("Você não está apto(a) para doar medula óssea devido ao uso de drogas recreativas.")
                    apto = False

                if apto:
                    st.success("Você está apto(a) para doar medula óssea!")

    # Verificação para doação de órgãos
    if tipo_doacao2 == "Órgãos":
        st.subheader("Verificação de Condições de Saúde para Doação de Órgãos")
        with st.form(key="form_orgaos"):
            idade_orgaos = st.number_input("Idade:", min_value=18)

            doencas_orgaos = st.multiselect("Você possui alguma das seguintes condições?",
                                            options=["Câncer", "Doença Cardíaca", "Diabetes",
                                                     "Doenças infecciosas (ex: HIV, Hepatite)", "Outras"])

            historico_cirurgico = st.radio("Você já passou por alguma cirurgia importante?", ("Sim", "Não"))
            habito_fumo = st.radio("Você fuma?", ("Sim", "Não"))
            uso_alcool = st.radio("Você consome álcool regularmente?", ("Sim", "Não"))
            consentimento_orgaos = st.radio("Você expressou sua vontade de ser doador para seus familiares?", ("Sim", "Não"))
            
            submit_orgaos = st.form_submit_button("Verificar Elegibilidade para Doação de Órgãos")

            if submit_orgaos:
                apto_orgaos = True

                # Verificação de condições médicas
                if "Câncer" in doencas_orgaos:
                    st.error("Você não está apto(a) para doar órgãos devido a histórico de câncer.")
                    apto_orgaos = False
                elif "Doenças infecciosas (ex: HIV, Hepatite)" in doencas_orgaos:
                    st.error("Você não está apto(a) para doar órgãos devido a doenças infecciosas.")
                    apto_orgaos = False

                # Outras condições
                if historico_cirurgico == "Sim":
                    st.error("Você não está apto(a) para doar órgãos devido ao histórico cirúrgico.")
                    apto_orgaos = False
                if habito_fumo == "Sim":
                    st.error("Você não está apto(a) para doar órgãos devido ao hábito de fumar.")
                    apto_orgaos = False
                if uso_alcool == "Sim":
                    st.error("Você não está apto(a) para doar órgãos devido ao uso regular de álcool.")
                    apto_orgaos = False

                if apto_orgaos:
                    st.success("Você está apto(a) para doar órgãos!")

    st.button('Ir para Agendamento', type="primary", on_click=MudarF)


elif pagina == "Agendamento":
    st.title("Agendamento de Doação de Sangue, Medula Óssea e Órgãos")

    # Formulário de Agendamento
    st.subheader("Agende Sua Doação")

    # Formulário de Agendamento
    with st.form("form_agendamento"):
        nome = st.text_input("Nome Completo")
        idade = st.number_input("Idade", min_value=16, max_value=120)
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        tipo_doacao = st.selectbox("Tipo de Doação", ["Sangue", "Medula Óssea", "Órgãos"])
        tipo_sanguineo = st.selectbox("Tipo Sanguíneo", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        local = st.text_input("Local da Doação")
        data_hora = st.date_input("Data da Doação", min_value=datetime.now().date())
        hora = st.time_input("Hora da Doação")
        notas = st.text_area("Notas (opcional)")

        submit_agendamento = st.form_submit_button("Agendar")

        if submit_agendamento:
            if not (nome and local):
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                salvar_agendamento(nome, idade, sexo, tipo_doacao, tipo_sanguineo, local, data_hora, hora, notas)
                st.success("Agendamento realizado com sucesso!")

                # Adicionar link para download do arquivo CSV
                st.markdown("### Baixe seus dados de agendamento")
                with open("agendamentos.csv", "rb") as file:
                    st.download_button(
                        label="Baixar agendamentos",
                        data=file,
                        file_name="agendamentos.csv",
                        mime="text/csv"
                    )

    st.button('Ir para Cadastro para Voluntários', type="primary", on_click=MudarG)

elif pagina == "Cadastro para Voluntários":
    st.title("Cadastro para Voluntários")

    with st.form("form_voluntarios"):
        nome_voluntario = st.text_input("Nome Completo")
        idade_voluntario = st.number_input("Idade", min_value=16, max_value=120)
        sexo_voluntario = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        contato = st.text_input("Contato (e-mail ou telefone)")
        interesse = st.multiselect("Áreas de Interesse", 
                                   ["Doação de Sangue", "Doação de Medula Óssea", "Doação de Órgãos", "Eventos", "Campanhas Educativas"])
        submit_voluntario = st.form_submit_button("Cadastrar")

        if submit_voluntario:
            if not (nome_voluntario and contato and interesse):
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                salvar_voluntario(nome_voluntario, idade_voluntario, sexo_voluntario, contato, ", ".join(interesse))
                st.success("Cadastro realizado com sucesso!")

                # Adicionar link para download do arquivo CSV
                st.markdown("### Baixe seus dados de voluntários")
                with open("voluntarios.csv", "rb") as file:
                    st.download_button(
                        label="Baixar cadastro de voluntários",
                        data=file,
                        file_name="voluntarios.csv",
                        mime="text/csv"
                    )

    st.button('Ir para Vídeo', type="primary", on_click=MudarH)



elif pagina == "Vídeo":
    st.title("Vídeo Explicativo sobre a Doação de Sangue")
    st.write("Aqui pode ser exibido um vídeo sobre o processo de doação.")
    st.video("Vídeo.mp4")
    st.button('Ir para Fim', type="primary", on_click=MudarI)

elif pagina == "Fim":
    add_bg_image("imagemfim.png")
    st.button('Voltar para Home', type="primary", on_click=MudarA)
