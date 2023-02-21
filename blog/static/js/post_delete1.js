function deletePost(postId) {
    if (confirm('Ви впевнені, що хочете видалити цей пост?')) {
        fetch(`/post/${postId}/delete`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        }).then(response => {
            if (response.redirected) {
                window.location.href = response.url; // перенаправити на домашню сторінку
            }
        });
    }
}