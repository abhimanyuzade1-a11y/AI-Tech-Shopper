# 🤖 AI Personal Tech Shopper

An agentic AI-powered technology shopping assistant that helps customers discover, compare, negotiate, and purchase technology products based on their budget, requirements, and preferences.

---

## 📌 Project Overview

AI Personal Tech Shopper is an intelligent shopping assistant designed to simplify the technology buying process.

The system understands customer requirements, identifies customer intent, searches the product catalog, evaluates products, recommends suitable products, supports product comparison and price negotiation, manages the shopping cart, and provides a checkout experience.

---

## 🎯 Project Objective

The main objective of this project is to build an intelligent AI-powered technology shopping assistant that can understand a customer's needs and assist them throughout the shopping journey.

The system is designed to:

- Understand customer requirements
- Identify customer intent
- Search available technology products
- Evaluate products based on customer needs
- Recommend suitable products
- Compare different products
- Explain product recommendations
- Support price negotiation
- Apply available discounts and offers
- Add products to the shopping cart
- Manage cart items and quantities
- Calculate discounts and final prices
- Maintain the shopping conversation
- Track important shopping activities

---

## 🚀 Main Features

### 1. 👤 Customer Understanding

The system understands customer requirements such as:

- Budget
- Product category
- Intended usage
- Performance requirements
- Product preferences

### 2. 🔎 Product Discovery

The shopping assistant searches the available product catalog and identifies products matching the customer's requirements.

### 3. 🤖 AI Product Recommendation

The recommendation system evaluates products using factors such as:

- Product price
- Customer budget
- Customer requirements
- Product match
- Product availability

The assistant recommends products that are suitable for the customer's needs.

### 4. 🧠 Agentic Decision Making

The system follows an agentic shopping workflow:

**Customer Goal → Intent Detection → Product Search → Product Evaluation → Decision → Action**

### 5. ⚖️ Product Comparison

Customers can compare products based on:

- Price
- Specifications
- Features
- Suitability
- Customer requirements

### 6. 💰 Price Negotiation

Customers can request a better price.

The system supports:

- Discount requests
- Target price requests
- Negotiation messages
- Offer evaluation

### 7. 🎁 Offers & Discounts

The system supports product offers and discounts and reflects applicable discounts in the shopping total.

### 8. 🛒 Shopping Cart

Customers can:

- Add products
- Select quantities
- Remove products
- View cart items
- View subtotal
- View discounts
- View final total

### 9. 💬 Conversation Management

The system maintains the shopping conversation so customers can continue interacting with the assistant throughout their shopping journey.

### 10. 📊 Analytics

The system records important shopping activities such as:

- Product recommendations
- Product views
- Cart actions
- Negotiations
- Shopping interactions

### 11. 💳 Checkout

The checkout interface supports:

- Full Name
- Delivery Address
- Phone Number
- UPI
- Credit / Debit Card
- Cash on Delivery

The checkout is a demonstration and does not process real payments.

---

## 🔄 Shopping Workflow

Customer Request → Requirement Understanding → Intent Detection → Product Search → Product Evaluation → Recommendation → Comparison → Negotiation → Cart → Checkout

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Agent-based architecture
- Python modules
- Session State
- Product catalog
- Data processing
- Git
- GitHub

---

 
## 📸 Application Screenshots
<img width="1912" height="1175" alt="1st" src="https://github.com/user-attachments/assets/279e740c-34e5-4f52-9b69-7c653d24af2b" />
<img width="1917" height="1062" alt="2nd" src="https://github.com/user-attachments/assets/a22308ba-e724-4337-9f47-0ad52ccc8545" />
<img width="1917" height="1057" alt="3rd" src="https://github.com/user-attachments/assets/f42d37ca-6c82-473b-92f1-f24ee8c81906" />
<img width="1917" height="1062" alt="4th" src="https://github.com/user-attachments/assets/9fc5cf73-ad44-4733-b83b-08acb89a1bba" />
<img width="1917" height="1135" alt="5th" src="https://github.com/user-attachments/assets/24d89dd0-75bf-4e26-8124-c1f59bccba26" />
<img width="1917" height="735" alt="6th" src="https://github.com/user-attachments/assets/8de62945-5d3d-49de-813f-b946e2d9dbbf" />


---

## 📂 Project Structure

The project is organized into application modules, shopping components, agent components, and test files.


```text
AI-Tech-Shopper/
│
├── app.py
├── agent.py
├── agent_brain.py
├── agent_planner.py
├── ai_brain.py
├── analytics.py
├── analytics_data.json
├── bundle.py
├── cart.py
├── cart_manager.py
├── cart_recovery.py
├── chat_agent.py
├── checkout.py
├── compare.py
├── comparison.py
├── conversation_manager.py
├── customer.py
├── intent_engine.py
├── main.py
├── memory.py
├── merchant_analytics.py
├── merchant_dashboard.py
├── merchant_rules.py
├── negotiation.py
├── offers.py
├── product_details.py
├── products.py
├── recommendation.py
├── shopper.py
├── smart_recommendation.py
├── tools.py
│
├── test_agent_brain.py
├── test_agent_offers.py
├── test_cart.py
├── test_cart_recovery_agent.py
├── test_catalog.py
├── test_checkout.py
├── test_commerce_flow.py
├── test_comparison.py
├── test_memory.py
├── test_negotiation_agent.py
├── test_offers.py
├── test_planner.py
├── test_search.py
├── test_tools.py
│
├── .gitignore
└── README.md
