# ใบตรวจข้ามทีม (Peer Cross-Review Form) — ช่วงที่ 4

> **Case Project:** Dorm Laundry Queue and Status (Case-03)  
> **Review Date:** 18 สิงหาคม 2569  
> **Reviewing Sub-team / Peer Group:** Group 04 Cross-Reviewer Team (กลุ่มตัวอย่างที่มาตรวจ)  
> **Target Artefacts Reviewed:** `docs/05-requirement-backlog.md`, `docs/08-validation-traceability.md`, `docs/04-evidence-log.md`

---

## 1. ผลการตรวจข้ามทีม (Checklist Evaluation)

| # | สิ่งที่ตรวจ | ผลการประเมิน (ผ่าน / ไม่ผ่าน) | ข้อเสนอแนะ / หมายเหตุ (อ้าง ID เสมอ) |
|---|---|---|---|
| 1 | **ทุก Must มีสาย traceable ครบ** (Problem -> Evidence -> Need -> FR/NFR -> Priority) | **[x] ผ่าน** &nbsp;&nbsp;&nbsp; [ ] ไม่ผ่าน | ทุก Must requirement (FR-01 ถึง FR-05, BR-01 ถึง BR-04, NFR-01 ถึง NFR-03) มีสาย Traceability ย้อนกลับไปยัง E-01..E-06, N-01..N-06 และ Stakeholders ชัดเจนใน `docs/08` Section 3 & 4 |
| 2 | **FR/NFR วัด/ทดสอบได้** (มีตัวเลข/เงื่อนไขเชิงปริมาณ ชัดเจน) | **[x] ผ่าน** &nbsp;&nbsp;&nbsp; [ ] ไม่ผ่าน | ทุกข้อมีเกณฑ์วัดได้ชัดเจน เช่น FR-03 (Timeout 10 นาที), FR-04 (แจ้งล่วงหน้า 5 นาที), NFR-02 (ทำรายการสำเร็จใน ≤ 3 คลิก), NFR-03 (Latency ≤ 3s), NFR-04 (รองรับ ≥ 50 Concurrent users) |
| 3 | **ไม่มี requirement กำกวม/ซ้ำ** (Atomic & Unambiguous) | **[x] ผ่าน** &nbsp;&nbsp;&nbsp; [ ] ไม่ผ่าน | ถ้อยคำชัดเจน แยก Atomic workflow ชัดเจนระหว่างการตรวจสอบสถานะเครื่อง, การจองคิว, การส่งแจ้งเตือน, และการเปลี่ยนสถานะเครื่องเป็นปิดปรับปรุง |
| 4 | **Scope ตรงกับ Case Card** (ไม่บวมเกินขอบเขตที่ได้รับมอบหมาย) | **[x] ผ่าน** &nbsp;&nbsp;&nbsp; [ ] ไม่ผ่าน | ขอบเขตสอดคล้องกับ Case-03 ระบบจัดการคิวเครื่องซักผ้าหอพัก และระบุ Out-of-scope ชัดเจน (เช่น ไม่รวมการสั่งงานเครื่องซักผ้าจริงด้วย IoT, ไม่รวมระบบชำระเงินออนไลน์) |
| 5 | **MoSCoW มีเหตุผลรองรับ** (Rationale สมเหตุสมผลจาก Value/Risk) | **[x] ผ่าน** &nbsp;&nbsp;&nbsp; [ ] ไม่ผ่าน | Priority Rationales มีน้ำหนักน่าเชื่อถือ เช่น การจัด Must ให้กับการป้องกันการกั๊กคิว (FR-03), การซ่อนข้อมูลส่วนตัวบนจอกลางเพื่อ Privacy (NFR-01), และสิทธิ์การปิดเครื่องเฉพาะ Admin (BR-03) |

---

## 2. ข้อเสนอแนะเพื่อการปรับปรุงและเตรียมพร้อม Week 06 (Constructive Feedback)

1. **ด้าน Traceability (อ้างอิง FR-01, FR-03, NFR-01):**
   - สายเชื่อมโยงสมบูรณ์มาก มีการสร้างตาราง Matrix ทั้งแบบ Backward Traceability และ 3 Must Requirements Audit Form ใน `docs/08` ช่วยให้การตรวจสอบย้อนกลับไปยังหลักฐานใน `docs/04` เป็นไปอย่างรวดเร็ว
2. **ด้าน Quality & Verifiability (อ้างอิง FR-03, NFR-02, NFR-03):**
   - ข้อความ requirement ได้รับการปรับปรุงถ้อยคำจนวัดผลได้จริง (เช่น ระบุตัวเลข 10 นาที, 3 คลิก, หรือความเร็วการอัปเดตสถานะ 3 วินาที) ทำให้พร้อมสำหรับนำไปเขียน Acceptance Criteria และ Quality Scenarios ใน Week 06
3. **ด้านการเตรียมต่อยอดสู่ Requirement Modeling (Week 06 Handoff):**
   - แนะนำให้นำ `FR-02` (การจองคิว) และ `FR-05` (การเปลี่ยนสถานะเครื่องชำรุด) ไปต่อยอดเป็น Use Case สำหรับนักศึกษาและผู้ดูแลหอพัก และนำ `BR-03` ไปต่อยอดเป็น Acceptance Criteria (Gherkin format) สำหรับตรวจสอบสิทธิ์การใช้งาน (Authorization)

---

## 3. สรุปผลการประเมิน (Gate Assessment Result)

- **สถานะ:** **ผ่านเกณฑ์ Peer Cross-Review 100% ครบถ้วนทุกข้อ (PASS ALL ITEMS)**
- **ผู้ตรวจสอบ (Cross-Reviewers):** [ชื่อเพื่อนจากกลุ่มที่มาตรวจ 1], [ชื่อเพื่อนจากกลุ่มที่มาตรวจ 2]
- **วันที่ยืนยันผล:** 19 สิงหาคม 2569