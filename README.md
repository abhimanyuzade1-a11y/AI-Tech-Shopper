# 🤖 AI Personal Tech Shopper

## 📌 Project Overview

AI Personal Tech Shopper is an agentic AI-powered shopping assistant designed to help customers find suitable technology products according to their budget, requirements, and preferences.

The system understands customer requests, searches the product catalog, evaluates products, recommends suitable products, supports price negotiation, and manages the shopping cart.

---

## 🎯 Main Objective

The main objective of this project is to create an intelligent shopping assistant that can:

- Understand customer requirements
- Identify customer intent
- Search available products
- Compare products
- Recommend suitable products
- Explain recommendations
- Negotiate product prices
- Apply discounts
- Add products to cart
- Manage cart items
- Calculate final prices

---

## 🚀 Main Features

### 1. Customer Understanding
The system understands customer requirements such as:

- Budget
- Product category
- Usage requirements
- Preferences

### 2. AI Product Recommendation

The agent evaluates products based on:

- Price
- Customer budget
- Requirements
- Product match score
- Availability

### 3. Agentic Decision Making

The system follows an agentic workflow:

Customer Goal → Intent Detection → Product Search → Product Evaluation → Decision → Action

### 4. Price Negotiation

Customers can request a better price using:

- Discount messages
- Target price requests

The system evaluates the request and returns an available offer.

### 5. Shopping Cart

Customers can:

- Add products
- Select quantity
- Remove products
- View subtotal
- View discount
- View final total

### 6. Conversation

The system maintains the shopping conversation so that the customer can continue interacting with the assistant.

### 7. Analytics

The system records important shopping activities such as:

- Product recommendations
- Product views
- Cart actions
- Negotiations

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Agent-based architecture
- Product catalog
- Session state
- Python modules
- Data processing

---

## 📂 Project Structure

```text
AI-Tech-Shopper/
│
├── app.py
├── agent_brain.py
├── customer.py
├── recommendation.py
├── intent_engine.py
├── conversation_manager.py
├── cart_manager.py
├── analytics.py
└── README.md