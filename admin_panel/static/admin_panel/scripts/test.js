$('document').ready(() => {
	let answer_template = '<div class="answer form-group form-inline" style="display: flex; flex-direction: row; justify-content: space-between">'+
		'<label class="control-label">Answer:</label>'+
		'<input style="width: 100%" type="text" class="form-control" name="answer_text">'+
		'<label>Right:</label>'+
		'<input type="checkbox" class="form-checkbox" name="is_right">'+
		'<button type="button" class="btn btn-danger remove-answer"><span class="glyphicon glyphicon-trash"></span></button>'+
	'</div>';
	let question_template = '<div class="panel question">'+
		'<div class="form-group">'+
			'<label>Question:</label>'+
			'<input type="text" class="form-control" name="question_text">'+
			'<label>Multianswer:</label>'+
			'<input type="checkbox" class="form-checkbox" name="is_multianswer">'+
		'</div>'+
		'<div class="answers">'+
		'</div>'+
		'<button type="button" class="btn btn-danger del-question">Del question</button>'+
		'<button type="button" class="btn btn-success add-answer" >Add answer</button><br>'+
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
				"title": $("input[name=test_title]").val(),
				"visible": $("input[name=test_visible]").prop("checked"),
				"questions": []
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
				testObj["questions"].push(questionObj);
			}
			//console.log(testObj);
		   	$.ajax({
				url: window.location.href,
				method: "POST",
				data: JSON.stringify(testObj),
				headers: {
					"X-CSRFToken": [$("input[name=csrfmiddlewaretoken]").val()]
				}
			}).fail(() => {
				alert("fail");
			});
			//fetch(window.location.href)
		});
	}
	set_handlers();
});


