import streamlit as st
from blockchain import Blockchain
from product import Product

# Initialize blockchain in session state if not already present
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()

# Alias for the blockchain object
blockchain = st.session_state.blockchain

st.title("Supply Chain Management System with Blockchain")

# Add new product to the supply chain
st.header("Add New Product")
product_id = st.text_input("Product ID")
name = st.text_input("Product Name")
origin = st.text_input("Origin")
destination = st.text_input("Destination")
status = st.selectbox("Product Status", ["Created", "In Transit", "Delivered"])

if st.button("Add Product"):
    if product_id and name and origin and destination:
        product = Product(product_id, name, origin, destination, status)
        blockchain.add_block(product.get_product_data())
        st.success("Product added to the blockchain!")
        st.write("New Block Data:", product.get_product_data())  # Debugging to confirm data is added
    else:
        st.error("Please fill all product details")

# View Blockchain
st.header("View Blockchain")
if st.button("Show Blockchain"):
    chain_data = blockchain.get_chain()
    if len(chain_data) > 0:
        for block in chain_data:
            st.write(f"Index: {block['index']}")
            st.write(f"Timestamp: {block['timestamp']}")
            st.write(f"Data: {block['data']}")
            st.write(f"Hash: {block['hash']}")
            st.write(f"Previous Hash: {block['previous_hash']}")
            st.write(f"Proof: {block['proof']}")
            st.write("---")
    else:
        st.info("No blocks in the blockchain yet.")

# Verify Blockchain Integrity
st.header("Verify Blockchain Integrity")
if st.button("Verify"):
    is_valid = blockchain.is_chain_valid()
    if is_valid:
        st.success("Blockchain is valid!")
    else:
        st.error("Blockchain is invalid!")