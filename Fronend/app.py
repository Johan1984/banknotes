import streamlit as st
import requests

def predict_banknote(variance, skewness, curtosis, entropy):
    # Define the FastAPI endpoint URL
    api_url = "https://my-api-a2qb64qvma-uc.a.run.app/predict"

    # Create the request payload
    payload = {
        "variance": variance,
        "skewness": skewness,
        "curtosis": curtosis,
        "entropy": entropy
    }

    try:
        # Send a POST request to the FastAPI endpoint
        response = requests.post(api_url, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            return prediction
        else:
            st.error("Failed to make a prediction. Please try again.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

def main():
    # Set the page title
    st.title("Banknote Authenticity Prediction")

    # Add input fields for the parameters
    variance = st.number_input("Variance")
    skewness = st.number_input("Skewness")
    curtosis = st.number_input("Curtosis")
    entropy = st.number_input("Entropy")

    # Add a button to trigger the prediction
    if st.button("Predict"):
        prediction = predict_banknote(variance, skewness, curtosis, entropy)
        if prediction is not None:
            st.success(f"The banknote is {prediction}")


if __name__ == "__main__":
    main()
