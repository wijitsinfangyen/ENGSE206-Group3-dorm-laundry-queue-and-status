# 15 — Individual Reflection (Requirement Baseline Review v1.0)

> **Case Project:** Dorm Laundry Queue and Status (Case-03)  
> **Course / Week:** ENGSE206 / Week 05 Consolidation Studio  
> **Date:** 19 สิงหาคม 2569

---

## Member 1: วิจิตรศิลป์ ฟังเย็น

### Student Information
| Field | Detail |
|---|---|
| Student ID | [68543210068-1] |
| Name | วิจิตรศิลป์ ฟังเย็น |
| Primary Role(s) | Facilitator, Requirements Lead |

### 1. My Contribution
รับหน้าที่เป็น Facilitator คุมภาพรวมของการทำ Baseline Review อนุมัติการล็อกฐานความต้องการเป็น Baseline v1.0 และร่วมตรวจสอบขอบเขต (Scope) ไม่ให้บานปลาย เช่น การตัดระบบชำระเงินออนไลน์ และการควบคุมวงจรเครื่องซักผ้าจริง (IoT) ออกจากโครงงาน รวมถึงดูแลการกระจายงานให้กับสมาชิกในทีมให้ทันตามกรอบเวลา

### 2. What I Learned About Requirements and Design
เรียนรู้ว่าการทำ Baseline ไม่ใช่แค่รวบรวมไฟล์ส่ง แต่คือการ "แช่แข็ง" ความต้องการที่ผ่านการตรวจสอบแล้ว เพื่อให้ทีมมีฐานที่มั่นคง หากไม่ล็อก Baseline ทีมอาจจะเปลี่ยนใจไปมาจนไม่สามารถเริ่มออกแบบ Use Case หรือ State Machine ใน Week 06 ได้เลย

### 3. A Decision I Influenced
ผลักดันให้ใช้วิธีปกปิดข้อมูลส่วนบุคคลบนหน้าจอคิวสาธารณะ โดยแสดงเฉพาะ "รหัสคิวสุ่ม" (NFR-01) แทนที่จะแสดงเลขห้องหรือชื่อจริง เพื่อรักษาสมดุลระหว่าง PDPA ความปลอดภัยของนักศึกษา และความสามารถในการติดตามสถานะคิว

### 4. Feedback I Received and How I Responded
ได้รับ Feedback จากเพื่อนในทีมว่าการจัดลำดับ MoSCoW บางข้อเหตุผลยังอ่อนไป จึงได้เข้าไปเพิ่ม Rationale ใน `docs/05-prioritization-rationale.md` โดยเน้นเหตุผลด้าน Risk (เช่น การป้องกันการกลั่นแกล้งกันหากให้นักศึกษากดปิดเครื่องเสียได้เอง)

### 5. What I Would Improve Next Time
ในคาบถัดไปจะเตรียมตัวอ่านเนื้อหาเกี่ยวกับ Requirement Modeling (Use Case Diagram และ Activity Diagram) ล่วงหน้า เพื่อให้สามารถนำทีมลุยงานออกแบบสถาปัตยกรรมระบบได้ทันทีหลังได้รับโจทย์

### 6. Answers to Reflection Questions
1. **วันนี้ฉันเข้าใจอะไรชัดขึ้นเกี่ยวกับ requirement ของทีม?**  
   เข้าใจว่า Requirement บางอย่างที่เราทำไม่ได้ด้วยข้อจำกัดทางเทคนิค (เช่น เชื่อม IoT) เราสามารถบันทึกข้อจำกัดนั้นไว้ และเสนอทางเลือกอื่น (เช่น Timer Simulation) เป็น Baseline แทนได้
2. **จุดที่ทีมเรายังอ่อนที่สุดคืออะไร และจะทำอย่างไรต่อ?**  
   เรื่องการรับส่งข้อมูลแบบ Real-time (Concurrency) ช่วงคนใช้เยอะ ทีมยังขาดความรู้ทางเทคนิคว่าจะใช้เทคโนโลยีใด จะต้องไปปรึกษาผู้รู้เพิ่มเติม
3. **คำถามที่อยากถามอาจารย์ในคาบหน้า (Week 6) คือ...**  
   ใน Use Case Diagram ของระบบนี้ ตัว "ระบบแจ้งเตือน (Notification System)" หรือ "ระบบจับเวลาถอยหลัง (Timer Simulation)" ควรถูกวาดให้เป็น External Actor แยกออกมาหรือไม่ครับ?

---

## Member 2: ปฐมพร หลีจาง

### Student Information
| Field | Detail |
|---|---|
| Student ID | [68543210034-3] |
| Name | ปฐมพร หลีจาง |
| Primary Role(s) | Traceability Auditor, Scribe |

### 1. My Contribution
รับหน้าที่เป็น Traceability Auditor ทำการไล่สายย้อนกลับจาก Must Requirements (`FR-01` ถึง `FR-05`, `NFR-01`) ไปยัง Evidence (`E-01`..`E-06`) และ Stakeholders ในเอกสาร `docs/08-validation-traceability.md` จนครบ 100% พร้อมทั้งเป็นคนร่างตาราง 3 Must Check Form

### 2. What I Learned About Requirements and Design
เรียนรู้ว่าการมี Traceability Matrix ช่วยป้องกันปัญหา "ผีหลอก (Phantom Requirements)" หรือความต้องการที่ทีมคิดขึ้นมาเองโดยที่ผู้ใช้ไม่ได้พูดถึง การที่ทุก Requirement ชี้กลับไปที่ Evidence ID ได้ ทำให้ฐานความต้องการของเรามีน้ำหนักและน่าเชื่อถือ

### 3. A Decision I Influenced
ผลักดันให้แยกประเด็น "นโยบายการจัดการผ้าค้างเครื่อง" (ISSUE-DLQS-03) ออกไปเป็น Open Question เพราะมองว่าทีมไม่มีอำนาจไปกำหนดพื้นที่ส่วนกลางหรือกฎระเบียบทรัพย์สินแทนเจ้าของหอพักได้ ต้องรอ Validation ก่อน

### 4. Feedback I Received and How I Responded
ได้รับ Feedback ตอนทำ Cross-review ว่าคำว่า "เวลาผ่านไปสักระยะให้ข้ามคิว" มันวัดผลไม่ได้ จึงกลับมาแก้ FR-03 และ BR-02 ร่วมกับทีม ให้ระบุตัวเลขชัดเจนว่าเป็น "No-show Timeout 10 นาที"

### 5. What I Would Improve Next Time
จะพยายามสรุปเอกสารให้กระชับมากขึ้น เพราะบางครั้งการเขียน Evidence หรือ Rationale ยาวเกินไปทำให้ตรวจสอบ (Audit) ได้ช้า

### 6. Answers to Reflection Questions
1. **วันนี้ฉันเข้าใจอะไรชัดขึ้นเกี่ยวกับ requirement ของทีม?**  
   เข้าใจกระบวนการไล่สาย Traceability อย่างลึกซึ้ง ว่าทุกฟังก์ชันในระบบต้องตอบโจทย์ Need และแก้ Pain point (Problem) ได้จริง
2. **จุดที่ทีมเรายังอ่อนที่สุดคืออะไร และจะทำอย่างไรต่อ?**  
   เรื่องนโยบายหอพักที่อยู่นอกเหนือการควบคุมของเรา จะแก้ปัญหาโดยออกแบบ Alternate Flow สำรองไว้ใน Use Case
3. **คำถามที่อยากถามอาจารย์ในคาบหน้า (Week 6) คือ...**  
   Business Rule เรื่อง "ผู้ดูแลหอพักเท่านั้นที่เปลี่ยนสถานะเครื่องชำรุดได้" (BR-03) ควรถูกเขียนไว้ใน Pre-condition ของ Use Case หรือเขียนในรูปแบบ Exception Flow ครับ?

---

## Member 3: พสิษฐิ์ เพชรอำพันธ์ุ

### Student Information
| Field | Detail |
|---|---|
| Student ID | [68543210036-8] |
| Name | พสิษฐิ์ เพชรอำพันธ์ุ |
| Primary Role(s) | Quality Checker, Timekeeper |

### 1. My Contribution
รับหน้าที่เป็น Quality Checker ตรวจประเมินคุณภาพของ FR/NFR ด้วยเกณฑ์ 4 มิติ (วัดได้, ไม่กำกวม, Atomic, มีที่มา) ช่วยปรับแก้ข้อความ requirement ให้เป็นเงื่อนไขที่ตรวจสอบได้ (Verifiable Criteria) จัดทำ Decision Log และทำหน้าที่คุมเวลา (Timekeeper) ในการประชุมกลุ่ม

### 2. What I Learned About Requirements and Design
เรียนรู้ว่าคำว่า "รวดเร็ว" หรือ "ใช้งานง่าย" เป็นคำกำกวมทางวิศวกรรมซอฟต์แวร์ การระบุให้ชัดเจนไปเลยว่า "ทำรายการสำเร็จใน 3 คลิก" (NFR-02) หรือ "Latency ไม่เกิน 3 วินาที" (NFR-03) จะทำให้ Tester รู้ว่าจะต้องทดสอบระบบอย่างไรในอนาคต

### 3. A Decision I Influenced
ตัดสินใจให้ปรับแก้ไขถ้อยคำ Requirement ทั้งชุด (Decision D-01) ให้มีตัวเลขและเงื่อนไขที่วัดได้ทั้งหมด เพื่อเตรียมพร้อมสำหรับการเขียน Acceptance Criteria ในสัปดาห์หน้า

### 4. Feedback I Received and How I Responded
ได้รับ Feedback ว่าการตรวจ Quality Check ใช้เวลานานเกินไป ทำให้เวลาในการนำเอกสารขึ้น GitHub ช่วงท้ายกระชั้นชิด จึงได้เร่งการตัดสินใจและให้เพื่อนช่วยกันทวนคำอ่านแทนการตรวจคนเดียว

### 5. What I Would Improve Next Time
จะบริหารเวลา (Timekeeping) ในการพูดคุยถกเถียงเรื่อง Requirement ให้มีประสิทธิภาพมากขึ้น ตัดสินใจให้เด็ดขาดขึ้นเมื่อมีทางเลือกที่สูสีกัน เพื่อให้มีเวลาเหลือในการทำเอกสารสรุป

### 6. Answers to Reflection Questions
1. **วันนี้ฉันเข้าใจอะไรชัดขึ้นเกี่ยวกับ requirement ของทีม?**  
   เข้าใจความสำคัญของคุณสมบัติ Atomicity คือ Requirement ไม่ควรมัดรวมกัน เช่น ต้องแยกการตรวจสอบสถานะเครื่อง ออกจากการจองคิว เพื่อให้สามารถเขียน Test Case แยกกันได้
2. **จุดที่ทีมเรายังอ่อนที่สุดคืออะไร และจะทำอย่างไรต่อ?**  
   ความรู้เกี่ยวกับการเขียน Requirement Models เช่น Gherkin syntax สำหรับ Acceptance Criteria ต้องศึกษาล่วงหน้าก่อนเข้า Week 06
3. **คำถามที่อยากถามอาจารย์ในคาบหน้า (Week 6) คือ...**  
   การเขียน Acceptance Criteria สำหรับเงื่อนไข No-show Timeout (10 นาที) เราควรเขียนจำลอง Background Timer อย่างไรในรูปแบบ Given-When-Then (Gherkin) เพื่อให้ครอบคลุมกรณีที่เน็ตผู้ใช้หลุดครับ?