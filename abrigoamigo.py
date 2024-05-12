#Instalando o SDK do Google
#!pip install -q -U google-generativeai
#Configurações iniciais
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyAADxHFaangSczoSim6KiVuFOsPytB-JV8"
genai.configure(api_key=GOOGLE_API_KEY)
#Listando os modelos disponíveis
#for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}
safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
    }
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)
chat = model.start_chat(history=[    
   # {
   #     "role": "user",
   #     "parts": ["Você é um gestor de uma plataforma de abrigos de animais da enchente de 2024 no rio grande do sul chamada Abrigo Amigo"]
    #},
    #{
    #    "role": "user",
   #     "parts": "['id\nnome\nendereco\ntelefone\nvagas\nvagasocupadas usuario_id\n10 Abrigo A\nRua das Flores, 123, Bairro Jardim Botânico, Porto Alegre\n(11) 1234-5678\n20\n7\n1\n11 Abrigo B\nRua dos Pinheiros, 456, Bairro Bela Vista, Canoas\n(22) 2345-6789\n15\n6\n1\n12 Abrigo C\nAvenida das Palmeiras, 789, Bairro Tristeza, Porto Alegre\n(33) 3456-7890\n25\n12\n1\n13 Abrigo D\nRua das Azaleias, 012, Bairro Santa Catarina, São Leopoldo\n(44) 4567-8901\n18\n2\n1\n14 Abrigo E\nRua dos Girassóis, 345, Bairro Marechal Rondon, Canoas\n(55) 5678-9012\n22\n16\n1\n15 Abrigo F\nAvenida dos Lírios, 678, Bairro Petrópolis, Porto Alegre\n(66) 6789-0123\n30\n20\n1\n16 Abrigo G\nRua das Violetas, 901, Bairro Lomba do Pinheiro, Porto Alegre\n(77) 7890-1234\n12\n0\n1\n17 Abrigo H\nRua dos Crisântemos, 234, Bairro Centro, Novo Hamburgo\n(88) 8901-2345\n17\n4\n1\n18 Abrigo I\nAvenida das Hortênsias, 567, Bairro Gramado, Gramado\n(99) 9012-3456\n28\n5\n1\n19 Abrigo J\nRua dos Jasmins, 890, Bairro São Geraldo, Porto Alegre\n(00) 0123-4567\n24\n8\n1\nid\nabrigo_id\ntipo_animais\ncor\nraça\nporte\nidade_aproximada\ndoenças\npersonalidade\n1\n10 Cão\nMarrom\nVira-lata\nMédio\n3 Não\nCarinhoso\n2\n10 Cão\nPreto\nVira-lata\nGrande\n2 Não\nBrincalhão\n3\n10 Cão\nBranco\nVira-lata\nPequeno\n4 Vermes\nCarinhoso\n4\n10 Cão\nCaramelo\nVira-lata\nMédio\n5 Não\nCarinhoso\n5\n10 Gato\nCinza\nVira-lata\nPequeno\n1 Não\nBrincalhão\n6\n10 Gato\nAmarelo\nVira-lata\nMédio\n2 Não\nCarinhoso\n7\n10 Gato\nBranco\nVira-lata\nPequeno\n3 Conjuntivite\nCarinhoso\n8\n11 Gato\nPreto\nVira-lata\nMédio\n2 Não\nCarinhoso\n9\n11 Gato\nCinza\nVira-lata\nPequeno\n4 Não\nBrincalhão\n10\n11 Cão\nMarrom\nVira-lata\nGrande\n5 Verme do coração\nCarinhoso\n11\n11 Cão\nBranco\nVira-lata\nMédio\n3 Não\nCarinhoso\n12\n12 Cão\nPreto\nVira-lata\nMédio\n2 Carrapatos\nBrincalhão\n13\n12 Cão\nMarrom\nVira-lata\nGrande\n4 Não\nCarinhoso\n14\n12 Gato\nAmarelo\nVira-lata\nPequeno\n1 Não\nCarinhoso\n15\n12 Gato\nBranco\nVira-lata\nMédio\n3 Não\nBrincalhão\n16\n12 Gato\nCinza\nVira-lata\nPequeno\n2 Doença respiratória\nCarinhoso\n17\n13 Cão\nMarrom\nVira-lata\nMédio\n4 Não\nCarinhoso\n18\n13 Cão\nPreto\nVira-lata\nGrande\n5 Verme do coração\nBrincalhão\n19\n13 Cão\nBranco\nVira-lata\nPequeno\n2 Conjuntivite\nCarinhoso\n20\n13 Gato\nAmarelo\nVira-lata\nPequeno\n1 Não\nCarinhoso\n21\n13 Gato\nCinza\nVira-lata\nMédio\n3 Não\nBrincalhão\n22\n14 Gato\nBranco\nVira-lata\nMédio\n2 Não\nCarinhoso\n23\n14 Gato\nCinza\nVira-lata\nPequeno\n4 Doença respiratória\nCarinhoso\n24\n14 Gato\nPreto\nVira-lata\nMédio\n5 Não\nBrincalhão\n25\n15 Cão\nCaramelo\nVira-lata\nGrande\n3 Não\nCarinhoso\n26\n15 Cão\nPreto\nVira-lata\nMédio\n4 Verme do coração\nCarinhoso\n27\n15 Gato\nAmarelo\nVira-lata\nPequeno\n2 Não\nBrincalhão\n28\n15 Gato\nCinza\nVira-lata\nMédio\n1 Não\nCarinhoso\n29\n16 Cão\nMarrom\nVira-lata\nGrande\n5 Carrapatos\nBrincalhão\n', '30\n16 Gato\nBranco\nVira-lata\nPequeno\n3 Não\nCarinhoso\n31\n17 Cão\nPreto\nVira-lata\nMédio\n4 Não\nCarinhoso\n32\n17 Cão\nBranco\nVira-lata\nGrande\n2 Verme do coração\nBrincalhão\n33\n17 Gato\nCinza\nVira-lata\nPequeno\n3 Não\nCarinhoso\n34\n17 Gato\nAmarelo\nVira-lata\nMédio\n1 Não\nBrincalhão\n35\n18 Cão\nMarrom\nVira-lata\nMédio\n2 Não\nCarinhoso\n36\n18 Cão\nPreto\nVira-lata\nGrande\n4 Carrapatos\nCarinhoso\n37\n18 Gato\nBranco\nVira-lata\nPequeno\n5 Doença respiratória\nBrincalhão\n38\n18 Gato\nCinza\nVira-lata\nMédio\n3 Não\nCarinhoso\n39\n19 Cão\nMarrom\nVira-lata\nMédio\n1 Conjuntivite\nBrincalhão\n40\n19 Cão\nPreto\nVira-lata\nGrande\n2 Verme do coração\nCarinhoso\n41\n19 Gato\nBranco\nVira-lata\nMédio\n3 Não\nCarinhoso\n42\n19 Gato\nCinza\nVira-lata\nPequeno\n4 Doença respiratória\nBrincalhão\n43\n10 Cão\nBranco e MarromVira-lata\nPequeno\n2 Não\nAlegre\n44\n10 Cão\nPreto\nLabrador\nGrande\n3 Não\nLeal\n45\n10 Cão\nCaramelo\nPoodle\nPequeno\n4 Artrite\nAmigável\n46\n10 Gato\nCinza\nSiamês\nMédio\n2 Não\nIndependente\n47\n11 Gato\nBranco\nPersa\nGrande\n1 Não\nMimoso\n48\n11 Cão\nMarrom\nBulldog\nMédio\n5 Displasia de quadril\nPreguiçoso\n49\n11 Cão\nPreto\nRottweiler\nGrande\n4 Verme do coração\nProtetor\n50\n11 Cão\nBranco\nHusky Siberiano Grande\n3 Não\nAtivo\n51\n12 Gato\nCaramelo\nAngorá\nMédio\n2 Não\nCarente\n52\n12 Gato\nPreto\nMaine Coon\nGrande\n1 Não\nCurioso\n53\n12 Cão\nBranco e MarromShih Tzu\nPequeno\n3 Não\nDivertido\n54\n12 Cão\nPreto\nDálmata\nGrande\n4 Não\nEnergético\n55\n13 Cão\nBranco\nAkita\nGrande\n5 Displasia de quadril\nLeal\n56\n13 Cão\nMarrom\nBorder Collie\nMédio\n2 Não\nInteligente\n57\n13 Gato\nPreto\nRagdoll\nGrande\n3 Não\nRelaxado\n58\n13 Gato\nCinza\nBritish Shorthair Médio\n1 Não\nElegante\n59\n14 Cão\nPreto\nGolden Retriever Grande\n4 Não\nAmigável\n60\n14 Cão\nBranco\nPug\nPequeno\n2 Obesidade\nBrincalhão\n61\n14 Gato\nAmarelo\nBengal\nMédio\n3 Não\nCurioso\n62\n14 Gato\nBranco\nSphynx\nPequeno\n1 Não\nAfetuoso\n']"
  #  },
 #   {
 #       "role": "user",
#        "parts": [". O seu Trabalho é ajudar as pessoas que acessarem o site a definir qual abrigo elas devem fornecer a sua ajuda, com base na cidade em que elas moram, na disponibilidade de recurso que elas tem e nos abrigos que apresentam maior necessidade. \nA tabela enviada contém os dados dos abrigos registrados na plataforma. Comece a conversa Perguntando o nome a cidade de quem está entrando no chat. A Seguir pergunte quais são as intenções da pessoa, ajudar com os abrigos ou encontrar um animal para adotar. No primeiro caso, pergunte o que a pessoa está disposta a oferecer e com base na resposta dela, analise a tabela para definir qual abrigo ela deve ajudar primeiro. No segundo, faça todas as perguntas que achar necessárias para encontrar um animal que mais se adapte ao que essa pessoa quer. (Caso não encontre um animal específico, sugira a adoção de um vira-lata pois ele é sempre o melhor amigo do homem) Adicione emojis às suas respostas para se aproximar da pessoa que está conversando"]
#    },
#    {
#       "role": "model",
#        "parts": ["Olá! 👋 Seja bem-vindo ao Abrigo Amigo! 💖\n\nPara te ajudar da melhor forma possível, me fale: qual a sua cidade? 🏘️😊"]
#    },
    ])

prompt = input('Esperando prompt: ')

while prompt != "fim":
  response = chat.send_message(prompt)
  print("Resposta:", response.text, '\n\n')
  prompt = input('Esperando prompt: ')