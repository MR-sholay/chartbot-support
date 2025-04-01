from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot(
    "SupportBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///chatbot.sqlite3",
    logic_adapters=[{
        "import_path": "chatterbot.logic.BestMatch",
        "default_response": "I'm sorry, I don't understand. Can you rephrase?",
        "maximum_similarity_threshold": 0.8
    }]
)

corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.english")

list_trainer = ListTrainer(chatbot)
list_trainer.train([
    "How can I add money to my GPay account?",
    "To add money, go to the 'Add Money' section in GPay and select your payment method.",
    "I can't make a payment, what should I do?",
    "Please check your internet connection and ensure your account balance is sufficient.",
    "How do I link my bank account to GPay?",
    "To link your bank account, go to 'Settings' > 'Payment Methods' and select 'Add Bank Account'.",
    "What is the limit for sending money on GPay?",
    "The maximum limit for sending money on GPay depends on your bank, but typically it's around ₹1,00,000 per transaction.",
    "How do I get a refund for a failed transaction?",
    "If the payment failed, you can request a refund by going to the transaction details and clicking 'Request Refund'.",
    "Why is my GPay transaction pending?",
    "Pending transactions usually happen due to issues with the payment gateway or your bank's authorization. Please try again later.",
    "Can I use GPay internationally?",
    "Yes, you can use GPay internationally if the merchant supports GPay as a payment option. Ensure your account is enabled for international payments.",
    "How do I contact GPay support?",
    "You can contact GPay support through the 'Help & Feedback' section in the app or visit the official GPay support website.",
    "What should I do if my GPay transaction is charged twice?",
    "If you're charged twice, please reach out to GPay support with the transaction details. They will assist you in resolving the issue.",
    "How can I change my GPay PIN?",
    "To change your GPay PIN, go to 'Settings' > 'Security' and select 'Change PIN'.",
    "I can't link my card to GPay.",
    "Please ensure that your card is eligible for use with GPay and check if it is linked to a supported bank account.",
    "How do I check my GPay balance?",
    "You can check your GPay balance by opening the app and checking the balance displayed at the top of the screen.",
    "What to do if my GPay payment is stuck?",
    "Try checking your internet connection, and if the issue persists, contact GPay support for assistance.",
    "How can I transfer money from GPay to my bank account?",
    "Go to 'Bank Account' section in the GPay app and select 'Transfer to Bank'. Choose your linked account and proceed.",
    "Why was my GPay transaction declined?",
    "Check if your bank has authorized the payment and ensure there are no issues with your account balance or internet connection."
])

print("Chatbot training completed!")

