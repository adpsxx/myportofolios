const editForm = document.getElementById('project-edit-form');

function getCookie(name) {
    const prefix = `${name}=`;
    const cookie = document.cookie.split(';').map(value => value.trim())
        .find(value => value.startsWith(prefix));
    return cookie ? decodeURIComponent(cookie.slice(prefix.length)) : null;
}

function apiErrorMessage(data, status) {
    const messages = Object.values(data).flat().filter(value => typeof value === 'string');
    return messages.join(' ') || `Request failed (HTTP ${status}).`;
}

if (editForm) {
    editForm.addEventListener('submit', async function(event) {
        event.preventDefault();
        const button = editForm.querySelector('button[type="submit"]');
        const apiUrl = editForm.dataset.apiUrl;
        const redirectUrl = editForm.dataset.redirectUrl;
        button.disabled = true;

        try {
            const fields = new FormData(editForm);
            const payload = {
                title: fields.get('title'),
                description: fields.get('description'),
                thumbnail: fields.get('thumbnail'),
                project_link: fields.get('project_link'),
            };

            const response = await fetch(apiUrl, {
                method: 'PATCH',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify(payload),
            });

            const data = await response.json().catch(() => ({}));
            if (!response.ok) {
                throw new Error(apiErrorMessage(data, response.status));
            }

            showToast('Success', 'Project updated.', 'success');
            window.location.href = redirectUrl;
        } catch (error) {
            showToast('Could not update project', error.message, 'error');
        } finally {
            button.disabled = false;
        }
    });
}
