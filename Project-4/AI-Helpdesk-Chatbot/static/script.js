// Save initial HTML of welcome view for reset/clear feature
const initialWelcomeViewHTML = `
    <div id="welcome-view" class="welcome-view">
        <div class="welcome-badge">
            <i class="fa-solid fa-sparkles"></i> Welcome to HR Virtual Support
        </div>
        <h2 class="welcome-heading">What would you like to ask today?</h2>
        <p class="welcome-subtext">Click any of the suggested topics below or type your question to start instant chat.</p>

        <div class="suggestion-grid">
            <div class="suggestion-card" onclick="sendQuickMessage('How do I apply for leave?')">
                <div class="card-icon icon-leave">
                    <i class="fa-solid fa-umbrella-beach"></i>
                </div>
                <div class="card-text">
                    <h3>Apply for Leave</h3>
                    <p>"How do I submit a leave application?"</p>
                </div>
                <i class="fa-solid fa-arrow-right card-arrow"></i>
            </div>

            <div class="suggestion-card" onclick="sendQuickMessage('When will salary come?')">
                <div class="card-icon icon-salary">
                    <i class="fa-solid fa-money-bill-wave"></i>
                </div>
                <div class="card-text">
                    <h3>Payroll & Salary</h3>
                    <p>"When will monthly salary be credited?"</p>
                </div>
                <i class="fa-solid fa-arrow-right card-arrow"></i>
            </div>

            <div class="suggestion-card" onclick="sendQuickMessage('What are your working hours?')">
                <div class="card-icon icon-timing">
                    <i class="fa-solid fa-business-time"></i>
                </div>
                <div class="card-text">
                    <h3>Office Hours</h3>
                    <p>"What are the official working hours?"</p>
                </div>
                <i class="fa-solid fa-arrow-right card-arrow"></i>
            </div>

            <div class="suggestion-card" onclick="sendQuickMessage('Show me company holiday list')">
                <div class="card-icon icon-holiday">
                    <i class="fa-solid fa-plane-departure"></i>
                </div>
                <div class="card-text">
                    <h3>Holidays & Calendar</h3>
                    <p>"Where can I view the company holiday list?"</p>
                </div>
                <i class="fa-solid fa-arrow-right card-arrow"></i>
            </div>

            <div class="suggestion-card" onclick="sendQuickMessage('What are the employee medical benefits?')">
                <div class="card-icon icon-benefits">
                    <i class="fa-solid fa-briefcase-medical"></i>
                </div>
                <div class="card-text">
                    <h3>Health & Benefits</h3>
                    <p>"What insurance and perks are provided?"</p>
                </div>
                <i class="fa-solid fa-arrow-right card-arrow"></i>
            </div>

            <div class="suggestion-card" onclick="sendQuickMessage('How do I contact HR?')">
                <div class="card-icon icon-contact">
                    <i class="fa-solid fa-headset"></i>
                </div>
                <div class="card-text">
                    <h3>Contact HR Team</h3>
                    <p>"What is HR email and phone contact?"</p>
                </div>
                <i class="fa-solid fa-arrow-right card-arrow"></i>
            </div>
        </div>
    </div>
`;

// Helper: Get Current Time String (e.g. 10:42 AM)
function getCurrentTimeString() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

// Send Quick Message when user clicks a suggestion card or topic chip
function sendQuickMessage(text) {
    const input = document.getElementById("user-input");
    input.value = text;
    sendMessage();
}

// Main Send Message Function
function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (message === "") return;

    const chatBox = document.getElementById("chat-box");
    const welcomeView = document.getElementById("welcome-view");

    // Remove welcome view on first user message
    if (welcomeView) {
        welcomeView.remove();
    }

    const timeStr = getCurrentTimeString();

    // 1. Display User Message
    const userMsgRow = document.createElement("div");
    userMsgRow.className = "message-row user-row";
    userMsgRow.innerHTML = `
        <div class="msg-avatar">
            <i class="fa-solid fa-user"></i>
        </div>
        <div class="msg-content-wrapper">
            <div class="msg-bubble">${escapeHTML(message)}</div>
            <div class="msg-meta">
                <span class="msg-time">${timeStr}</span>
            </div>
        </div>
    `;
    chatBox.appendChild(userMsgRow);

    // Clear input
    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    // 2. Display Typing Indicator
    const typingIndicatorRow = document.createElement("div");
    typingIndicatorRow.className = "message-row bot-row typing-row";
    typingIndicatorRow.id = "typing-indicator";
    typingIndicatorRow.innerHTML = `
        <div class="msg-avatar">
            <i class="fa-solid fa-robot"></i>
        </div>
        <div class="msg-content-wrapper">
            <div class="msg-bubble">
                <div class="typing-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    `;
    chatBox.appendChild(typingIndicatorRow);
    chatBox.scrollTop = chatBox.scrollHeight;

    // 3. Fetch Chat API Response
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Remove typing indicator
        const indicator = document.getElementById("typing-indicator");
        if (indicator) indicator.remove();

        const botReply = data.reply || "Sorry, I couldn't process your request.";
        const botTimeStr = getCurrentTimeString();

        // Display Bot Message
        const botMsgRow = document.createElement("div");
        botMsgRow.className = "message-row bot-row";
        botMsgRow.innerHTML = `
            <div class="msg-avatar">
                <i class="fa-solid fa-robot"></i>
            </div>
            <div class="msg-content-wrapper">
                <div class="msg-bubble">${escapeHTML(botReply)}</div>
                <div class="msg-meta">
                    <span class="msg-time">${botTimeStr}</span>
                    <button class="copy-btn" onclick="copyToClipboard(this, \`${escapeHTML(botReply).replace(/`/g, '\\`')}\`)" title="Copy reply">
                        <i class="fa-regular fa-copy"></i> Copy
                    </button>
                </div>
            </div>
        `;
        chatBox.appendChild(botMsgRow);
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error("Error communicating with chatbot:", error);
        const indicator = document.getElementById("typing-indicator");
        if (indicator) indicator.remove();

        const errorRow = document.createElement("div");
        errorRow.className = "message-row bot-row";
        errorRow.innerHTML = `
            <div class="msg-avatar">
                <i class="fa-solid fa-triangle-exclamation"></i>
            </div>
            <div class="msg-content-wrapper">
                <div class="msg-bubble" style="border-color: #fca5a5; background: #fef2f2; color: #991b1b;">
                    Sorry, a network error occurred. Please try again.
                </div>
            </div>
        `;
        chatBox.appendChild(errorRow);
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}

// Reset & Clear Chat Window
function clearChat() {
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML = initialWelcomeViewHTML;
}

// Toggle Help Modal
function toggleHelpModal(event) {
    if (event && event.target !== event.currentTarget && event.target.id !== "help-modal") return;
    const modal = document.getElementById("help-modal");
    modal.classList.toggle("hidden");
}

// Copy Text Helper
function copyToClipboard(btn, text) {
    navigator.clipboard.writeText(text).then(() => {
        const originalHTML = btn.innerHTML;
        btn.innerHTML = `<i class="fa-solid fa-check" style="color:#22c55e;"></i> Copied!`;
        setTimeout(() => {
            btn.innerHTML = originalHTML;
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

// Utility to prevent XSS injection
function escapeHTML(str) {
    return str
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

// Initialize Event Listeners & Rotating Input Placeholder
document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("user-input");

    // Fix keypress Enter handler
    if (input) {
        input.addEventListener("keypress", (event) => {
            if (event.key === "Enter") {
                event.preventDefault();
                sendMessage();
            }
        });
    }

    // Dynamic rotating input placeholders to guide new users
    const samplePlaceholders = [
        "Ask about leave policy (e.g. How do I apply for leave?)...",
        "Ask about payday (e.g. When is salary credited?)...",
        "Ask about office timings (e.g. What are working hours?)...",
        "Ask about benefits (e.g. Tell me about health insurance)...",
        "Ask about ID card (e.g. How to replace lost ID badge?)...",
        "Ask about HR support (e.g. What is HR contact email?)..."
    ];

    let placeholderIdx = 0;
    setInterval(() => {
        if (input && document.activeElement !== input && input.value === "") {
            placeholderIdx = (placeholderIdx + 1) % samplePlaceholders.length;
            input.setAttribute("placeholder", samplePlaceholders[placeholderIdx]);
        }
    }, 4000);
});