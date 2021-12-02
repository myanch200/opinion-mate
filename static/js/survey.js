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
                `;
                if (question.options.length > 0){
                    question.options.map(option => {
                        question_div.innerHTML += renderOption(question.question_type, option);
                    });
                }else{
                    question_div.innerHTML += renderOption(question.question_type, {"question_id": question.id});
                }
                
                console.log(question.question_type)
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

const renderOption = (type, option) => {
    
    if(type === 'Open Answer'){
        return `
            <div class="answerBox">
            <input type="text" name="${option.question_id}"  class="form-control" placeholder="Write your asnwer">
            </div>
            `
       
    }
    else if(type === 'Normal'){
        return `
            <div class="answerBox">
            <div class="answer">
            <label class="radio-inline">
                <input type="radio" name="${option.question_id}" value="${option.id}">
                ${option.text}
            </label>
            </div>
            </div>
        `;
    }else if(type === 'One To Ten'){
        
        for(var i = 1; i  <11; i++){
            answerBox.innerHTML += `
                <label class="radio-inline">
                    <input type="radio" name="${option.question_id}" value="${i}">
                    
                </label>
            `;
        }
        return answerBox;
    }
}

