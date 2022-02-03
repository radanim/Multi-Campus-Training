package main

import ( // 패키지 함수 structure 가져오기
	"encoding/json" // 49 .json 데이터파일 호출하는 unmarshal을 포함하는 패키지
	"flag"          // 28~37 flag 패키지 적용. flag.string 함수 호출 패키지, 옵션값 받아오는 패키지, json 링크파일 읽고 위도, 경도 입력
	"fmt"           // 화면에 출력하는 프린트 기능을 가진 패키지
	"io/ioutil"     // 39번 코드와 연결.
	"math"          // 제곱근, 제곱, 삼각함수, 파이값 활용하기 위한 패키지.
	"strconv"       // 문자열 변환 패키지
	"strings"       // .split 함수를 사용하기 위해 사용된 패키지
)

type Collection struct { //같은 문자열 하이퍼링크, 구조체, 여러가지 타입의 값들을 하나의 형태로 구별. 하나하나의 단위로 구별되는 몸통을 나타내는 구조체.
	Type     string `json:"type"` // json 데이터파일 구조를 가져옴. 코드로 구조를 알려줌. 구조체 선언.
	Features []struct {
		Type     string `json:"type"`
		Geometry struct {
			Type        string      `json:"type"`
			Coordinates [][]float64 `json:"coordinates"` //좌표가 두값의 쌍으로 존재
		} `json:"geometry"`
		Properties struct {
			ID string `json:"id"`
		} `json:"properties"`
	} `json:"features"`
}

func main() {
	link := flag.String("links", "", "linksfile.json")     // 파일명을 스트링으로 받아옴. links라는 옵션명을 사용. 파일명이 바뀌면 역시 옵션값 변경.
	target := flag.String("target", "", "target geometry") // 타겟 좌표를 스트링으로 받아옴. target이라는 옵션명을 사용.
	var pX float64                                         // var = 변수선언 pX,pY 실수값 64비트
	var pY float64

	flag.Parse()           // flag string 파싱, 파싱 = 쪼개기 옵션명 = 값, 옵션명 = 값, 세트 순서 상관없음. 구글 검색 스터디
	if flag.NFlag() == 0 { // 옵션값이 안들어가 있을 경우
		flag.Usage() // 옵션 사용방식을 출력
		return
	}

	file, _ := ioutil.ReadFile(*link) //파일인지 아닌지 확인. link가 가리키는 스트링을 쓰는 파일을 읽어옴.

	s := strings.Split(*target, ",") // 타겟 값을 , 로 구분하여 나눠서 s 변수에 저장. 명령어의 타겟 옵션의 값을 strings.Split으로 나눠서 s변수값에 넣는다.
	x1, y1 := s[0], s[1]             // 위도, 경도 s 0,1번째 인덱스에 값을 x1,y1으로 넣는다.

	pX, _ = strconv.ParseFloat(x1, 64) //strconv 스트링을 float으로 변환. strconv 패키지내 parsefloat 함수사용
	pY, _ = strconv.ParseFloat(y1, 64) // ,_ 형식, 저런 형태로 표현해야됨. 28~45번줄 태진이형 파트.
	//
	data := Collection{} // data 변수를 collection 구조체로 선언.

	_ = json.Unmarshal([]byte(file), &data) // Json 데이터 로드 완료, 데이터 로드하는 함수 unmarshal. &: 변수값의 주소, 함수의 형태

	var shortDistanceIndex = findCloseGroup(data, pX, pY) // 필요한 3개 인자. 태진이형 파트.

	var result = calcVectorPoint(pX, pY, data, shortDistanceIndex)        // 태진이형 파트.
	fmt.Println("좌표 : ", result)                                          // result가 수선의발 H점의 좌표
	fmt.Println("최단거리 : ", measureDistance(pX, pY, result[0], result[1])) //fnt.println, result[0,1]이 수선의 발 H의 좌표 x,y값. 태진이형 파트.

}

// 가까운 거리의 그룹 찾기
func findCloseGroup(data Collection, latitude float64, longitude float64) int {
	var shortDistance float64 = 9999. //  굉장히 높은값을 임의로 선언. 먼저 특정값을 설정해줌.
	var indexID int

	for i := 0; i < len(data.Features); i++ { // features에서 몇번째냐.
		for j := 0; j < len(data.Features[i].Geometry.Coordinates); j++ {
			var x = data.Features[i].Geometry.Coordinates[j][0]
			var y = data.Features[i].Geometry.Coordinates[j][1]
			var tmpDis = math.Sqrt(math.Pow(latitude-x, 2) + math.Pow(longitude-y, 2))

			if tmpDis <= shortDistance {
				shortDistance = tmpDis
				indexID = i
			}
		}
	}

	return indexID
}

func calcVectorPoint(latitude float64, longitude float64, data Collection, indexID int) [2]float64 {

	var feature = data.Features[indexID]
	// fmt.Println("ID : ", feature.Properties.ID)
	var x1, x2, y1, y2 float64

	if len(feature.Geometry.Coordinates) == 2 { // 좌표가 두개뿐 일 때는 굳이 두 좌표를 찾을 필요 없음
		x1 = feature.Geometry.Coordinates[0][0]
		y1 = feature.Geometry.Coordinates[0][1]
		x2 = feature.Geometry.Coordinates[1][0]
		y2 = feature.Geometry.Coordinates[1][1]
	} else { // 좌표가 여러개일 때는 가까운 좌표 두개 검색
		var firstX, firstY, secondX, secondY float64
		var distanceFirst = 999.
		var distanceSecond = 999.

		for i := 0; i < len(feature.Geometry.Coordinates); i++ {
			var x = feature.Geometry.Coordinates[i][0]
			var y = feature.Geometry.Coordinates[i][1]

			var tmpDis = math.Sqrt(math.Pow(latitude-x, 2) + math.Pow(longitude-y, 2))

			if tmpDis <= distanceFirst {
				firstX = x
				firstY = y
				distanceFirst = tmpDis
			} else if tmpDis <= distanceSecond {
				secondX = x
				secondY = y
				distanceSecond = tmpDis
			}
		}

		x1 = firstX
		y1 = firstY
		x2 = secondX
		y2 = secondY

		// fmt.Println("x1", x1, "y1", y1)
		// fmt.Println("x2", x2, "y2", y2)
	}

	var a = (y2 - y1)
	var b = -(x2 - x1)
	var c = -(x1*y2 - x2*y1)
	var k = (a*latitude + b*longitude + c) / (math.Pow(a, 2) + math.Pow(b, 2))
	var x = latitude - a*k
	var y = longitude - b*k

	return [2]float64{x, y}
}

func measureDistance(latitude float64, longitude float64, pX float64, pY float64) float64 { // 타입만 지정해줄뿐 위의 pX,pY와는 다르다.
	var R = 6378.137 // Radius of earth in KM
	var dLat = pX*math.Pi/180 - latitude*math.Pi/180
	var dLon = pY*math.Pi/180 - longitude*math.Pi/180

	var a = math.Sin(dLat/2)*math.Sin(dLat/2) + math.Cos(latitude*math.Pi/180)*math.Cos(pX*math.Pi/180)*math.Sin(dLon/2)*math.Sin(dLon/2)
	var c = 2 * math.Atan2(math.Sqrt(a), math.Sqrt(1-a))
	var d = R * c

	return d * 1000 // meter
}
