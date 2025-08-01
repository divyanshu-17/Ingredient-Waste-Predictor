import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Contact Us", page_icon="📬", layout="wide")
st.title("📬 Contact Us")

st.markdown("""
If you have any feedback, questions, or would like to collaborate, feel free to contact us using the form below:
""")

#HTML with EmailJS integration and toast notification
components.html(
"""
<link href="https://cdn.jsdelivr.net/npm/toastify-js/src/toastify.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/toastify-js"></script>
<script src="https://cdn.jsdelivr.net/npm/emailjs-com@3/dist/email.min.js"></script>
<style>
    form {
        max-width: 600px;
        margin: 0 auto;
    }
    input, textarea {
        width: 100%;
        padding: 12px;
        margin-bottom: 12px;
        border-radius: 8px;
        border: 1px solid #ccc;
        font-family: sans-serif;
    }
    button {
        background-color: #facc15;
        color: black;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        cursor: pointer;
    }
    button:hover {
        background-color: #fbbf24;
    }
</style>

<form id="contact-form">
    <input type="text" name="from_name" placeholder="Your Name" required>
    <input type="email" name="reply_to" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message..." rows="5" required></textarea>
    <button type="submit">Send ✉️</button>
</form>

<script>
    emailjs.init("hJ32Y1fqpn_Y6zsXs");

    document.getElementById("contact-form").addEventListener("submit", function(event) {
        event.preventDefault();
        emailjs.sendForm("service_wo9yxma", "template_ri6ky3l", this)
            .then(() => {
                Toastify({
                    text: "✅ Message sent successfully!",
                    duration: 3000,
                    gravity: "top",
                    position: "right",
                    backgroundColor: "#10b981"
                }).showToast();
                this.reset();
            }, (error) => {
                Toastify({
                    text: "❌ Failed to send. Try again!",
                    duration: 3000,
                    gravity: "top",
                    position: "right",
                    backgroundColor: "#ef4444"
                }).showToast();
            });
    });
</script>
""",
height=600,
)