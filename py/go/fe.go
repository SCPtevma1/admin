package main

import "fmt"

// 100 =>  >= 5 สอบผ่าน , สอยไม่ผ่าน
func main() {
	// รับ input
	// ตัวเลข
	var number int
	fmt.Print("ตะแนน =")
	fmt.Scanf("%d", &number)

	if number == 1 {
		fmt.Println("เปิดบัณชีใหม่")
	} else if number == 2 {
		fmt.Println("ฟากเงิน")
	} else {
		fmt.Println("ไม่ถูกต้อง")
	}
}
