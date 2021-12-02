const addCommentBtn = document.getElementById('addCommentBtn');
const commentSection = document.getElementById('commentSection');
addCommentBtn.addEventListener('click', e => {
    e.preventDefault();
    let commentBody = document.getElementById('id_body');
    let id = document.getElementById('commentForm').getAttribute('data-id');
    let url = `/comment/add_comment/${id}/`;
    let csrftoken = getCookie('csrftoken');
    

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrftoken);
    fd.append('body', commentBody.value)
    

    $.ajax({
        type: 'POST',
        url: url,
        data: fd,
        success: function(response){
            console.log(response)
            const data = response.data;
            commentBody.value = ''
            commentSection.innerHTML += `<div class="d-flex flex-row comment-row">
            <div class="p-2"><span class="round"><img src="https://i.imgur.com/uIgDDDd.jpg" alt="user" width="50"></span></div>
            <div class="comment-text w-100">
                <h5>${data.author}</h5>
                <div class="comment-footer"> <span class="date">${data.created_at}</span>  <span class="action-icons"> <a href="#" data-abc="true"><i class="fa fa-pencil"></i></a> </span> </div>
                <p class="m-b-5 m-t-10">${data.comment}</p>
            </div>
        </div>`
        },
        error: function(error){
            alert(error.message)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
} );




export default function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}