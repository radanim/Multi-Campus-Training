//엘리먼트들에 대한 데이터를 테이블 형식으로 화면에 표현하기

function makeTable(elem){
	var $table = $("<table border=1>"); //테이블 테그 하나 만듬. 
	
	//컬럼 정의하기
	for(var i =0; i<1;i++){ //반복문 돌린 이유: 반복문 없어도 됨. 밑에랑 구조 똑같이 만들기 0부터 1전까지
		var $tr=$("<tr>");
		for(var j=0; j<elem.eq(0).children().length;j++){
			var $td=$("<td>").append(elem.eq(0).children().eq(j).prop("tagName"));
			$tr.append($td); //0~4까지 태그네임을 가지고 와라. 총 5개. 
		}
		$table.append($tr);
	}
	
	//데이터 넣기
	for(var i =0; i<elem.length;i++){ // 
		var $tr=$("<tr>"); //100~206까지 107개 돌림.
		for(var j=0; j<elem.eq(i).children().length;j++){
			var $td=$("<td>").append(elem.eq(i).children().eq(j).text());
			$tr.append($td); //텍스트 요소 자식들을 불러와서 바디에 붙이게 됨. 
		}
		$table.append($tr);
	}
	
	//만들어진 테이블 반환
	return $table;
}



