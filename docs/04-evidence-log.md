# 04 — Evidence Log: Laundry Queue & Status Tracking

## 1. Source Summary

| Field | Value |
| :--- | :--- |
| **Case** | Case 03: ระบบจองคิวและติดตามสถานะเครื่องซักผ้าหอพัก |
| **AI role(s) used** | Student Requester (STU), Dorm Officer / Maid (MAID), System Admin (ADMIN) |
| **Source files** | Problem Brief (Week 01), Elicitation Plan & Interview Guide (Week 03), Interview Transcripts / Raw Notes (Week 04) |
| **Conversation excerpt** | `../evidence/week-04/ai-conversation-excerpt.md` |

---

## 2. Evidence Log

| E-ID | Source / Role | Evidence quote or summary | Tag | Interpreted Need | Related RC | Follow-up / Unknown |
| :---: | :--- | :--- | :---: | :--- | :---: | :--- |
| **E-01** | STU-01 (Q-01, Q-02) | "ปกติมาซักช่วง 19.00-22.00 น. ต้องเดินลงมาเช็กเครื่อง 2-3 รอบตลอด พอมาถึงก็เจอเครื่องเต็มหรือมีตะกร้ากั๊กไว้แต่ตัวไม่อยู่ ต้องเดินกลับห้องฟรี" | **NEED** | ผู้ใช้ต้องเห็นสถานะเครื่องซักผ้าและจำนวนคิวรอจริงก่อนลงมาใช้งาน | RC-01 | ต้องยืนยันว่าสถานะมาจาก Sensor หรือ Simulation |
| **E-02** | STU-02 (Q-04) | "อยากให้มีการแจ้งเตือนล่วงหน้าสัก 5-10 นาทีก่อนเครื่องซักเสร็จ เพราะบางทีลืม หรือกะเวลาพลาด จนคนอื่นมารอต่อ" | **NEED** | ผู้ใช้ต้องการระบบแจ้งเตือนก่อนเครื่องซักเสร็จและเมื่อถึงคิวซัก | RC-02 | ต้องตกลงระยะเวลาแจ้งเตือนที่เหมาะสม (5 หรือ 10 นาที) |
| **E-03** | STU-03 (Q-03) | "ถ้าระบบเปิดให้จองล่วงหน้าได้ ควรให้เวลามาแสดงตัวไม่เกิน 5-10 นาที ถ้าไม่มาต้องตัดสิทธิ์ให้คนถัดไป ไม่งั้นจะกลายเป็นการกั๊กคิวจากระยะไกล" | **CONSTRAINT** | เงื่อนไขการเข้าคิวต้องกำหนดระยะเวลา No-show timeout ที่เป็นธรรม | RC-03 | ต้องระบุระยะเวลา timeout ที่แน่นอนกับผู้ดูแลหอพัก |
| **E-04** | MAID-01 (Q-05) | "ผ้าค้างเครื่องเป็นปัญหามาก แม่บ้านไม่กล้าย้ายเพราะกลัวของหาย แต่ถ้ารอก็เสียโอกาสคนอื่น ถ้าค้างเกิน 15 นาที ควรมีระบบบันทึกจุดที่ย้ายผ้าไปวาง" | **NEED** | แม่บ้านและผู้ดูแลต้องมีขั้นตอนบันทึก (SOP) และจุดติดตามเมื่อต้องย้ายผ้าค้างเครื่อง | RC-04 | ต้องยืนยันสถานที่วางผ้าค้างเครื่องและกฎ SOP |
| **E-05** | DORM-01 (Q-06, Q-09) | "เวลาเครื่องเสีย นักศึกษาชอบหยอดเหรียญซ้ำแล้วโดนกินเหรียญ อยากให้มีระบบแจ้งเครื่องเสีย และให้เจ้าหน้าที่กดปิดรับคิวเครื่องนั้นได้ทันที" | **NEED** | ผู้ใช้และผู้ดูแลต้องการระบบรายงานและปรับสถานะเครื่องเสียเพื่อป้องกันการใช้งานซ้ำ | RC-05 | ต้องกำหนด authority ให้ชัดเจนว่าใครมีสิทธิ์ปิดเครื่อง |
| **E-06** | STU-01, STU-02 (Q-07) | "ไม่อยากให้แสดงชื่อจริงหรือเลขห้องพักบนหน้าจอสาธารณะ กลัวเรื่องความเป็นส่วนตัวและความปลอดภัย เห็นแค่อักษรย่อหรือรหัสคิวสุ่มก็พอ" | **CONSTRAINT** | ระบบต้องแสดงข้อมูลคิวแบบ Anonymous โดยไม่เปิดเผยข้อมูลส่วนบุคคล (PII) | RC-06 | ต้องยืนยัน Data Fields ที่อนุญาตให้แสดงบน UI Public |

---

## 3. How the Team Derived Needs

| Evidence | ทำไมถือเป็น Need/Constraint | Need/Constraint ที่ได้ |
| :--- | :--- | :--- |
| **E-01** (จาก Q-01, Q-02) | Stakeholder พูดถึง Pain Point เรื่องการเสียเวลาเดินฟรีและการกั๊กคิวด้วยตะกร้า ซึ่งแก้ได้ด้วยการมองเห็นสถานะล่วงหน้า | **N-01:** ผู้ใช้ต้องเห็นสถานะเครื่องและจำนวนคิวก่อนตัดสินใจลงมาซักผ้า |
| **E-03** (จาก Q-03) | เป็นข้อจำกัดทางพฤติกรรม (Behavioral Constraint) เพื่อป้องกันปัญหา No-show และการกั๊กคิวจากระยะไกล | **N-03:** ระบบต้องมีเงื่อนไขจำกัดเวลาการแสดงตัว (Timeout) หลังกดเข้าคิว |
| **E-04** (จาก Q-05) | มีความขัดแย้งเรื่องทรัพย์สินสูญหาย จึงต้องแปลงเป็นกระบวนการที่มีระบบบันทึกรองรับเพื่อลดข้อโต้แย้ง | **N-04:** แม่บ้าน/ผู้ดูแลต้องมีระบบบันทึกสถานที่เก็บผ้าค้างเครื่องที่เป็นสัดส่วน |
| **E-06** (จาก Q-07) | ผู้ใช้งานกังวลเรื่อง Privacy การแสดงผลข้อมูลจึงต้องอยู่ภายใต้ข้อจำกัดด้านความปลอดภัยของข้อมูลส่วนบุคคล | **N-06:** การแสดงผลข้อมูลคิวสาธารณะต้องปกปิดข้อมูลส่วนบุคคล (PII) |

---

## 4. Need Summary

| Need ID | Need statement | Based on E-ID(s) | Notes |
| :---: | :--- | :---: | :--- |
| **N-01** | Student Requester needs to see actual machine availability and queue status before coming down. | E-01 | ตอบโจทย์ EO-01 / OQ-01 |
| **N-02** | Student Requester needs automated notification alerts before cycle completion and when queue is ready. | E-02 | ตอบโจทย์ EO-01 / OQ-02 |
| **N-03** | Student Requester needs a fair No-show timeout policy to prevent holding queues remotely. | E-03 | ตอบโจทย์ EO-01 / OQ-01, OQ-02 |
| **N-04** | Maid and Dorm Officer need an explicit workflow and logging interface for handling leftover clothes. | E-04 | ตอบโจทย์ EO-02 / OQ-03 |
| **N-05** | Student and Dorm Officer need a fast mechanism to report and disable out-of-order machines. | E-05 | ตอบโจทย์ EO-02 / OQ-03 |
| **N-06** | Student Requester needs public queue status to maintain privacy without disclosing PII. | E-06 | ตอบโจทย์ EO-03 / OQ-04 |

---

## 5. Unknowns / Follow-up for Week 05

| OQ-ID | Question | Why it matters | Who/what can verify |
| :---: | :--- | :--- | :--- |
| **OQ-01** | ระยะเวลา No-show Timeout ที่เหมาะสมควรเป็นกี่นาที (เช่น 5 หรือ 10 นาที)? | กระทบต่ออัตรา No-show และความเป็นธรรมในการใช้งาน | Student Survey / Dorm Officer |
| **OQ-02** | ระยะเวลาแจ้งเตือนก่อนเครื่องซักเสร็จควรเป็นกี่นาที? | กระทบต่อการมารับผ้าทันเวลาและลดผ้าค้างเครื่อง | Student Requester |
| **OQ-03** | ใครมีสิทธิ์กดเปลี่ยนสถานะ "เครื่องเสีย/พร้อมใช้งาน" ได้บ้าง (นักศึกษาแจ้งได้เลย หรือต้องรอผู้ดูแลยืนยัน)? | กระทบต่อความถูกต้องของข้อมูลสถานะ (Data Integrity) | Dorm Officer / System Admin |
| **OQ-04** | จุดวางผ้าค้างเครื่องควรระบุตำแหน่งอย่างไรในระบบ (เช่น Basket A, Shelf B)? | กระทบต่อ Workflow การติดตามผ้าค้างเครื่องของแม่บ้าน | Maid / Dorm Officer |