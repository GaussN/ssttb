$('document').ready(() => {
	let answer_template = '<div class="answer form-group form-inline" > '+
		'<label class="control-label">Ответ:</label>'+
		'<input style="width: 100%" type="text" class="form-control" name="answer_text">'+
		'<label>Правильный:</label>'+
		'<input type="checkbox" class="form-checkbox" name="is_right">'+
		'<button type="button" class="btn btn-danger remove-answer"><span class="glyphicon glyphicon-trash"></span></button>'+
	'</div>';
	let question_template = '<div class="panel question">'+
		'<div class="form-group">'+
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
					let asnwerObj = {
						"answer": $(answer).find("input[name=answer_text]").val(),
						"right": $(answer).find("input[name=is_right]").prop("checked")
					};
					questionObj["answers"].push(asnwerObj);
				}
				testObj["test_json"].push(questionObj);
			}
			testObj["test_json"] = JSON.stringify(testObj["test_json"])
		   	$.ajax({
				url: window.location.href,
				method: "POST",
				data: testObj,
				headers: {
					"X-CSRFToken": [$("input[name=csrfmiddlewaretoken]").val()]
				}
				success: (response)=>{
				    if (response.redirected) {
                        window.location.href = response.url;
                    }
				},
				error: () => {
				    alert("fail");
				}
			});
			//fetch(window.location.href)
		});
	}
	set_handlers();
});


