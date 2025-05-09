# ❓ FAQ Chatbot for BudgetPro

The **FAQ Chatbot** is a streamlined conversational assistant designed to address common queries related to the BudgetPro platform. Integrated seamlessly into [BudgetPro](https://github.com/maharshijani05/BudgetPro), this chatbot enhances user experience by providing instant, accurate responses to frequently asked questions.

## 🚀 Features

* **Instant Responses**: Provides quick answers to predefined frequently asked questions.
* **Streamlit Integration**: Offers an interactive web interface for user-friendly interactions.
* **Modular Design**: Structured codebase for easy maintenance and scalability.
* **Lightweight Implementation**: Efficient performance with minimal resource consumption.

## 📁 Project Structure

```bash
├── faq_chatbot.py         # Core logic for handling chatbot responses
├── streamlit_app.py       # Streamlit app entry point
├── faq.txt                # Text file containing FAQs and their answers
├── requirements.txt       # Python dependencies
└── LICENSE                # MIT License
```

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/maharshijani05/FAQ_CHATBOT.git
   cd FAQ_CHATBOT
   ```

2. **Set Up Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## 🚶‍♂️ Usage

To run the Streamlit application locally:

```bash
streamlit run streamlit_app.py
```

Access the application in your browser at `http://localhost:8501`.

## 🧠 How It Works

* **User Interaction**: Users input queries through the Streamlit interface.
* **Processing**: The `faq_chatbot.py` module processes inputs and matches them against the predefined FAQs in `faq.txt`.
* **Response Generation**: Based on the matched question, the chatbot returns the corresponding answer.

## 📆 Dependencies

Key Python packages used:

* `streamlit`
* `langchain`

For a complete list, refer to `requirements.txt`.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📬 Contact

For questions or support, please open an issue in the repository.
