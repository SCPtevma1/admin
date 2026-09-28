package main

import "fmt"

// 100 =>  >= 5 สอบผ่าน , สอยไม่ผ่าน
func main() {
	// รับ input

	var score int
	fmt.Print("ตะแนน =")
	fmt.Scanf("%d", &score)

	fmt.Println("คะสอบ+ จิอาสา = ", score)
	// ประมวลผลคะแนน
	if score >= 50 {
		fmt.Println("ผ่าน")
	} else {
		fmt.Println("ไม่ผ่าน")
	}

}
