import pandas as pd

# DADOS DO PARTICIPANTE
# Faixa Etária
tp_faixa_etaria = pd.DataFrame({
    "ID": list(range(1, 21)),
    "Descrição": [
        "Menor de 17 anos", "17 anos", "18 anos", "19 anos", "20 anos",
        "21 anos", "22 anos", "23 anos", "24 anos", "25 anos",
        "Entre 26 e 30 anos", "Entre 31 e 35 anos", "Entre 36 e 40 anos",
        "Entre 41 e 45 anos", "Entre 46 e 50 anos", "Entre 51 e 55 anos",
        "Entre 56 e 60 anos", "Entre 61 e 65 anos", "Entre 66 e 70 anos",
        "Maior de 70 anos"
    ]
})

# Sexo
tp_sexo = pd.DataFrame({
    "ID": ["M", "F"],
    "Descrição": ["Masculino", "Feminino"]
})

# Estado Civil
tp_estado_civil = pd.DataFrame({
    "ID": [0, 1, 2, 3, 4],
    "Descrição": [
        "Não informado", "Solteiro(a)", "Casado(a)/Mora com companheiro(a)",
        "Divorciado(a)/Desquitado(a)/Separado(a)", "Viúvo(a)"
    ]
})

# Cor/Raça
tp_cor_raca = pd.DataFrame({
    "ID": [0, 1, 2, 3, 4, 5, 6],
    "Descrição": [
        "Não declarado", "Branca", "Preta", "Parda", "Amarela", "Indígena", "Não dispõe da informação"
    ]
})

# Nacionalidade
tp_nacionalidade = pd.DataFrame({
    "ID": [0, 1, 2, 3, 4],
    "Descrição": [
        "Não informado", "Brasileiro(a)", "Brasileiro(a) Naturalizado(a)",
        "Estrangeiro(a)", "Brasileiro(a) Nato(a), nascido(a) no exterior"
    ]
})

# Situação de Conclusão do Ensino Médio
tp_st_conclusao = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Descrição": [
        "Já conclui o Ensino Médio",
        "Estou cursando e concluirei o Ensino Médio em 2023",
        "Estou cursando e concluirei o Ensino Médio após 2023",
        "Não conclui e não estou cursando o Ensino Médio"
    ]
})

# Ano de Conclusão do Ensino Médio
tp_ano_concluiu = pd.DataFrame({
    "ID": list(range(0, 18)),
    "Descrição": [
        "Não informado", "2022", "2021", "2020", "2019", "2018", "2017", "2016",
        "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "Antes de 2007"
    ]
})

# Tipo de escola do Ensino Médio
tp_escola = pd.DataFrame({
    "ID": [1, 2, 3],
    "Descrição": ["Não Respondeu", "Pública", "Privada"]
})

# Tipo de Instituição
tp_ensino = pd.DataFrame({
    "ID": [1, 2],
    "Descrição": [
        "Ensino Regular", "Educação Especial - Modalidade Substitutiva"
    ]
})

# Inscrito fez a prova apenas para treinar
in_treineiro = pd.DataFrame({
    "ID": [1, 0],
    "Descrição": ["Sim", "Não"]
})

# ################################################################################################
# DADOS DA ESCOLA
# Dependência administrativa (Escola)
tp_dependencia_adm_esc = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Descrição": ["Federal", "Estadual", "Municipal", "Privada"]
})

# Localização (Escola)
tp_localizacao_esc = pd.DataFrame({
    "ID": [1, 2],
    "Descrição": ["Urbana", "Rural"]
})

# Situação de funcionamento (Escola)
tp_sit_func_esc = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Descrição": ["Em atividade", "Paralisada", "Extinta", "Escola extinta em anos anteriores."]
})

# ################################################################################################
# DADOS DA PROVA OBJETIVA
# Presença na prova objetiva de Ciências da Natureza
tp_presenca_cn = pd.DataFrame({
    "ID": [0, 1, 2],
    "Descrição": ["Faltou à prova", "Presente na prova", "Eliminado da prova"]
})

# Presença na prova objetiva de Ciências Humanas
tp_presenca_ch = pd.DataFrame({
    "ID": [0, 1, 2],
    "Descrição": ["Faltou à prova", "Presente na prova", "Eliminado da prova"]
})

# Presença na prova objetiva de Linguagens e Códigos
tp_presenca_lc = pd.DataFrame({
    "ID": [0, 1, 2],
    "Descrição": ["Faltou à prova", "Presente na prova", "Eliminado da prova"]
})

# Presença na prova objetiva de Matemática
tp_presenca_mt = pd.DataFrame({
    "ID": [0, 1, 2],
    "Descrição": ["Faltou à prova", "Presente na prova", "Eliminado da prova"]
})

# Código do tipo de prova de Ciências da Natureza
co_prova_cn = pd.DataFrame({
    "ID": [1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1301, 1302, 1303, 1304],
    "Descrição": [
        "Azul",
        "Amarela",
        "Rosa",
        "Cinza",
        "Rosa - Ampliada",
        "Rosa - Superampliada",
        "Laranja - Braile",
        "Laranja - Adaptada Ledor",
        "Verde - Videoprova - Libras",
        "Azul (Reaplicação)",
        "Amarela (Reaplicação)",
        "Cinza (Reaplicação)",
        "Rosa (Reaplicação)",
    ]
})

# Código do tipo de prova de Ciências Humanas
co_prova_ch = pd.DataFrame({
    "ID": [1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1271, 1272, 1273, 1274],
    "Descrição": [
        "Azul",
        "Amarela",
        "Branca",
        "Rosa",
        "Rosa - Ampliada",
        "Rosa - Superampliada",
        "Laranja - Braile",
        "Laranja - Adaptada Ledor",
        "Verde - Videoprova - Libras",
        "Azul (Reaplicação)",
        "Amarela (Reaplicação)",
        "Branca (Reaplicação)",
        "Rosa (Reaplicação)",
    ]
})

# Código do tipo de prova de Linguagens e Códigos
co_prova_lc = pd.DataFrame({
    "ID": [1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1281, 1282, 1283, 1284],
    "Descrição": [
        "Azul",
        "Amarela",
        "Rosa",
        "Branca",
        "Rosa - Ampliada",
        "Rosa - Superampliada",
        "Laranja - Braile",
        "Laranja - Adaptada Ledor",
        "Verde - Videoprova - Libras",
        "Azul (Reaplicação)",
        "Amarela (Reaplicação)",
        "Rosa (Reaplicação)",
        "Branca (Reaplicação)",
    ]
})

# Código do tipo de prova de Matemática
co_prova_mt = pd.DataFrame({
    "ID": [1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1291, 1292, 1293, 1294],
    "Descrição": [
        "Azul",
        "Amarela",
        "Rosa",
        "Cinza",
        "Rosa - Ampliada",
        "Rosa - Superampliada",
        "Laranja - Braile",
        "Laranja - Adaptada Ledor",
        "Verde - Videoprova - Libras",
        "Azul (Reaplicação)",
        "Amarela (Reaplicação)",
        "Rosa (Reaplicação)",
        "Cinza (Reaplicação)",
    ]
})

# Língua Estrangeira
tp_lingua = pd.DataFrame({
    "ID": [0, 1],
    "Descrição": ["Inglês", "Espanhol"]
})

# ################################################################################################
# DADOS DA REDAÇÃO
# Situação da redação do participante
tp_status_redacao = pd.DataFrame({
    "ID": [1, 2, 3, 4, 6, 7, 8, 9],
    "Descrição": [
        "Sem problemas",
        "Anulada",
        "Cópia Texto Motivador",
        "Em Branco",
        "Fuga ao tema",
        "Não atendimento ao tipo textual",
        "Texto insuficiente",
        "Parte desconectada"
    ]
})

# ################################################################################################
# DADOS QUESTIONARIO SOCIOECONOMICO
# Até que série seu pai, ou o homem responsável por você, estudou?
q001 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Descrição": [
        "Nunca estudou.",
        "Não completou a 4ª série/5º ano do Ensino Fundamental.",
        "Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.",
        "Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.",
        "Completou o Ensino Médio, mas não completou a Faculdade.",
        "Completou a Faculdade, mas não completou a Pós-graduação.",
        "Completou a Pós-graduação.",
        "Não sei."
    ]
})

# Até que série sua mãe, ou a mulher responsável por você, estudou?
q002 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Descrição": [
        "Nunca estudou.",
        "Não completou a 4ª série/5º ano do Ensino Fundamental.",
        "Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.",
        "Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.",
        "Completou o Ensino Médio, mas não completou a Faculdade.",
        "Completou a Faculdade, mas não completou a Pós-graduação.",
        "Completou a Pós-graduação.",
        "Não sei."
    ]
})

# A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você. (Se ele não estiver trabalhando, escolha uma ocupação pensando no último trabalho dele).
q003 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E", "F"],
    "Descrição": [
        "Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor, pescador, lenhador, seringueiro, extrativista.",
        "Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, faxineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.",
        "Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.",
        "Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.",
        "Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel, professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.",
        "Não sei"
    ]
})

# A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você. (Se ela não estiver trabalhando, escolha uma ocupação pensando no último trabalho dela).
q004 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E", "F"],
    "Descrição": [
        "Grupo 1: Lavradora, agricultora sem empregados, bóia fria, criadora de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultora, pescadora, lenhadora, seringueira, extrativista",
        "Grupo 2: Diarista, empregada doméstica, cuidadora de idosos, babá, cozinheira (em casas particulares), motorista particular, jardineira, faxineira de empresas e prédios, vigilante, porteira, carteira, office-boy, vendedora, caixa, atendente de loja, auxiliar administrativa, recepcionista, servente de pedreiro, repositora de mercadoria.",
        "Grupo 3: Grupo 3: Padeira, cozinheira industrial ou em restaurantes, sapateira, costureira, joalheira, torneira mecânica, operadora de máquinas, soldadora, operária de fábrica, trabalhadora da mineração, pedreira, pintora, eletricista, encanadora, motorista, caminhoneira, taxista.",
        "Grupo 4: Profissionais autônomos e técnicos especializados",
        "Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel, professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.",
        "Não sei"
    ]
})

# Incluindo você, quantas pessoas moram atualmente em sua residência?
q005 = pd.DataFrame({
    "ID": list(range(1, 21)),
    "Descrição": ["1, pois moro sozinho(a)"] + [f"{i}" for i in range(2, 21)]
})

# Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)
q006 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"],
    "Descrição": [
        "Nenhuma Renda",
        "Até R$ 1.320,00",
        "De R$ 1.320,01 até R$ 1.980,00",
        "De R$ 1.980,01 até R$ 2.640,00",
        "De R$ 2.640,01 até R$ 3.300,00",
        "De R$ 3.300,01 até R$ 3.960,00",
        "De R$ 3.960,01 até R$ 5.280,00",
        "De R$ 5.280,01 até R$ 6.600,00",
        "De R$ 6.600,01 até R$ 7.920,00",
        "De R$ 7.920,01 até R$ 9240,00",
        "De R$ 9.240,01 até R$ 10.560,00",
        "De R$ 10.560,01 até R$ 11.880,00",
        "De R$ 11.880,01 até R$ 13.200,00",
        "De R$ 13.200,01 até R$ 15.840,00",
        "De R$ 15.840,01 até R$19.800,00",
        "De R$ 19.800,01 até R$ 26.400,00",
        "Acima de R$ 26.400,00"
    ]
})

# Q007 Em sua residência trabalha empregado(a) doméstico(a)?
q007 = pd.DataFrame({
    "ID": ["A", "B", "C", "D"],
    "Descrição": [
        "Não",
        "Sim, um ou dois dias por semana.",
        "Sim, três ou quatro dias por semana.",
        "Sim, pelo menos cinco dias por semana."
    ]
})

# Q008 - Na sua residência tem banheiro?
q008 = pd.DataFrame({
    "ID": ["A", "B", "C", "D","E"],
    "Descrição": [
        "Não", 
        "Sim, um", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q009 - Na sua residência tem quartos para dormir?
q009 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, um", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q010 - Na sua residência tem carro?
q010 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, um", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q011 - Na sua residência tem motocicleta?
q011 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, um", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q012 - Na sua residência tem geladeira?
q012 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, uma", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q013 - Na sua residência tem freezer (independente ou segunda porta da geladeira)?
q013 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, um", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q014 - Na sua residência tem máquina de lavar roupa?
q014 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, uma", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q015 - Na sua residência tem máquina de secar roupa?
q015 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, uma", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q016 - Na sua residência tem forno micro-ondas?
q016 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, um", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q017 - Na sua residência tem máquina de lavar louça?
q017 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, uma", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q018 - Na sua residência tem aspirador de pó?
q018 = pd.DataFrame({
    "ID": ["A", "B"],
    "Descrição": ["Não", "Sim"]
})

# Q019 - Na sua residência tem televisão em cores?
q019 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, uma", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q020 - Na sua residência tem aparelho de DVD?
q020 = pd.DataFrame({
    "ID": ["A", "B"],
    "Descrição": ["Não", "Sim"]
})

# Q021 - Na sua residência tem TV por assinatura?
q021 = pd.DataFrame({
    "ID": ["A", "B"],
    "Descrição": ["Não", "Sim"]
})

# Q022 - Na sua residência tem telefone celular?
q022 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, um", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q023 - Na sua residência tem telefone fixo?
q023 = pd.DataFrame({
    "ID": ["A", "B"],
    "Descrição": ["Não", "Sim"]
})

# Q024 - Na sua residência tem computador?
q024 = pd.DataFrame({
    "ID": ["A", "B", "C", "D", "E"],
    "Descrição": [
        "Não", 
        "Sim, um", 
        "Sim, dois", 
        "Sim, três", 
        "Sim, quatro ou mais"]
})

# Q025 - Na sua residência tem acesso à internet?
q025 = pd.DataFrame({
    "ID": ["A", "B"],
    "Descrição": ["Não", "Sim"]
})