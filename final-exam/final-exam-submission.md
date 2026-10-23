# ใบส่งงานสอบปลายภาค ส่วน ก งานกลุ่ม

| รายการ | รายละเอียด |
|---|---|
| กลุ่ม / Case | กลุ่ม 03 / Case 03 |
| ชื่อระบบ | ระบบจองคิวและติดตามสถานะเครื่องซักผ้าหอพัก / Dorm Laundry Queue and Status |
| Repository | https://github.com/wijitsinfangyen/ENGSE206-Group3-dorm-laundry-queue-and-status |
| CR เสริมที่เลือก | CR-FX-02B เวลาเหลือครึ่งหนึ่ง — Pending |
| Branch | final-exam |
| Pull Request | [#2 submit(final): change-to-design take-home](https://github.com/wijitsinfangyen/ENGSE206-Group3-dorm-laundry-queue-and-status/pull/2) เข้า main |
| Commit hash ของคำตอบที่ตรวจครบ | `c9bbec3c45120d268a72b29963a99bba2252bab5` — snapshot ของ Word และหลักฐานสมาชิกก่อน commit เติม URL PR ในใบส่งงาน |
| Commit ล่าสุดของชุดส่ง | ดู SHA ของ HEAD ล่าสุดใน [commits ของ PR #2](https://github.com/wijitsinfangyen/ENGSE206-Group3-dorm-laundry-queue-and-status/pull/2/commits); SHA เต็มระบุในรายละเอียด PR เพื่อให้รวม commit metadata ของใบส่งงานนี้ด้วย |
| สถานะ SRS ที่ใช้เป็นฐาน | CASE03-SRS-W07-v1, 1.0-draft / Baseline Candidate |

## งานเดิมที่ใช้เป็นฐาน

ทุกไฟล์ฐานอ้าง commit `b46b207cb148c2730f1f3b68af9989b11f9d12f1`

| งาน | ไฟล์ / สถานะ |
|---|---|
| SRS W07 | docs/07-srs-v1.md — Baseline Candidate |
| Models W06 | docs/06-requirement-models.md |
| Review / trace / CR W08 | docs/08-validation-traceability.md — ไม่ใช้ข้อความ Approved ในไฟล์เดิมเป็นหลักฐานอนุมัติ SRS/CR ของงานสอบ |
| Design Strategy / Spine W10 | design/10-design-strategy.md ยังเป็นแม่แบบ; ไม่พบ design/00-design-spine.md ในฐานนี้; G3 สังเคราะห์ข้อเสนอใหม่จาก SRS และเปิดเผยข้อจำกัด |
| Architecture W11 | design/11-conceptual-architecture.md ยังเป็นแม่แบบ; G4 เสนอ Context/Container ใหม่ตามที่โจทย์อนุญาต |

## ไฟล์ที่เตรียมแล้ว

- [x] final-exam/final-exam-group-answer.docx
- [x] final-exam/diagrams/context-after.drawio และ .png
- [x] final-exam/diagrams/container-after.drawio และ .png
- [x] final-exam/final-exam-submission.md
- [x] final-exam/ai-use-log.md

## สมาชิกและการมีส่วนร่วม

| ชื่อ–สกุล | รหัสนักศึกษา | ส่วนที่รับผิดชอบ | หลักฐาน / commit |
|---|---|---|---|
| นายวิจิตรศิลป์ ฟังเย็น | 68543210068-1 | G1/G2; ผู้ตรวจร่วม G3/G5 ตามคำยืนยันพสิษฐิ์ | commit `734986dd63a056792713de2759a257283f1492ec`; g1-g2-wijitsilp.md และ G1/G2 ใน Word |
| นายพสิษฐิ์ เพชรอำพันธุ์ | 68543210036-8 | G3/G5; รวม Word และชุดงาน | G3/G5 commit `410676027237260b4552ab2ce7feb30f3f3c6ec2`; Word/ไฟล์รวมอยู่ใน commit ถัดไปบน branch final-exam |
| นายปฐมพร หลีจาง | 68543210034-3 | G4 และภาพ; ผู้ตรวจร่วม G3/G5 ตามคำยืนยันพสิษฐิ์ | commit `85c21659a51fd2927b613a5e49767b2e79579865`; g4-architecture-pathomporn.md และ diagrams/ |

## ตรวจรับก่อนส่ง

- [ ] สมาชิกทุกคนอ่าน Word ฉบับรวมและพร้อมอธิบาย oral spot-check (การยืนยัน G3/G5 ไม่แทนการอ่านทั้งฉบับ)
- [x] ค่าที่ยังไม่ตกลงระบุ TBD และมี OI/DD; ค่า 5/10 นาทีมีฐาน SRS เดิม
- [x] SRS เป็น Baseline Candidate; CR Pending; decision Proposed
- [x] งานสอบใหม่อยู่ใน final-exam/ และไม่แก้ไฟล์รายสัปดาห์
- [ ] สมาชิกเปิด source .drawio ทั้งสองภาพในแอปและตรวจว่าตรง PNG
- [x] ทุกคนมี commit ส่วนของตนตามชื่อผู้เขียนจริงใน Git และกรอกหลักฐานแล้ว: วิจิตรศิลป์ 734986d, พสิษฐิ์ 4106760/20bd38f, ปฐมพร 85c2165
- [x] push branch final-exam และเปิด PR #2 ชื่อตามกำหนด โดยไม่ merge
- [x] เติม hash snapshot คำตอบและ URL PR จริง; HEAD ล่าสุดของการส่งอ้างจาก commits และรายละเอียด PR ไม่อ้างว่า snapshot ก่อน metadata เป็น commit ล่าสุด

## กำหนดเวลา

หน้า Week 15 ระบุส่ง 21 ตุลาคม 2569 เวลา 09:00 น. ชุดนี้จัดเตรียมวันที่ 23 ตุลาคม 2569 จึงไม่อ้างว่าส่งทันเวลา กติกาส่งช้า/การขยายเวลาให้ยึดประกาศผู้สอนที่กลุ่มได้รับ ไม่เปลี่ยนเวลาหรือประวัติ commit ย้อนหลัง
