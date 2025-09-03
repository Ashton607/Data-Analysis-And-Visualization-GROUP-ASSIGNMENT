import pandas as pd
import streamlit as st
import altair as alt

maternal_clean = pd.read_csv("maternal_mortality_ZAF_clean.csv")
labor_clean = pd.read_csv("female_labor_force_ZAF_clean.csv")


df = pd.merge(maternal_clean, labor_clean, on="Year")


st.title("Data Visualisation Demo")

maternalLine= alt.Chart(maternal_clean).mark_line().encode(
    x=alt.X("Year:O", title="Year", axis=alt.Axis(labelAngle=-45)),
    y=alt.Y("Maternal_Mortality_per_100k:O", title="Maternal Mortality (per 100k)")
).properties(
    title="Maternal Mortality in South Africa"
)
maternalPoint = alt.Chart(maternal_clean).mark_point(size=10, color="blue").encode(
    x=alt.X("Year:O", title="Year", axis=alt.Axis(labelAngle=-45)),
    y=alt.Y("Maternal_Mortality_per_100k:O", title="Maternal Mortality (per 100k)"),
    tooltip=["Year:O", "Maternal_Mortality_per_100k:O"],
)
maternalChart =maternalLine + maternalPoint
st.altair_chart(maternalChart)
    

femaleLabourLine = alt.Chart(labor_clean).mark_line().encode(
    x=alt.X("Year:O", title="Year", axis=alt.Axis(labelAngle=-45)),
    y=alt.Y("Female_Labor_Force_%:Q", title="Female Labour Force (%)"),
    tooltip="Year",
)
femaleLabourPoint = alt.Chart(labor_clean).mark_point(size=10, color="blue").encode(
    x=alt.X("Year:O", title="Year", axis=alt.Axis(labelAngle=-45)),
    y=alt.Y("Female_Labor_Force_%:Q", title="Female Labour Force (%)"),
    tooltip=["Year:O", "Female_Labor_Force_%:Q"]
).properties(
    title="Female Labour Force in South Africa"
)
femaleLabour= femaleLabourLine + femaleLabourPoint
st.altair_chart(femaleLabour)

avrData = pd.DataFrame({
    'avg_values': [df["Maternal_Mortality_per_100k"].mean(),df["Female_Labor_Force_%"].mean()],
    'categories': ["Maternal Mortality (per 100k)", "Female Labor Force (%)"]
})


averagesBar = alt.Chart(avrData).mark_bar().encode(
    x=alt.X("categories", title="Categories", axis=alt.Axis(labelAngle=0)),
    y=alt.Y("avg_values", title="Average"),
    ).properties(
        title="Average Levels – South Africa (Maternal Mortality vs Labor Force)"
    )
st.altair_chart(averagesBar)

latest = df.sort_values("Year").iloc[-1]

pie_data = pd.DataFrame({
    'Indicator': ["Maternal Mortality (per 100k)", "Female Labor Force (%)"],
    'Value': [latest["Maternal_Mortality_per_100k"], latest["Female_Labor_Force_%"]]
})

pie_chart = alt.Chart(pie_data).mark_arc().encode(
    theta=alt.Theta('Value:Q'),
    color=alt.Color('Indicator:N', 
                   scale=alt.Scale(range=["#E67E22", "#1ABC9C"]),
                   legend=alt.Legend(title="Indicators")),
    tooltip=['Indicator', 'Value']
).properties(
    title=f"South Africa Indicators – {int(latest['Year'])}",
    width=500,
    height=500
)


st.altair_chart(pie_chart, use_container_width=True)


   
