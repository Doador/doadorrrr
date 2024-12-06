import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime

# Fun��o para adicionar imagem de fundo na p�gina Home
def add_bg_image(image_path):
    try:
        img = Image.open(image_path)
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"Imagem n�o encontrada em {image_path}. Verifique o caminho.")

# Fun��o para salvar os dados em um CSV (Doador)
def salvar_doador(nome, idade, sexo, tipo_sanguineo):
    arquivo = "doadores.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Tipo Sangu�neo"])
    novo_doador = pd.DataFrame([[nome, idade, sexo, tipo_sanguineo]], columns=["Nome", "Idade", "Sexo", "Tipo Sangu�neo"])
    df = pd.concat([df, novo_doador], ignore_index=True)
    df.to_csv(arquivo, index=False)

# Fun��o para salvar o agendamento em CSV
def salvar_agendamento(nome, idade, sexo, tipo_doacao, tipo_sanguineo, local, data_hora, hora, notas):
    df_agendamento = pd.DataFrame({
        "Nome": [nome],
        "Idade": [idade],
        "Sexo": [sexo],
        "Tipo Sangu�neo": [tipo_sanguineo],
        "Local": [local],
        "Data": [data_hora],
        "Hora": [hora],
        "Notas": [notas if notas else "Nenhuma"]
    })
    df_agendamento.to_csv('agendamentos.csv', index=False, mode='a', header=False)

# Fun��o para salvar volunt�rios em CSV
def salvar_voluntario(nome, idade, sexo, contato, interesse):
    arquivo = "voluntarios.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    novo_voluntario = pd.DataFrame([[nome, idade, sexo, contato, interesse]], columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    df = pd.concat([df, novo_voluntario], ignore_index=True)
    df.to_csv(arquivo, index=False)

# Inicializa as op��es de navega��o no estado da sess�o
if "Ops" not in st.session_state:
    st.session_state.ops = [
        "Home", "Import�ncia", "Requisitos para Doa��o",
        "Etapas para Doa��o", "Elegibilidade de Doa��o", 
        'Agendamento', "Cadastro para Volunt�rios", 'V�deo', 'Fim'
    ]

# Barra lateral para navega��o
with st.sidebar:
    pagina = st.radio('Navega��o', st.session_state.ops, key='Nav')

def MudarA():
    st.session_state.Nav = 'Home'
def MudarB():
    st.session_state.Nav = 'Import�ncia'
def MudarC():
    st.session_state.Nav = 'Requisitos para Doa��o'
def MudarD():
    st.session_state.Nav = 'Etapas para Doa��o'
def MudarE():
    st.session_state.Nav = 'Elegibilidade de Doa��o'
def MudarF():
    st.session_state.Nav = 'Agendamento'  
def MudarG():
    st.session_state.Nav = 'Cadastro para Volunt�rios'
def MudarH():
    st.session_state.Nav = 'V�deo'
def MudarI():
    st.session_state.Nav = 'Fim'


# Interface Streamlit
st.title("Sistema de Doa��o de Sangue, Medula �ssea e �rg�os")

# L�gica para exibir a p�gina selecionada
if pagina == "Home":
    st.subheader("Doa��o de Sangue")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi institu�da pela 
    Organiza��o Mundial da Sa�de (OMS) para lembrar da import�ncia da conscientiza��o quanto � 
    necessidade da doa��o de sangue e como uma forma de agradecimento aos doadores.""")
    
    st.subheader("Doa��o de �rg�os")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi institu�da pela 
    Organiza��o Mundial da Sa�de (OMS) para lembrar da import�ncia da conscientiza��o quanto � 
    necessidade da doa��o de sangue e como uma forma de agradecimento aos doadores.""")

    st.subheader("Doa��o de Medula �ssea")
    st.write("""O Dia Mundial da Doa��o de Medula �ssea � celebrado no terceiro s�bado de setembro. Essa data, estabelecida pela World Marrow Donor Association (WMDA), tem como objetivo aumentar a conscientiza��o sobre a doa��o de medula �ssea e promover o registro de novos doadores. O dia tamb�m destaca a import�ncia de contar com uma base diversificada de doadores cadastrados, j� que a compatibilidade entre doadores e receptores � complexa e depende de fatores gen�ticos.""")
    add_bg_image("doe.png")
    st.button('Ir para Import�ncia', type="primary", on_click=MudarB)

elif pagina == "Import�ncia":
    st.title("A Import�ncia da Doa��o de Sangue, Medula �ssea e �rg�os")

    # Explica��o sobre a import�ncia da doa��o de sangue
    st.subheader("A Import�ncia da Doa��o de Sangue")
    st.write("""A doa��o de sangue � um ato de solidariedade e amor ao pr�ximo que ajuda a salvar in�meras vidas diariamente. O sangue doado � essencial para tratamentos m�dicos, como em cirurgias, acidentes e no suporte a pacientes com doen�as graves, como c�ncer e anemias. Cada doa��o pode beneficiar at� tr�s pessoas, pois o sangue � separado em componentes (plasma, plaquetas e gl�bulos vermelhos), utilizados para necessidades distintas.""")
    
    st.subheader("Qrcode com informa��es em tempo real")
    st.write("""Acessando este qrcode voc� tem acesso a informa��es em tempo real sobre o estoque de sangue""")
    st.image("qrr.png")

    # Explica��o sobre a import�ncia da doa��o de medula �ssea
    st.subheader("A Import�ncia da Doa��o de Medula �ssea")
    st.write("""A doa��o de medula �ssea � vital para pacientes com doen�as hematol�gicas graves, como leucemia, linfoma e anemia apl�stica. A medula �ssea, respons�vel pela produ��o de c�lulas sangu�neas, precisa ser substitu�da por uma saud�vel em casos de danos graves. O procedimento de doa��o � seguro e pode salvar vidas, especialmente em crian�as e jovens. Registre-se em bancos de medula, como o REDOME e HEMOBRAZ, e fa�a a diferen�a.""")

    # Explica��o sobre a import�ncia da doa��o de �rg�os
    st.subheader("A Import�ncia da Doa��o de �rg�os")
    st.write("""A doa��o de �rg�os � uma forma de garantir que pessoas com fal�ncia de �rg�os tenham uma segunda chance de vida. Um �nico doador pode salvar v�rias vidas, doando �rg�os como cora��o, rins, f�gado e pulm�es, al�m de tecidos como c�rnea e pele. A decis�o de ser um doador deve ser informada � fam�lia, pois o consentimento � fundamental para que a doa��o seja realizada.""")

    st.button('Ir para Requisitos para Doa��o', type="primary", on_click=MudarC)

# Explica��o sobre a import�ncia da doa��o de �rg�os
elif pagina == "Requisitos para Doa��o":
    st.title("Requisitos para Doa��o de Sangue")
    
    # Adicionando logs para verificar se as partes est�o sendo executadas
    st.write("Verificando requisitos de doa��o de sangue...")
    st.write(""" 
    - Apresentar boa condi��o de sa�de.
    - Ter entre 16 e 69 anos.
    - Pesar no m�nimo 51 quilos.
    - Estar descansado (dormido pelo menos seis horas nas 24 horas anteriores).
    - Estar alimentado (evitar alimenta��o gordurosa nas 4 horas anteriores).
    - Apresentar documento original com foto recente.
    """)
    st.write(""" 
    Fatores que podem impedir a doa��o:
    - Doen�as cr�nicas, HIV, Hepatite, Mal�ria.
    - Uso de drogas il�citas ou medicamentos.
    """)

    # Requisitos sobre a import�ncia da doa��o de Medula �ssea
    st.subheader("Requisitos para Doa��o de Medula �ssea")
    st.write("Verificando requisitos de medula �ssea...")
    st.write(""" 
    - Ter entre 18 e 55 anos.
    - Estar em boas condi��es de sa�de.
    - N�o ter doen�as autoimunes, HIV, Hepatite ou outras doen�as graves.
    - N�o ter hist�rico de c�ncer.
    - Estar disposto a se cadastrar e realizar os exames necess�rios.
    """)

    # Requisitos sobre a import�ncia da doa��o de �rg�os
    st.subheader("Requisitos para Doa��o de �rg�os")
    st.write("Verificando requisitos de doa��o de �rg�os...")
    st.write(""" 
    - Ser maior de idade (no Brasil, � necess�rio ter 18 anos).
    - N�o ter doen�as que impe�am a doa��o (ex: c�ncer, doen�as infecciosas).
    - Informar a fam�lia sobre a decis�o de ser doador.
    - Assinar o documento de doa��o ou ser registrado em um sistema de doa��o de �rg�os.
    """)

    st.button('Ir para Etapas para Doa��o', type="primary", on_click=MudarD)

elif pagina == "Etapas para Doa��o":
    st.title("Etapas para Doa��o de Sangue, Medula �ssea e �rg�os")

    st.subheader("Etapas para Doa��o de Sangue")
    st.write("""
    1. Registro: O doador deve se registrar na unidade de coleta de sangue.
    2. Triagem: Avalia��o de sa�de e verifica��o dos requisitos.
    3. Coleta: O sangue � coletado de forma segura.
    4. P�s-Coleta: O doador recebe orienta��es sobre cuidados ap�s a doa��o e um lanche.
    """)

    st.subheader("Etapas para Doa��o de Medula �ssea")
    st.write("""
    1. Cadastro: O interessado deve se cadastrar em um banco de sangue de medula �ssea.
    2. Coleta de Amostra: O doador fornece uma amostra de sangue para tipagem HLA.
    3. Triagem: Avalia��o m�dica e exames de sa�de.
    4. Procedimento de Coleta: A medula � coletada por aferese ou pun��o.
    5. Acompanhamento: Monitoramento da sa�de do doador ap�s a doa��o.
    """)

    st.subheader("Etapas para Doa��o de �rg�os")
    st.write("""
    1. Cadastro: O interessado deve se cadastrar e informar a fam�lia.
    2. Consentimento: Garantir que a fam�lia concorda com a doa��o.
    3. Avalia��o M�dica: An�lise da possibilidade de doa��o em caso de morte cerebral.
    4. Coleta: Os �rg�os s�o removidos em ambiente cir�rgico.
    5. Acompanhamento: Monitoramento dos receptores dos �rg�os.
    """)
    st.button('Ir para Elegibilidade de doa��o', type="primary", on_click=MudarE)


# P�gina para Elegibilidade de Doa��o 
if pagina == "Elegibilidade de Doa��o":
    st.title("Verifica��o de Elegibilidade para Doa��o de Sangue, Medula �ssea e �rg�os")

    # Sele��o do tipo de doa��o
    tipo_doacao2 = st.selectbox("Selecione o tipo de doa��o", ["Sangue", "Medula �ssea", "�rg�os"])

    # Verifica��o para doa��o de sangue
    if tipo_doacao2 == "Sangue":
        st.subheader("Verifica��o de Condi��es de Sa�de para Doa��o de Sangue")
        with st.form(key="form_elegibilidade_de_sangue"):
            hiv = st.radio("J� teve HIV?", ("Sim", "N�o"))
            hepatite = st.radio("J� teve Hepatite?", ("Sim", "N�o"))
            malaria = st.radio("J� teve Mal�ria?", ("Sim", "N�o"))
            doencas_cronicas = st.radio("Possui alguma doen�a cr�nica?", ("Sim", "N�o"))

            if doencas_cronicas == "Sim":
                dc = st.multiselect('Quais doen�as cr�nicas?', options=['Diabetes', 'Hipertens�o', 'Asma', 'AVC', 'Obesidade', 'Depress�o'])
                if dc:
                    st.write(f"Voc� selecionou: {', '.join(dc)}")

            if hepatite == "Sim":
                hp = st.multiselect('Qual tipo de Hepatite?', options=['A', 'B', 'C'])
                if hp:
                    st.write(f"Voc� teve Hepatite do tipo: {', '.join(hp)}")

            dst = st.multiselect('Voc� j� teve alguma das seguintes Doen�as Sexualmente Transmiss�veis (DSTs)?',
                                 options=['S�filis', 'Gonorreia', 'Herpes', 'HPV', 'Outras'])
            if dst:
                st.write(f"Voc� teve: {', '.join(dst)}")

            tuberculose = st.radio("J� teve Tuberculose?", ("Sim", "N�o"))
            drogas = st.radio("Faz ou j� fez uso de Drogas?", ("Sim", "N�o"))
            if drogas == "Sim":
                dg = st.multiselect('Quais drogas?', options=['Maconha', 'Coca�na', 'Crack'])
                if dg:
                    st.write(f"Voc� fez uso de: {', '.join(dg)}")

            fumar = st.radio("Fuma?", ("Sim", "N�o"))
            bebidas = st.radio("Faz uso de bebidas alco�licas?", ("Sim", "N�o"))

            verificar_button = st.form_submit_button(label="Verificar Elegibilidade")

            if verificar_button:
                if hiv == "Sim" or hepatite == "Sim" or malaria == "Sim" or doencas_cronicas == "Sim":
                    st.error("Infelizmente, voc� n�o pode doar sangue devido a uma condi��o m�dica.")
                else:
                    st.success("Voc� est� apto(a) para doar sangue!")

    # Verifica��o para doa��o de medula �ssea
    if tipo_doacao2 == "Medula �ssea":
        st.subheader("Verifica��o de Condi��es de Sa�de para Medula �ssea")
        with st.form(key="form_medula"):
            idade_medula = st.number_input("Idade:", min_value=18, max_value=55)

            condicoes = st.multiselect("Voc� tem alguma das seguintes condi��es de sa�de?",
                                       options=["Doen�as autoimunes (ex: lupus, artrite reumatoide)",
                                                "C�ncer", "Infec��es cr�nicas (ex: HIV, hepatite)",
                                                "Doen�as do sangue (ex: anemia, leucemia)",
                                                "Doen�as card�acas", "Diabetes", "Outras (especifique)"])

            tratamento = st.radio("Voc� est� atualmente sob tratamento m�dico?", ("Sim", "N�o"))
            transfusao = st.radio("Voc� j� realizou uma transfus�o de sangue?", ("Sim", "N�o"))
            alergia = st.radio("Voc� � al�rgico a algum medicamento ou subst�ncia?", ("Sim", "N�o"))
            fumo = st.radio("Voc� fuma?", ("Sim", "N�o"))
            alcool = st.radio("Voc� consome bebidas alco�licas?", ("Sim", "N�o"))
            drogas_recreativas = st.radio("Voc� faz uso de drogas recreativas?", ("Sim", "N�o"))
            consentimento = st.radio("Voc� est� disposto a realizar exames de compatibilidade?", ("Sim", "N�o"))
            ciente = st.radio("Voc� est� ciente de que poder� ser chamado para realizar a doa��o a qualquer momento, se compat�vel?", ("Sim", "N�o"))
            
            submit_medula = st.form_submit_button("Verificar Elegibilidade para Doa��o de Medula �ssea")

            if submit_medula:
                apto = True

                # Verifica��o de condi��es m�dicas
                if "Doen�as autoimunes (ex: lupus, artrite reumatoide)" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a doen�as autoimunes.")
                    apto = False
                elif "C�ncer" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a hist�rico de c�ncer.")
                    apto = False
                elif "Infec��es cr�nicas (ex: HIV, hepatite)" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a infec��es cr�nicas.")
                    apto = False
                elif "Doen�as do sangue (ex: anemia, leucemia)" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a doen�as do sangue.")
                    apto = False
                elif "Doen�as card�acas" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a doen�as card�acas.")
                    apto = False
                elif "Diabetes" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido ao hist�rico de diabetes.")
                    apto = False

                # Outras condi��es
                if tratamento == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea enquanto estiver em tratamento m�dico.")
                    apto = False
                if transfusao == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a transfus�o recente.")
                    apto = False
                if alergia == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a alergias.")
                    apto = False
                if fumo == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido ao uso de tabaco.")
                    apto = False
                if alcool == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido ao consumo de �lcool.")
                    apto = False
                if drogas_recreativas == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido ao uso de drogas recreativas.")
                    apto = False

                if apto:
                    st.success("Voc� est� apto(a) para doar medula �ssea!")

    # Verifica��o para doa��o de �rg�os
    if tipo_doacao2 == "�rg�os":
        st.subheader("Verifica��o de Condi��es de Sa�de para Doa��o de �rg�os")
        with st.form(key="form_orgaos"):
            idade_orgaos = st.number_input("Idade:", min_value=18)

            doencas_orgaos = st.multiselect("Voc� possui alguma das seguintes condi��es?",
                                            options=["C�ncer", "Doen�a Card�aca", "Diabetes",
                                                     "Doen�as infecciosas (ex: HIV, Hepatite)", "Outras"])

            historico_cirurgico = st.radio("Voc� j� passou por alguma cirurgia importante?", ("Sim", "N�o"))
            habito_fumo = st.radio("Voc� fuma?", ("Sim", "N�o"))
            uso_alcool = st.radio("Voc� consome �lcool regularmente?", ("Sim", "N�o"))
            consentimento_orgaos = st.radio("Voc� expressou sua vontade de ser doador para seus familiares?", ("Sim", "N�o"))
            
            submit_orgaos = st.form_submit_button("Verificar Elegibilidade para Doa��o de �rg�os")

            if submit_orgaos:
                apto_orgaos = True

                # Verifica��o de condi��es m�dicas
                if "C�ncer" in doencas_orgaos:
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido a hist�rico de c�ncer.")
                    apto_orgaos = False
                elif "Doen�as infecciosas (ex: HIV, Hepatite)" in doencas_orgaos:
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido a doen�as infecciosas.")
                    apto_orgaos = False

                # Outras condi��es
                if historico_cirurgico == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido ao hist�rico cir�rgico.")
                    apto_orgaos = False
                if habito_fumo == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido ao h�bito de fumar.")
                    apto_orgaos = False
                if uso_alcool == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido ao uso regular de �lcool.")
                    apto_orgaos = False

                if apto_orgaos:
                    st.success("Voc� est� apto(a) para doar �rg�os!")

    st.button('Ir para Agendamento', type="primary", on_click=MudarF)


elif pagina == "Agendamento":
    st.title("Agendamento de Doa��o de Sangue, Medula �ssea e �rg�os")

    # Formul�rio de Agendamento
    st.subheader("Agende Sua Doa��o")

    # Formul�rio de Agendamento
    with st.form("form_agendamento"):
        nome = st.text_input("Nome Completo")
        idade = st.number_input("Idade", min_value=16, max_value=120)
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        tipo_doacao = st.selectbox("Tipo de Doa��o", ["Sangue", "Medula �ssea", "�rg�os"])
        tipo_sanguineo = st.selectbox("Tipo Sangu�neo", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        local = st.text_input("Local da Doa��o")
        data_hora = st.date_input("Data da Doa��o", min_value=datetime.now().date())
        hora = st.time_input("Hora da Doa��o")
        notas = st.text_area("Notas (opcional)")

        submit_agendamento = st.form_submit_button("Agendar")

        if submit_agendamento:
            if not (nome and local):
                st.error("Por favor, preencha todos os campos obrigat�rios.")
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

    st.button('Ir para Cadastro para Volunt�rios', type="primary", on_click=MudarG)

elif pagina == "Cadastro para Volunt�rios":
    st.title("Cadastro para Volunt�rios")

    with st.form("form_voluntarios"):
        nome_voluntario = st.text_input("Nome Completo")
        idade_voluntario = st.number_input("Idade", min_value=16, max_value=120)
        sexo_voluntario = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        contato = st.text_input("Contato (e-mail ou telefone)")
        interesse = st.multiselect("�reas de Interesse", 
                                   ["Doa��o de Sangue", "Doa��o de Medula �ssea", "Doa��o de �rg�os", "Eventos", "Campanhas Educativas"])
        submit_voluntario = st.form_submit_button("Cadastrar")

        if submit_voluntario:
            if not (nome_voluntario and contato and interesse):
                st.error("Por favor, preencha todos os campos obrigat�rios.")
            else:
                salvar_voluntario(nome_voluntario, idade_voluntario, sexo_voluntario, contato, ", ".join(interesse))
                st.success("Cadastro realizado com sucesso!")

                # Adicionar link para download do arquivo CSV
                st.markdown("### Baixe seus dados de volunt�rios")
                with open("voluntarios.csv", "rb") as file:
                    st.download_button(
                        label="Baixar cadastro de volunt�rios",
                        data=file,
                        file_name="voluntarios.csv",
                        mime="text/csv"
                    )

    st.button('Ir para V�deo', type="primary", on_click=MudarH)



elif pagina == "V�deo":
    st.title("V�deo Explicativo sobre a Doa��o de Sangue")
    st.write("Aqui pode ser exibido um v�deo sobre o processo de doa��o.")
    st.video("V�deo.mp4")
    st.button('Ir para Fim', type="primary", on_click=MudarI)

elif pagina == "Fim":
    add_bg_image("imagemfim.png")
    st.button('Voltar para Home', type="primary", on_click=MudarA)import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime

# Fun��o para adicionar imagem de fundo na p�gina Home
def add_bg_image(image_path):
    try:
        img = Image.open(image_path)
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"Imagem n�o encontrada em {image_path}. Verifique o caminho.")

# Fun��o para salvar os dados em um CSV (Doador)
def salvar_doador(nome, idade, sexo, tipo_sanguineo):
    arquivo = "doadores.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Tipo Sangu�neo"])
    novo_doador = pd.DataFrame([[nome, idade, sexo, tipo_sanguineo]], columns=["Nome", "Idade", "Sexo", "Tipo Sangu�neo"])
    df = pd.concat([df, novo_doador], ignore_index=True)
    df.to_csv(arquivo, index=False)

# Fun��o para salvar o agendamento em CSV
def salvar_agendamento(nome, idade, sexo, tipo_doacao, tipo_sanguineo, local, data_hora, hora, notas):
    df_agendamento = pd.DataFrame({
        "Nome": [nome],
        "Idade": [idade],
        "Sexo": [sexo],
        "Tipo Sangu�neo": [tipo_sanguineo],
        "Local": [local],
        "Data": [data_hora],
        "Hora": [hora],
        "Notas": [notas if notas else "Nenhuma"]
    })
    df_agendamento.to_csv('agendamentos.csv', index=False, mode='a', header=False)

# Fun��o para salvar volunt�rios em CSV
def salvar_voluntario(nome, idade, sexo, contato, interesse):
    arquivo = "voluntarios.csv"
    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    novo_voluntario = pd.DataFrame([[nome, idade, sexo, contato, interesse]], columns=["Nome", "Idade", "Sexo", "Contato", "Interesse"])
    df = pd.concat([df, novo_voluntario], ignore_index=True)
    df.to_csv(arquivo, index=False)

# Inicializa as op��es de navega��o no estado da sess�o
if "Ops" not in st.session_state:
    st.session_state.ops = [
        "Home", "Import�ncia", "Requisitos para Doa��o",
        "Etapas para Doa��o", "Elegibilidade de Doa��o", 
        'Agendamento', "Cadastro para Volunt�rios", 'V�deo', 'Fim'
    ]

# Barra lateral para navega��o
with st.sidebar:
    pagina = st.radio('Navega��o', st.session_state.ops, key='Nav')

def MudarA():
    st.session_state.Nav = 'Home'
def MudarB():
    st.session_state.Nav = 'Import�ncia'
def MudarC():
    st.session_state.Nav = 'Requisitos para Doa��o'
def MudarD():
    st.session_state.Nav = 'Etapas para Doa��o'
def MudarE():
    st.session_state.Nav = 'Elegibilidade de Doa��o'
def MudarF():
    st.session_state.Nav = 'Agendamento'  
def MudarG():
    st.session_state.Nav = 'Cadastro para Volunt�rios'
def MudarH():
    st.session_state.Nav = 'V�deo'
def MudarI():
    st.session_state.Nav = 'Fim'


# Interface Streamlit
st.title("Sistema de Doa��o de Sangue, Medula �ssea e �rg�os")

# L�gica para exibir a p�gina selecionada
if pagina == "Home":
    st.subheader("Doa��o de Sangue")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi institu�da pela 
    Organiza��o Mundial da Sa�de (OMS) para lembrar da import�ncia da conscientiza��o quanto � 
    necessidade da doa��o de sangue e como uma forma de agradecimento aos doadores.""")
    
    st.subheader("Doa��o de �rg�os")
    st.write("""Dia 14 de Junho, comemora-se o Dia Mundial do Doador de Sangue. A data foi institu�da pela 
    Organiza��o Mundial da Sa�de (OMS) para lembrar da import�ncia da conscientiza��o quanto � 
    necessidade da doa��o de sangue e como uma forma de agradecimento aos doadores.""")

    st.subheader("Doa��o de Medula �ssea")
    st.write("""O Dia Mundial da Doa��o de Medula �ssea � celebrado no terceiro s�bado de setembro. Essa data, estabelecida pela World Marrow Donor Association (WMDA), tem como objetivo aumentar a conscientiza��o sobre a doa��o de medula �ssea e promover o registro de novos doadores. O dia tamb�m destaca a import�ncia de contar com uma base diversificada de doadores cadastrados, j� que a compatibilidade entre doadores e receptores � complexa e depende de fatores gen�ticos.""")
    add_bg_image("doe.png")
    st.button('Ir para Import�ncia', type="primary", on_click=MudarB)

elif pagina == "Import�ncia":
    st.title("A Import�ncia da Doa��o de Sangue, Medula �ssea e �rg�os")

    # Explica��o sobre a import�ncia da doa��o de sangue
    st.subheader("A Import�ncia da Doa��o de Sangue")
    st.write("""A doa��o de sangue � um ato de solidariedade e amor ao pr�ximo que ajuda a salvar in�meras vidas diariamente. O sangue doado � essencial para tratamentos m�dicos, como em cirurgias, acidentes e no suporte a pacientes com doen�as graves, como c�ncer e anemias. Cada doa��o pode beneficiar at� tr�s pessoas, pois o sangue � separado em componentes (plasma, plaquetas e gl�bulos vermelhos), utilizados para necessidades distintas.""")
    
    st.subheader("Qrcode com informa��es em tempo real")
    st.write("""Acessando este qrcode voc� tem acesso a informa��es em tempo real sobre o estoque de sangue""")
    st.image("qrr.png")

    # Explica��o sobre a import�ncia da doa��o de medula �ssea
    st.subheader("A Import�ncia da Doa��o de Medula �ssea")
    st.write("""A doa��o de medula �ssea � vital para pacientes com doen�as hematol�gicas graves, como leucemia, linfoma e anemia apl�stica. A medula �ssea, respons�vel pela produ��o de c�lulas sangu�neas, precisa ser substitu�da por uma saud�vel em casos de danos graves. O procedimento de doa��o � seguro e pode salvar vidas, especialmente em crian�as e jovens. Registre-se em bancos de medula, como o REDOME e HEMOBRAZ, e fa�a a diferen�a.""")

    # Explica��o sobre a import�ncia da doa��o de �rg�os
    st.subheader("A Import�ncia da Doa��o de �rg�os")
    st.write("""A doa��o de �rg�os � uma forma de garantir que pessoas com fal�ncia de �rg�os tenham uma segunda chance de vida. Um �nico doador pode salvar v�rias vidas, doando �rg�os como cora��o, rins, f�gado e pulm�es, al�m de tecidos como c�rnea e pele. A decis�o de ser um doador deve ser informada � fam�lia, pois o consentimento � fundamental para que a doa��o seja realizada.""")

    st.button('Ir para Requisitos para Doa��o', type="primary", on_click=MudarC)

# Explica��o sobre a import�ncia da doa��o de �rg�os
elif pagina == "Requisitos para Doa��o":
    st.title("Requisitos para Doa��o de Sangue")
    
    # Adicionando logs para verificar se as partes est�o sendo executadas
    st.write("Verificando requisitos de doa��o de sangue...")
    st.write(""" 
    - Apresentar boa condi��o de sa�de.
    - Ter entre 16 e 69 anos.
    - Pesar no m�nimo 51 quilos.
    - Estar descansado (dormido pelo menos seis horas nas 24 horas anteriores).
    - Estar alimentado (evitar alimenta��o gordurosa nas 4 horas anteriores).
    - Apresentar documento original com foto recente.
    """)
    st.write(""" 
    Fatores que podem impedir a doa��o:
    - Doen�as cr�nicas, HIV, Hepatite, Mal�ria.
    - Uso de drogas il�citas ou medicamentos.
    """)

    # Requisitos sobre a import�ncia da doa��o de Medula �ssea
    st.subheader("Requisitos para Doa��o de Medula �ssea")
    st.write("Verificando requisitos de medula �ssea...")
    st.write(""" 
    - Ter entre 18 e 55 anos.
    - Estar em boas condi��es de sa�de.
    - N�o ter doen�as autoimunes, HIV, Hepatite ou outras doen�as graves.
    - N�o ter hist�rico de c�ncer.
    - Estar disposto a se cadastrar e realizar os exames necess�rios.
    """)

    # Requisitos sobre a import�ncia da doa��o de �rg�os
    st.subheader("Requisitos para Doa��o de �rg�os")
    st.write("Verificando requisitos de doa��o de �rg�os...")
    st.write(""" 
    - Ser maior de idade (no Brasil, � necess�rio ter 18 anos).
    - N�o ter doen�as que impe�am a doa��o (ex: c�ncer, doen�as infecciosas).
    - Informar a fam�lia sobre a decis�o de ser doador.
    - Assinar o documento de doa��o ou ser registrado em um sistema de doa��o de �rg�os.
    """)

    st.button('Ir para Etapas para Doa��o', type="primary", on_click=MudarD)

elif pagina == "Etapas para Doa��o":
    st.title("Etapas para Doa��o de Sangue, Medula �ssea e �rg�os")

    st.subheader("Etapas para Doa��o de Sangue")
    st.write("""
    1. Registro: O doador deve se registrar na unidade de coleta de sangue.
    2. Triagem: Avalia��o de sa�de e verifica��o dos requisitos.
    3. Coleta: O sangue � coletado de forma segura.
    4. P�s-Coleta: O doador recebe orienta��es sobre cuidados ap�s a doa��o e um lanche.
    """)

    st.subheader("Etapas para Doa��o de Medula �ssea")
    st.write("""
    1. Cadastro: O interessado deve se cadastrar em um banco de sangue de medula �ssea.
    2. Coleta de Amostra: O doador fornece uma amostra de sangue para tipagem HLA.
    3. Triagem: Avalia��o m�dica e exames de sa�de.
    4. Procedimento de Coleta: A medula � coletada por aferese ou pun��o.
    5. Acompanhamento: Monitoramento da sa�de do doador ap�s a doa��o.
    """)

    st.subheader("Etapas para Doa��o de �rg�os")
    st.write("""
    1. Cadastro: O interessado deve se cadastrar e informar a fam�lia.
    2. Consentimento: Garantir que a fam�lia concorda com a doa��o.
    3. Avalia��o M�dica: An�lise da possibilidade de doa��o em caso de morte cerebral.
    4. Coleta: Os �rg�os s�o removidos em ambiente cir�rgico.
    5. Acompanhamento: Monitoramento dos receptores dos �rg�os.
    """)
    st.button('Ir para Elegibilidade de doa��o', type="primary", on_click=MudarE)


# P�gina para Elegibilidade de Doa��o 
if pagina == "Elegibilidade de Doa��o":
    st.title("Verifica��o de Elegibilidade para Doa��o de Sangue, Medula �ssea e �rg�os")

    # Sele��o do tipo de doa��o
    tipo_doacao2 = st.selectbox("Selecione o tipo de doa��o", ["Sangue", "Medula �ssea", "�rg�os"])

    # Verifica��o para doa��o de sangue
    if tipo_doacao2 == "Sangue":
        st.subheader("Verifica��o de Condi��es de Sa�de para Doa��o de Sangue")
        with st.form(key="form_elegibilidade_de_sangue"):
            hiv = st.radio("J� teve HIV?", ("Sim", "N�o"))
            hepatite = st.radio("J� teve Hepatite?", ("Sim", "N�o"))
            malaria = st.radio("J� teve Mal�ria?", ("Sim", "N�o"))
            doencas_cronicas = st.radio("Possui alguma doen�a cr�nica?", ("Sim", "N�o"))

            if doencas_cronicas == "Sim":
                dc = st.multiselect('Quais doen�as cr�nicas?', options=['Diabetes', 'Hipertens�o', 'Asma', 'AVC', 'Obesidade', 'Depress�o'])
                if dc:
                    st.write(f"Voc� selecionou: {', '.join(dc)}")

            if hepatite == "Sim":
                hp = st.multiselect('Qual tipo de Hepatite?', options=['A', 'B', 'C'])
                if hp:
                    st.write(f"Voc� teve Hepatite do tipo: {', '.join(hp)}")

            dst = st.multiselect('Voc� j� teve alguma das seguintes Doen�as Sexualmente Transmiss�veis (DSTs)?',
                                 options=['S�filis', 'Gonorreia', 'Herpes', 'HPV', 'Outras'])
            if dst:
                st.write(f"Voc� teve: {', '.join(dst)}")

            tuberculose = st.radio("J� teve Tuberculose?", ("Sim", "N�o"))
            drogas = st.radio("Faz ou j� fez uso de Drogas?", ("Sim", "N�o"))
            if drogas == "Sim":
                dg = st.multiselect('Quais drogas?', options=['Maconha', 'Coca�na', 'Crack'])
                if dg:
                    st.write(f"Voc� fez uso de: {', '.join(dg)}")

            fumar = st.radio("Fuma?", ("Sim", "N�o"))
            bebidas = st.radio("Faz uso de bebidas alco�licas?", ("Sim", "N�o"))

            verificar_button = st.form_submit_button(label="Verificar Elegibilidade")

            if verificar_button:
                if hiv == "Sim" or hepatite == "Sim" or malaria == "Sim" or doencas_cronicas == "Sim":
                    st.error("Infelizmente, voc� n�o pode doar sangue devido a uma condi��o m�dica.")
                else:
                    st.success("Voc� est� apto(a) para doar sangue!")

    # Verifica��o para doa��o de medula �ssea
    if tipo_doacao2 == "Medula �ssea":
        st.subheader("Verifica��o de Condi��es de Sa�de para Medula �ssea")
        with st.form(key="form_medula"):
            idade_medula = st.number_input("Idade:", min_value=18, max_value=55)

            condicoes = st.multiselect("Voc� tem alguma das seguintes condi��es de sa�de?",
                                       options=["Doen�as autoimunes (ex: lupus, artrite reumatoide)",
                                                "C�ncer", "Infec��es cr�nicas (ex: HIV, hepatite)",
                                                "Doen�as do sangue (ex: anemia, leucemia)",
                                                "Doen�as card�acas", "Diabetes", "Outras (especifique)"])

            tratamento = st.radio("Voc� est� atualmente sob tratamento m�dico?", ("Sim", "N�o"))
            transfusao = st.radio("Voc� j� realizou uma transfus�o de sangue?", ("Sim", "N�o"))
            alergia = st.radio("Voc� � al�rgico a algum medicamento ou subst�ncia?", ("Sim", "N�o"))
            fumo = st.radio("Voc� fuma?", ("Sim", "N�o"))
            alcool = st.radio("Voc� consome bebidas alco�licas?", ("Sim", "N�o"))
            drogas_recreativas = st.radio("Voc� faz uso de drogas recreativas?", ("Sim", "N�o"))
            consentimento = st.radio("Voc� est� disposto a realizar exames de compatibilidade?", ("Sim", "N�o"))
            ciente = st.radio("Voc� est� ciente de que poder� ser chamado para realizar a doa��o a qualquer momento, se compat�vel?", ("Sim", "N�o"))
            
            submit_medula = st.form_submit_button("Verificar Elegibilidade para Doa��o de Medula �ssea")

            if submit_medula:
                apto = True

                # Verifica��o de condi��es m�dicas
                if "Doen�as autoimunes (ex: lupus, artrite reumatoide)" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a doen�as autoimunes.")
                    apto = False
                elif "C�ncer" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a hist�rico de c�ncer.")
                    apto = False
                elif "Infec��es cr�nicas (ex: HIV, hepatite)" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a infec��es cr�nicas.")
                    apto = False
                elif "Doen�as do sangue (ex: anemia, leucemia)" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a doen�as do sangue.")
                    apto = False
                elif "Doen�as card�acas" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a doen�as card�acas.")
                    apto = False
                elif "Diabetes" in condicoes:
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido ao hist�rico de diabetes.")
                    apto = False

                # Outras condi��es
                if tratamento == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea enquanto estiver em tratamento m�dico.")
                    apto = False
                if transfusao == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a transfus�o recente.")
                    apto = False
                if alergia == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido a alergias.")
                    apto = False
                if fumo == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido ao uso de tabaco.")
                    apto = False
                if alcool == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido ao consumo de �lcool.")
                    apto = False
                if drogas_recreativas == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar medula �ssea devido ao uso de drogas recreativas.")
                    apto = False

                if apto:
                    st.success("Voc� est� apto(a) para doar medula �ssea!")

    # Verifica��o para doa��o de �rg�os
    if tipo_doacao2 == "�rg�os":
        st.subheader("Verifica��o de Condi��es de Sa�de para Doa��o de �rg�os")
        with st.form(key="form_orgaos"):
            idade_orgaos = st.number_input("Idade:", min_value=18)

            doencas_orgaos = st.multiselect("Voc� possui alguma das seguintes condi��es?",
                                            options=["C�ncer", "Doen�a Card�aca", "Diabetes",
                                                     "Doen�as infecciosas (ex: HIV, Hepatite)", "Outras"])

            historico_cirurgico = st.radio("Voc� j� passou por alguma cirurgia importante?", ("Sim", "N�o"))
            habito_fumo = st.radio("Voc� fuma?", ("Sim", "N�o"))
            uso_alcool = st.radio("Voc� consome �lcool regularmente?", ("Sim", "N�o"))
            consentimento_orgaos = st.radio("Voc� expressou sua vontade de ser doador para seus familiares?", ("Sim", "N�o"))
            
            submit_orgaos = st.form_submit_button("Verificar Elegibilidade para Doa��o de �rg�os")

            if submit_orgaos:
                apto_orgaos = True

                # Verifica��o de condi��es m�dicas
                if "C�ncer" in doencas_orgaos:
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido a hist�rico de c�ncer.")
                    apto_orgaos = False
                elif "Doen�as infecciosas (ex: HIV, Hepatite)" in doencas_orgaos:
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido a doen�as infecciosas.")
                    apto_orgaos = False

                # Outras condi��es
                if historico_cirurgico == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido ao hist�rico cir�rgico.")
                    apto_orgaos = False
                if habito_fumo == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido ao h�bito de fumar.")
                    apto_orgaos = False
                if uso_alcool == "Sim":
                    st.error("Voc� n�o est� apto(a) para doar �rg�os devido ao uso regular de �lcool.")
                    apto_orgaos = False

                if apto_orgaos:
                    st.success("Voc� est� apto(a) para doar �rg�os!")

    st.button('Ir para Agendamento', type="primary", on_click=MudarF)


elif pagina == "Agendamento":
    st.title("Agendamento de Doa��o de Sangue, Medula �ssea e �rg�os")

    # Formul�rio de Agendamento
    st.subheader("Agende Sua Doa��o")

    # Formul�rio de Agendamento
    with st.form("form_agendamento"):
        nome = st.text_input("Nome Completo")
        idade = st.number_input("Idade", min_value=16, max_value=120)
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        tipo_doacao = st.selectbox("Tipo de Doa��o", ["Sangue", "Medula �ssea", "�rg�os"])
        tipo_sanguineo = st.selectbox("Tipo Sangu�neo", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        local = st.text_input("Local da Doa��o")
        data_hora = st.date_input("Data da Doa��o", min_value=datetime.now().date())
        hora = st.time_input("Hora da Doa��o")
        notas = st.text_area("Notas (opcional)")

        submit_agendamento = st.form_submit_button("Agendar")

        if submit_agendamento:
            if not (nome and local):
                st.error("Por favor, preencha todos os campos obrigat�rios.")
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

    st.button('Ir para Cadastro para Volunt�rios', type="primary", on_click=MudarG)

elif pagina == "Cadastro para Volunt�rios":
    st.title("Cadastro para Volunt�rios")

    with st.form("form_voluntarios"):
        nome_voluntario = st.text_input("Nome Completo")
        idade_voluntario = st.number_input("Idade", min_value=16, max_value=120)
        sexo_voluntario = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        contato = st.text_input("Contato (e-mail ou telefone)")
        interesse = st.multiselect("�reas de Interesse", 
                                   ["Doa��o de Sangue", "Doa��o de Medula �ssea", "Doa��o de �rg�os", "Eventos", "Campanhas Educativas"])
        submit_voluntario = st.form_submit_button("Cadastrar")

        if submit_voluntario:
            if not (nome_voluntario and contato and interesse):
                st.error("Por favor, preencha todos os campos obrigat�rios.")
            else:
                salvar_voluntario(nome_voluntario, idade_voluntario, sexo_voluntario, contato, ", ".join(interesse))
                st.success("Cadastro realizado com sucesso!")

                # Adicionar link para download do arquivo CSV
                st.markdown("### Baixe seus dados de volunt�rios")
                with open("voluntarios.csv", "rb") as file:
                    st.download_button(
                        label="Baixar cadastro de volunt�rios",
                        data=file,
                        file_name="voluntarios.csv",
                        mime="text/csv"
                    )

    st.button('Ir para V�deo', type="primary", on_click=MudarH)



elif pagina == "V�deo":
    st.title("V�deo Explicativo sobre a Doa��o de Sangue")
    st.write("Aqui pode ser exibido um v�deo sobre o processo de doa��o.")
    st.video("V�deo.mp4")
    st.button('Ir para Fim', type="primary", on_click=MudarI)

elif pagina == "Fim":
    add_bg_image("imagemfim.png")
    st.button('Voltar para Home', type="primary", on_click=MudarA)
