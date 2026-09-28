<?php
require __DIR__ . '/vendor/autoload.php';

// 1. ยืนยันตัวตนเข้าใช้งาน Google API (ห้ามเปลี่ยนคำว่า Google_Client เป็นอีเมล)
$client = new \Google_Client();
$client->setApplicationName('PHP to Google Sheets');
$client->setScopes([\Google_Service_Sheets::SPREADSHEETS]);
$client->setAuthConfig(__DIR__ . '/credentials.json'); // เรียกใช้ไฟล์ json ที่คุณเปิดอยู่
$client->setAccessType('offline');

// ตรงนี้ก็ต้องใช้คลาสของ Google ห้ามเปลี่ยนเป็นอีเมลเช่นกันครับ
$service = new \Google_Service_Sheets($client);

// 2. ใส่ไอดีสเปรดชีตของคุณตรงบรรทัดนี้ได้เลยครับ!
$spreadsheetId = '1_ElyfjYZoy5uzpnvVLNHENAKskgQG6LayFASBTYIYc'; 

// 3. ระบุชื่อชีตของคุณ
$range = 'ชีต1!A:C'; 

// 4. ข้อมูลที่ต้องการส่งไปบันทึก
$values = [
    ['ลำดับ', 'ชื่อ-นามสกุล', 'เบอร์โทรศัพท์'], 
    ['1', 'สมชาย ใจดี', '081-234-5678']
];

// ตรงนี้แก้ไขให้ใช้คลาสที่ถูกต้องของ Google ครับ
$body = new \Google_Service_Sheets_ValueRange([
    'values' => $values
]);

$params = [
    'valueInputOption' => 'USER_ENTERED'
];

try {
    $result = $service->spreadsheets_values->append($spreadsheetId, $range, $body, $params);
    echo "เชื่อมข้อมูลสำเร็จ! ข้อมูลถูกส่งไปที่ Google Sheet แล้ว";
} catch (Exception $e) {
    echo 'เกิดข้อผิดพลาด: ',  $e->getMessage(), "\n"; 
    