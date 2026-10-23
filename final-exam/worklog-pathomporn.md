# บันทึกร่างส่วนปฐมพร

| วันที่ | ผู้รับผิดชอบตามการแบ่งงาน | งานที่เกิดขึ้นในแชตนี้ | หลักฐาน | สถานะ |
|---|---|---|---|---|
| 23 ตุลาคม 2569 | ปฐมพร หลีจาง — G4 | ผู้ใช้มอบหมายให้ AI ช่วยร่าง G4 จาก SRS และโจทย์ โดยเลือก 02B; จัด Context/Container, ตาราง, NFR mapping, Decision cards และ Spine walk | g4-architecture-pathomporn.md; diagrams/context-after.drawio/.png; diagrams/container-after.drawio/.png | AI draft เสร็จ; รอปฐมพรตรวจ/ปรับและเพื่อน review |
| 23 ตุลาคม 2569 | ปฐมพร — ประสาน G3/G5 | ปรับชื่อ container, SP-FX-01–07, D-FX-01–05 และ DD-FX-01–06 ให้ตรงไฟล์ร่างพสิษฐิ์ที่ผู้ใช้ส่ง | references/pasit-g3-g5-draft.md; เพิ่ม DD-G4-01/02 โดยไม่ชน ID เพื่อน | ยังต้องตรวจ G1/G2 ต้นฉบับและยืนยันข้อเสนอร่วมกัน |

ผู้ใช้อนุญาต commit/push ส่วน G4 บน branch `final-exam` โดยใช้ Git identity ที่ตั้งอยู่ `poleon48` ไม่เปลี่ยน author หรือเวลาแทนสมาชิกอื่น; hash จริงตรวจได้จาก git log หลัง commit ไม่สร้างหลักฐานย้อนหลัง

รอบแก้ 23 ตุลาคม 2569: ผู้ใช้แนบ g4-review-notes.md; AI ปรับ G4 และภาพตาม ID เว็บ/audit ล่าสุดที่ผล review ระบุ เพิ่ม atomic transaction/rollback และเส้นทางอ่าน audit ตามสิทธิ์ พร้อมจัด ZIP รวม .drawio, PNG, เอกสารและสคริปต์ ไม่อ้างว่า reviewer ได้รับ source หรือเปิดใน draw.io แล้ว และยังรอเทียบ G1/G2/G3 ล่าสุดกับเจ้าของงาน

รอบตรวจ Word ก่อน commit: รับ origin/final-exam ถึง 20bd38f อ่าน G1–G6 จาก Word และเทียบ G4 กับ G2/G3/G5 ล่าสุด ตรวจภาพฝังทั้งสอง SHA-256 ตรง PNG ในเครื่อง การเปิด source ผ่าน draw.io ยังไม่สำเร็จเพราะ file chooser ไม่ทำงาน; ไม่ติ๊กการเปิด source หรือการอ่าน oral ของสมาชิกแทน ดู g4-handoff-pasit.md
