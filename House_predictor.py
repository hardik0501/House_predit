import pandas as pd
from sklearn.linear_model import LinearRegression
import gradio as gr

df = pd.read_csv("indian_house_data.csv")
features = ["Area (sqft)", "Bedrooms", "Age (years)", "Location Score (1-10)"]
X = df[features]
y = df["Price (in lakhs)"]
model = LinearRegression()
model.fit(X, y)

def predict_price(city, locality, area, bedrooms, age, score):
    input_data = pd.DataFrame([[area, bedrooms, age, score]], columns=features)
    predicted_price = model.predict(input_data)[0]
    match = df[(df["City"].str.lower() == city.lower()) & (df["Locality"].str.lower() == locality.lower())]
    if not match.empty:
        avg = match["Price (in lakhs)"].mean()
        return f"🏡 Estimated Price: ₹{predicted_price:.2f} Lakhs\n📊 Avg Price in {locality}: ₹{avg:.2f} Lakhs"
    else:
        return f"🏡 Estimated Price: ₹{predicted_price:.2f} Lakhs\n⚠️ No historical data found for {locality}"

city_list = sorted(df["City"].unique())
locality_map = {city: sorted(df[df["City"] == city]["Locality"].unique()) for city in city_list}

def update_localities(city):
    return gr.update(choices=locality_map[city], value=locality_map[city][0])

with gr.Blocks() as app:
    gr.Markdown("# 🏠 Indian House Price Predictor")
    with gr.Row():
        city_input = gr.Dropdown(label="Select City", choices=city_list, value="Delhi")
        locality_input = gr.Dropdown(label="Select Locality")
    city_input.change(fn=update_localities, inputs=city_input, outputs=locality_input)
    area_input = gr.Number(label="Area (sqft)", value=1000)
    bed_input = gr.Number(label="Bedrooms", value=2)
    age_input = gr.Number(label="Age (years)", value=5)
    score_input = gr.Slider(1, 10, step=1, label="Location Score", value=7)
    output = gr.Textbox(label="Prediction Result")
    predict_btn = gr.Button("Predict Price")
    predict_btn.click(predict_price, inputs=[city_input, locality_input, area_input, bed_input, age_input, score_input], outputs=output)

app.launch()
