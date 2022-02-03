package main

import (
    "encoding/json"
   "fmt"
   "math"
   "io/ioutil"
)

type Collection struct {
   Type     string `json:"type"`
   Features []struct {
      Type     string `json:"type"`
      Geometry struct {
         Type        string      `json:"type"`
         Coordinates [][]float64 `json:"coordinates"`
      } `json:"geometry"`
      Properties struct {
         ID string `json:"id"`
      } `json:"properties"`
   } `json:"features"`
}


func main() {

    // 주어진 좌표
    const (
        pX = 127.027268062
        pY = 37.499212063
    )

    file, _ := ioutil.ReadFile("links.geojson.txt")
    
    data := Collection{}
    
    _ = json.Unmarshal([]byte(file), &data) // Json 데이터 로드 완료
    
    var shortDistanceIndex = findCloseGroup(data, pX, pY)

    var result = calcVectorPoint(pX, pY, data, shortDistanceIndex)
    fmt.Println("좌표 : ", result)
    fmt.Println("최단거리 : ", measureDistance(pX, pY, result[0], result[1]))

}

// 가까운 거리의 그룹 찾기
func findCloseGroup(data Collection, latitude float64, longitude float64) int {
    var shortDistance float64 = 9999.
    var indexID int

     for i := 0; i < len(data.Features); i++ {
        for j:= 0; j < len(data.Features[i].Geometry.Coordinates); j++ {
            var x = data.Features[i].Geometry.Coordinates[j][0]
            var y = data.Features[i].Geometry.Coordinates[j][1]
            var tmpDis = math.Sqrt(math.Pow(latitude - x, 2) + math.Pow(longitude - y, 2))

            if (tmpDis <= shortDistance) {
                shortDistance = tmpDis
                indexID = i
            } 
        }
   }

    return indexID;
}

func calcVectorPoint(latitude float64, longitude float64, data Collection, indexID int) [2]float64 {

    var feature = data.Features[indexID];
    fmt.Println("ID : ", feature.Properties.ID)
    var x1, x2, y1, y2 float64

    if (len(feature.Geometry.Coordinates) == 2) { // 좌표가 두개뿐 일 때는 굳이 두 좌표를 찾을 필요 없음
        x1 = feature.Geometry.Coordinates[0][0]
        y1 = feature.Geometry.Coordinates[0][1]
        x2 = feature.Geometry.Coordinates[1][0]
        y2 = feature.Geometry.Coordinates[1][1]
    } else { // 좌표가 여러개일 때는 가까운 좌표 두개 검색
        var firstX, firstY, secondX, secondY float64
        var distanceFirst = 999.
        var distanceSecond = 999.

        for i:= 0; i < len(feature.Geometry.Coordinates); i++ {
            var x = feature.Geometry.Coordinates[i][0]
            var y = feature.Geometry.Coordinates[i][1]

             var tmpDis = math.Sqrt(math.Pow(latitude - x, 2) + math.Pow(longitude - y, 2))

                if (tmpDis <= distanceFirst) {
                    firstX = x
                    firstY = y
                    distanceFirst = tmpDis
                } else if (tmpDis <= distanceSecond) {
                    secondX = x
                    secondY = y
                    distanceSecond = tmpDis
                }
        }

        x1 = firstX
        y1 = firstY
        x2 = secondX
        y2 = secondY

        fmt.Println("x1", x1, "y1", y1)
        fmt.Println("x2", x2, "y2", y2)
    }


   var a = (y2 - y1)
   var b = -(x2 - x1)
   var c = -(x1*y2 - x2*y1)
   var k = (a * latitude + b * longitude + c) / (math.Pow(a, 2) + math.Pow(b, 2))
   var x = latitude - a * k
   var y = longitude - b * k

    return [2]float64{x, y}
}

func measureDistance(latitude float64, longitude float64, pX float64, pY float64) float64 {
    var R = 6378.137 // Radius of earth in KM
    var dLat = pX * math.Pi / 180 - latitude * math.Pi / 180
    var dLon = pY * math.Pi / 180 - longitude * math.Pi / 180

    var a = math.Sin(dLat/2) * math.Sin(dLat/2) + math.Cos(latitude * math.Pi /180) * math.Cos(pX * math.Pi / 180) * math.Sin(dLon/2) * math.Sin(dLon/2)
    var c = 2 * math.Atan2(math.Sqrt(a), math.Sqrt(1-a))
    var d = R * c

    return d * 1000 // meter


