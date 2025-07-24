import streamlit as st

st.set_page_config(
    page_title="Núb.ia ensina",
    page_icon="📚",
    layout="centered"
)

st.logo("assets/Assinatura_padrao.png")
st.title("📚 Núb.ia Ensina")
st.write("Aprenda sobre as soluções da NeoAssist com a Núb.ia! 🤗")

home_tab, categoria_tab, tag_tab, config_geral_tab = st.tabs(["Home", "Categorias", "Tags", "Configurações Gerais"])

with home_tab:
	st.title("Bem-vindo!")
	st.markdown('''
Para auxiliar no treinamento e *onboarding* de nossos clientes, a NeoAssist desenvolveu o **Núb.ia ensina**,
um repositório de vídeos onde você encontrará conteúdos que vão te ajudar na sua jornada conosco.
			 
Selecione um item na lista de opções ao lado da página *Home* para acessar os materiais produzidos 
sobre o assunto.
''')

with categoria_tab:
	st.title("Categorias")
	st.markdown("Aprenda mais sobre **Categorias** na NeoAssist!")
	st.subheader("Introdução a Categorias")
	st.markdown("Do conceito à aplicação no seu atendimento, domine as categorias na Neo!")

	introducao_categorias_url = "https://youtu.be/Udu8_neddJQ"

	if introducao_categorias_url:
		st.video(introducao_categorias_url)

with tag_tab:
	st.title("Tags")
	st.markdown("Aprenda mais sobre **Tags** na NeoAssist!")
	st.subheader("Introdução a Tags")
	st.markdown("Conheça mais sobre a solução de Tags na NeoAssist para otimizar sua inteligência operacional!")

	introducao_tags_url = "https://www.youtube.com/watch?v=yBOWLh5GJfk"

	if introducao_tags_url:
		st.video(introducao_tags_url)

with config_geral_tab:
	st.title("Configurações Gerais")
	st.markdown("Aprenda mais sobre **Configurações Gerais** na NeoAssist!")
	st.subheader("Introdução a Configurações Gerais")
	st.markdown("Personalize seu atendimento configurando-o como quiser na Neo!")

	introducao_config_geral_url = "https://youtu.be/cAaYNkToKEM"

	if introducao_config_geral_url:
		st.video(introducao_config_geral_url)
