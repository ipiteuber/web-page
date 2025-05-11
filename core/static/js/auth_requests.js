class AuthRequests {
    static async submitForm(formElement, successCallback, errorCallback) {
        const formData = new FormData(formElement);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
        try {
            const response = await fetch(formElement.action, {
                method: formElement.method,
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken,
                    "X-Requested-With": "XMLHttpRequest"
                },
                credentials: 'include'
            });
            
            const data = await response.json();
            
            if (response.ok) {
                successCallback(data);
            } else {
                errorCallback(data);
            }
        } catch (error) {
            errorCallback({message: 'Network error. Please try again.'});
        }
    }
    
    static showError(container, message) {
        container.classList.remove('d-none');
        container.innerHTML = typeof message === 'string' ? message : 
            `<ul class="mb-0">${Object.values(message).map(err => `<li>${err}</li>`).join('')}</ul>`;
        container.scrollIntoView({ behavior: 'smooth' });
    }
}