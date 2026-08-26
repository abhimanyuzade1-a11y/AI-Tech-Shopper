# 🤖 AI Personal Tech Shopper

An agentic AI-powered technology shopping assistant that helps customers discover, compare, negotiate, and purchase technology products based on their budget, requirements, and preferences.

---

## 📌 Project Overview

AI Personal Tech Shopper is an intelligent shopping assistant designed to simplify the technology buying process.

The system understands customer requirements, identifies customer intent, searches the product catalog, evaluates products, recommends suitable products, supports product comparison and price negotiation, manages the shopping cart, and provides a checkout experience.
## 🚀 Live Demo
---

🌐 **Live Website:** https://ai-tech-shopper.streamlit.app/

💻 **GitHub Repository:** https://github.com/abhimanyuzade1-a11y/AI-Tech-Shopper

The AI Personal Tech Shopper is publicly deployed and can be tested directly through the live website.
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
---
```
---
## 💻 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/abhimanyuzade1-a11y/AI-Tech-Shopper.git
cd AI-Tech-Shopper
---

```
---
## 📊 Project Status

🟢 **Live and Deployed**

The AI Personal Tech Shopper is currently working locally and publicly deployed using Streamlit Community Cloud.

### Current Capabilities

- AI-powered product recommendations
- Customer requirement understanding
- Product search
- Product comparison
- Price negotiation
- Discount calculation
- Shopping cart management
- Checkout flow
- Order confirmation
- Shopping analytics
---

## 🏗️ System Architecture

The AI Personal Tech Shopper follows an agentic shopping workflow:
```

Customer Request
↓
Intent Detection
↓
Requirement Understanding
↓
Product Search
↓
Product Evaluation
↓
AI Recommendation
↓
Comparison / Negotiation
↓
Shopping Cart
↓
Checkout
↓
Order Confirmation
↓
Analytics
```
---

## 🧩 Core Components

The project is organized into multiple Python modules, with each module responsible for a specific part of the shopping workflow.

### 🤖 Agent Brain

**`agent_brain.py`**

Handles the main AI decision-making logic and coordinates the shopper's actions.

### 🧠 Agent Planner

**`agent_planner.py`**

Helps plan the sequence of actions required to fulfill a customer's shopping request.

### 🎯 Intent Engine

**`intent_engine.py`**

Identifies the customer's intent and determines what action the shopper should perform.

### 🔎 Product Search & Catalog

**`products.py`**

Contains the product catalog and product information used by the shopping system.

**`product_details.py`**

Handles detailed product information.

### ⭐ Recommendation Engine

**`recommendation.py`**

Generates product recommendations based on customer requirements.

**`smart_recommendation.py`**

Provides additional recommendation logic for matching products with customer needs.

### ⚖️ Product Comparison

**`comparison.py`**

Handles product comparison and helps customers evaluate different products.

### 💰 Price Negotiation

**`negotiation.py`**

Handles customer price negotiation requests and determines applicable offers.

**`offers.py`**

Manages available offers and discounts.

### 🛒 Shopping Cart

**`cart.py`**

Contains shopping cart functionality.

**`cart_manager.py`**

Manages cart items, quantities, totals, and cart operations.

### 💳 Checkout

**`checkout.py`**

Handles the checkout process and final purchase calculations.

### 💬 Conversation Management

**`conversation_manager.py`**

Maintains the shopping conversation and helps the assistant continue interacting with the customer.

### 📊 Analytics

**`analytics.py`**

Records and manages shopping activity and analytics data.

**`merchant_analytics.py`**

Provides analytics functionality for merchant-related insights.

### 🖥️ Application

**`app.py`**

Provides the Streamlit user interface and connects the different components into the complete AI shopping experience.
