import streamlit as st
from PIL import Image

# Sample data for 18 bikes
bikes = {
    "S1": {"name": "Mountain Bike", "price": 200, "threshold": 150, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 1.jpg", "description": "Versatile mountain bike designed for durability and comfort."},
    "S2": {"name": "Road Bike", "price": 160, "threshold": 130, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 2.jpg", "description": "Road bike built for speed and performance on smooth surfaces."},
    "S3": {"name": "Hybrid Bike", "price": 180, "threshold": 140, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 4.jpg", "description": "Hybrid bike perfect for city rides and off-road trails."},
    "S4": {"name": "Electric Bike", "price": 300, "threshold": 250, "image": r"C:\Aga\Belajar\Coding\auction\Electric Polygon.png", "description": "Electric bike offering a smooth and fast riding experience."},
    "S5": {"name": "BMX Bike", "price": 120, "threshold": 100, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 4_.png", "description": "BMX bike suitable for tricks and off-road adventures."},
    "S6": {"name": "Folding Bike", "price": 220, "threshold": 180, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 6.jpg", "description": "Compact folding bike, easy to store and transport."},
    "S7": {"name": "Fat Tire Bike", "price": 250, "threshold": 200, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 1.jpg", "description": "Bike with fat tires for riding on sand, snow, or rough terrain."},
    "S8": {"name": "Gravel Bike", "price": 270, "threshold": 220, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 2.jpg", "description": "Gravel bike built for rough roads and off-road trails."},
    "S9": {"name": "Cruiser Bike", "price": 150, "threshold": 120, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 1.jpg", "description": "Comfortable cruiser bike for leisurely rides."},
    "S10": {"name": "Kids Bike", "price": 100, "threshold": 80, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 2.jpg", "description": "Kid-friendly bike designed for safety and fun."},
    "S11": {"name": "Touring Bike", "price": 280, "threshold": 240, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 1.jpg", "description": "Bike designed for long-distance touring and carrying cargo."},
    "S12": {"name": "Track Bike", "price": 300, "threshold": 250, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 2.jpg", "description": "Track bike optimized for racing on velodromes."},
    "S13": {"name": "City Bike", "price": 130, "threshold": 100, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 1.jpg", "description": "City bike designed for commuting and urban riding."},
    "S14": {"name": "Adventure Bike", "price": 290, "threshold": 240, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 2.jpg", "description": "Adventure bike built for exploring various terrains."},
    "S15": {"name": "Beach Cruiser", "price": 140, "threshold": 110, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 1.jpg", "description": "Stylish beach cruiser bike for casual seaside rides."},
    "S16": {"name": "Enduro Bike", "price": 320, "threshold": 270, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 2.jpg", "description": "High-performance enduro bike for mountain trails."},
    "S17": {"name": "Cyclocross Bike", "price": 275, "threshold": 225, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 1.jpg", "description": "Bike for cyclocross racing and mixed-terrain adventures."},
    "S18": {"name": "Fixed Gear Bike", "price": 150, "threshold": 120, "image": r"C:\Aga\Belajar\Coding\auction\Polygon 2.jpg", "description": "Fixed gear bike for a minimalist and stylish ride experience."},
}

# Sample data for buyers
buyers = {
    "Alice": {"budget": 250},
    "Bob": {"budget": 180},
    "Charlie": {"budget": 300},
    "Diana": {"budget": 160},
}

# Initialize session state for negotiation and logging
if "offers" not in st.session_state:
    st.session_state["offers"] = {bike_id: [] for bike_id in bikes.keys()}
if "accepted_offer" not in st.session_state:
    st.session_state["accepted_offer"] = {bike_id: None for bike_id in bikes.keys()}
if "negotiation_log" not in st.session_state:
    st.session_state["negotiation_log"] = {bike_id: [] for bike_id in bikes.keys()}
if "seller_price" not in st.session_state:
    st.session_state["seller_price"] = {bike_id: bikes[bike_id]["price"] for bike_id in bikes.keys()}

# CSS for styling
st.markdown("""
    <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem;
            background-color: #232F3E;
            color: white;
            font-size: 1.5rem;
        }
        .logo {
            font-weight: bold;
            font-size: 2rem;
            color: #FF9900;
            margin-right: 1rem;
        }
        .nav-links {
            display: flex;
            gap: 1rem;
        }
        .nav-link {
            color: white;
            text-decoration: none;
            font-size: 1.1rem;
        }
        .nav-link:hover {
            text-decoration: underline;
            color: #FF9900;
        }
        .product-card {
            border: 1px solid #e1e1e1;
            border-radius: 8px;
            padding: 10px;
            margin: 5px;
            background-color: #f9f9f9;
            text-align: center;
        }
        .price-tag {
            font-size: 1.2rem;
            color: #b12704;
            font-weight: bold;
        }
        .negotiation-history {
            font-style: italic;
            font-size: 0.9rem;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# Header with logo and navigation
st.markdown("""
    <div class="header">
        <div class="logo">BikeStore</div>
        <div class="nav-links">
            <a href="#available-bikes" class="nav-link">Home</a>
            <a href="#all-negotiation-logs" class="nav-link">Negotiation Logs</a>
            <a href="#accepted-offers" class="nav-link">Accepted Offers</a>
            <a href="#product-dashboard" class="nav-link">Dashboard</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar for product details
st.sidebar.title("Product Dashboard")
selected_bike_id = st.sidebar.selectbox("Select a product to view details", options=bikes.keys())
if selected_bike_id:
    selected_bike = bikes[selected_bike_id]
    try:
        st.sidebar.image(selected_bike["image"], caption=selected_bike["name"], use_column_width=True)
    except FileNotFoundError:
        st.sidebar.error("Image not found.")
    st.sidebar.write(f"**Current Price (Counter Offer):** ${st.session_state['seller_price'][selected_bike_id]}")
    st.sidebar.write(f"**Description:** {selected_bike['description']}")

    # Show negotiation history for selected product
    st.sidebar.subheader("Negotiation History")
    if st.session_state["negotiation_log"][selected_bike_id]:
        for entry in st.session_state["negotiation_log"][selected_bike_id]:
            st.sidebar.write(f"- {entry[0]} offered ${entry[1]}")
    else:
        st.sidebar.write("No negotiation history available.")

# Main Page - Amazon-style product grid
st.markdown('<h1 id="available-bikes">Amazon-style Bike Store</h1>', unsafe_allow_html=True)

# Display available bikes in a grid layout with consistent column order
st.header("Available Bikes")
cols = st.columns(3)  # Display 3 bikes per row

for idx, (bike_id, bike) in enumerate(bikes.items()):
    col = cols[idx % 3]
    with col:
        with st.container():
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            try:
                image = Image.open(bike["image"])
                st.image(image, caption=bike["name"], use_column_width="auto")
            except FileNotFoundError:
                st.error(f"Image for {bike['name']} not found.")
            st.markdown(f"<h4>{bike['name']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<div class='price-tag'>${bike['price']}</div>", unsafe_allow_html=True)
            st.markdown(f"**Current Seller Price (Counter Offer):** ${st.session_state['seller_price'][bike_id]}")
            if st.session_state["accepted_offer"][bike_id] is not None:
                st.markdown(f"**Status:** Sold to {st.session_state['accepted_offer'][bike_id][0]} for ${st.session_state['accepted_offer'][bike_id][1]}")
            else:
                selected_buyer_name = st.selectbox("Choose a buyer", options=list(buyers.keys()), key=f"buyer_{bike_id}")
                buyer_budget = buyers[selected_buyer_name]["budget"]
                st.write(f"Buyer {selected_buyer_name} has a budget of ${buyer_budget}")
                offer_price = st.number_input("Your Offer Price", min_value=0, max_value=buyer_budget, step=5, key=f"offer_{bike_id}")
                if st.button("Submit Offer", key=f"submit_{bike_id}"):
                    if offer_price >= st.session_state["seller_price"][bike_id]:  # Accept if meets/exceeds price
                        st.session_state["accepted_offer"][bike_id] = (selected_buyer_name, offer_price)
                        st.session_state["negotiation_log"][bike_id].append((selected_buyer_name, offer_price))
                        st.success(f"Deal reached! {bike['name']} sold to {selected_buyer_name} for ${offer_price}.")
                    else:
                        st.session_state["offers"][bike_id].append((selected_buyer_name, offer_price))
                        st.session_state["negotiation_log"][bike_id].append((selected_buyer_name, offer_price))
                        st.info(f"Offer of ${offer_price} from {selected_buyer_name} for {bike['name']} did not meet seller's price.")
                        decrement = (bikes[bike_id]["price"] - bikes[bike_id]["threshold"]) / 5
                        st.session_state["seller_price"][bike_id] = max(bikes[bike_id]["threshold"], st.session_state["seller_price"][bike_id] - decrement)
            st.markdown('</div>', unsafe_allow_html=True)

# Display negotiation history log for each bike
st.markdown('<h2 id="all-negotiation-logs">All Negotiation Logs</h2>', unsafe_allow_html=True)
for bike_id, log in st.session_state["negotiation_log"].items():
    if log:
        st.write(f"### Offers for {bikes[bike_id]['name']}:")
        for entry in log:
            st.write(f"- {entry[0]} offered ${entry[1]}")

# Display accepted offers
st.markdown('<h2 id="accepted-offers">Accepted Offers</h2>', unsafe_allow_html=True)
for bike_id, deal in st.session_state["accepted_offer"].items():
    if deal:
        st.write(f"{bikes[bike_id]['name']} sold to {deal[0]} for ${deal[1]}")

# Reset option for the session state (for testing or restarting)
if st.button("Reset Offers"):
    st.session_state["offers"] = {bike_id: [] for bike_id in bikes.keys()}
    st.session_state["accepted_offer"] = {bike_id: None for bike_id in bikes.keys()}
    st.session_state["negotiation_log"] = {bike_id: [] for bike_id in bikes.keys()}
    st.session_state["seller_price"] = {bike_id: bikes[bike_id]["price"] for bike_id in bikes.keys()}
    st.success("All offers and logs have been reset.")
