$('document').ready(() => {
	let answer_template = '<div class="answer form-group form-inline" > '+
	    '<span class="form-error-message"></span><br>'+
		'<label class="control-label">Ответ:</label>'+
		'<input style="width: 100%" type="text" class="form-control" name="answer_text">'+
		'<label>Правильный:</label>'+
		'<input type="checkbox" class="form-checkbox" name="is_right">'+
		'<button type="button" class="btn btn-danger remove-answer"><span class="glyphicon glyphicon-trash"></span></button>'+
	'</div>';
	let question_template = '<div class="panel question">'+
		'<div class="form-group">'+
		    '<span class="form-error-message"></span><br>'+
			'<label>Вопрос:</label>'+
			'<input type="text" class="form-control" name="question_text">'+
			'<label>Несколько ответов:</label>'+
			'<input type="checkbox" class="form-checkbox" name="is_multianswer">'+
		'</div>'+
		'<div class="answers">'+
		'</div>'+
		'<button type="button" class="btn btn-danger del-question">Удалить ответ</button>'+
		'<button type="button" class="btn btn-success add-answer" >Добавить ответ</button><br>'+
	'</div>';
	function set_handlers(){
		$("button").off();
		$("button.remove-answer").click((event)=>{
			$(event.target).closest("div.answer").remove();
		});
		$("button.add-answer").click((event)=>{
			$(event.target).parent().find("div.answers").append(answer_template);
			set_handlers();
		});
		$("button.del-question").click((event)=>{
			console.log($(event.target).parent());
			$(event.target).parent().remove();
		});
		$("button.add-question").click((event)=>{
			$("div.questions").append(question_template);
			set_handlers();
		});
		$("button.submit").click((event)=>{
			event.preventDefault();
			let testObj = {
				"topic": $("input[name=test_title]").val(),
				"visible": $("input[name=test_visible]").prop("checked"),
				"test_json": []
			};
	
			let questions = $("div.question");
			for(let question of questions){
				let questionObj = {
					"text": $(question).find("input[name=question_text]").val(),
					"multianswer": $(question).find("input[name=is_multianswer]").prop("checked"),
					"answers": []
				};
				let answers = $(question).find("div.answer");
				for(let answer of answers){
					let answerObj = {
						"answer": $(answer).find("input[name=answer_text]").val(),
						"right": $(answer).find("input[name=is_right]").prop("checked")
					};
					questionObj["answers"].push(answerObj);
				}
				testObj["test_json"].push(questionObj);
			}
			testObj["test_json"] = JSON.stringify(testObj["test_json"])

            $('span.form-error-message').text("");
            if (!$("input[name=test_title]").val()){
                $('span.form-error-message').text("Тест дожен иметь название");
                return;
            }
            if (!$("div.question").length){
                $('span.form-error-message').text("Тест должен содержать вопросы");
                return;
            }

            for (let question of $("div.question")){
                let question_error = $(question).find('.form-group span.form-error-message:first');
                question_error.text("");
                console.log(question_error);
                if (!$(question).find("input[type=text]").val()){
                    question_error.text("Вопрос должен содержать текст");
                    return;
                }
                if (!$(question).find(".answers>.answer").length){
                    question_error.text("Вопрос должен иметь ответы");
                    return;
                }

                let have_right = false;
                for (let answer of $(question).find(".answers > .answer")){
                    let answer_error = $(answer).find('span.form-error-message');

                    if(!$(answer).find('input[type=text]').val()){
                        answer_error.text("Ответ должен содержать текст");
                        return;
                    }
                    if($(answer).find('input[type=checkbox]').prop("checked")){
                        have_right = true;
                    }
                }
                if (!have_right){
                    console.log(question_error);
                    question_error.text("Вопрос должен содержать правильные ответы");
                    return;
                }
            }
            // Мне стыдно зa этот костыль
            let form = $('.hide-block>form');
            let topic = form.find('input[name=topic]'); topic.val(testObj['topic']);
            let test_json = form.find('textarea[name=test_json]'); test_json.val(testObj['test_json']);
            let visible = form.find('input[name=visible]'); visible.prop('checked', testObj['visible']);

            form.submit();
            //
		});
	}
	set_handlers();
});


