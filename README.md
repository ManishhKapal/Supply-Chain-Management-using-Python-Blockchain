---

# Supply Chain Management System Using Python and Blockchain

This project is a **Supply Chain Management System** built using **Python** and **Blockchain technology**. The system ensures transparency, security, and immutability in tracking supply chain processes. The frontend is developed using **Streamlit**, providing an intuitive and interactive interface for users.

---

## 🚀 Features
- **Blockchain Integration**: Secure and immutable record-keeping using blockchain principles.
- **Real-Time Tracking**: Track products throughout the supply chain lifecycle.
- **Decentralized Ledger**: Distributed architecture ensures no single point of failure.
- **Interactive Frontend**: User-friendly interface powered by Streamlit.
- **Customizable**: Adaptable to various industries and use cases.

---

## 🛠️ Technologies Used
- **Python**: Backend logic and blockchain implementation.
- **Streamlit**: Web-based user interface.
- **JSON**: Data storage format for blockchain.
- **Libraries**:
  - `streamlit`
  - `hashlib`
  - `datetime`
  - `json`

---

## 📂 Project Structure
```
Supply-Chain-Management/
│
├── blockchain.py       # Contains blockchain implementation
├── product.py          # Manages product-related functionalities
├── app.py              # Streamlit application file (entry point)
├── README.md           # Documentation (this file)
└── requirements.txt    # Python dependencies
```

---

## ⚙️ Setup and Running Steps

### 1. Clone the Repository
```bash
git clone https://github.com/ManishhKapal/Supply-Chain-Management-using-Python-Blockchain.git
cd Supply-Chain-Management-using-Python-Blockchain
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Streamlit application using the following command:
```bash
streamlit run app.py
```

### 5. Access the Application
- Open your browser and go to **http://localhost:8501** or the link provided by Streamlit.
- Use the interface to interact with the supply chain system.

---

## 📘 How It Works
1. **Blockchain Implementation**:
   - Each transaction or process in the supply chain is stored as a block.
   - Blocks are chained together using cryptographic hashes, ensuring immutability.

2. **Product Management**:
   - `product.py` handles product-related functionalities, such as adding new products or retrieving product details.

3. **User Interaction**:
   - Users can add new blocks (transactions) via the Streamlit interface.
   - View the entire blockchain ledger to ensure transparency.

4. **Data Storage**:
   - The blockchain and product information are stored in-memory during the application runtime.

---

## 🛡️ Security
- The system uses cryptographic hashes (`SHA-256`) to ensure data integrity.
- Each block in the chain references the hash of the previous block, making the chain tamper-proof.

---

## ✨ Future Enhancements
- Integration with IoT devices for automated data entry.
- Smart contract implementation for automated actions.
- Enhanced visualization with supply chain analytics.

---

## 💻 Author
**Manish Kapal**

Feel free to reach out or contribute to the repository for improvements and feature suggestions! 😊

---

## 🌟 Contributing
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

---

Let me know if you'd like further changes!
