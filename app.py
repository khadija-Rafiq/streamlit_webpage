

import streamlit as st

# 🎯 Page Configurations
st.set_page_config(page_title="Scourer - Best Cleaning Sponge", page_icon="🧽", layout="wide")

# 🏠 Page Title
st.title("🧼 Scourer Order Page")

# ✅ Google Form ka sahi public link
google_form_link = "https://forms.gle/pw5PvmeogjPyyTNP8"

# 🔹 Custom CSS for Button Styling with Hover Effect
st.markdown("""
    <style>
        .order-button {
            background-color: #FF7E79; 
            color: white; 
            text-decoration: none;
            padding: 12px 24px; 
            font-size: 18px; 
            font-weight: bold; 
            border-radius: 8px; 
            display: inline-block; 
            text-align: center;
            transition: 0.3s ease-in-out; /* Smooth transition */
            border: none;
        }
        .order-button:hover {
            background-color: red; /* Hover pe color red ho jayega */
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 Centered Order Now Button
st.markdown(
    f'<div style="display: flex; justify-content: center; margin-top: 20px;">'
    f'<a href="{google_form_link}" target="_blank" class="order-button">🛒 Order Now</a></div>',
    unsafe_allow_html=True,
)

# 🌟 Header
st.title("🧽 Ultimate Scourer for Sparkling Clean Dishes!")
st.write("The perfect solution for removing tough stains and grease from your kitchenware.")

# 🖼️ Product Image
st.image("https://firebrandbbq.com.au/wp-content/uploads/2019/03/stainless-steel-scourer-2.jpg", width=300, caption="High-Quality Scourer")

# 🔥 Features Section
st.header("✨ Why Choose Our Scourer?")
st.markdown("""
✅ **Removes tough grease & stains easily**  
✅ **Durable and long-lasting**  
✅ **Safe for hands & all types of utensils**  
✅ **Available in multiple sizes**  
""")

# 📢 Pricing & Contact
st.header("💰 Price & Order Now!")
st.write("🛒 **Only 259Rs/- per pack! 01 pack = 12 pieces.** Bulk discounts available.")

st.subheader("📞 Contact Us:")
st.write("📍 **Visit Store:** D/386 Hasrat Mohani Colony, Bara Board, Karachi")  
st.write("📧 **Email:** dijaduaa@gmail.com")  # ✅ Email spelling fixed
st.write("📞 **Phone:** 0314-3504308")  

# 🛍️ Buy Now Section
st.header("🛍️ Get Yours Today!")


st.markdown(
     f'<div style="display: flex; justify-content: center; margin-top: 20px;">'
     f'<a href="{google_form_link}" target="_blank" style="background-color:#FF7E79; color:white ; '
     f'text-decoration:none; padding:12px 24px; font-size:18px; font-weight:bold; border-radius:8px; '
    f'display:inline-block; text-align:center;">'
    f'🛒 Order Now</a></div>',
    unsafe_allow_html=True,
 )


# 🎉 Title Below
st.title("Show your Love & Support! ❤️")

# 🔥 Interactive Footer
st.markdown("---")  # Separator Line
st.subheader("👍 Like, 💬 Comment, 🔄 Share & 📢 Subscribe!")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("👍 Like"):
        st.toast("💙 Thanks for liking!")

with col2:
    if st.button("💬 Comment"):
        st.toast("📝 Thanks for your feedback!")

with col3:
    if st.button("🔄 Share"):
        st.toast("🔗 Share this with your friends!")

with col4:
    if st.button("📢 Subscribe"):
        st.toast("🎉 You're subscribed!")

# 📢 Footer
st.markdown("---")
st.write("© 2025 Scourer Brand. All rights reserved. Created by **M. Rafiq**.")

