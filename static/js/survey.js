document.addEventListener('DOMContentLoaded', () => {
    const url = '/survey/get-questions/1';
    $.ajax({
        type: 'GET',
        url: url,
        dataType: 'json',
        success: function(response){
            const questions = response;
            console.log(questions);
            questions.map(question => {
                let question_div = document.createElement('div');
                question_div.classList.add('question');
                question_div.id = question.id;
                question_div.innerHTML = `
                    <h3>${question.question}</h3>
                    <div class="answers">
                        ${question.options.map(option => `<div class="answer" data-id="${option.id}">${option.text}</div>`).join('')}
                    </div>
                `;
                document.querySelector('#questionBox').appendChild(question_div);
            })
        },
        error: function(error){
            alert(error.message)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
} );



