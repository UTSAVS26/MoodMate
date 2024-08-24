import streamlit as st
from sentiment_analysis import analyze_sentiment
from mood_suggestions import generate_suggestions

def main():
    st.title("MoodMate")

    # Input text area for mood description
    mood_description = st.text_area("Enter your mood description:")

    if st.button("Submit"):
        if mood_description.strip() == "":
            st.warning("Please enter a mood description.")
        else:
            # Analyze sentiment and generate suggestion
            mood = analyze_sentiment(mood_description)
            suggestion = generate_suggestions(mood)
            
            # Display results
            st.subheader("Detected Mood:")
            st.write(mood)
            st.subheader("Suggestion:")
            st.write(suggestion)

if __name__ == "__main__":
    main()