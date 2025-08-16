import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

new_df = pd.read_csv('datasets/data_viz1.csv')
# feature_text = pickle.load(open('datasets/feature_text.pkl','rb'))


group_df = new_df.groupby('sector', as_index=False).mean(numeric_only=True)[
    ['sector','price','price_per_sqft','built_up_area','latitude','longitude']
]


st.header(' 1. Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name="sector")

st.plotly_chart(fig,use_container_width=True)


# ----------------------------------------------------------------------------------------------------------------------------------------------------

st.header('2. Area Vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom")

    st.plotly_chart(fig1, use_container_width=True)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------


st.header('3. BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)


# -----------------------------------------------------------------------------------------------------------------------------------------


st.header('4. Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)

# ----------------------------------------------------------------------------------------------------------

st.header('5. Stacked Bar Chart — Property Type vs Furnishing_type')

a_df=pd.read_csv("gurgaon_properties_cleaned_v2.csv")
df_grouped = a_df.groupby(["property_type", "furnishing_type"]).size().reset_index(name="count")

st.markdown("""
- **0** : Unfurnished  
- **1** : Semi-Furnished  
- **2** : Furnished
""")

fig5 = px.bar(
    df_grouped,
    x="property_type",
    y="count",
    color="furnishing_type",
    title="Furnishing Distribution by Property Type",
    text="count"
)

fig5.update_layout(
    barmode="stack",
    xaxis_title="Property Type",
    yaxis_title="Number of Listings",
    legend_title="Furnishing Level"
)

st.plotly_chart(fig5, use_container_width=True)









# -----------------------------------


