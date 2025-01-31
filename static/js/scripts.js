document.addEventListener('DOMContentLoaded', () => {
    const commentForm = document.querySelector('form');
    const commentList = document.querySelector('.comment-list');

    if (commentForm) {
        commentForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const commentText = commentForm.querySelector('textarea').value;
            
            if (commentText) {
                const newComment = document.createElement('div');
                newComment.classList.add('comment-item');
                newComment.innerHTML = `<p>${commentText}</p>`;
                
                commentList.appendChild(newComment);
                commentForm.querySelector('textarea').value = '';
            }
        });
    }
});
