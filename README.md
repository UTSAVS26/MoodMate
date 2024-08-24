# MoodMate

**MoodMate** is an AI-powered mental health check-in tool designed to analyze users' mood descriptions and provide mood-enhancing suggestions. The application uses sentiment analysis to gauge a user's mental well-being based on their daily journal entries or mood descriptions.

## Features

- **Sentiment Analysis**: Analyzes mood descriptions to detect the user's current emotional state.
- **Mood Suggestions**: Provides personalized suggestions to improve or maintain the user's mood based on sentiment analysis.
- **Web-Based Interface**: Easy-to-use interface built with Streamlit, allowing users to input mood descriptions and receive suggestions.

## Project Structure

- **`src/`**: Contains source code for the application.
  - **`app.py`**: Entry point for the application.
  - **`sentiment_analysis.py`**: Module for sentiment analysis.
  - **`data_preprocessing.py`**: Utilities for data preprocessing.
  - **`mood_suggestions.py`**: Module for generating mood-enhancing suggestions.
  - **`utils.py`**: Utility functions.
  - **`web_app.py`**: Streamlit application file for the web interface.

- **`data/`**: Directory for datasets and external files.
  - **`data.csv`**: Example dataset used for the project.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/UTSAVS26/moodmate.git
   cd moodmate
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   To start the Streamlit app, use the following command:

   ```bash
   streamlit run src/web_app.py
   ```

   Open your browser and go to `http://localhost:8501` to interact with the application.

## Usage

1. Open the application in your web browser.
2. Enter your mood description in the text area.
3. Click the "Submit" button.
4. View the detected mood and the personalized suggestion provided.

## Contributing

Contributions to the project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and push to your branch.
4. Submit a pull request with a description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact [utsavsinghal26@gmail.com](mailto:utsavsinghal26@gmail.com).

---