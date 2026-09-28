package main

import "fmt"

// 100 =>  >= 5 สอบผ่าน , สอยไม่ผ่าน
func main() {
	// รับ input
	// ตัวเลข
	var number int
	fmt.Print("ตะแนน =")
	fmt.Scanf("%d", &number)

	switch number {
	case 1:
		fmt.Println("เปิดบัณชีใหม่")
	case 2:
		fmt.Println("ฟากเงิน")
	default:
		fmt.Println("ไม่ถูกต้อง")
	}
}
