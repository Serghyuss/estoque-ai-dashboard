import streamlit as st
import plotly.express as px

# Importações do projeto
from app.utils.data_loader import carregar_csv
from app.utils.validators import validar_colunas
from app.services.kpis import calcular_kpis
from app.utils.formatters import formatar_moeda
from app.services.forecast import prever_demanda
from app.services.ai_insights import gerar_insights

# Configuração da página
st.set_page_config(layout="wide")

st.title("📊 Plataforma de Análise de Estoque com IA")

# Upload do arquivo CSV
file = st.file_uploader("Upload do CSV", type=["csv"])

if file:
    try:
        # =========================
        # 🔹 CARREGAMENTO E VALIDAÇÃO
        # =========================
        df = carregar_csv(file)
        validar_colunas(df)

        # =========================
        # 🔹 KPIs E PROCESSAMENTO
        # =========================
        kpis, df = calcular_kpis(df)
        df = prever_demanda(df)

        # =========================
        # 🔹 KPIs (CARDS)
        # =========================
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("💰 Estoque Total", formatar_moeda(kpis['valor_total']))
        col2.metric("🎯 Ticket Médio", f"{kpis['ticket_medio']:.2f}")
        col3.metric("📦 Total SKUs", kpis['total_skus'])
        col4.metric("⚠️ Ruptura (%)", f"{kpis['ruptura_pct']:.1f}%")

        # =========================
        # 🔹 GRÁFICO DE RUPTURA (Distribuição de estoque)
        # =========================
        st.subheader("📉 Distribuição de Estoque (Ruptura)")

        fig_ruptura = px.histogram(
            df,
            x="Stock",
            nbins=30,
            title="Distribuição de Quantidade em Estoque"
        )

        st.plotly_chart(fig_ruptura, use_container_width=True)

        # =========================
        # 🔹 TOP PRODUTOS POR VALOR
        # =========================
        st.subheader("🏆 Top 10 Produtos por Valor em Estoque")

        top_produtos = df.sort_values(
            by="valor_estoque",
            ascending=False
        ).head(10)

        # Tabela
        st.dataframe(top_produtos)

        # Gráfico
        fig_top = px.bar(
            top_produtos,
            x="Name",
            y="valor_estoque",
            title="Top 10 Produtos por Valor"
        )

        st.plotly_chart(fig_top, use_container_width=True)

        # =========================
        # 🔹 DEMANDA ESTIMADA
        # =========================
        st.subheader("🔮 Demanda Estimada")

        fig_demanda = px.bar(
            df.head(10),
            x="Name",
            y="demanda_estimada",
            title="Top Produtos por Demanda Estimada"
        )

        st.plotly_chart(fig_demanda, use_container_width=True)

        # =========================
        # 🔹 IA - INSIGHTS
        # =========================
        st.subheader("🧠 Análise Inteligente")

        if st.button("Gerar análise com IA"):
            insights = gerar_insights(kpis)
            st.write(insights)

    except Exception as e:
        st.error(f"Erro ao processar arquivo: {e}")