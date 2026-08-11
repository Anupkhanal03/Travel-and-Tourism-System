console.log("Nepal Travel System loaded");

document.addEventListener("DOMContentLoaded", function () {
    // ===== INITIALIZE AOS =====
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-out-cubic',
            once: true,
            offset: 50
        });
    }

    // ===== NAVBAR SCROLL EFFECT =====
    const navbar = document.getElementById("mainNavbar");
    if (navbar) {
        window.addEventListener("scroll", function () {
            if (window.scrollY > 50) {
                navbar.classList.add("scrolled");
            } else {
                navbar.classList.remove("scrolled");
            }
        });
    }

    // ===== CHATBOT FUNCTIONALITY =====
    const toggleBtn = document.getElementById("chatbotToggleBtn");
    const closeBtn = document.getElementById("chatbotCloseBtn");
    const windowDiv = document.getElementById("chatbotWindow");
    const form = document.getElementById("chatbotForm");
    const input = document.getElementById("chatbotInput");
    const messagesContainer = document.getElementById("chatbotMessages");

    if (toggleBtn && windowDiv) {
        // Toggle Chat Window
        toggleBtn.addEventListener("click", function () {
            windowDiv.classList.toggle("d-none");
            scrollToBottom();
        });

        closeBtn.addEventListener("click", function () {
            windowDiv.classList.add("d-none");
        });

        // Click Suggestion Chips
        messagesContainer.addEventListener("click", function (e) {
            if (e.target.classList.contains("suggestion-chip")) {
                const query = e.target.getAttribute("data-query");
                if (query) {
                    submitMessage(query);
                }
            }
        });

        // Submit Form
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            const message = input.value.trim();
            if (!message) return;
            submitMessage(message);
            input.value = "";
        });
    }

    function scrollToBottom() {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function formatText(text) {
        // Basic Markdown-to-HTML parser for chatbot messages
        let html = text;
        // Bold
        html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        // Links format: [text](url) -> check if local url
        html = html.replace(/\[(.*?)\]\((.*?)\)/g, function(match, label, url) {
            // Check if local route
            const fullUrl = url.startsWith('http') ? url : '/' + url;
            return `<a href="${fullUrl}" class="fw-bold text-decoration-underline" target="_blank">${label}</a>`;
        });
        // Linebreaks
        html = html.replace(/\r?\n/g, '<br>');
        return html;
    }

    function submitMessage(message) {
        // Append User Message
        appendMessage(message, "user");
        scrollToBottom();

        // Append Typing Indicator
        const typingId = appendTypingIndicator();
        scrollToBottom();

        // Call Backend API
        fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            removeTypingIndicator(typingId);
            
            // Append Bot Message
            appendMessage(data.response, "bot");
            
            // If we have recommended packages in structured format, show them
            if (data.packages && data.packages.length > 0) {
                appendPackageCards(data.packages);
            }
            scrollToBottom();
        })
        .catch(err => {
            console.error("Chatbot API error:", err);
            removeTypingIndicator(typingId);
            appendMessage("Sorry, I am facing connectivity issues. Please try again later.", "bot");
            scrollToBottom();
        });
    }

    function appendMessage(text, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("chat-message", sender === "user" ? "user-message" : "bot-message", "mb-3");
        
        const contentDiv = document.createElement("div");
        contentDiv.classList.add("message-content");
        contentDiv.innerHTML = sender === "user" ? escapeHTML(text) : formatText(text);
        
        messageDiv.appendChild(contentDiv);
        messagesContainer.appendChild(messageDiv);
    }

    function appendTypingIndicator() {
        const typingId = "typing_" + Date.now();
        const indicatorDiv = document.createElement("div");
        indicatorDiv.id = typingId;
        indicatorDiv.classList.add("chat-message", "bot-message", "mb-3");
        
        const contentDiv = document.createElement("div");
        contentDiv.classList.add("message-content", "text-muted");
        contentDiv.innerHTML = `
            <div class="spinner-grow spinner-grow-sm" role="status" style="width: 8px; height: 8px;"></div>
            <div class="spinner-grow spinner-grow-sm" role="status" style="width: 8px; height: 8px; animation-delay: 0.2s"></div>
            <div class="spinner-grow spinner-grow-sm" role="status" style="width: 8px; height: 8px; animation-delay: 0.4s"></div>
        `;
        
        indicatorDiv.appendChild(contentDiv);
        messagesContainer.appendChild(indicatorDiv);
        return typingId;
    }

    def_remove = function(id) {
        const el = document.getElementById(id);
        if (el) el.remove();
    }
    
    window.removeTypingIndicator = def_remove;

    function appendPackageCards(packages) {
        const container = document.createElement("div");
        container.classList.add("d-flex", "flex-column", "gap-2", "mt-1", "mb-3", "w-100");
        
        packages.forEach(pkg => {
            const card = document.createElement("div");
            card.classList.add("card", "w-100", "border-light-subtle", "bg-white", "shadow-sm");
            card.style.cssText = "font-size: 0.82rem; border-radius: 10px; overflow: hidden;";
            
            // Build proper image URL – image field is a local filename like 'annapurna_pkg.png'
            let imgSrc = '/static/images/pokhara_pkg.jpg'; // default fallback
            if (pkg.image) {
                if (pkg.image.startsWith('http')) {
                    imgSrc = pkg.image;
                } else {
                    imgSrc = '/static/images/' + pkg.image;
                }
            }
            
            const price = typeof pkg.price === 'number' ? pkg.price.toLocaleString() : pkg.price;
            const duration = pkg.duration_days || pkg.duration || '?';
            const destName = pkg.dest_name || pkg.destination_name || '';
            const bookUrl = pkg.id ? `/book/${pkg.id}` : '/packages';
            
            card.innerHTML = `
                <div class="row g-0 align-items-center">
                    <div class="col-4">
                        <img src="${imgSrc}" class="img-fluid" alt="${pkg.title}"
                             style="height: 80px; width: 100%; object-fit: cover;"
                             onerror="this.src='/static/images/pokhara_pkg.jpg'">
                    </div>
                    <div class="col-8 px-2 py-2">
                        <h6 class="mb-1 fw-bold" style="font-size: 0.78rem; line-height: 1.2;">${pkg.title}</h6>
                        ${destName ? `<p class="text-muted mb-1" style="font-size: 0.68rem;">&#128205; ${destName}</p>` : ''}
                        <p class="text-muted mb-2" style="font-size: 0.7rem;">&#9200; ${duration} Days &nbsp;|&nbsp; &#128176; Rs. ${price}</p>
                        <a href="${bookUrl}" class="btn btn-primary btn-sm py-0 px-2 fw-semibold" style="font-size: 0.65rem; border-radius: 4px;">Book Now &rarr;</a>
                    </div>
                </div>
            `;
            container.appendChild(card);
        });
        messagesContainer.appendChild(container);
    }

    function escapeHTML(str) {
        return str.replace(/[&<>'"]/g, 
            tag => ({
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                "'": '&#39;',
                '"': '&quot;'
            }[tag] || tag)
        );
    }
});