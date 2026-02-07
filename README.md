🎬 Movie Recommender System (Gemini Powered)
An AI-powered Movie Recommender built using Python, Streamlit, Machine Learning, and Google Gemini AI.
It recommends similar movies and generates AI-based movie posters dynamically.

🧠 Features
Movie recommendation using similarity model
AI poster generation using Google Gemini API
Interactive and simple Streamlit UI
Displays top 5 similar movies with posters

🛠️ Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
ML Model	Cosine Similarity
AI	Google Gemini 1.5 Flash
Data	Pickle (.pkl) files

📂 Project Structure
movie/
│
├── app.py
├── movies_list.pkl
├── similarity.pkl
├── requirements.txt
└── README.md

⚙️ Installation
Clone the repository
git clone https://github.com/Akash-2412/Movie_Recomendation_System.git
cd movie-recommender
Install dependencies
pip install -r requirements.txt
Run the application
streamlit run app.py

🔑 API Setup
Replace your Gemini API key inside app.py
genai.configure(api_key="YOUR_GEMINI_API_KEY")

🎯 How It Works
User selects a movie
Similar movies are fetched using ML similarity
Posters are generated via Gemini AI
Streamlit displays the recommendations

🏁 Future Enhancements
Add movie search by genre
Add rating-based recommendations
Deploy publicly using Streamlit Cloud

👨‍💻 Developer
Akash Awasthi
