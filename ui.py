import chart_generator as cg
import data_handler as dh
import streamlit as st

data = dh.datahandler()

st.title("Data Visualizer")

file = st.file_uploader("Upload CSV",type=["csv"])
if data.load_dataset(file):
    st.write(data.get_preview())
    columns = data.get_columns()

    charts = cg.gen_chart(data.get_dataframe())
    uni = charts.univariate
    biv = charts.bivariate
    ty_a = st.selectbox(options=["Univariate","Bivariate"],label="Select Type Of Analysis")


    if ty_a == "Univariate":
        chart_type = st.selectbox(options=["Bar","Pie","Histogram"],label="Select a ChartType")
        if chart_type == "Bar":
            x=st.selectbox(options=columns,label="Select X Axis")
            fig = uni.column(x_axis=x)
        elif chart_type == "Pie":
            x=st.selectbox(options=columns,label="Select X Axis")
            fig = uni.pie(name=x)
        elif chart_type == "Histogram":
            x=st.selectbox(options=columns,label="Select X Axis")
            fig = uni.histplot(name=x)
    elif ty_a == "Bivariate":
        chart_type = st.selectbox(options=["Bar","Pie","Scatter"],label="Select a ChartType")
        if chart_type == "Bar":
            x=st.selectbox(options=columns,label="Select X Axis")
            y=st.selectbox(options=columns,label="Select Y Axis")
            fig = biv.column(x_axis=x,y_axis=y)
        elif chart_type == "Pie":
            x=st.selectbox(options=columns,label="Select X Axis")
            y=st.selectbox(options=columns,label="Select Y AXis")
            fig = biv.pie(name=x,value=y)
        elif chart_type == "Scatter":
            x=st.selectbox(options=columns,label="Select X Axis")
            y=st.selectbox(options=columns,label="Select Y Axis")
            fig = biv.scatter(x_axis=x,y_axis=y)


    if st.button(label="Generate"):
        st.plotly_chart(fig)