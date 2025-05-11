function setupAccountDeletion(formId, confirmationOptions) {
    const form = document.getElementById(formId);
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Configuracion de la confirmacion
        const { 
            title = 'Are you sure?', 
            text = "You won't be able to revert this!",
            confirmText = 'Yes, delete it!',
            successMessage = 'Your account has been deleted.',
            redirectUrl = '/'
        } = confirmationOptions || {};
        
        // Mostrar confirmacion
        const result = await Swal.fire({
            title,
            text,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#dc3545',
            cancelButtonColor: '#6c757d',
            confirmButtonText: confirmText
        });
        
        if (result.isConfirmed) {
            try {
                const formData = new FormData(form);
                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                    credentials: 'include'
                });
                
                const data = await response.json();
                
                if (response.ok && data.success) {
                    await Swal.fire(
                        'Deleted!',
                        successMessage,
                        'success'
                    );
                    window.location.href = redirectUrl;
                } else {
                    throw new Error(data.message || 'Could not delete account');
                }
            } catch (error) {
                Swal.fire(
                    'Error!',
                    error.message,
                    'error'
                );
            }
        }
    });
}